from refine_keyword5_20261029 import ROOT,OUT,DATA
from bs4 import BeautifulSoup
import requests,json,sys

def text(s):return ' '.join(s.main.stripped_strings)
def verify(n):
 d=next(x for x in DATA if x['n']==n);f=ROOT/(d['path'][1:]+'.html')
 local=BeautifulSoup(f.read_text('utf-8'),'html.parser')
 r=requests.get('https://hospital.hbuby.com'+d['path'],timeout=30)
 s=BeautifulSoup(r.text,'html.parser')
 rec={'n':n,'url':r.url,'status':r.status_code,'title':s.title.get_text() if s.title else None,'bodyMatches':bool(s.main) and text(s)==text(local)}
 if not s.main or not s.h1 or not s.find('link',rel='canonical'):
  rec.update(passed=False,error='Incomplete public HTML for verification')
  (OUT/f'{n:02d}-public-audit.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2),'utf-8')
  return rec
 rec['canonicalMatches']=s.find('link',rel='canonical')['href']=='https://hospital.hbuby.com'+d['path']
 rec['h1Matches']=s.h1.get_text()==d['title']
 rec['metadataMatches']=all(s.find('meta',attrs={a:v}) and s.find('meta',attrs={a:v}).get('content')==local.find('meta',attrs={a:v}).get('content') for a,v in [('name','description'),('property','og:title'),('property','og:description'),('name','twitter:title'),('name','twitter:description')])
 rec['relatedLinks']=all(s.main.find('a',href=p) for p in d['related'])
 old=BeautifulSoup((OUT/'before'/f.name).read_text('utf-8'),'html.parser')
 rec['imagesPreserved']=[str(i) for i in old.main.find_all('img')]==[str(i) for i in s.main.find_all('img')]
 rec['images']=[]
 for im in s.main.find_all('img'):
  ir=requests.get('https://hospital.hbuby.com'+im['src'],timeout=30)
  rec['images'].append({'src':im['src'],'status':ir.status_code})
 rec['passed']=r.status_code==200 and rec['title']==d['title'] and all(rec[k] for k in ['bodyMatches','canonicalMatches','h1Matches','metadataMatches','relatedLinks','imagesPreserved']) and all(x['status']==200 for x in rec['images'])
 (OUT/f'{n:02d}-public-audit.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2),'utf-8')
 return rec

if __name__=='__main__':
 r=verify(int(sys.argv[1]));print(json.dumps(r,ensure_ascii=False));sys.exit(0 if r['passed'] else 1)
