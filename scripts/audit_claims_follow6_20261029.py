from pathlib import Path
from bs4 import BeautifulSoup
import json,sys,requests,hashlib,subprocess
from claims_follow6_data import DATA
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'docs/claims-follow5-publication-2026-10-29';BASE='https://hospital.hbuby.com'
def public(n):
 d=DATA[n-1];u=BASE+d['path']+'?v=20261029follow6';r=requests.get(u,timeout=30);r.encoding='utf-8';s=BeautifulSoup(r.text,'html.parser');local=BeautifulSoup((ROOT/(d['path'][1:]+'.html')).read_text(encoding='utf-8'),'html.parser')
 result={'url':BASE+d['path'],'verificationUrl':u,'status':r.status_code,'title':s.h1.get_text() if s.h1 else None,'canonical':s.find('link',rel='canonical').get('href') if s.find('link',rel='canonical') else None,'bodyMatches':bool(s.main and s.main.get_text(' ',strip=True)==local.main.get_text(' ',strip=True)),'images':[],'parents':[]}
 if result['title']!=d['title'] or not result['bodyMatches']:print(json.dumps(result,ensure_ascii=False));sys.exit(2)
 for im in s.main.find_all('img'):
  src=im['src'];rr=requests.get(BASE+src+'?v=20261029follow6',timeout=30);raw=(ROOT/src[1:]).read_bytes();result['images'].append({'src':src,'status':rr.status_code,'hashMatches':hashlib.sha256(rr.content).digest()==hashlib.sha256(raw).digest()})
 for parent in d['parents']:
  rr=requests.get(BASE+parent+'?v=20261029follow6',timeout=30);rr.encoding='utf-8';ss=BeautifulSoup(rr.text,'html.parser');result['parents'].append({'path':parent,'status':rr.status_code,'newLink':bool(ss.select_one('a[href="'+d['path']+'"]'))})
 result['passed']=result['canonical']==BASE+d['path'] and all(x['hashMatches'] for x in result['images']) and all(x['newLink'] for x in result['parents'])
 (OUT/f'{n}-public-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result,ensure_ascii=False));return result['passed']
def preserve():
 results=[]
 for path in sorted({x for d in DATA for x in d['parents']}):
  f=path[1:]+'.html';old=BeautifulSoup(subprocess.check_output(['git','show','bb8829c:'+f],cwd=ROOT).decode('utf-8'),'html.parser');new=BeautifulSoup((ROOT/f).read_text(encoding='utf-8'),'html.parser')
  for x in new.select('[id^=follow6-]'):x.decompose()
  results.append({'path':path,'bodyPreserved':old.main.get_text(' ',strip=True)==new.main.get_text(' ',strip=True),'titlePreserved':old.title.string==new.title.string,'imagesPreserved':[x.get('src') for x in old.main.find_all('img')]==[x.get('src') for x in new.main.find_all('img')],'canonicalPreserved':old.find('link',rel='canonical')['href']==new.find('link',rel='canonical')['href']})
 (OUT/'parent-preservation.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(results,ensure_ascii=False))
if __name__=='__main__':
 if sys.argv[1]=='preserve':preserve()
 else:sys.exit(0 if public(int(sys.argv[1])) else 2)
