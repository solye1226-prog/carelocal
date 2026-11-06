"""Verify restored public routes without executing JavaScript or advertising."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import json
import re
import requests

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/maintenance-restored-2026-11-06'
OUT.mkdir(exist_ok=True)
PATHS = ['/', '/surgery-benefit/surgery-classification',
         '/claims/insurance-claim-process', '/silbi/leqembi-silbi-claim',
         '/surgery-benefit/cataract-surgery-benefit.html', '/assets/site.css',
         '/sitemap.xml', '/robots.txt', '/ads.txt']

def check(path):
    response = requests.get('https://hospital.hbuby.com' + path, timeout=35)
    response.encoding = 'utf-8'
    title = re.search(r'<title>(.*?)</title>', response.text, re.S)
    canonical = re.search(r'<link[^>]*rel=["\x27]canonical["\x27][^>]*>', response.text)
    local = ROOT / (path.strip('/') or 'index.html')
    if not local.suffix:
        local = local.with_suffix('.html')
    # Pages adds its existing analytics beacon at the edge; article content must match.
    normalized = re.sub(r'<!-- Cloudflare Pages Analytics -->.*?<!-- Cloudflare Pages Analytics -->', '', response.text, flags=re.S)
    local_match = normalized == local.read_text(encoding='utf-8') if local.is_file() else None
    return dict(path=path, url=response.url, status=response.status_code,
                maintenance=response.headers.get('X-Carelocal-Maintenance'),
                title=title.group(1).strip() if title else None,
                canonical=canonical.group(0) if canonical else None,
                matches_local=local_match,
                passed=response.status_code == 200
                and not response.headers.get('X-Carelocal-Maintenance')
                and '잠시 점검하고 있습니다' not in response.text
                and local_match is not False)

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(check, PATHS))
report = dict(checked_at=datetime.now(timezone.utc).isoformat(),
              method='HTTP only; no JavaScript or advertisement execution', results=results)
(OUT / 'public-verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(results, ensure_ascii=True, indent=2))
assert all(row['passed'] for row in results), 'Restoration not fully verified'
