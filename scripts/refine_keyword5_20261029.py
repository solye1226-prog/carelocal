from pathlib import Path
from bs4 import BeautifulSoup
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/keyword5-refinement-2026-10-29'
KB = 'https://www.kbinsure.co.kr/CG205020003.ec'
HIRA = 'https://www.hira.or.kr/npay/index.do'
KDCA = 'https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=5818'
DATA = [
 dict(n=1, path='/treatment-costs/cartistem-stem-cell-knee-cost', keyword='카티스템 수술비용',
 title='카티스템 수술비용, 재료대·수술료·입원비 견적 비교',
 lead='카티스템 수술비용은 제품 관련 비용만인지, 수술료·마취료·입원비·검사비까지 포함한 금액인지 나누어 비교하세요. 퇴원 후 재활비와 함께 시행하는 다른 수술의 비용은 별도일 수 있습니다. 이 글은 치료 전 견적과 실제 부담할 비용을 확인하는 방법을 다루며, 치료 후 실비 청구서류는 별도 안내로 연결합니다.',
 headings={'핵심 요약':'카티스템 수술비용 비교 전 핵심 항목', '무릎 연골 치료비에서 먼저 구분할 것':'카티스템 비용과 다른 무릎 치료비를 구분하세요', '병원에 확인할 항목':'제품 비용과 전체 수술비용의 차이', '카티스템 치료비와 수술비 보험은 따로 확인합니다':'카티스템 수술비용과 보험금은 다른 금액입니다', '청구 자료는 필요한 범위로 준비하세요':'치료 전 견적과 치료 후 영수증을 구분하세요', '치료 전 견적을 총액과 포함 항목으로 나눠 보세요':'카티스템 병원 견적 비교: 포함 비용과 별도 비용', '문의할 때 사용할 질문':'병원에 수술비용을 문의할 질문'},
 boundary='치료 전 병원 견적·총비용 비교 전용. 실비 제출서류는 /silbi/cartistem-silbi-claim, 동시수술 기록·수술비는 기존 시술별 글로 연결.',
 related=['/silbi/cartistem-silbi-claim','/surgery-benefit/cartistem-concurrent-procedure-records']),
 dict(n=2, path='/surgery-benefit/hemorrhoid-repeat-surgery-benefit',keyword='치핵 재수술 수술비',
 title='치핵 재수술 수술비, 같은 부위 반복수술 보험금 확인사항',
 lead='치핵 재수술 수술비를 청구할 때는 첫 수술과 재수술의 날짜·부위·실제 행위를 나누고, 가입한 특약의 반복수술 지급 조건을 확인합니다. 같은 부위를 다시 치료했다는 이유만으로 지급 또는 제외가 정해지지는 않습니다. 이 글은 첫 치핵 수술의 종수보다 두 번째 수술의 지급 횟수와 필요한 기록에 집중합니다.',
 headings={'두 번째 병원 방문과 두 번째 지급사유를 구분합니다':'치핵 재수술과 후속 처치의 지급단위 비교', '첫 치료와 이번 치료를 나눠 적으세요':'첫 치핵 수술과 재수술 기록 비교', '반복수술 조항을 찾으세요':'재수술 수술비의 기간·횟수 조항 확인', '접수 전 체크':'치핵 재수술 보험금 청구 전 체크리스트'},
 boundary='첫 수술의 종수 분류나 결찰술·절제술 치료법 재설명보다 재수술의 지급단위·이전 지급내역 비교에 집중.',
 related=['/surgery-benefit/hemorrhoid-surgery-benefit','/claims/hemorrhoid-surgery-claim-documents']),
 dict(n=3, path='/claims/silbi-fixed-surgery-same-claim',keyword='실비 수술비 중복 청구',
 title='실비·수술비 중복 청구, 함께 접수할 때 서류와 담보 확인',
 lead='실비와 수술비를 중복 청구하려면 실제 의료비를 보상하는 실손의료비와 약관상 정액 수술비 특약에 각각 가입했는지 확인하세요. 여기서 중복 청구는 서로 다른 두 담보를 함께 신청한다는 뜻입니다. 같은 병원비를 여러 실손보험에서 실제 부담액 이상으로 받는다는 의미가 아니며, 두 담보의 지급 여부와 금액은 각각 심사됩니다.',
 headings={'실손 지급 완료와 수술비 심사 완료는 같은 표시가 아닙니다':'실비 지급 후 수술비 특약 접수 여부 확인', '두 담보는 같은 비용을 계산하지 않습니다':'실비·수술비 청구서류를 담보별로 나누는 법', '한 보험사에 접수했더라도 처리 담보를 확인하세요':'같은 보험사·다른 보험사의 중복 청구 접수 확인', '접수 화면에서 확인할 순서':'실비와 수술비 함께 청구하는 순서'},
 boundary='실손·정액의 계산 원리는 /standards/actual-vs-fixed-benefit로 연결하고 이 글은 누락된 담보·접수번호·제출자료 확인에 집중.',
 related=['/standards/actual-vs-fixed-benefit','/claims/surgery-claim-documents']),
 dict(n=4, path='/silbi/outpatient-prescription-diagnosis-code',keyword='처방전 질병코드 누락',
 title='처방전 질병코드 누락, 실비 청구 대체서류와 재발급 확인',
 lead='처방전에 질병코드(질병분류기호)가 누락됐다면 실비 청구에 필요한 진단명 확인 자료를 보험사에 먼저 문의하세요. 기존 진료 자료로 대체할 수 있는지 확인한 뒤, 필요할 때 병원에 실제 기록에 따른 정정·재발급을 요청합니다. 질병코드를 직접 찾아 처방전에 적거나 고치지 않습니다.',
 headings={'요청받은 항목을 정확히 묻습니다':'처방전 질병코드 누락 시 보험사에 확인할 항목', '병원과 약국 서류를 나눕니다':'실비 대체서류: 병원 자료와 약국 영수증 구분', '기존 서류를 수정하지 않습니다':'질병분류기호 정정·재발급은 병원에 문의', '코드 누락으로 보완 요청을 받았다면':'처방전 코드 누락 보완서류 제출 순서'},
 boundary='약값 청구의 전체 준비물은 pharmacy-prescription-claim, 이 글은 처방전 코드 누락·대체자료·정정에 한정.',
 related=['/silbi/pharmacy-prescription-claim','/claims/insurance-claim-supplement-documents']),
 dict(n=5, path='/surgery-benefit/surgery-benefit-amount-review',keyword='수술비 보험금 적게 지급',
 title='수술비 보험금 적게 지급된 이유, 종수·감액·지급횟수 확인',
 lead='수술비 보험금이 예상보다 적게 지급됐다면 보험증권의 가입금액, 적용한 수술 종수, 감액·반복수술·동시수술 조항을 지급내역과 대조하세요. 병원에 낸 수술비용과 정액 수술비 보험금은 같은 금액이 아닙니다. 이 글은 지급액 차이의 원인을 찾는 단계까지 다루며, 판단에 이견이 남으면 별도의 이의신청 안내로 이어집니다.',
 headings={'예상액과 지급액의 기준을 맞추세요':'수술비 보험금 지급액: 종수·가입금액·감액 비교', '보험사에 적용 근거를 요청하세요':'적게 지급된 수술비의 산출내역·약관 조항 요청', '재검토를 요청하기 전':'수술비 감액 사유 확인 후 재검토 준비'},
 boundary='새로운 종수 분류 안내나 이의신청서 절차를 반복하지 않고 예상액과 지급액의 차이 원인 찾기에 집중.',
 related=['/surgery-benefit/surgery-classification','/claims/insurance-claim-appeal'])
]

def replace_text(node,text):
 node.clear();node.append(text)

def section_nodes(h):
 result=[]
 for node in h.next_siblings:
  if getattr(node,'name',None)=='h2':break
  result.append(node)
 return result

def refine(n):
 d=next(x for x in DATA if x['n']==n);f=ROOT/(d['path'][1:]+'.html')
 (OUT/'before').mkdir(parents=True,exist_ok=True)
 backup=OUT/'before'/f.name
 if backup.exists():raise RuntimeError('Already started; inspect existing output instead of reapplying')
 raw=f.read_text('utf-8');backup.write_text(raw,'utf-8');s=BeautifulSoup(raw,'html.parser')
 old_title=s.title.get_text();old_h1=s.h1.get_text()
 images=[str(x) for x in s.main.find_all('img')]
 canonical=s.find('link',rel='canonical')['href']
 replace_text(s.title,d['title']);replace_text(s.h1,d['title'])
 lead=s.main.find('p',class_='lead')
 if not lead:
  for p in s.h1.find_next_siblings('p'):
   if not set(p.get('class',[])) & {'article-meta','eyebrow'}:lead=p;break
 assert lead is not None
 replace_text(lead,d['lead'])
 for attr,value in [('name','description'),('property','og:title'),('property','og:description'),('name','twitter:title'),('name','twitter:description')]:
  m=s.find('meta',attrs={attr:value})
  if m is None:m=s.new_tag('meta');m[attr]=value;s.head.append(m)
  m['content']=d['lead'] if 'description' in value else d['title']
 breadcrumb=s.main.find(class_='breadcrumb')
 if breadcrumb:
  for txt in list(breadcrumb.find_all(string=True)):
   if txt.parent==breadcrumb and old_h1 in str(txt):txt.replace_with(str(txt).replace(old_h1,d['title']))
 for h in s.main.find_all('h2'):
  text=h.get_text(' ',strip=True)
  if text in d['headings']:replace_text(h,d['headings'][text])
 if n==1:
  h=s.main.find('h2',string='제품 비용과 전체 수술비용의 차이')
  h.insert_after(BeautifulSoup('<p>카티스템 제품 한 품목의 가격과 병원에서 시행하는 수술 전체의 비용은 구분해야 합니다. 제품 비용만 안내받았다면 수술·마취·입원·검사와 재활 비용이 추가되는지 물어보세요. 반대로 묶음 견적이라면 어떤 항목이 포함됐는지 확인해 같은 범위끼리 비교합니다.</p>','html.parser'))
  a=s.main.find('a',href='https://www.chubb.com/kr-kr/claims-service/claims-documents-forms.html')
  a['href']=HIRA;replace_text(a,'심평원 비급여 진료비용 조회 · 공개 항목과 병원 전체 견적은 구분 · 새 창 ↗')
  h=s.main.find('h2',string=d['headings']['카티스템 치료비와 수술비 보험은 따로 확인합니다'])
  for node in section_nodes(h):
   if getattr(node,'name',None) in ['figure','img']:continue
   node.extract()
  h.insert_after(BeautifulSoup('<p>카티스템 수술비용은 병원에 내는 치료비이고, 정액 수술비 보험금은 가입한 특약의 지급 조건에 따라 따로 판단하는 금액입니다. 제품 비용이나 병원 견적만으로 보험 종수와 받을 금액을 계산하지 않습니다. 치료 후 비용 항목별 접수 자료는 <a href="/silbi/cartistem-silbi-claim">카티스템 실비 청구서류</a>, 함께 시행한 수술의 기록은 <a href="/surgery-benefit/cartistem-concurrent-procedure-records">카티스템 동시수술 기록 안내</a>에서 확인하세요.</p>','html.parser'))
  h=s.main.find('h2',string=d['headings']['청구 자료는 필요한 범위로 준비하세요'])
  for node in section_nodes(h):
   if getattr(node,'name',None)=='p':replace_text(node,'치료 전에는 예정된 항목과 포함 비용을 적은 견적을, 치료 뒤에는 실제 시행 내용이 적힌 영수증·세부내역서를 확인합니다. 추가 처치나 입원 일정 변경으로 최종 금액이 달라졌다면 병원 원무 창구에 차이 항목을 문의하세요. 보험 청구용 기록은 보험사가 확인하려는 내용과 필요한 범위를 안내받은 뒤 준비합니다.')
  h=s.main.find('h2',string=d['headings']['치료 전 견적을 총액과 포함 항목으로 나눠 보세요'])
  h.insert_after(BeautifulSoup('<p><a href="'+HIRA+'" target="_blank" rel="noopener">건강보험심사평가원 비급여 진료비용 정보</a>에서 의료기관별 공개 항목을 확인할 수 있습니다. 같은 항목이라도 함께 제공되는 진료·치료재료에 따라 실제 총진료비는 다를 수 있으므로, 공개된 개별 가격을 카티스템 전체 수술비용으로 단정하지 마세요. 해당 병원의 항목과 기준 단위를 확인하고 최종 견적을 문의합니다.</p>','html.parser'))
  ul=s.main.select_one('.article-summary ul')
  ul.clear()
  for text in ['제품 관련 비용과 수술·마취·입원·검사 비용의 포함 여부를 비교합니다.','재활·추가 처치와 함께 시행하는 다른 수술의 별도 비용을 확인합니다.','공개된 개별 항목 가격, 병원 예상 견적, 치료 후 실제 정산액을 구분합니다.','실비 청구서류와 정액 수술비의 지급 조건은 관련 글에서 따로 확인합니다.']:
   li=s.new_tag('li');li.string=text;ul.append(li)
 if n==3:
  h=s.main.find('h2',string=d['headings']['두 담보는 같은 비용을 계산하지 않습니다'])
  for node in section_nodes(h):
   if getattr(node,'name',None)=='p' and '삼성화재의 공식' in node.get_text():replace_text(node,'KB손해보험 공식 질병 청구서류 안내는 실손의료비와 수술 관련 제출자료를 담보별로 구분합니다. 다른 보험사·상품의 요구서류는 각 회사 안내에서 확인하세요. 보상 구조와 계산 원리는 아래의 실손·정액 비교 글로 나누어 확인할 수 있습니다.')
 if n==4:
  for p in s.main.find_all('p'):
   if '삼성화재 통원 실손 안내' in p.get_text():replace_text(p,'KB손해보험 공식 질병 청구서류 안내는 질병분류코드가 기재된 처방전 등 진단명 확인 자료를 안내합니다. 현대해상 공식 청구서류 안내도 처방전의 질병분류코드가 없으면 추가 증빙이 필요할 수 있다고 설명합니다. 회사·청구 건마다 대체자료가 같다고 가정하지 말고 어떤 정보가 누락됐는지부터 확인하세요.')
  h=s.main.find('h2',string=d['headings']['요청받은 항목을 정확히 묻습니다'])
  h.insert_after(BeautifulSoup('<p><a href="'+KB+'" target="_blank" rel="noopener">KB손해보험 질병 청구서류</a>에서 코드 기재와 담보별 자료를 확인할 수 있습니다. 질병코드는 의료기관의 실제 진단 기록을 확인하기 위한 정보이며, 코드 하나만으로 보험금 지급을 결정하지 않습니다.</p>','html.parser'))
 # Repair confirmed unavailable addresses within the five authorized pages only.
 for a in s.main.find_all('a',href=True):
  href=a['href']
  if 'direct.samsungfire.com' in href and ('PP040202_001' in href or 'MP040202_001' in href):
   a['href']=KB
   label=a.get_text(' ',strip=True)
   if a.find(class_='guide-title'):
    replace_text(a.find(class_='guide-title'),'KB손해보험 담보별 청구서류 확인')
   else:
    for text in list(a.find_all(string=True)):
     if '삼성화재' in str(text):text.replace_with(str(text).replace('삼성화재','KB손해보험'))
  if 'health.kdca.go.kr' in href and 'cntnts_sn=5818' in href:a['href']=KDCA
 for sc in s.find_all('script',type='application/ld+json'):
  try:obj=json.loads(sc.string)
  except (TypeError,ValueError):continue
  def visit(x):
   if isinstance(x,dict):
    if x.get('@type') in ['Article','BlogPosting']:
     x.update(headline=d['title'],description=d['lead'],dateModified='2026-10-29')
    if x.get('@type')=='BreadcrumbList':
     for item in x.get('itemListElement',[]):
      if item.get('name') in [old_h1,old_title]:item['name']=d['title']
    for v in x.values():visit(v)
   elif isinstance(x,list):
    for v in x:visit(v)
  visit(obj);sc.string=json.dumps(obj,ensure_ascii=False)
 f.write_text(str(s)+'\n','utf-8')
 assert images==[str(x) for x in s.main.find_all('img')], 'Existing images changed'
 assert canonical==s.find('link',rel='canonical')['href']
 assert s.title.get_text()==s.h1.get_text()==d['title']
 for path in d['related']:assert s.main.find('a',href=path),path
 # Only the owning section index is adjusted; existing article backlinks stay intact.
 idx=ROOT/d['path'].split('/')[1]/'index.html';index_before=idx.read_text('utf-8')
 if not (OUT/'before'/f'{idx.parent.name}-index.html').exists():(OUT/'before'/f'{idx.parent.name}-index.html').write_text(index_before,'utf-8')
 ix=BeautifulSoup(index_before,'html.parser')
 for a in ix.find_all('a',href=True):
  if a['href'] in [d['path'],d['path']+'.html']:
   if a.find('h3'):
    replace_text(a.h3,d['title'])
    if a.find('p'):replace_text(a.p,'제품 비용·수술료·입원비의 포함 여부와 병원 견적을 비교합니다.' if n==1 else d['lead'])
   else:replace_text(a,d['title'])
 idx.write_text(str(ix)+'\n','utf-8')
 sm=ROOT/'sitemap.xml';txt=sm.read_text('utf-8');txt=re.sub(r'(<loc>https://hospital\.hbuby\.com'+re.escape(d['path'])+r'</loc>\s*<lastmod>)[^<]+',r'\g<1>2026-10-29',txt);sm.write_text(txt,'utf-8')
 rec={**d,'oldTitle':old_title,'oldH1':old_h1,'imagesPreserved':True,'canonicalPreserved':True,'state':'local_ready'}
 (OUT/f'{n:02d}-changes.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2),'utf-8')
 print(json.dumps({'n':n,'title':d['title'],'imagesPreserved':True},ensure_ascii=False))

if __name__=='__main__':refine(int(sys.argv[1]))
