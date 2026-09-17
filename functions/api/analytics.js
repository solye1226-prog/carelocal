const ACCOUNT = '711d4c4f4c33bbf38637e372b5141b94';
const SITE = '4c272d6ba9604360826d7c1090a5adbb';
const HOST = 'hospital.hbuby.com';

function reply(body, status = 200) {
  return new Response(JSON.stringify(body), { status, headers: {
    'Content-Type': 'application/json; charset=utf-8',
    'Cache-Control': 'private, no-store',
    'X-Robots-Tag': 'noindex, nofollow, noarchive',
    'X-Content-Type-Options': 'nosniff',
    'Vary': 'Authorization',
  } });
}

async function matches(value, expected) {
  const hash = async (text) => new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text)));
  const [a, b] = await Promise.all([hash(value), hash(expected)]);
  let difference = 0;
  for (let i = 0; i < a.length; i++) difference |= a[i] ^ b[i];
  return difference === 0;
}

function number(value) {
  if (typeof value !== 'number' || !Number.isFinite(value) || value < 0) throw new Error('Invalid metric');
  return Math.round(value);
}

function koreaDate(value) {
  return new Date(new Date(value).getTime() + 9 * 3600000).toISOString().slice(0, 10);
}

export function normalizePath(path) {
  return path.replace(/\.html$/, '').replace(/\/$/, '') || '/';
}

export function normalize(account, start, end) {
  if (!account || !['total', 'series', 'pages', 'referrers', 'devices'].every((key) => Array.isArray(account[key]))) throw new Error('Missing analytics');
  const daily = new Map();
  for (let day = new Date(`${koreaDate(start)}T00:00:00+09:00`); day <= end; day = new Date(day.getTime() + 86400000)) daily.set(koreaDate(day), { views: 0, visits: 0 });
  for (const row of account.series) {
    const date = koreaDate(row.dimensions.datetimeHour);
    if (!daily.has(date)) throw new Error('Unexpected date');
    const day = daily.get(date);
    day.views += number(row.count);
    day.visits += number(row.sum.visits);
  }
  const total = account.total[0];
  return {
    visits: total ? number(total.sum.visits) : 0,
    views: total ? number(total.count) : 0,
    daily: [...daily].map(([date, metrics]) => ({ date, ...metrics })),
    pages: account.pages.map((row) => {
      if (typeof row.dimensions.requestPath !== 'string') throw new Error('Missing path');
      return { path: row.dimensions.requestPath, views: number(row.count) };
    }),
    pagesComplete: account.pages.length < 10000,
    referrers: account.referrers.map((row) => ({ host: row.dimensions.refererHost || '', views: number(row.count) })),
    devices: account.devices.map((row) => ({ device: row.dimensions.deviceType || 'Unknown', views: number(row.count) })),
    generatedAt: end.toISOString(),
  };
}

export async function onRequest({ request, env }) {
  if (request.method !== 'GET') return reply({ message: '허용되지 않은 요청입니다.' }, 405);
  if (!env.CF_ANALYTICS_TOKEN || !env.ANALYTICS_ADMIN_PASSWORD || env.ANALYTICS_ADMIN_PASSWORD.length < 32) {
    return reply({ message: '통계 서버 연결 설정이 아직 완료되지 않았습니다.' }, 503);
  }
  const supplied = request.headers.get('Authorization') || '';
  if (supplied.length > 1024 || !await matches(supplied, `Bearer ${env.ANALYTICS_ADMIN_PASSWORD}`)) {
    return reply({ message: '운영자 인증이 필요합니다.' }, 401);
  }
  const url = new URL(request.url);
  const days = Number(url.searchParams.get('days') || 7);
  if (![1, 7, 30].includes(days)) return reply({ message: '조회 기간을 확인해 주세요.' }, 400);
  const end = new Date();
  const start = new Date(`${koreaDate(new Date(end.getTime() - (days - 1) * 86400000))}T00:00:00+09:00`);
  const path = url.searchParams.get('path');
  if (path && (!path.startsWith('/') || path.startsWith('//') || path.length > 500 || /[?#\\\u0000-\u001f]/.test(path))) {
    return reply({ message: '게시글 주소를 확인해 주세요.' }, 400);
  }
  // Only fixed account, site and hostname filters are sent upstream.
  const selectedPath = path ? normalizePath(path) : null;
  const paths = selectedPath ? [selectedPath, `${selectedPath}.html`, `${selectedPath}/`] : null;
  const pathFilter = paths ? `, requestPath_in: ${JSON.stringify(paths)}` : '';
  const queryFor = (from, to) => {
    const filter = `siteTag: "${SITE}", requestHost: "${HOST}", requestPath_notlike: "/dashboard%", datetime_geq: "${from.toISOString()}", datetime_lt: "${to.toISOString()}"${pathFilter}`;
    return `{ viewer { accounts(filter: { accountTag: "${ACCOUNT}" }) {
    total: rumPageloadEventsAdaptiveGroups(limit: 1, filter: {${filter}}) { count sum { visits } }
    series: rumPageloadEventsAdaptiveGroups(limit: 1000, filter: {${filter}}, orderBy: [datetimeHour_ASC]) { count sum { visits } dimensions { datetimeHour } }
    pages: rumPageloadEventsAdaptiveGroups(limit: 10000, filter: {${filter}}, orderBy: [count_DESC]) { count dimensions { requestPath } }
    referrers: rumPageloadEventsAdaptiveGroups(limit: 100, filter: {${filter}}, orderBy: [count_DESC]) { count dimensions { refererHost } }
    devices: rumPageloadEventsAdaptiveGroups(limit: 20, filter: {${filter}}, orderBy: [count_DESC]) { count dimensions { deviceType } }
  } } }`;
  };
  try {
    // Short windows avoid excessive adaptive sampling on a low-traffic site.
    const windows = [];
    for (let from = start; from < end;) {
      const to = new Date(Math.min(from.getTime() + 7 * 86400000, end.getTime()));
      windows.push([from, to]);
      from = to;
    }
    const accounts = await Promise.all(windows.map(async ([from, to]) => {
    const result = await fetch('https://api.cloudflare.com/client/v4/graphql', {
      method: 'POST',
      headers: { Authorization: `Bearer ${env.CF_ANALYTICS_TOKEN}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({ query: queryFor(from, to) }),
      signal: AbortSignal.timeout(20000),
    });
    if (!result.ok) throw new Error('Upstream failure');
    const data = await result.json();
    if (data.errors?.length) throw new Error('Analytics query failed');
    const account = data.data?.viewer?.accounts?.[0];
    if (!account || !['total', 'series', 'pages', 'referrers', 'devices'].every((key) => Array.isArray(account[key]))) throw new Error('Missing analytics');
    return account;
    }));
    const combined = { total: [{ count: 0, sum: { visits: 0 } }], series: [], pages: [], referrers: [], devices: [] };
    for (const account of accounts) {
      for (const row of account.total) { combined.total[0].count += number(row.count); combined.total[0].sum.visits += number(row.sum.visits); }
      combined.series.push(...account.series);
    }
    for (const [key, dimension] of [['pages', 'requestPath'], ['referrers', 'refererHost'], ['devices', 'deviceType']]) {
      const groups = new Map();
      for (const account of accounts) for (const row of account[key]) {
        const name = row.dimensions[dimension];
        groups.set(name, (groups.get(name) || 0) + number(row.count));
      }
      combined[key] = [...groups].map(([name, count]) => ({ count, dimensions: { [dimension]: name } })).sort((a, b) => b.count - a.count);
    }
    const report = normalize(combined, start, end);
    report.pagesComplete = accounts.every((account) => account.pages.length < 10000);
    return reply({ ...report, days, path: selectedPath });
  } catch {
    return reply({ message: 'Cloudflare 통계를 불러오지 못했습니다. 연결 권한 또는 조회 가능 기간을 확인해 주세요.' }, 502);
  }
}
