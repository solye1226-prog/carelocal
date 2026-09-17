import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

const code = await readFile(new URL('../functions/api/analytics.js', import.meta.url), 'utf8');
const { onRequest, normalize, normalizePath } = await import(`data:text/javascript;base64,${Buffer.from(code).toString('base64')}`);
const env = { CF_ANALYTICS_TOKEN: 'test-only', ANALYTICS_ADMIN_PASSWORD: 'x'.repeat(40) };
const request = (days = '7', authenticated = true) => new Request(`https://hospital.hbuby.com/api/analytics?days=${days}`, {
  headers: authenticated ? { Authorization: `Bearer ${env.ANALYTICS_ADMIN_PASSWORD}` } : {},
});
test('unconfigured and unauthorized requests never return statistics', async () => {
  assert.equal((await onRequest({ request: request(), env: {} })).status, 503);
  const response = await onRequest({ request: request('7', false), env });
  assert.equal(response.status, 401);
  assert.equal(response.headers.get('Cache-Control'), 'private, no-store');
  assert.equal((await onRequest({ request: request('90'), env })).status, 400);
});
test('empty data is zero, malformed data is not zero', () => {
  const start = new Date('2026-09-16T15:00:00Z');
  const end = new Date('2026-09-17T03:00:00Z');
  const result = normalize({ total: [], series: [], pages: [], referrers: [], devices: [] }, start, end);
  assert.equal(result.views, 0);
  assert.deepEqual(result.daily, [{ date: '2026-09-17', views: 0, visits: 0 }]);
  assert.throws(() => normalize({}, start, end));
  assert.throws(() => normalize({ total: [{ count: 3 }], series: [], pages: [] }, start, end));
});
test('upstream failures are not presented as zero visits', async () => {
  const original = globalThis.fetch;
  try {
    globalThis.fetch = async () => Response.json({ errors: [{ message: 'sensitive upstream details' }] });
    const response = await onRequest({ request: request(), env });
    assert.equal(response.status, 502);
    assert.equal((await response.text()).includes('sensitive'), false);
  } finally { globalThis.fetch = original; }
});
test('authenticated data uses fixed hostname and converts hourly series to Korea dates', async () => {
  const original = globalThis.fetch;
  try {
    globalThis.fetch = async (url, options) => {
      assert.equal(url, 'https://api.cloudflare.com/client/v4/graphql');
      assert.match(JSON.parse(options.body).query, /requestHost: "hospital.hbuby.com"/);
      return Response.json({ data: { viewer: { accounts: [{
        total: [{ count: 12, sum: { visits: 4 } }],
        series: [{ count: 12, sum: { visits: 4 }, dimensions: { datetimeHour: new Date().toISOString() } }],
        pages: [{ count: 12, dimensions: { requestPath: '/insurance-claims/' } }],
        referrers: [{ count: 12, dimensions: { refererHost: 'search.naver.com' } }],
        devices: [{ count: 12, dimensions: { deviceType: 'mobile' } }],
      }] } } });
    };
    const response = await onRequest({ request: request(), env });
    assert.equal(response.status, 200);
    const data = await response.json();
    assert.equal(data.views, 12);
    assert.equal(data.visits, 4);
    assert.equal(data.referrers[0].host, 'search.naver.com');
    assert.equal(data.devices[0].device, 'mobile');
    assert.equal(data.daily.reduce((sum, day) => sum + day.views, 0), 12);
  } finally { globalThis.fetch = original; }
});
test('unsafe paths are rejected and canonical aliases are normalized', async () => {
  assert.equal(normalizePath('/claims/test.html'), '/claims/test');
  assert.equal(normalizePath('/claims/test/'), '/claims/test');
  for (const path of ['//other.example', '/a?secret', '/a\\b']) {
    const url = new URL(request().url);
    url.searchParams.set('path', path);
    const response = await onRequest({ request: new Request(url, { headers: request().headers }), env });
    assert.equal(response.status, 400);
  }
});
