from pathlib import Path
from bs4 import BeautifulSoup
import requests,json,hashlib
R=Path(__file__).resolve().parents[1];O=R/'docs/surgery-table-rewrite-2026-11-03';U='https://hospital.hbuby.com/surgery-benefit/surgery-classification'
s=BeautifulSoup((R/'surgery-benefit/surgery-classification.html').read_text(encoding='utf8'),'html.parser');r=requests.get(U,timeout=40);r.raise_for_status();p=BeautifulSoup(r.text,'html.parser')
def norm(n):return ' '.join(n.stripped_strings)
assert norm(s.main)==norm(p.main),'Public body not yet current'
assert p.select_one('link[rel=canonical]')['href']==U
assert len(p.select('h1'))==1 and len(p.select('.source-table tbody tr'))==11
assert [x.get('href') for x in s.main.find_all('a')]==[x.get('href') for x in p.main.find_all('a')]
assert [x.get_text() for x in s.head.find_all('style')]==[x.get_text() for x in p.head.find_all('style')]
assert not [a['href'] for a in p.main.find_all('a',href=True) if a['href'].startswith('#') and not p.find(id=a['href'][1:])]
imgs=[]
for x in p.main.find_all('img'):
 q=requests.get('https://hospital.hbuby.com'+x['src'],timeout=25);q.raise_for_status();assert hashlib.sha256(q.content).digest()==hashlib.sha256((R/x['src'].lstrip('/')).read_bytes()).digest();imgs.append(x['src'])
result={'url':U,'status':'passed','http_status':r.status_code,'example_rows':11,'local_public_body_links_styles':'match','images_verified':imgs,'indexing':'not checked or requested'}
(O/'public-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(result,ensure_ascii=False))
