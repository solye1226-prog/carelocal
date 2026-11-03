import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
const source = fs.readFileSync(new URL('../functions/_middleware.js', import.meta.url), 'utf8');
const { handleRequest, MAINTENANCE_HTML } = await import(`data:text/javascript;base64,${Buffer.from(source).toString('base64')}`);
const context = (path, method = 'GET') => ({ request: new Request(`https://hospital.hbuby.com${path}`, { method }), next: () => new Response('original handler', { status: 200 }) });

test('maintenance catches root, articles, static source, APIs and unknown paths without redirects', async () => {
  for (const path of ['/', '/surgery-benefit/surgery-classification', '/claims/insurance-claim-process.html', '/api/analytics', '/assets/site.css', '/docs/preview.html', '/missing?preview=1']) {
    const response = await handleRequest(context(path));
    assert.equal(response.status, 503);
    assert.equal(response.headers.get('retry-after'), '3600');
    assert.match(response.headers.get('cache-control'), /no-store/);
    assert.equal(response.headers.get('location'), null);
    assert.equal(await response.text(), MAINTENANCE_HTML);
  }
});
test('HEAD has no body; metadata endpoints remain available', async () => {
  assert.equal(await (await handleRequest(context('/', 'HEAD'))).text(), '');
  for (const path of ['/robots.txt', '/ads.txt']) assert.equal(await (await handleRequest(context(path))).text(), 'original handler');
});
test('off switch restores original handlers and maintenance markup never loads ads or scripts', async () => {
  assert.equal(await (await handleRequest(context('/claims/'), false)).text(), 'original handler');
  assert.doesNotMatch(MAINTENANCE_HTML, /<script|<iframe|adsbygoogle|ca-pub-|https?:\/\//i);
  const response = await handleRequest(context('/'));
  assert.match(response.headers.get('content-security-policy'), /default-src 'none'/);
  assert.equal(response.headers.get('x-robots-tag'), null);
});
