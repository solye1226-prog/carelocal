from pathlib import Path
import json,sys,requests
from bs4 import BeautifulSoup
from publish_trend610_20261027 import DATA,OUT,ROOT,BASE
n=int(sys.argv[1]);d=DATA[n-6]
local=BeautifulSoup((ROOT/(d['path'][1:]+'.html')).read_text('utf-8'),'html.parser')
r=requests.get(BASE+d['path'],timeout=40);s=BeautifulSoup(r.text,'html.parser')
text=lambda x:' '.join(x.main.stripped_strings) if x.main else ''
rec={'n':n,'url':r.url,'status':r.status_code,'bodyMatches':text(local)==text(s),'canonical':s.find('link',rel='canonical')['href'] if s.find('link',rel='canonical') else None,'images':[]}
if rec['bodyMatches']:
 for im in s.main.find_all('img'):
  ir=requests.get(BASE+im['src'],timeout=40);rec['images'].append({'url':ir.url,'status':ir.status_code,'bytes':len(ir.content)})
 pr=requests.get(BASE+d['parent'],timeout=40);ps=BeautifulSoup(pr.text,'html.parser');rec['parentLinksNew']=bool(ps.find('a',href=d['path']));rec['newLinksParent']=bool(s.find('a',href=d['parent']))
 before=BeautifulSoup((OUT/(Path(d['parent']).name+'-before.html')).read_text('utf-8'),'html.parser')
 after=BeautifulSoup((ROOT/(d['parent'][1:]+'.html')).read_text('utf-8'),'html.parser');after.find(id='trend610-related').decompose();rec['parentBodyPreserved']=text(before)==text(after)
rec['passed']=rec['bodyMatches'] and rec['status']==200 and rec['canonical']==BASE+d['path'] and all(x['status']==200 for x in rec['images']) and len(rec['images'])==3 and rec.get('parentLinksNew',False) and rec.get('newLinksParent',False) and rec.get('parentBodyPreserved',False)
(OUT/f'{n}-public-audit.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2),'utf-8')
print(json.dumps(rec,ensure_ascii=False));sys.exit(0 if rec['passed'] else 1)
