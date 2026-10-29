from pathlib import Path
from bs4 import BeautifulSoup
import sys,json,re
from decision_comparison10_20261029_data import UPDATES,NEW,CSS
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/decision-comparison10-2026-10-29'
def update(n):
 d=next(x for x in UPDATES if x['n']==n);f=ROOT/(d['path'][1:]+'.html');raw=f.read_text('utf-8');s=BeautifulSoup(raw,'html.parser')
 if s.find(id='decision-refresh-'+str(n)):raise RuntimeError('Already updated')
 (OUT/'before').mkdir(exist_ok=True);(OUT/'before'/f.name).write_text(raw,'utf-8')
 style=s.new_tag('style');style.string=CSS;s.head.append(style)
 module=BeautifulSoup('<section class="decision-refresh" id="decision-refresh-'+str(n)+'">'+d['module']+'</section>','html.parser');first=s.main.find('h2')
 if first:first.insert_before(module)
 else:s.main.append(module)
 for sc in s.find_all('script',type='application/ld+json'):
  try:
   obj=json.loads(sc.string)
   if isinstance(obj,dict) and obj.get('@type') in ['Article','BlogPosting']:obj['dateModified']='2026-10-29';sc.string=json.dumps(obj,ensure_ascii=False)
  except (TypeError,ValueError):pass
 f.write_text(str(s)+'\n','utf-8')
 sm=ROOT/'sitemap.xml';txt=sm.read_text('utf-8');txt=re.sub(r'(<loc>https://hospital\.hbuby\.com'+re.escape(d['path'])+r'</loc>\s*<lastmod>)[^<]+',r'\g<1>2026-10-29',txt);sm.write_text(txt,'utf-8')
 before=BeautifulSoup(raw,'html.parser');after=BeautifulSoup(str(s),'html.parser');after.find(id='decision-refresh-'+str(n)).decompose()
 body=lambda x:' '.join(x.main.stripped_strings)
 assert body(before)==body(after)
 assert str(before.h1)==str(after.h1) and str(before.title)==str(after.title)
 assert [str(x) for x in before.find_all('meta')]==[str(x) for x in after.find_all('meta')]
 assert [str(x) for x in before.main.find_all('img')]==[str(x) for x in after.main.find_all('img')]
 (OUT/f'{n:02d}-preservation.json').write_text(json.dumps({'path':d['path'],'bodyPreserved':True,'titlePreserved':True,'metaPreserved':True,'imagesPreserved':True},ensure_ascii=False,indent=2),'utf-8')
 print(json.dumps({'n':n,'path':d['path'],'preserved':True},ensure_ascii=False))
if __name__=='__main__':update(int(sys.argv[1]))
