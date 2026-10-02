const pathKey = (path) => path.replace(/\.html$/, '').replace(/\/$/, '') || '/';

function cell(value) {
  if (typeof value === 'number') {
    if (!Number.isFinite(value) || value < 0) throw new Error('Invalid metric');
    return String(value);
  }
  let text = String(value ?? '');
  // Spreadsheet applications may execute formula-like text even inside quotes.
  if (/^[\s\u0000-\u001f]*[=+@-]/.test(text) || /^[\t\r\n]/.test(text)) text = `'${text}`;
  return `"${text.replaceAll('"', '""')}"`;
}

export function buildAnalyticsCsv(report, catalog = []) {
  if (!report?.daily?.length || !Array.isArray(report.pages) || !Array.isArray(report.referrers) || !Array.isArray(report.devices)) {
    throw new Error('Missing report');
  }
  const start = report.daily[0].date;
  const end = report.daily.at(-1).date;
  const scope = report.path ? pathKey(report.path) : '';
  const coverage = report.pagesComplete ? 'complete' : 'partial';
  const rows = [['record_type', 'start_date', 'end_date', 'generated_at', 'page_path', 'title', 'dimension', 'views', 'visits', 'coverage']];
  const add = (type, path, title, dimension, views, visits, status = 'collected') => {
    rows.push([type, start, end, report.generatedAt, path, title, dimension, views, visits, status]);
  };
  add('summary', scope, '', '', report.views, report.visits);
  for (const day of report.daily) add('daily', scope, '', day.date, day.views, day.visits);
  for (const referrer of report.referrers) add('referrer', scope, '', referrer.host || '(direct or unknown)', referrer.views, '');
  for (const device of report.devices) add('device', scope, '', device.device, device.views, '');

  const counts = new Map();
  for (const page of report.pages) {
    const key = pathKey(page.path);
    if (!Number.isFinite(page.views) || page.views < 0) throw new Error('Invalid metric');
    counts.set(key, (counts.get(key) || 0) + page.views);
  }
  const titles = new Map(catalog.map((article) => [pathKey(article.path), article.title]));
  const paths = scope ? new Set([scope]) : new Set([...titles.keys(), ...counts.keys()]);
  for (const path of paths) {
    const known = counts.has(path) || report.pagesComplete;
    add('page', path, titles.get(path) || '', '', known ? counts.get(path) || 0 : '', '', known ? coverage : 'unknown');
  }
  return '\uFEFF' + rows.map((row) => row.map(cell).join(',')).join('\r\n') + '\r\n';
}
