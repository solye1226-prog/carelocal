// Change to false and deploy to restore the existing site and API handlers.
export const MAINTENANCE_ENABLED = true;

export const MAINTENANCE_HTML = `<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>사이트 점검 안내 | 케어로컬</title><style>
*{box-sizing:border-box}body{margin:0;min-height:100vh;display:grid;place-items:center;background:#f3f6fa;color:#172d46;font-family:system-ui,"Malgun Gothic",sans-serif;padding:24px}.card{max-width:620px;width:100%;background:#fff;border:1px solid #dce5ee;border-radius:20px;padding:clamp(28px,7vw,56px);box-shadow:0 20px 60px #17304b0b}.brand{color:#315e88;font-weight:700;letter-spacing:.06em}.badge{display:inline-block;margin:28px 0 6px;padding:7px 12px;border-radius:30px;background:#eef4fa;font-size:14px}h1{font-size:clamp(27px,5vw,38px);line-height:1.5;word-break:keep-all;margin:16px 0}p{font-size:17px;line-height:1.9;word-break:keep-all;color:#52677c}.footer{margin-top:32px;padding-top:20px;border-top:1px solid #e4eaf1;font-size:13px;color:#6c7f91}
</style></head><body><main class="card"><div class="brand">케어로컬</div><span class="badge">사이트 점검 안내</span><h1>더 나은 안내를 위해<br>잠시 점검하고 있습니다.</h1><p>점검 중에는 게시글을 이용하실 수 없습니다.<br>잠시 후 다시 방문해 주세요.</p><p class="footer">hospital.hbuby.com</p></main></body></html>`;

export function handleRequest(context, enabled = MAINTENANCE_ENABLED) {
  const { pathname } = new URL(context.request.url);
  if (!enabled || pathname === '/robots.txt' || pathname === '/ads.txt') {
    return context.next();
  }
  return new Response(context.request.method === 'HEAD' ? null : MAINTENANCE_HTML, {
    status: 503,
    headers: {
      'Content-Type': 'text/html; charset=utf-8',
      'Cache-Control': 'no-store, max-age=0',
      'Retry-After': '3600',
      'X-Carelocal-Maintenance': 'enabled',
      'Content-Security-Policy': "default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'",
      'X-Content-Type-Options': 'nosniff',
      'Referrer-Policy': 'no-referrer',
    },
  });
}

export function onRequest(context) {
  return handleRequest(context);
}
