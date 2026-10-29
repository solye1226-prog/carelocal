from pathlib import Path
from bs4 import BeautifulSoup
import json,requests,sys
from decision_comparison10_20261029_data import UPDATES,NEW
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'docs/decision-comparison10-2026-10-29';BASE='https://hospital.hbuby.com'
def maintext(s):return ' '.join(s.main.stripped_strings) if s.main else ''
def verify(n):
 d=next(x for x in UPDATES+NEW if x['n']==n);f=ROOT/(d['path'][1:]+'.html');local=BeautifulSoup(f.read_text('utf-8'),'html.parser');r=requests.get(BASE+d['path'],timeout=35);s=BeautifulSoup(r.text,'html.parser');rec={'n':n,'url':r.url,'status':r.status_code,'bodyMatches':maintext(local)==maintext(s),'canonical':s.find('link',rel='canonical').get('href') if s.find('link',rel='canonical') else None,'h1':s.h1.get_text(' ',strip=True) if s.h1 else None}
 if rec['bodyMatches']:
  if d in NEW:
   rec['images']=[]
   for im in s.main.find_all('img'):
    ir=requests.get(BASE+im['src'],timeout=30);rec['images'].append({'src':im['src'],'status':ir.status_code,'bytes':len(ir.content)})
   pr=BeautifulSoup(requests.get(BASE+d['parent'],timeout=30).text,'html.parser');rec['parentLinksNew']=bool(pr.find('a',href=d['path']));rec['newLinksParent']=bool(s.find('a',href=d['parent']))
  else:
   before=BeautifulSoup((OUT/'before'/f.name).read_text('utf-8'),'html.parser');after=BeautifulSoup(str(local),'html.parser')
   for obj in [before,after]:
    for node in obj.main.select('[id^="decision-refresh-"],#decision-new-related'):node.decompose()
   rec['oldBodyPreserved']=maintext(before)==maintext(after);rec['oldImagesPreserved']=[str(im) for im in before.main.find_all('img')]==[str(im) for im in after.main.find_all('img')]
 rec['passed']=rec['bodyMatches'] and rec['status']==200 and rec['canonical']==BASE+d['path'] and (all(x['status']==200 for x in rec.get('images',[]))) and rec.get('parentLinksNew',True) and rec.get('newLinksParent',True) and rec.get('oldBodyPreserved',True) and rec.get('oldImagesPreserved',True)
 (OUT/f'{n:02d}-public-audit.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2),'utf-8');return rec
if __name__=='__main__':
 result=verify(int(sys.argv[1]));print(json.dumps(result,ensure_ascii=False));sys.exit(0 if result['passed'] else 1)
