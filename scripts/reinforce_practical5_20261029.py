from pathlib import Path
from bs4 import BeautifulSoup
from collections import Counter
import json, re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/core5-practical-2026-10-29'
PATHS=['/surgery-benefit/surgery-classification','/claims/surgery-claim-documents','/surgery-benefit/gallbladder-surgery-benefit','/surgery-benefit/cataract-surgery-benefit','/silbi/cartistem-silbi-claim']
CHUBB='https://www.chubb.com/kr-kr/claims-service/claims-documents-forms.html'
KB='https://www.kbinsure.co.kr/CG205020003.ec'
FAQ='https://www.snuh.org/board/B052/view.do?bbs_no=4154'
MFDS='https://nedrug.mfds.go.kr/pbp/CCBBB01/getItemDetail?itemSeq=202106062'

def frag(html): return BeautifulSoup(html,'html.parser')
def put(n,text): n.clear();n.append(text)
def table(caption,heads,rows):
 s=frag('<table class="practical-comparison"><caption></caption><thead><tr></tr></thead><tbody></tbody></table>')
 t=s.table;put(t.caption,caption)
 for head in heads:
  th=s.new_tag('th',scope='col');th.string=head;t.thead.tr.append(th)
 for row in rows:
  tr=s.new_tag('tr')
  for head,text in zip(heads,row):
   td=s.new_tag('td');label=s.new_tag('span',attrs={'class':'cell-label','aria-hidden':'true'});label.string=head;td.append(label);td.append(text);tr.append(td)
  t.tbody.append(tr)
 return t
def checklist(items):
 s=frag('<ul class="practical-checklist"></ul>')
 for item in items:
  li=s.new_tag('li');li.string='□ '+item;s.ul.append(li)
 return s.ul
def next_table(h):
 for n in h.next_siblings:
  if getattr(n,'name',None)=='h2':break
  if getattr(n,'name',None)=='table':return n
 raise AssertionError(h)
def h2(s,text): return next(h for h in s.main.select('h2')if h.get_text(' ',strip=True)==text)
def mark(n):n['data-practical-review']='20261029';return n
def paragraph(html):return frag('<p>'+html+'</p>').p

def main():
 assert not (OUT/'manifest.json').exists(),'Already applied'
 (OUT/'before').mkdir(parents=True,exist_ok=True);manifest=[];dedup=[]
 for idx,path in enumerate(PATHS):
  f=ROOT/(path[1:]+'.html');raw=f.read_text('utf-8');s=BeautifulSoup(raw,'html.parser');old=BeautifulSoup(raw,'html.parser');changes=[]
  if idx==0:
   # Enhance the existing checklist; do not append another checklist or example.
   sec=s.select_one('#record-check').parent;ul=sec.find('ul');assert ul
   ul.replace_with(mark(checklist([
    '증권에서 상품명·특약명·가입일을 옮겨 적고 약관 파일의 상품명·판본과 맞춥니다. 현재 판매 약관만 있다면 적용 약관부터 요청합니다.',
    '특약 본문이 인용한 별표 이름과 쪽수를 적습니다. PDF에서 수술명 검색 결과가 없다는 사실만으로 비보장이라고 결론내리지 않습니다.',
    '수술확인서의 실제 수술명·방법·부위·날짜를 대조합니다. 진단코드나 비용으로 종수를 대신 정하지 않습니다.',
    '후보 항목 옆에 주석·제외·사용 지침의 쪽수를 함께 적고, 이름이 비슷하다는 이유로 항목을 확정하지 않습니다.',
    '동시수술·재수술·지급 횟수·가입금액은 분류 항목과 별도로 기록합니다. 답변이 없는 칸은 확인 필요로 남깁니다.'
   ])))
   first=s.main.find('table');first.replace_with(mark(table('수술분류표를 찾는 단계별 자료 대조',['단계','맞춰 볼 자료','없거나 다를 때'],[
    ['적용 계약','증권의 특약명 ↔ 가입 당시 적용 약관','상품명·판본이 다르면 해당 계약에 적용되는 약관을 보험사에 요청'],
    ['실제 수술','병원 기록의 행위명·부위·방법 ↔ 분류표 후보 항목','종수를 추정하지 않고 필요한 기록과 분류 근거를 문의'],
    ['지급 조건','분류 항목 ↔ 사용 지침·횟수·가입금액 조항','분류 답변만으로 횟수·최종 지급액까지 확인됐다고 기록하지 않기']
   ])))
   ex=h2(s,'가상 예시: 진단명만으로 분류표 항목을 고르지 않기');p=ex.find_next_sibling('p')
   put(p,'가상의 증권에는 질병종수술비 A특약, 진단서에는 담석증, 수술확인서에는 복강경 담낭절제술이라고 적혀 있다고 가정합니다. 인터넷에서 찾은 B상품의 표는 일단 대조 대상에서 빼고, A특약의 적용 약관을 요청합니다. 아래는 자료 정리 예시이며 실제 상품·지급 사례가 아닙니다.');mark(p)
   source_note=next(t for t in s.find_all(string=True)if '인쇄 쪽수 166쪽에는' in t)
   source_note.replace_with(str(source_note).replace('인쇄 쪽수 166쪽에는','인쇄 쪽수 167쪽에는'))
   changes=['기존 5항목 체크리스트를 자료 위치·미확인 시 행동까지 구체화','기존 3단계 비교표와 약관 불일치 가상 예시 갱신','공식 약관 사용 지침 인쇄 쪽수 166→167 수정']
   dedup.append({'path':path,'alreadyPresent':'3단계 표·약관 불일치 예시·하단 체크리스트·문의 양식','decision':'기존 표·체크리스트·예시를 교체하여 설명을 중복 추가하지 않음'})
  elif idx==1:
   h=s.select_one('#certificate-choice');next_table(h).replace_with(mark(table('수술확인서·진단서·수술기록지 발급 전 비교',['자료','확인할 역할','발급 전 대조'],[
    ['수술확인서','수술명·수술일, 진단명·코드 기재 여부','이미 가진 서류에 필요한 정보가 있는지, 본인 보험사의 인정 목록과 비교'],
    ['진단서','진단 내용과 기재된 수술 사실','필요한 수술명·수술일이 함께 있는지 확인하고 두 서류 모두 필요한지 문의'],
    ['수술기록지','실제로 시행한 방법·부위·범위의 진료기록','추가 확인 목적과 수술일·페이지 범위, 병원의 발급 가능 문서명을 문의']
   ])))
   sec=s.select_one('#before-issuance').parent;intro=sec.find('p')
   intro.replace_with(mark(checklist([
    '보험사의 요청 문서명과 부족한 정보를 적고, 보유 서류의 기재 항목·전체 페이지와 대조합니다.',
    '병원에 발급 가능한 자료명·신청 방법·비용을 묻습니다. 대리 신청이라면 필요한 동의·위임 서류도 확인합니다.',
    '재발급이 필요한지와 보유자료 추가 제출로 가능한지를 구분하고, 제출 뒤 기존 접수에 반영됐는지 확인합니다.'
   ])))
   p=next(p for p in s.main.select('p')if p.get_text().startswith('가상 상황에서 이미 2쪽짜리 기록'))
   p.replace_with(mark(paragraph('<strong>가상 예시: 기록은 있는데 첨부가 빠진 경우.</strong> 수술기록지 2쪽을 갖고 있으나 앱의 첨부 목록에는 1쪽만 보인다고 가정합니다. ① 보유 파일의 전체 쪽을 대조하고 ② 누락 쪽을 기존 접수에 추가할 수 있는지 문의한 뒤 ③ 보완 자료 반영을 확인합니다. 보유한 기록 자체에 요청 정보가 없다면 그때 필요한 발급 범위를 확인합니다. 실제 처리·지급 사례가 아닌 확인 순서 예시입니다.')))
   # Correct the source paraphrase: SNUH also lists a diagnosis certificate.
   p=next(p for p in s.main.select('p')if p.find('a',href=FAQ)and'별도 수술확인서 대신' in p.get_text())
   p.replace_with(paragraph(f'<a href="{FAQ}" target="_blank" rel="noopener noreferrer">서울대학교병원 사본발급 FAQ</a>는 별도 수술확인서가 없으며 수술 내용이 적힌 진단서 또는 수술기록지로 확인할 수 있다고 안내합니다. 이 병원의 예시를 다른 병원에 일반화하지 말고 현재 발급 가능한 자료와 보험사의 인정 여부를 각각 확인하세요.'))
   changes=['기존 서류 비교표를 중복 발급 전 대조 중심으로 갱신','기존 발급 메모 앞 안내를 3단계 체크리스트로 정리','기존 2쪽 기록 누락 예시를 확인→추가→반영 순서로 구체화','서울대병원 FAQ의 진단서 대안도 반영']
   dedup.append({'path':path,'alreadyPresent':'서류 3종 비교표·추가 요청 원인표·2쪽 누락 예시·발급 메모','decision':'같은 구성 추가 없이 기존 비교표·메모 앞 문장·예시를 개선'})
  elif idx==2:
   # Keep the ERCP example and its links; add a missing triad rather than another ERCP story.
   anchor=h2(s,'담낭절제술 청구서류와 접수 순서');anchor['id']='gallbladder-document-check'
   original=anchor.find_next_sibling();assert original
   block=frag(f'''<section class="practical-tools" id="gallbladder-record-comparison"><h3>진단명·수술명·조직검사 결과지의 역할 비교</h3></section>''').section
   block.append(table('담낭절제술 보험청구 자료의 역할',['자료','옮겨 적을 사실','단정하지 않을 것'],[
    ['진단서 등 진단 자료','진단명·질병분류코드','진단명만으로 실제 수술 방법이나 보험 종수를 확정하지 않기'],
    ['수술확인서·필요 시 기록지','실제 수술명·시행일·방법','담낭절제술과 별도 담도 시술을 같은 행위로 적지 않기'],
    ['조직검사 결과지(요청 시)','검사한 조직·검사일·확정 결과의 유무','모든 담낭 수술 청구의 공통 필수서류 또는 진단비 지급 증거로 간주하지 않기']
   ]))
   block.append(paragraph(f'<a href="{CHUBB}" target="_blank" rel="noopener noreferrer">라이나손해보험(Chubb) 서류 안내</a>도 수술과 암 진단의 자료를 나누어 안내합니다. 이는 회사별 예시이며, 조직검사 결과를 추가로 요청받았다면 어느 담보의 어떤 사실을 확인하는지 본인 보험사에 먼저 문의하세요.'))
   block.append(paragraph('<strong>가상 예시: 담석 진단과 담낭절제술 자료만 가진 경우.</strong> 진단서에는 담석증, 수술확인서에는 복강경 담낭절제술이 적혀 있고 조직검사 결과지는 아직 없다고 가정합니다. 수술비에 필요한 정보와 추가 요청 자료를 구분하고, 조직검사가 실제 시행됐는지 확인합니다. 미발급·결과 미확정·검사 미시행을 같은 상태로 기록하지 않습니다. 보험 종수나 지급을 정하는 예시는 아닙니다.'))
   mark(block);anchor.insert_after(block)
   existing=block.find_next_sibling('ul');assert existing
   existing['class']=list(dict.fromkeys(existing.get('class',[])+['practical-checklist']))
   li=s.new_tag('li');li.string='□ 조직검사 결과를 요청받았다면 환자·검사일과 시행 여부·결과 확정 상태를 확인하고, 미확인 정보는 추정해 채우지 않습니다.';existing.append(li);mark(existing)
   changes=['기존 ERCP 예시는 유지하고 빠져 있던 진단·수술·병리 자료 비교 보강','자료 보유 상태 체크리스트와 조직검사 미보유 가상 예시 추가']
   dedup.append({'path':path,'alreadyPresent':'종수 핵심표·담낭절제술/ERCP 가상 예시·문의 양식','decision':'ERCP를 다시 설명하지 않고 진단·수술·병리 자료의 역할만 보강; 자세한 추가 요청은 기존 연결 글 유지'})
  elif idx==3:
   first=s.main.find('table');first.replace_with(mark(table('백내장 수술 후 담보별 확인 자료 비교',['담보','중심 자료','보험사에 나눠 물을 항목'],[
    ['종수술비','실제 수술명·수술일·좌우 눈 + 적용 수술분류표','어느 항목·사용 지침을 적용하는지. 렌즈 가격으로 종수 추정 금지'],
    ['질병수술비','진단·수술 사실 + 특약의 수술 정의·제외 규정','가입 담보의 지급사유와 횟수 조건. 종수술비 답변으로 대신하지 않기'],
    ['실손의료비','진료비 영수증·세부내역서 + 계약상 입원·통원 기준','실제 부담액 중 검토·제외·공제하는 항목과 추가자료. 정액 수술비와 별도 확인']
   ])))
   h=h2(s,'청구 전 자료 준비 순서');ul=h.find_next_sibling('ul');assert ul
   ul.replace_with(mark(checklist(['증권에서 종수술비·질병수술비·실손 담보를 각각 적고 없는 담보는 가입한 것으로 가정하지 않습니다.','양쪽 눈이라면 수술명·시행일·좌우 표시를 나누고, 검사일·서류 발급일과 혼동하지 않습니다.','비용자료의 수술·검사·렌즈 항목을 구분하고 실제 부담액과 계약의 확인 항목을 따로 적습니다.','새 진단서·기록지를 발급하기 전 필요한 사실과 보유자료 대체 가능 여부부터 문의합니다.'])))
   h=s.select_one('#record-check');p=h.find_next_sibling('p');put(p,'가상으로 왼쪽 눈과 오른쪽 눈 수술 뒤 정액 수술비에 관한 회신만 받았고, 실손 비용은 심사 중이라고 가정합니다. 정액 수술비 답변을 근거로 실손도 승인됐다고 적지 않고 아래처럼 미확인 항목을 남깁니다. 실제 지급 사례나 종수의 정답이 아닙니다.');mark(p)
   t=next_table(h);t.replace_with(mark(table('가상 양안 수술의 회신 상태 정리',['가상 기록','확인된 부분','남은 확인'],[
    ['왼쪽 눈 수술의 분류 회신','해당 계약·수술일에 대한 분류 항목 회신을 보관','오른쪽 눈과 묶는지·각각인지의 지급 횟수 규정'],
    ['오른쪽 눈의 별도 수술 기록','좌우·시행일·수술명 자료를 구분','왼쪽 눈의 답변이 오른쪽에도 적용되는지와 근거'],
    ['실손 비용은 심사 중','영수증·세부내역서 제출 및 접수 상태까지만 기록','검사·수술·인공수정체 항목별 결과와 제외·공제 사유']
   ])))
   changes=['기존 핵심표를 담보별 자료·질문 비교표로 개선','기존 준비 체크리스트 구체화','기존 양안 가상 예시를 확인됨/미확인 상태 비교로 갱신']
   dedup.append({'path':path,'alreadyPresent':'담보 3종 표·청구 전 체크리스트·양안 예시·문의 양식','decision':'기존 표·목록·예시 갱신; 입원/통원·다초점·횟수 상세 글의 내용을 재복제하지 않음'})
  else:
   h=s.select_one('#record-check');put(h,'카티스템 견적서·최종 영수증·세부내역서 대조')
   t=next_table(h);t.replace_with(mark(table('카티스템 치료 전후 청구자료 대조',['자료','확인할 항목','차이가 있으면'],[
    ['치료 전 견적서','예상 품목·포함 범위·작성 시점','보험금 산출서나 최종 지출 증빙으로 쓰지 않고 변경 항목 표시'],
    ['최종 계산서·영수증','실제 정산 내역·진료기간·본인부담액','견적과 다르면 병원에 추가·변경·정산된 비용의 항목을 문의'],
    ['진료비 세부산정내역서','제품명·수량·약제/행위/치료재료 구분·급여/비급여','실제 병원 기재를 유지하며 항목 이름·수량의 의미를 원무과에 확인'],
    ['보험사 보완 요청','접수번호·요청 문서·필요한 기간과 사실','이미 제출한 비용자료와 대조하고 필요한 진료기록 범위를 문의']
   ])))
   sec=h.parent
   p=next(p for p in sec.select('p')if'카티스템은 의약품입니다' in p.get_text())
   p.insert_after(mark(checklist(['견적·영수증·세부내역서의 환자·진료기간이 같은 치료를 가리키는지 확인합니다.','제품 관련 비용과 수술·마취·입원·재활 비용을 분리하되 병원 항목명을 임의로 바꾸지 않습니다.','원무과의 정산 설명과 보험사의 보장 판단을 별도로 기록합니다. 비용 차이만으로 과다청구나 지급 거절을 단정하지 않습니다.'])))
   check=sec.select_one('.practical-checklist')
   check.insert_after(mark(paragraph('<strong>가상 예시: 견적보다 최종 금액이 달라진 경우.</strong> 견적에는 제품·수술 예상액이 묶여 있고 최종 내역에는 약제·마취·추가 입원 항목이 나뉘어 있다고 가정합니다. 먼저 병원에 같은 기간의 최종 정산과 항목별 차이를 묻고, 실제 본인부담 자료를 보험사에 제출합니다. 견적과의 차액을 예상 보험금으로 계산하지 않습니다. 가상의 정리 상황이며 실제 병원 가격·권장 사용량·지급 사례가 아닙니다.')))
   p.clear();p.append(frag(f'<a href="{MFDS}" target="_blank" rel="noopener noreferrer">식약처 품목정보</a>').a);p.append('에서 카티스템은 의약품으로 확인됩니다. 제품 관련 비용을 편의상 재료대라고 부르더라도 실제 약제·행위·치료재료 구분은 병원 세부내역을 따릅니다. 이 비교는 비용자료 정리 방법이며, 허가사항이 개인 실손의 지급 여부를 정하지 않습니다.')
   changes=['기존 보완서류 표를 견적·영수증·세부내역·보완요청 대조표로 교체','치료 전후 자료 체크리스트와 정산 차이 가상 예시 보강']
   dedup.append({'path':path,'alreadyPresent':'청구 핵심표·비용별 서류표·접수 순서·보완요청 표','decision':'중복되던 하단 보완요청 표를 치료 전후 비교로 교체; 상단 청구 항목표와 역할 분리'})
  # Stable URLs, titles, images, existing links and anchor IDs are preserved.
  assert s.title.get_text()==old.title.get_text() and s.h1.get_text()==old.h1.get_text()
  assert s.find('link',rel='canonical')==old.find('link',rel='canonical')
  assert [str(n)for n in s.main.select('img')]==[str(n)for n in old.main.select('img')]
  assert not Counter(a['href']for a in old.main.select('a[href]'))-Counter(a['href']for a in s.main.select('a[href]'))
  assert set(n['id']for n in old.main.select('[id]')).issubset(set(n['id']for n in s.main.select('[id]')))
  ids=[n['id']for n in s.select('[id]')];assert len(ids)==len(set(ids)),path
  for sc in s.select('script[type="application/ld+json"]'):
   try:obj=json.loads(sc.string)
   except (TypeError,ValueError):continue
   def upd(x):
    if isinstance(x,dict):
     if x.get('@type')in['Article','BlogPosting']:x['dateModified']='2026-10-29'
     for v in x.values():upd(v)
    elif isinstance(x,list):
     for v in x:upd(v)
   upd(obj);sc.string=json.dumps(obj,ensure_ascii=False)
  (OUT/'before'/(path[1:].replace('/','__')+'.html')).write_text(raw,'utf-8');f.write_text(str(s)+'\n','utf-8')
  manifest.append({'path':path,'title':s.title.get_text(),'changes':changes,'preserved':['URL','title','H1','canonical','image tags','existing links','existing anchor IDs']})
 # Scoped caption/checklist styles: no shared site CSS changes.
 for path in PATHS:
  f=ROOT/(path[1:]+'.html');s=BeautifulSoup(f.read_text('utf-8'),'html.parser');style=s.new_tag('style',id='practical-review-style');style.string='.cluster-reading .practical-comparison caption{caption-side:top;text-align:left;font-size:16px;font-weight:700;line-height:1.7;color:#244463;padding:12px 0}.cluster-reading .practical-checklist{list-style:none;padding-left:0}.cluster-reading .practical-checklist li{margin-bottom:12px}.cluster-reading .practical-tools h3{font-size:21px;line-height:1.6;margin-top:28px;overflow-wrap:anywhere}@media(max-width:600px){.cluster-reading .practical-comparison caption{display:block;padding:10px 0;font-size:15px}.cluster-reading .practical-tools h3{font-size:19px}}';s.head.append(style);f.write_text(str(s)+'\n','utf-8')
 sm=ROOT/'sitemap.xml';text=sm.read_text('utf-8')
 for path in PATHS:text=re.sub(r'(<loc>https://hospital\.hbuby\.com'+re.escape(path)+r'</loc>\s*<lastmod>)[^<]+',r'\g<1>2026-10-29',text)
 sm.write_text(text,'utf-8')
 (OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),'utf-8')
 (OUT/'duplicate-review.json').write_text(json.dumps(dedup,ensure_ascii=False,indent=2),'utf-8')
 print('Updated',len(manifest),'existing articles')

if __name__=='__main__':main()
