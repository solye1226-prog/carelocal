from pathlib import Path
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import requests,json,re
R=Path(__file__).resolve().parents[1];O=R/'docs/related-next10-2026-11-02';B='https://hospital.hbuby.com'
files=set()
for name in [f'changed-{n}.json' for n in range(1,11)]:
 files.update(json.loads((O/name).read_text(encoding='utf8')))
def norm(s):return re.sub(r'\s+',' ',s.get_text(' ',strip=True)).strip()
def audit(f):
 local=BeautifulSoup((R/f).read_text(encoding='utf8'),'html.parser');url=local.find('link',rel='canonical')['href']
 r=requests.get(url,timeout=35);r.raise_for_status();pub=BeautifulSoup(r.text,'html.parser')
 assert pub.find('link',rel='canonical')['href']==url,'canonical'
 assert norm(pub.title)==norm(local.title),'title: '+url
 assert norm(pub.main)==norm(local.main),'body stale: '+url
 assert [x.get('href') for x in pub.main.find_all('a')]==[x.get('href') for x in local.main.find_all('a')],'links'
 assert [x.get('src') for x in pub.main.find_all('img')]==[x.get('src') for x in local.main.find_all('img')],'images'
 assert [x.get_text() for x in pub.head.find_all('style')]==[x.get_text() for x in local.head.find_all('style')],'inline CSS stale: '+url
 assert [x.get('href') for x in pub.select('link[rel=stylesheet]')]==[x.get('href') for x in local.select('link[rel=stylesheet]')],'CSS links stale: '+url
 lm=local.find('meta',attrs={'name':'description'});pm=pub.find('meta',attrs={'name':'description'})
 if lm:assert pm and lm['content']==pm['content'],'description'
 robots=pub.find('meta',attrs={'name':'robots'});assert not robots or 'noindex' not in robots.get('content','').lower()
 return {'url':url,'status':r.status_code,'title_body_links_images':'match','indexing':'not verified'}
with ThreadPoolExecutor(max_workers=6) as ex:results=list(ex.map(audit,sorted(f for f in files if f.endswith('.html'))))
(O/'public-final.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'verified':len(results),'status':'passed'},ensure_ascii=False))
