"""Publish source-reviewed 16-20, one article per explicit invocation."""
from pathlib import Path
from bs4 import BeautifulSoup
import json,sys,subprocess,re
from PIL import Image
from publish_trend5_20261027 import p,h,a,ul,table,CSS
from trend1620_data import DATA
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/trend16-20-publication-2026-10-28'
BASE='https://hospital.hbuby.com'
DATE='2026-10-28'
def image(d,key):
 src='/assets/images/'+d['slug']+'-'+key+'.webp'
 with Image.open(ROOT/src[1:]) as im:w,hh=im.size
 return f'<figure><img src="{src}" width="{w}" height="{hh}" alt="{d["title"]} 관련 상담·자료 확인 장면" loading="{"eager" if key=="thumb" else "lazy"}" decoding="async">'+('<figcaption>AI로 만든 설명용 이미지이며 실제 환자·진료기록이나 공식 기관 화면이 아닙니다.</figcaption>' if key=='thumb' else '')+'</figure>'

def label_tables(soup):
 for tb in soup.main.find_all('table'):
  headers=[x.get_text(' ',strip=True) for x in tb.select('thead th')]
  for row in tb.select('tbody tr'):
   for j,td in enumerate(row.find_all('td',recursive=False)):
    if not td.find(class_='cell-label'):
     lab=soup.new_tag('span',attrs={'class':'cell-label'});lab.string=headers[j] if j<len(headers) else '';td.insert(0,lab)

def publish(n):
 d=DATA[n-16];dest=ROOT/(d['path'][1:]+'.html')
 if dest.exists():raise SystemExit('Already exists: '+str(dest))
 soup=BeautifulSoup((ROOT/'surgery-benefit/wound-suture-specific-rider.html').read_text(encoding='utf-8'),'html.parser');soup.title.string=d['title']
 for attr,key,val in [('name','description',d['desc']),('property','og:title',d['title']),('property','og:description',d['desc']),('property','og:image',BASE+'/assets/images/'+d['slug']+'-thumb.webp')]:soup.find('meta',attrs={attr:key})['content']=val
 soup.find('link',rel='canonical')['href']=BASE+d['path'];og=soup.new_tag('meta',attrs={'property':'og:url','content':BASE+d['path']});soup.head.append(og)
 style=soup.new_tag('style');style.string=CSS+'@media(max-width:600px){.trend5 .trend-table table{min-width:0}}';soup.head.append(style)
 schema=json.loads(soup.find('script',type='application/ld+json').string);schema.update(headline=d['title'],description=d['desc'],image=BASE+'/assets/images/'+d['slug']+'-thumb.webp',mainEntityOfPage=BASE+d['path'],datePublished=DATE,dateModified=DATE);soup.find('script',type='application/ld+json').string=json.dumps(schema,ensure_ascii=False)
 main=soup.main;cta=str(main.find('section',class_='kakao-inquiry-cta'));main.clear();main['class']=['section','article-body','insurance-series-article','cluster-reading','trend5'];section=d['path'].split('/')[1]
 text=f'<div class="breadcrumb"><a href="/">홈</a> / <a href="/{section}/">{d["cat"]}</a></div><h1>{d["title"]}</h1><p class="lead">{d["desc"]}</p><div class="status-note"><strong>이용·시행 단계</strong><br>{d["status"]}</div>'+image(d,'thumb')
 if d['insurance']:text+='<p>'+a('/insurance-companies/','보험사별 공식 홈페이지 확인하기')+'</p>'
 for i,part in enumerate(d['body']):
  text+=part
  if i==1:text+=image(d,'body1')
  if i==3:text+=image(d,'body2')
 text+='<section class="official-guide-actions"><h2>공식 확인처와 상세 안내</h2><div class="official-guide-grid">'
 for url,title,scope in d['sources']:text+=f'<a class="official-guide-button" href="{url}" target="_blank" rel="noopener"><strong>{title}</strong><span>{scope} · 새 창 ↗</span></a>'
 text+='</div></section><p>작성: 케어로컬 사이트 운영자. '+a('/legal/about','작성 기준과 운영자 역할')+'을 확인할 수 있습니다. 개인의 진단·치료 적합성은 의료진에게, 보험 보장은 해당 계약의 공식 안내에서 확인하세요.</p>'
 if d['insurance']:text+='<div class="insurance-company-cta">'+a('/insurance-companies/','보험사별 공식 홈페이지 확인하기')+'</div>'+cta
 main.append(BeautifulSoup(text,'html.parser'));label_tables(soup);dest.write_text(str(soup)+'\n',encoding='utf-8')
 parent=ROOT/(d['parent'][1:]+'.html');raw=parent.read_text(encoding='utf-8');(OUT/(parent.stem+'-before.html')).write_text(raw,encoding='utf-8');ps=BeautifulSoup(raw,'html.parser')
 block=BeautifulSoup('<aside class="notice" id="trend1620-related"><strong>함께 확인할 내용</strong><p>'+d['parent_note']+' '+a(d['path'],d['title'])+'</p></aside>','html.parser');anchor=ps.main.find('section',class_='official-guide-actions')
 if anchor:anchor.insert_before(block)
 else:ps.main.append(block)
 for script in ps.find_all('script',type='application/ld+json'):
  try:o=json.loads(script.string);o['dateModified']=DATE;script.string=json.dumps(o,ensure_ascii=False)
  except(ValueError,TypeError):pass
 parent.write_text(str(ps)+'\n',encoding='utf-8')
 idx=ROOT/section/'index.html';cs=BeautifulSoup(idx.read_text(encoding='utf-8'),'html.parser');(cs.main or cs.body).append(BeautifulSoup('<section class="section"><h2>제도와 이용 절차</h2><p>'+a(d['path'],d['title'])+'</p></section>','html.parser'));idx.write_text(str(cs)+'\n',encoding='utf-8')
 sm=ROOT/'sitemap.xml';raw=sm.read_text(encoding='utf-8');raw=raw.replace('</urlset>',f'  <url><loc>{BASE+d["path"]}</loc><lastmod>{DATE}</lastmod></url>\n</urlset>');raw=re.sub(r'(<loc>'+re.escape(BASE+d['parent'])+r'</loc>\s*<lastmod>)[^<]+',r'\g<1>'+DATE,raw);sm.write_text(raw,encoding='utf-8');subprocess.run([sys.executable,str(ROOT/'scripts/build-article-catalog.py')],check=True)
 (OUT/'manifest.json').write_text(json.dumps([{k:v for k,v in x.items() if k!='body'} for x in DATA],ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'n':n,'article':str(dest.relative_to(ROOT)),'parent':str(parent.relative_to(ROOT))},ensure_ascii=False))
if __name__=='__main__':publish(int(sys.argv[1]))
