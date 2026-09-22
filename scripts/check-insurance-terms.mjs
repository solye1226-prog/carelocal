import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { articles } from './insurance-terms-data.mjs';

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const require = createRequire(import.meta.url);
const [base = 'http://localhost:8788', moduleRoot] = process.argv.slice(2);
const { chromium } = moduleRoot ? require(join(moduleRoot, 'playwright')) : require('playwright');
const output = join(root, '.deploy', 'terms-qa');
mkdirSync(output, { recursive: true });
const browser = await chromium.launch({ headless: true, channel: process.env.PLAYWRIGHT_CHANNEL || 'msedge' });
const reports = [];
const sample = process.argv.includes('--sample');
try {
  for (const width of [1440, 390, 320]) {
    const page = await browser.newPage({ viewport: { width, height: 900 } });
    await page.route('**/*', route => {
      const url = new URL(route.request().url());
      return url.origin === new URL(base).origin ? route.continue() : route.abort();
    });
    for (const a of sample ? articles.slice(0, 1) : articles) {
      const response = await page.goto(`${base}/${a.section}/${a.slug}.html`, { waitUntil: 'networkidle' });
      assert.equal(response.status(), 200, a.slug);
      assert.equal(await page.locator('h1').innerText(), a.title);
      await page.locator('main img').evaluateAll(images => images.forEach(img => { img.loading = 'eager'; }));
      await page.waitForFunction(() => [...document.querySelectorAll('main img')].every(img => img.complete && img.naturalWidth > 0));
      const stats = await page.evaluate(() => ({
        width: innerWidth, scrollWidth: document.documentElement.scrollWidth,
        imageCount: document.querySelectorAll('main img').length,
        fontSize: getComputedStyle(document.querySelector('main section p')).fontSize,
        tableWidth: document.querySelector('table').getBoundingClientRect().width,
        firstCellWidth: document.querySelector('td').getBoundingClientRect().width,
        firstCellBackgrounds: [...document.querySelectorAll('tbody tr td:first-child')].map(cell => getComputedStyle(cell).backgroundColor),
        kakaoBackground: getComputedStyle(document.querySelector('.kakao-button')).backgroundColor,
        textLength: document.querySelector('main').innerText.length,
        replacementCharacters: document.querySelector('main').innerText.includes('\uFFFD'),
        canonical: document.querySelector('link[rel=canonical]').href,
        imageSizes: [...document.querySelectorAll('main img')].map(i => [i.naturalWidth, i.naturalHeight]),
      }));
      assert.ok(stats.scrollWidth <= width + 1, `${a.slug}: page overflow at ${width}`);
      assert.equal(stats.imageCount, 3, a.slug);
      assert.equal(stats.replacementCharacters, false, a.slug);
      assert.ok(parseFloat(stats.fontSize) >= 18, `${a.slug}: body type too small`);
      assert.ok(stats.textLength > 1800, `${a.slug}: unexpectedly short article`);
      if (width <= 390) assert.ok(stats.firstCellWidth >= stats.tableWidth - 3, `${a.slug}: narrow mobile first cell`);
      if (width <= 390) assert.ok(stats.firstCellBackgrounds.every(color => color === 'rgb(23, 33, 43)'), `${a.slug}: mobile row heading contrast`);
      assert.equal(stats.canonical, `https://hospital.hbuby.com/${a.section}/${a.slug}`);
      reports.push({ order: a.order, path: `/${a.section}/${a.slug}`, ...stats });
      if ([4, 13, 18].includes(a.order)) {
        await page.screenshot({ path: join(output, `${a.order}-${width}-top.png`) });
        await page.locator('table').scrollIntoViewIfNeeded();
        await page.screenshot({ path: join(output, `${a.order}-${width}-table.png`) });
        await page.locator('.kakao-inquiry-cta').scrollIntoViewIfNeeded();
        await page.screenshot({ path: join(output, `${a.order}-${width}-footer.png`) });
      }
    }
    if (!sample) {
      for (const [path, count] of [['/standards/', 9], ['/standards/page/2/', 7]]) {
        await page.goto(base + path, { waitUntil: 'networkidle' });
        assert.equal(await page.locator('.post-card').count(), count);
        assert.equal(await page.locator('.pagination [aria-current=page]').count(), 1);
        const sizes = await page.locator('.post-card').evaluateAll(cards => cards.slice(0, 3).map(c => c.getBoundingClientRect().height));
        if (width === 1440) assert.ok(Math.max(...sizes) - Math.min(...sizes) < 2, 'Unequal desktop card heights');
        assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1));
        await page.screenshot({ path: join(output, `index-${count}-${width}.png`), fullPage: true });
      }
    }
    await page.close();
  }
  writeFileSync(join(output, 'results.json'), JSON.stringify({ base, reports }, null, 2));
  console.log(`PASS: ${reports.length} article viewport checks; screenshots: ${output}`);
} finally {
  await browser.close();
}
