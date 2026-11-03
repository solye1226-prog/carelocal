from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests,json
O=Path(__file__).resolve().parents[1]/'docs/maintenance-2026-11-04';O.mkdir(exist_ok=True)
paths=['/','/surgery-benefit/surgery-classification','/claims/insurance-claim-process','/silbi/leqembi-silbi-claim','/surgery-benefit/cataract-surgery-benefit.html','/api/hospitals','/api/analytics','/assets/site.css','/maintenance-probe-not-a-page','/robots.txt','/ads.txt']
def check(path):
 r=requests.get('https://hospital.hbuby.com'+path,timeout=35);h={k.lower():v for k,v in r.headers.items()};metadata=path in ['/robots.txt','/ads.txt']
 ok=r.status_code==200 if metadata else (r.status_code==503 and h.get('x-carelocal-maintenance')=='enabled' and h.get('retry-after')=='3600' and 'no-store' in h.get('cache-control','') and '<script' not in r.text.lower() and 'adsbygoogle' not in r.text.lower())
 return {'path':path,'final_url':r.url,'status':r.status_code,'maintenance':h.get('x-carelocal-maintenance'),'retry_after':h.get('retry-after'),'cache_control':h.get('cache-control'),'scripts':'<script' in r.text.lower(),'passed':ok}
with ThreadPoolExecutor(max_workers=4) as ex:results=list(ex.map(check,paths))
(O/'hospital-public-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(results,ensure_ascii=True));assert all(x['passed'] for x in results),'Deployment not fully current'
