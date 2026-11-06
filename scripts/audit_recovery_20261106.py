"""Audit all sitemap routes via HTTP without loading advertising."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from html.parser import HTMLParser
from datetime import datetime, timezone
import requests, json, xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/naver-recovery-2026-11-06'
OUT.mkdir(exist_ok=True)
class Meta(HTMLParser):
    def __init__(self):
        super().__init__(); self.canonical=[]; self.robots=[]; self.h1=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='link' and a.get('rel')=='canonical': self.canonical.append(a.get('href'))
        if tag=='meta' and a.get('name','').lower() in ('robots','naverbot','yeti'): self.robots.append(a.get('content',''))
        if tag=='h1': self.h1+=1
urls=[e.text for e in ET.parse(ROOT/'sitemap.xml').findall('.//{*}loc')]
def check(url):
    try:
        r=requests.get(url,timeout=25);r.encoding='utf-8';p=Meta();p.feed(r.text)
        issues=[]
        if r.status_code!=200: issues.append('http_'+str(r.status_code))
        if r.url!=url: issues.append('redirect')
        if p.canonical!=[url]: issues.append('canonical')
        if any('noindex' in x.lower() for x in p.robots+[r.headers.get('X-Robots-Tag','')]): issues.append('noindex')
        if r.headers.get('X-Carelocal-Maintenance') or '잠시 점검하고 있습니다' in r.text: issues.append('maintenance')
        if not p.h1: issues.append('missing_h1')
        return dict(url=url,status=r.status_code,final_url=r.url,canonical=p.canonical,robots=p.robots,issues=issues)
    except requests.RequestException as e: return dict(url=url,issues=['request_error'],error=str(e))
rows=[]
with ThreadPoolExecutor(max_workers=5) as ex:
    for f in as_completed([ex.submit(check,u) for u in urls]):
        rows.append(f.result())
rows.sort(key=lambda x:x['url'])
report=dict(checked_at=datetime.now(timezone.utc).isoformat(),count=len(rows),issues=sum(bool(x['issues']) for x in rows),results=rows)
(OUT/'sitewide-http-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(count=len(rows),issues=[x for x in rows if x['issues']]),ensure_ascii=True))
