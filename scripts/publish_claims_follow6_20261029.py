"""Build exactly one reviewed article; deployment is a separate verified step."""
from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image
import json,sys,subprocess,re,hashlib
from claims_follow6_data import DATA
from publish_trend5_20261027 import CSS,a
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/claims-follow5-publication-2026-10-29'
BASE='https://hospital.hbuby.com'
DATE='2026-10-29'
def figure(d,key):
 path='/assets/images/'+d['slug']+'-'+key+'.webp'
 with Image.open(ROOT/path[1:]) as im:w,hh=im.size
 return f'<figure><img src="{path}" width="{w}" height="{hh}" alt="{d["title"]} 관련 자료 확인" loading="{"eager" if key=="thumb" else "lazy"}" decoding="async">'+('<figcaption>AI로 만든 설명용 이미지이며 실제 환자·진료기록이나 공식 기관 화면이 아닙니다.</figcaption>' if key=='thumb' else '')+'</figure>'
def publish(n):
 d=DATA[n-1]; dest=ROOT/(d['path'][1:]+'.html')
 if dest.exists():raise SystemExit('Refusing overwrite '+str(dest))
 soup=BeautifulSoup((ROOT/'surgery-benefit/wound-suture-specific-rider.html').read_text(encoding='utf-8'),'html.parser')
 soup.title.string=d['title']
 meta={'description':d['desc'],'og:title':d['title'],'og:description':d['desc'],'og:image':BASE+'/assets/images/'+d['slug']+'-thumb.webp','og:url':BASE+d['path'],'twitter:title':d['title'],'twitter:description':d['desc'],'twitter:image':BASE+'/assets/images/'+d['slug']+'-thumb.webp'}
 for key,value in meta.items():
  attr='property' if key.startswith('og:') else 'name'
  el=soup.find('meta',attrs={attr:key})
  if el:el['content']=value
  else:soup.head.append(soup.new_tag('meta',attrs={attr:key,'content':value}))
 soup.find('link',rel='canonical')['href']=BASE+d['path']
 schema=json.loads(soup.find('script',type='application/ld+json').string)
 schema.update(headline=d['title'],description=d['desc'],image=meta['og:image'],mainEntityOfPage=BASE+d['path'],datePublished=DATE,dateModified=DATE)
 soup.find('script',type='application/ld+json').string=json.dumps(schema,ensure_ascii=False)
 style=soup.new_tag('style');style.string=CSS+' .trend5 .cell-label{display:none}@media(max-width:600px){.trend5 .trend-table table{min-width:0}.trend5 .cell-label{display:block}}';soup.head.append(style)
 cta=str(soup.main.find('section',class_='kakao-inquiry-cta'))
 soup.main.clear();soup.main['class']=['section','article-body','insurance-series-article','cluster-reading','trend5']
 section=d['path'].split('/')[1]
 content='<div class="breadcrumb">'+a('/','홈')+' / '+a('/'+section+'/',d['cat'])+'</div><h1>'+d['title']+'</h1><p class="lead">'+d['desc']+'</p><div class="insurance-company-cta">'+a('/insurance-companies/','보험사별 공식 홈페이지 확인하기')+'</div>'+figure(d,'thumb')
 for i,part in enumerate(d['body']):
  content+=part
  if i==1:content+=figure(d,'body1')
  if i==3:content+=figure(d,'body2')
 content+='<section class="official-guide-actions" aria-label="공식 상세 안내"><h2>공식 확인처와 상세 안내</h2><div class="official-guide-grid">'
 for url,title,scope in d['sources']:content+=f'<a class="official-guide-button" href="{url}" target="_blank" rel="noopener"><strong>{title}</strong><span>{scope} · 새 창 ↗</span></a>'
 content+='</div></section><p>작성: 케어로컬 사이트 운영자. '+a('/legal/about','작성 기준과 운영자 역할')+'을 확인할 수 있습니다. 의학적 진단과 치료는 의료진에게, 개별 보험계약의 보장은 해당 보험사에 확인하세요.</p><div class="insurance-company-cta">'+a('/insurance-companies/','보험사별 공식 홈페이지 확인하기')+'</div>'+cta
 soup.main.append(BeautifulSoup(content,'html.parser'))
 for im in soup.main.select('figure img'):im['alt']=d['title']+' 관련 자료를 확인하는 설명용 장면'
 for tb in soup.main.find_all('table'):
  headers=[t.get_text(' ',strip=True) for t in tb.select('thead th')]
  for row in tb.select('tbody tr'):
   for j,td in enumerate(row.find_all('td',recursive=False)):
    lab=soup.new_tag('span',attrs={'class':'cell-label','aria-hidden':'true'});lab.string=headers[j];td.insert(0,lab)
 dest.write_text(str(soup)+'\n',encoding='utf-8')
 changed=[str(dest.relative_to(ROOT))]
 for pp in d['parents']:
  parent=ROOT/(pp[1:]+'.html'); raw=parent.read_text(encoding='utf-8')
  backup=OUT/'before'/parent.relative_to(ROOT);backup.parent.mkdir(parents=True,exist_ok=True)
  if not backup.exists():backup.write_text(raw,encoding='utf-8')
  ps=BeautifulSoup(raw,'html.parser')
  block=BeautifulSoup('<aside class="notice" id="follow6-'+d['slug']+'"><strong>관련 서류를 더 확인하려면</strong><p>'+a(d['path'],d['title'])+'</p></aside>','html.parser')
  anchor=ps.main.find('section',class_='official-guide-actions') or ps.main.find('section',class_='kakao-inquiry-cta')
  if anchor:anchor.insert_before(block)
  else:ps.main.append(block)
  for sc in ps.find_all('script',type='application/ld+json'):
   try:
    o=json.loads(sc.string)
    if o.get('@type')=='Article':o['dateModified']=DATE;sc.string=json.dumps(o,ensure_ascii=False)
   except (TypeError,ValueError):pass
  parent.write_text(str(ps)+'\n',encoding='utf-8');changed.append(str(parent.relative_to(ROOT)))
 idx=ROOT/section/'index.html';ix=BeautifulSoup(idx.read_text(encoding='utf-8'),'html.parser');block=ix.main.find(id='claims-follow6-20261029')
 if not block:
  block=ix.new_tag('section',id='claims-follow6-20261029');block.append(BeautifulSoup('<h2>수술·청구자료 상세 안내</h2><div class="grid guide-section-grid"></div>','html.parser'));block.h2.string='수술·청구자료 상세 안내';ix.main.append(block)
 block.select_one('div').append(BeautifulSoup('<a class="card" href="'+d['path']+'"><h3>'+d['title']+'</h3><p>'+d['desc']+'</p></a>','html.parser'));idx.write_text(str(ix)+'\n',encoding='utf-8');changed.append(str(idx.relative_to(ROOT)))
 sm=ROOT/'sitemap.xml';raw=sm.read_text(encoding='utf-8');raw=raw.replace('</urlset>',f'<url><loc>{BASE+d["path"]}</loc><lastmod>{DATE}</lastmod></url>\n</urlset>')
 for pp in d['parents']:raw=re.sub(r'(<loc>'+re.escape(BASE+pp)+r'</loc>\s*<lastmod>)[^<]+',r'\g<1>'+DATE,raw)
 sm.write_text(raw,encoding='utf-8');changed+=['sitemap.xml','assets/article-catalog.json']
 subprocess.run([sys.executable,str(ROOT/'scripts/build-article-catalog.py')],check=True)
 changed += ['assets/images/'+d['slug']+'-'+k+'.webp' for k in ['thumb','body1','body2']]
 (OUT/f'changed-{n}.json').write_text(json.dumps(changed,ensure_ascii=False,indent=2),encoding='utf-8')
 (OUT/'manifest.json').write_text(json.dumps([{k:v for k,v in x.items() if k!='body'} for x in DATA],ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps({'n':n,'files':changed},ensure_ascii=False))
if __name__=='__main__':publish(int(sys.argv[1]))
