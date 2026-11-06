from pathlib import Path
from bs4 import BeautifulSoup
import json,re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/major-article-recovery-2026-11-06'
OUT.mkdir(exist_ok=True)
POLICY=(ROOT/'docs/surgery-table-rewrite-2026-11-03/source-url.txt').read_text(encoding='utf-8').strip()
SPECS={
 'surgery-benefit/injury-surgery-classification':{
  'title':'상해 종수술비 분류표, 골절·인대 수술명과 특약 확인법',
  'lead':'<strong>상해수술비는 약정한 수술급여금을 지급하는 담보이고, 상해 종수술비는 수술분류표의 종수별 지급액을 확인하는 담보입니다.</strong> 증권에 실제로 가입한 특약 이름이 무엇인지 먼저 구분하세요. 골절·인대 파열이라는 진단명이나 병원 행위코드만으로 1종·2종·3종을 정할 수는 없습니다.',
  'description':'상해수술비와 상해 종수술비 차이부터 확인합니다. 골절·인대 수술명, 가입 당시 특별약관의 수술분류표, 동시수술·제거술의 지급 단위를 대조하는 방법입니다.'},
 'surgery-benefit/hemorrhoid-surgery-benefit':{
  'title':'치질 수술비 몇종? 치핵 근본수술 약관 예시와 청구서류',
  'lead':'<strong>치핵 근본수술을 1종으로 정한 1~5종 약관 예시가 있습니다.</strong> 하지만 모든 치질 치료나 모든 보험의 공통 종수는 아닙니다. 실제 시행한 치핵절제술·결찰·경화 처치를 구분하고 본인 특약의 수술 정의와 제외 조건을 확인하세요.',
  'description':'치질 수술비 몇종인지 실제 치핵 근본수술 1종 약관 예시로 확인합니다. 보험별 차이와 근치 목적 조건, 절제술·결찰술 구분, 청구서류를 정리합니다.',
  'section':f'''<section id="policy-example-hemorrhoid"><h2>치핵 수술비 1종의 실제 약관 예시</h2><p>ABL생명 (무)ABL인터넷네개딱패키지건강보험(갱신형) 2023년 11월판 별표5는 치핵·치루 등의 근본수술을 1종으로 분류하며, 근치를 목적으로 하지 않은 수술은 제외합니다. 결찰·경화 처치를 이 항목과 자동으로 같게 볼 수 없습니다.</p><p><strong>특정 상품의 1~5종 표 예시입니다. 다른 보험·특약·가입 시기나 과거 1~3종 표에 그대로 적용하지 마세요.</strong> <a href="{POLICY}#page=163" target="_blank" rel="noopener">ABL생명 예시 약관 원문 보기</a> · <a href="/surgery-benefit/surgery-classification">수술분류표 전체 예시</a></p></section>'''},
 'surgery-benefit/lumbar-disc':{
  'title':'허리디스크 수술비 몇종? 관혈·내시경 약관 예시와 청구서류',
  'lead':'<strong>추간판 관혈수술은 3종, 척추 내시경·경피적 수술은 2종으로 나눈 1~5종 약관 예시가 있습니다.</strong> 허리디스크라는 진단명만으로 3종을 정할 수는 없습니다. 실제 수술 방법과 본인 계약의 표·주석을 확인해야 합니다.',
  'description':'허리디스크 수술비 몇종인지 관혈수술 3종·내시경/경피적 수술 2종으로 구분한 특정 약관 예시를 비교합니다. 실제 시행명, 제외 사항, 청구기록을 확인하세요.',
  'section':f'''<section id="policy-example-disc"><h2>허리디스크 관혈수술·내시경수술 종수 비교</h2><table><caption>ABL생명 2023년 11월판 1~5종 약관의 예시</caption><thead><tr><th scope="col">해당 약관의 수술 항목</th><th scope="col">표에 적힌 종수</th></tr></thead><tbody><tr><td>척추·골반·추간판 관혈수술</td><td>3종</td></tr><tr><td>척추 내시경·경피적 수술</td><td>2종</td></tr></tbody></table><p>별표5의 9항과 88-2항을 비교한 예시입니다. 신경차단·약물주입까지 같은 수술로 보지 않으며, 진단명만으로 위 행에 대입하지 않습니다. <strong>보험·특약·가입 시기별 표와 제외 조건은 다릅니다.</strong> <a href="{POLICY}#page=162" target="_blank" rel="noopener">예시 약관 원문</a> · <a href="/surgery-benefit/surgery-classification#method-difference">관혈·내시경 적용 차이</a></p></section>'''},
 'surgery-benefit/acl-reconstruction':{
  'title':'십자인대 재건술 수술비, 상해 담보·동반 수술 청구서류',
  'lead':'<strong>십자인대 재건술 수술비는 재건술의 실제 시행명과 가입한 상해 담보를 대조해 청구합니다.</strong> 같은 날 연골판 봉합·절제도 받았다면 각 수술의 기록은 구분하되, 지급 횟수까지 자동으로 늘어난다고 보지는 않습니다. 봉합술·재건술과 보존적 치료를 나누어 확인하세요.',
  'description':'십자인대 재건술 수술비 청구 시 상해수술비·종수술비를 나눠 확인합니다. 재건술과 동반 연골판 수술, 사고 경위와 수술확인서·기록지 준비 순서입니다.'},
 'surgery-benefit/ureteroscopy':{
  'title':'요로결석 수술비 몇종? 요관경·체외충격파쇄석술 비교',
  'lead':'<strong>요로결석 수술비는 요관경 결석 제거와 체외충격파쇄석술(ESWL)을 구분해야 합니다.</strong> 요관경 수술은 몸 안으로 기구를 넣는 방법이고 ESWL은 몸 밖의 충격파로 결석을 부수는 방법입니다. 같은 결석 치료라도 가입 약관의 적용 항목과 반복 치료 규정은 따로 확인합니다.',
  'description':'요로결석 수술비 몇종인지 요관경 결석 제거와 ESWL 체외충격파쇄석술을 나눠 확인합니다. 특정 1~5종 약관 예시, 반복 치료 조건과 청구자료를 비교합니다.',
  'section':f'''<section id="policy-example-stone"><h2>요관경·체외충격파쇄석술 수술비 약관 비교</h2><table><caption>ABL생명 2023년 11월판 1~5종 표의 예시</caption><thead><tr><th scope="col">해당 표의 항목</th><th scope="col">종수·조건</th></tr></thead><tbody><tr><td>비뇨기 내시경·경피적 수술</td><td>88-3항: 1종</td></tr><tr><td>체외충격파쇄석술 ESWL</td><td>87항: 2종. ESWT는 제외</td></tr></tbody></table><p>요관경 수술이 해당 내시경 항목에 해당하는지 실제 기록으로 대조하는 예시입니다. 이 표의 두 항목에는 60일 이내 반복수술을 한 번으로 계산하는 조건도 있습니다. <strong>다른 보험의 공통 종수·반복 기준은 아닙니다.</strong> <a href="{POLICY}#page=165" target="_blank" rel="noopener">예시 약관의 항목·주석 보기</a> · <a href="/claims/surgery-claim-documents">수술확인서·기록지 준비</a></p></section>'''},
 'claims/insurance-claim-payout-period':{
  'title':'보험금 지급 기간, 3영업일 기준과 조사·지연 시 확인사항',
  'lead':'<strong>사고보험금은 청구서류 접수 후 3영업일 이내 지급을 기본으로 안내하지만, 조사·확인이 필요한 경우에는 적용 약관의 별도 기한과 지급예정일을 확인해야 합니다.</strong> 달력상의 3일과 영업일은 다릅니다. 접수번호·서류 접수일과 지연 사유를 함께 확인하세요.',
  'description':'보험금 지급 기간의 3영업일 기준, 토요일·공휴일 제외와 추가 조사 시 확인사항을 정리합니다. 접수일·보완 요청·지급예정일을 나누고 지연 사유를 문의하세요.',
  'section':'''<section id="business-day-basics"><h2>보험금 지급 기간의 3영업일은 달력 3일과 다릅니다</h2><p><a href="https://www.shinhangroup.com/kr/archive/insight/extend/detail/33149" target="_blank" rel="noopener">신한금융그룹 사고보험금 지급 안내</a>는 서류 접수 후 3영업일을 기본으로 설명하며, 토요일·일요일·공휴일을 영업일에서 제외합니다. 추가 조사 때의 기한·예정일은 별도로 확인하도록 안내합니다. 자동차·화재·배상책임 등 다른 청구까지 하나의 기한으로 단정하지 말고 본인 약관의 지급절차를 확인하세요.</p><p><strong>보완서류를 냈다는 이유만으로 기간이 언제나 처음부터 다시 시작된다고 생각하지 마세요.</strong> 보험사에 기산일, 적용 약관 조항, 부족한 자료, 지급예정일을 구체적으로 요청합니다. 실제 날짜를 받았다면 <a href="/claims/insurance-claim-delay">보험금 지급 지연 대응</a>에서 다음 절차를 확인할 수 있습니다.</p></section>'''}
}

for path,spec in SPECS.items():
    f=ROOT/(path+'.html');before=f.read_text(encoding='utf-8');(OUT/(f.stem+'-before.html')).write_text(before,encoding='utf-8')
    s=BeautifulSoup(before,'html.parser');m=s.select_one('main');s.title.string=spec['title'];m.h1.string=spec['title']
    lead=m.select_one('p.lead');lead.clear();lead.append(BeautifulSoup(spec['lead'],'html.parser'))
    for attrs,value in [({'name':'description'},spec['description']),({'property':'og:title'},spec['title']),({'name':'twitter:title'},spec['title']),({'property':'og:description'},spec['description']),({'name':'twitter:description'},spec['description'])]:
        tag=s.find('meta',attrs=attrs)
        if tag:tag['content']=value
    for h in m.select('h2'):
        text=h.get_text(' ',strip=True)
        if '핵심 확인' in text and len(text)>35:h.string=spec['title'].split('?')[0]+' 청구 전 핵심 확인'
    if spec.get('section'):
        frag=BeautifulSoup(spec['section'],'html.parser')
        if frag.select('table'):
            style=s.new_tag('link',rel='stylesheet',href='/assets/recovery-comparison.css?v=20261106');s.head.append(style)
        for table in frag.select('table'):
            table['class']=['recovery-comparison']
            headers=[x.get_text() for x in table.select('th')]
            for tr in table.select('tbody tr'):
                for j,td in enumerate(tr.select('td')):
                    label=frag.new_tag('span',attrs={'class':'cell-label','aria-hidden':'true'});label.string=headers[j];td.insert(0,label)
        first=m.find('h2');first.insert_before(frag)
    for tag in s.select('script[type="application/ld+json"]'):
        try:data=json.loads(tag.string or tag.get_text())
        except json.JSONDecodeError:continue
        def update(obj):
            if isinstance(obj,dict):
                if obj.get('@type') in ('Article','BlogPosting'):obj.update(headline=spec['title'],description=spec['description'],dateModified='2026-11-06')
                for v in obj.values():update(v)
            elif isinstance(obj,list):
                for v in obj:update(v)
        update(data);tag.string=json.dumps(data,ensure_ascii=False)
    f.write_text(str(s)+'\n',encoding='utf-8')

# Touch only modification dates for genuinely revised pages, preserving sitemap formatting.
p=ROOT/'sitemap.xml';text=p.read_text(encoding='utf-8')
for path in SPECS:
    pattern=r'(<url><loc>https://hospital\.hbuby\.com/'+re.escape(path)+r'</loc>)(.*?)(</url>)'
    def lastmod(match):
        inside=match.group(2)
        if '<lastmod>' in inside:inside=re.sub(r'<lastmod>.*?</lastmod>','<lastmod>2026-11-06</lastmod>',inside)
        else:inside='<lastmod>2026-11-06</lastmod>'+inside
        return match.group(1)+inside+match.group(3)
    text=re.sub(pattern,lastmod,text,flags=re.S)
p.write_text(text,encoding='utf-8')
(OUT/'changed-paths.json').write_text(json.dumps(list(SPECS),ensure_ascii=False,indent=2),encoding='utf-8')
print('Updated',len(SPECS),'existing articles.')
