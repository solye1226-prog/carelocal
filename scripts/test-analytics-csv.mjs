import test from 'node:test';
import assert from 'node:assert/strict';
import { buildAnalyticsCsv } from '../assets/analytics-csv.mjs';

const report = () => ({
  generatedAt: '2026-10-02T03:00:00Z', path: null, views: 5, visits: 2,
  daily: [{ date: '2026-10-02', views: 5, visits: 2 }],
  pages: [{ path: '/claims/example.html', views: 2 }, { path: '/claims/example/', views: 3 }],
  pagesComplete: true, referrers: [{ host: 'search.naver.com', views: 5 }],
  devices: [{ device: 'mobile', views: 5 }],
});
const catalog = [{ path: '/claims/example', title: '예시, "서류"' }, { path: '/claims/other', title: '다른 글' }];

test('CSV has UTF-8 BOM, snapshot dates, aliases combined and escaped titles', () => {
  const csv = buildAnalyticsCsv(report(), catalog);
  assert.ok(csv.startsWith('\uFEFF'));
  assert.match(csv, /"page","2026-10-02","2026-10-02","2026-10-02T03:00:00Z","\/claims\/example","예시, ""서류""","",5,"","complete"/);
  assert.match(csv, /"\/claims\/other","다른 글","",0,"","complete"/);
  assert.ok(!csv.includes('password'));
});

test('partial results leave missing page views unknown, not zero', () => {
  const data = report(); data.pagesComplete = false;
  assert.match(buildAnalyticsCsv(data, catalog), /"\/claims\/other","다른 글","","","","unknown"/);
});

test('article snapshot exports only selected path and retains non-article pages for site snapshots', () => {
  const data = report(); data.path = '/claims/example';
  assert.ok(!buildAnalyticsCsv(data, catalog).includes('/claims/other'));
  data.path = null; data.pages.push({ path: '/insurance-companies/', views: 1 });
  assert.match(buildAnalyticsCsv(data, catalog), /"\/insurance-companies","","",1/);
});

test('formula-like strings are inert, even with leading whitespace', () => {
  const data = report(); data.referrers[0].host = '  =HYPERLINK("https://example.com")';
  const csv = buildAnalyticsCsv(data, [{ path: '/claims/example', title: '@SUM(1)' }]);
  assert.ok(csv.includes('"\'  =HYPERLINK(""https://example.com"")"'));
  assert.ok(csv.includes('"\'@SUM(1)"'));
});

test('missing data and invalid metrics cannot be downloaded as a zero report', () => {
  assert.throws(() => buildAnalyticsCsv(null));
  const data = report(); data.views = NaN;
  assert.throws(() => buildAnalyticsCsv(data));
});
