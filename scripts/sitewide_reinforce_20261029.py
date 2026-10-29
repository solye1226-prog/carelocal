from pathlib import Path
from bs4 import BeautifulSoup
from collections import Counter
import json,re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/sitewide-reinforcement-2026-10-29'
DEST='https://www.samsungfire.com/v2/html/customer/13/G_030_010_010.html?init=direct'
PRIORITY=['/silbi/cartistem-silbi-claim','/claims/gallbladder-pathology-request','/surgery-benefit/hemorrhoid-surgery-benefit','/claims/surgery-claim-documents','/silbi/mri-silbi-claim']
EDIT={
 PRIORITY[0]:dict(title='카티스템 실비 청구서류, 재료대·수술료 접수 확인',lead='카티스템 실비 청구서류는 치료 후 받은 진료비 영수증·세부내역서와 진단명 확인 자료부터 구분합니다. 재료대·수술료·입원 또는 통원비 중 어느 항목을 접수했는지 확인하고, 추가 기록은 보험사가 요청한 목적과 범위에 맞춰 준비하세요. 치료 전 견적 비교는 카티스템 수술비용 글에서, 이 글에서는 치료 후 청구자료와 담보별 접수를 다룹니다.',headings={'카티스템 치료비는 어떤 항목으로 나뉘나요?':'카티스템 실비 청구 항목: 재료대·수술료·입원비','청구 금액과 추가자료 요청을 항목별로 확인하세요':'카티스템 실비 보완서류: 요청 항목과 제출자료 대조'}),
 PRIORITY[1]:dict(title='담낭절제술 조직검사 결과지, 보험청구 추가서류 확인',lead='담낭절제술 보험청구 중 조직검사 결과지를 요청받았다면 어느 담보에서 어떤 사실을 확인하려는지 먼저 문의하세요. 수술확인서의 수술 사실과 조직검사 결과의 확인 목적은 다를 수 있습니다. 이 글은 담석 수술의 전체 준비물보다 조직검사 추가 제출의 목적·결과 확정 여부·기존 접수번호 연결에 집중합니다.',headings={'어느 담보의 추가 서류인지 확인하세요':'담낭절제술 조직검사 결과지의 추가 요청 목적','병원에서는 결과가 확정됐는지 확인하세요':'조직검사 결과지 발급 전 확정 여부 확인','추가 제출 순서':'담낭 수술 보험청구 보완서류 제출 순서'})
}

def old_link(u):return 'direct.samsungfire.com' in u and any(t in u for t in ['PP040202_001','MP040202_001'])
def put(n,t):n.clear();n.append(t)
def lead(s):
 n=s.main.find('p',class_='lead')
 if n:return n
 return next((p for p in s.h1.find_next_siblings('p') if not set(p.get('class',[])) & {'eyebrow','article-meta'}),None)
def payload(s):
 c=BeautifulSoup(str(s.main),'html.parser')
 for n in c.select('h1,h2,.breadcrumb'):n.decompose()
 for p in c.find_all('p'):
  if p.get_text(' ',strip=True) in [d['lead'] for d in EDIT.values()]:p.decompose()
 return Counter(c.stripped_strings)

def main():
 if (OUT/'manifest.json').exists():raise RuntimeError('Already applied; inspect manifest')
 (OUT/'before').mkdir(exist_ok=True)
 catalog=json.loads((ROOT/'assets/article-catalog.json').read_text('utf-8'));manifest=[]
 for row in catalog:
  path=row['path'];f=ROOT/(path[1:]+'.html');raw=f.read_text('utf-8');s=BeautifulSoup(raw,'html.parser');before=BeautifulSoup(raw,'html.parser');reasons=[];count=0
  for a in s.main.find_all('a',href=True):
   if old_link(a['href']):a['href']=DEST;count+=1
  if count:reasons.append('official_links')
  hs=s.main.find_all('h2');names=Counter(h.get_text(' ',strip=True) for h in hs);renames=[]
  for h in hs:
   text=h.get_text(' ',strip=True)
   if text!='이 상황도 함께 확인하세요' or (names[text]<2 and path not in PRIORITY):continue
   a=None
   for sib in h.next_siblings:
    if getattr(sib,'name',None)=='h2':break
    if hasattr(sib,'find'):
     a=sib.find('a',href=True)
     if a and a['href'].startswith('/'):break
   if not a or not a['href'].startswith('/'):continue
   title=a.get_text(' ',strip=True)
   new='관련 안내: '+title
   # Repeated links are kept; headings must still be unique.
   if new in [x.get_text(' ',strip=True) for x in s.main.find_all('h2')]:new='상황별 확인: '+title
   put(h,new);renames.append({'before':text,'after':new})
  if renames:reasons.append('contextual_headings')
  contacts=[]
  for h in s.main.find_all('h2'):
   if '보장이 궁금' in h.get_text():
    block=h.find_parent(class_='kakao-inquiry-cta')
    if block and h.find_next('h2') and h.find_next('h2') in s.main.find_all('h2'):
     block.extract();s.main.append(block);contacts.append('moved_to_article_end')
  if contacts:reasons.append('contact_order')
  old_title=s.title.get_text();old_h1=s.h1.get_text();old_lead=None
  if path in EDIT:
   d=EDIT[path];lp=lead(s);assert lp is not None;old_lead=lp.get_text(' ',strip=True);put(lp,d['lead']);put(s.title,d['title']);put(s.h1,d['title'])
   for k,v in d['headings'].items():
    h=next((h for h in s.main.find_all('h2') if h.get_text(' ',strip=True)==k),None)
    assert h is not None,k
    put(h,v)
   for attr,name in [('name','description'),('property','og:title'),('property','og:description'),('name','twitter:title'),('name','twitter:description')]:
    tag=s.find('meta',attrs={attr:name})
    if tag is None:tag=s.new_tag('meta');tag[attr]=name;s.head.append(tag)
    tag['content']=d['lead'] if 'description' in name else d['title']
   bc=s.main.find(class_='breadcrumb')
   if bc:
    for t in list(bc.find_all(string=True)):
     if t.parent==bc and old_h1 in str(t):t.replace_with(str(t).replace(old_h1,d['title']))
   reasons.append('keyword_focus')
  if not reasons:continue
  if old_lead is not None:
   oldp=lead(before);assert oldp is not None;oldp.decompose()
  assert payload(before)==payload(s),(path,'Unplanned main text change')
  original=BeautifulSoup(raw,'html.parser')
  assert [str(i) for i in original.main.find_all('img')]==[str(i) for i in s.main.find_all('img')]
  assert original.find('link',rel='canonical')==s.find('link',rel='canonical')
  expected=Counter(DEST if old_link(a['href']) else a['href'] for a in original.main.find_all('a',href=True))
  assert expected==Counter(a['href'] for a in s.main.find_all('a',href=True))
  for sc in s.find_all('script',type='application/ld+json'):
   try:obj=json.loads(sc.string)
   except (TypeError,ValueError):continue
   def update(x):
    if isinstance(x,dict):
     if x.get('@type') in ['Article','BlogPosting']:
      x['dateModified']='2026-10-29'
      if path in EDIT:x.update(headline=EDIT[path]['title'],description=EDIT[path]['lead'])
     for v in x.values():update(v)
    elif isinstance(x,list):
     for v in x:update(v)
   update(obj);sc.string=json.dumps(obj,ensure_ascii=False)
  (OUT/'before'/f.name).write_text(raw,'utf-8');f.write_text(str(s)+'\n','utf-8')
  manifest.append({'path':path,'title':s.title.get_text(),'oldTitle':old_title,'reasons':reasons,'officialLinksReplaced':count,'headingRenames':renames,'imagesPreserved':True,'linksPreservedExceptOfficialDestination':True,'remainingBodyTextPreserved':True})
 # Sync only owning category indexes for the two approved keyword refinements.
 for path,d in EDIT.items():
  f=ROOT/path.split('/')[1]/'index.html';raw=f.read_text('utf-8');s=BeautifulSoup(raw,'html.parser')
  (OUT/'before'/(f.parent.name+'-index.html')).write_text(raw,'utf-8')
  for a in s.find_all('a',href=True):
   if a['href'] in [path,path+'.html']:
    put(a.find('h3') or a,d['title'])
  f.write_text(str(s)+'\n','utf-8')
 sm=ROOT/'sitemap.xml';text=sm.read_text('utf-8')
 for r in manifest:text=re.sub(r'(<loc>https://hospital\.hbuby\.com'+re.escape(r['path'])+r'</loc>\s*<lastmod>)[^<]+',r'\g<1>2026-10-29',text)
 sm.write_text(text,'utf-8')
 manifest.sort(key=lambda r:(PRIORITY.index(r['path']) if r['path'] in PRIORITY else 100,r['path']))
 (OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),'utf-8')
 print(json.dumps({'changed':len(manifest),'linkPages':sum('official_links'in x['reasons'] for x in manifest),'headingPages':sum('contextual_headings'in x['reasons'] for x in manifest),'contactPages':sum('contact_order'in x['reasons'] for x in manifest)},ensure_ascii=False))

if __name__=='__main__':main()
