from pathlib import Path
from collections import Counter, defaultdict
from urllib.parse import urlsplit
from bs4 import BeautifulSoup
import json, re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/article-connections-2026-10-29'
# Each destination is linked from a contextually related existing article.
GROUPS = {
 '/claims/dental-implant-insurance-claim-documents': ['/claims/dental-extraction-implant-dates'],
 '/claims/gallstone-surgery-claim-documents': ['/claims/gallbladder-polyp-surgery-insurance-documents'],
 '/claims/insurance-claim-documents': ['/claims/insurance-claim-original-documents-request'],
 '/claims/overseas-hospital-bill-documents': ['/claims/overseas-hospital-card-slip-insurance','/claims/overseas-medical-note-diagnosis-claim','/claims/overseas-pharmacy-prescription-claim'],
 '/claims/surgery-claim-documents': ['/claims/sinus-endoscopic-surgery-documents','/claims/surgery-certificate-missing-diagnosis'],
 '/silbi/mri-silbi-claim': ['/silbi/ct-scan-cost-claim'],
 '/checkups/fatty-liver-ultrasound-followup': ['/silbi/abdominal-ultrasound-cost-claim'],
 '/guides/flu-vaccination-2026': ['/silbi/flu-test-cost-claim'],
 '/silbi/pharmacy-prescription-claim': ['/silbi/h-pylori-eradication-pharmacy-test','/silbi/outpatient-prescription-diagnosis-code'],
 '/diagnosis-benefit/brain-heart-major-treatment-vs-diagnosis': ['/silbi/heart-echo-exam-purpose'],
 '/claims/discharge-day-outpatient-silbi': ['/silbi/hospital-interim-bill-silbi-claim'],
 '/claims/uterine-fibroid-surgery-claim-documents': ['/surgery-benefit/adenomyosis-hysterectomy-benefit','/surgery-benefit/endometrial-polyp-hysteroscopy-benefit'],
 '/surgery-benefit/endometriosis-laparoscopy-benefit': ['/surgery-benefit/ovarian-cyst-surgery-benefit'],
 '/surgery-benefit/surgery-classification': ['/surgery-benefit/bph-surgery-benefit','/surgery-benefit/vocal-polyp-surgery-benefit','/surgery-benefit/varicocele-surgery-benefit'],
 '/surgery-benefit/breast-fibroadenoma-excision-benefit': ['/surgery-benefit/breast-duct-excision-benefit'],
 '/surgery-benefit/lumbar-disc': ['/surgery-benefit/cervical-disc-surgery-benefit'],
 '/surgery-benefit/cataract-surgery-benefit': ['/surgery-benefit/diabetic-retinopathy-vitrectomy-benefit','/surgery-benefit/glaucoma-surgery-benefit'],
 '/surgery-benefit/ureteroscopy': ['/surgery-benefit/percutaneous-kidney-stone-surgery-benefit'],
 '/surgery-benefit/achilles-rupture-repair-claim': ['/surgery-benefit/plantar-fasciitis-release-benefit'],
 '/treatment-costs/out-of-pocket-cap-refund': ['/treatment-costs/nhis-copayment-refund-notice'],
 '/standards/actual-vs-fixed-benefit': ['/standards/third-sector-insurance'],
 '/silbi/simplified-silbi-prescription-exclusion': ['/underwriting/simplified-health-insurance-cancer-brain'],
 '/checkups/cancer-screening': ['/cancers/cervical-cancer'],
 '/guides/cancer-treatment-cost': ['/cancers/pancreatic-cancer','/guides/proton-therapy'],
 '/guides/night-hospital-checklist': ['/guides/sunday-hospital-checklist'],
}
LEADS = {
 '/surgery-benefit/ovarian-cyst-surgery-benefit': '난소낭종 복강경 수술비는 진단명만으로 종수를 정할 수 없습니다. 이 글에서는 낭종 제거와 난소 절제의 실제 수술 기록을 구분하고, 수술확인서의 수술명·방법·날짜를 가입 당시 수술분류표와 대조하는 순서를 다룹니다. 실손의료비는 수술비 특약과 별도로 실제 지출한 비용을 확인합니다.',
 '/claims/leqembi-repeat-claim-ledger': '레켐비 실비 반복 청구는 진료일별 영수증과 접수·지급내역을 연결해 관리하는 데 초점을 둡니다. 이 글은 치료 전 비용 견적이나 실비 적용 기준 전반보다, 여러 투여일의 미접수·중복 제출·지급 상태를 구분하는 기록 방법을 설명합니다.',
 '/silbi/leqembi-silbi-claim': '레켐비 실비 청구는 약제비·투여비·MRI 검사비를 나누고 가입한 약관에서 어떤 담보를 확인할지 정하는 것부터 시작합니다. 이 글은 치료 후 청구 항목과 준비자료를 다룹니다. 치료 전 견적 비교나 여러 진료일의 접수내역 관리는 연결된 별도 글에서 확인할 수 있습니다. 치료를 받았다는 사실만으로 보험금 지급이 확정되지는 않습니다.',
 '/treatment-costs/leqembi-cost-insurance': '레켐비 치료비는 약제 자체 금액과 검사·투여·MRI 모니터링까지 포함한 금액을 구분해서 물어봐야 합니다. 이 글은 치료 전 병원 견적과 비용 구성 확인에 집중합니다. 치료 후 실비 청구서류와 반복 청구내역 관리는 별도 글로 나누어 안내합니다. 병원에 같은 기간의 비용내역을 요청하고 급여·비급여 구분과 가입 약관의 한도를 확인하세요.',
}
HEADINGS = {
 '/claims/bile-culture-vs-pathology-records': {'세 종류의 기록은 확인하는 사실이 다릅니다':'담즙 배양검사·조직검사·시술기록의 차이','검체와 날짜를 먼저 맞춥니다':'배양검사 결과지의 검체·검사일 확인','보험사의 요청 목적을 문서명으로 좁힙니다':'보험청구 추가서류: 필요한 검사결과지 확인'},
 '/claims/leqembi-repeat-claim-ledger': {'치료 일정표와 보험 청구표는 따로 만듭니다':'레켐비 투여 일정과 실비 청구내역 구분','이번 상황의 자료 대조표':'레켐비 진료일별 영수증·접수·지급 대조표'},
}
EXTRA = {
 '/treatment-costs/leqembi-cost-insurance':['/silbi/leqembi-silbi-claim','/claims/leqembi-repeat-claim-ledger'],
 '/silbi/leqembi-silbi-claim':['/treatment-costs/leqembi-cost-insurance','/claims/leqembi-repeat-claim-ledger'],
 '/claims/leqembi-repeat-claim-ledger':['/treatment-costs/leqembi-cost-insurance','/silbi/leqembi-silbi-claim'],
}

def soup(path): return BeautifulSoup((ROOT/(path[1:]+'.html')).read_text('utf-8'),'html.parser')
def inbound(cat):
 counts=Counter(); paths={x['path'] for x in cat}
 for x in cat:
  for a in soup(x['path']).main.select('a[href]'):
   u=urlsplit(a['href']); p=u.path.removesuffix('.html').rstrip('/')
   if (not u.netloc or u.netloc=='hospital.hbuby.com') and p in paths and p!=x['path']: counts[p]+=1
 return counts

if __name__=='__main__':
 cat=json.loads((ROOT/'assets/article-catalog.json').read_text('utf-8')); titles={x['path']:x['title'] for x in cat}
 # Resolve exact existing parent names, never create a missing URL.
 for p in list(GROUPS):
  if p not in titles: raise ValueError('Missing parent '+p)
 for p in [v for vs in GROUPS.values() for v in vs]: assert p in titles,p
 assert not (OUT/'manifest.json').exists(),'Already applied'
 before_counts=inbound(cat); targets=[p for vs in GROUPS.values() for p in vs]
 assert len(targets)==34 and len(set(targets))==34
 assert all(before_counts[p]==0 for p in targets)
 (OUT/'before').mkdir(parents=True,exist_ok=True)
 manifest=[]
 for path in sorted(set(GROUPS)|set(LEADS)|set(HEADINGS)|set(EXTRA)):
  f=ROOT/(path[1:]+'.html'); raw=f.read_text('utf-8'); s=BeautifulSoup(raw,'html.parser'); old=BeautifulSoup(raw,'html.parser'); edits=[]
  if path in LEADS:
   p=s.main.find('p',class_='lead'); assert p is not None,path
   p.clear();p.append(LEADS[path]);edits.append('lead_scope')
   for tag in s.select('meta[name="description"],meta[property="og:description"],meta[name="twitter:description"]'): tag['content']=LEADS[path]
  if path=='/surgery-benefit/ovarian-cyst-surgery-benefit':
   s.h1.string=titles[path];edits.append('h1_title_consistency')
  for h in s.main.select('h2'):
   t=h.get_text(' ',strip=True)
   if t in HEADINGS.get(path,{}):h.clear();h.append(HEADINGS[path][t]);edits.append('keyword_heading')
  added=[]
  existing={urlsplit(a['href']).path.removesuffix('.html').rstrip('/') for a in s.main.select('a[href]')}
  for dest in GROUPS.get(path,[])+EXTRA.get(path,[]):
   if dest not in existing:added.append(dest);existing.add(dest)
  if added:
   section=s.new_tag('section');section['class']='related-topic-connections';h=s.new_tag('h2');h.string='관련 상황별 확인 안내';section.append(h)
   ul=s.new_tag('ul')
   for dest in added:
    li=s.new_tag('li');a=s.new_tag('a',href=dest);a.string=titles[dest];li.append(a);ul.append(li)
   section.append(ul)
   anchor=s.main.select_one('.official-guide-actions,.kakao-inquiry-cta')
   if anchor:
    while anchor.parent!=s.main:anchor=anchor.parent
    anchor.insert_before(section)
   else:s.main.append(section)
   edits.append('contextual_internal_links')
  assert [str(x) for x in old.main.select('img')]==[str(x) for x in s.main.select('img')]
  assert old.find('link',rel='canonical')==s.find('link',rel='canonical')
  oldlinks=Counter(a['href'] for a in old.main.select('a[href]'));newlinks=Counter(a['href'] for a in s.main.select('a[href]'));assert not oldlinks-newlinks
  # Every original paragraph outside the explicitly rewritten lead remains intact.
  assert Counter(p.get_text(' ',strip=True) for p in old.main.select('p') if not(path in LEADS and 'lead'in p.get('class',[])))==Counter(p.get_text(' ',strip=True) for p in s.main.select('p') if not(path in LEADS and 'lead'in p.get('class',[])))
  for sc in s.select('script[type="application/ld+json"]'):
   try:obj=json.loads(sc.string)
   except (ValueError,TypeError):continue
   def upd(x):
    if isinstance(x,dict):
     if x.get('@type') in ['Article','BlogPosting']:
      x['dateModified']='2026-10-29'
      if path in LEADS:x['description']=LEADS[path]
     for v in x.values():upd(v)
    elif isinstance(x,list):
     for v in x:upd(v)
   upd(obj);sc.string=json.dumps(obj,ensure_ascii=False)
  (OUT/'before'/(path[1:].replace('/','__')+'.html')).write_text(raw,'utf-8');f.write_text(str(s)+'\n','utf-8')
  manifest.append({'path':path,'title':titles[path],'edits':edits,'addedLinks':added,'imagesCanonicalAndExistingLinksPreserved':True})
 sm=ROOT/'sitemap.xml'; text=sm.read_text('utf-8')
 for x in manifest:text=re.sub(r'(<loc>https://hospital\.hbuby\.com'+re.escape(x['path'])+r'</loc>\s*<lastmod>)[^<]+',r'\g<1>2026-10-29',text)
 sm.write_text(text,'utf-8')
 after_counts=inbound(cat);assert all(after_counts[p]>0 for p in targets)
 (OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),'utf-8')
 (OUT/'connections.json').write_text(json.dumps([{'path':p,'before':before_counts[p],'after':after_counts[p]} for p in targets],ensure_ascii=False,indent=2),'utf-8')
 print(json.dumps({'changed':len(manifest),'linksAdded':sum(len(x['addedLinks']) for x in manifest),'previouslyUnlinkedConnected':len(targets)},ensure_ascii=False))
