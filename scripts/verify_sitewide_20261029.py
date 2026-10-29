from pathlib import Path
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import requests,json

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/sitewide-reinforcement-2026-10-29'
def verify(item):
 path=item['path'];local=BeautifulSoup((ROOT/(path[1:]+'.html')).read_text('utf-8'),'html.parser');rec={'path':path}
 try:
  r=requests.get('https://hospital.hbuby.com'+path,timeout=30);s=BeautifulSoup(r.text,'html.parser');rec['status']=r.status_code
  rec['bodyMatches']=bool(s.main) and ' '.join(s.main.stripped_strings)==' '.join(local.main.stripped_strings)
  rec['titleMatches']=bool(s.title) and s.title.get_text()==local.title.get_text()
  c=s.find('link',rel='canonical');rec['canonicalMatches']=bool(c) and c['href']=='https://hospital.hbuby.com'+path
  rec['imagesMatch']=bool(s.main) and [str(i) for i in s.main.find_all('img')]==[str(i) for i in local.main.find_all('img')]
  rec['linksMatch']=bool(s.main) and [a['href'] for a in s.main.find_all('a',href=True)]==[a['href'] for a in local.main.find_all('a',href=True)]
  rec['passed']=r.status_code==200 and all(rec.get(k) for k in ['bodyMatches','titleMatches','canonicalMatches','imagesMatch','linksMatch'])
 except Exception as e:rec.update(passed=False,error=str(e))
 return rec
if __name__=='__main__':
 items=json.loads((OUT/'manifest.json').read_text('utf-8'))
 with ThreadPoolExecutor(max_workers=6) as p:rs=list(p.map(verify,items))
 (OUT/'public-audit.json').write_text(json.dumps(rs,ensure_ascii=False,indent=2),'utf-8')
 print(json.dumps({'passed':sum(x['passed'] for x in rs),'total':len(rs),'failed':[x for x in rs if not x['passed']]},ensure_ascii=False))
