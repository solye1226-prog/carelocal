from pathlib import Path
import re, json, html
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/ctr-refresh5-plan5-2026-10-27'
OUT.mkdir(exist_ok=True)

def fragment(text):
    return BeautifulSoup(text, 'html.parser')

def replace_section(soup, heading, markup):
    h = next(x for x in soup.select('main h2') if x.get_text(strip=True) == heading)
    following = []
    for node in h.next_siblings:
        if getattr(node, 'name', None) == 'h2':
            break
        following.append(node)
    h.insert_before(fragment(markup))
    for node in following:
        node.extract()
    h.extract()

updates = [
('surgery-benefit/thyroid-surgery-benefit.html',
 '갑상선 수술비 몇 종일까? 암·양성결절과 절제술 확인법',
 '갑상선 절제술의 수술 종수는 진단코드 하나로 정해지지 않습니다. 암·양성결절, 엽절제·전절제·고주파 치료를 구분하고 내 수술분류표와 청구서류를 대조하는 순서를 안내합니다.',
 '<strong>갑상선 수술이 몇 종인지는 실제 수술명과 가입한 특약의 수술분류표를 대조해야 알 수 있습니다.</strong> 갑상선암인지 양성결절인지, 엽절제·전절제인지 고주파 치료인지부터 구분하세요. 암 진단비의 분류와 수술비 종수는 별개입니다. 아래에서 본인 치료에 맞는 확인 경로를 고를 수 있습니다.'),
('surgery-benefit/type-surgery-benefit-claim.html',
 '종수술비 청구서류와 계산 방법, 내 수술 몇 종인지 확인하기',
 '종수술비 청구는 수술확인서의 진단명·수술명·수술일과 가입 당시 분류표를 대조하는 것부터 시작합니다. 종수별 지급액, 동시수술과 추가서류 요청 시 확인할 항목을 정리합니다.',
 '<strong>종수술비는 수술확인서와 내 계약의 수술분류표를 대조한 뒤, 해당 종수의 약정 금액과 지급 조건을 확인해 청구합니다.</strong> 먼저 증권에서 특약명·가입금액을 찾고, 확인서에서 진단명·수술명·시행일을 확인하세요. 1~3종인지 1~5종인지에 따라 표가 다르며, 진단코드만으로 종수를 정할 수는 없습니다.'),
('standards/actual-vs-fixed-benefit.html',
 '실손·정액보험 차이, 보험 2개면 중복으로 받을 수 있을까?',
 '실손은 보장 대상 의료비에서 공제·한도를 적용하고, 정액은 약관의 지급 사유와 약정 금액을 확인합니다. 실비 두 건과 실비·수술비 조합의 중복 청구 차이를 비교합니다.',
 '<strong>실손은 보장 대상인 실제 의료비를 기준으로, 정액은 약관에서 정한 사건과 금액을 기준으로 지급합니다.</strong> 실비와 정액 수술비는 각 요건을 충족하면 함께 청구할 수 있습니다. 실비 두 건은 같은 의료비를 두 배로 받는 조합이 아닙니다. 아래 표에서 내 보험 조합과 준비할 자료를 확인하세요.'),
('standards/indemnity-proportional-compensation.html',
 '실손 비례보상 계산, 보험 2개인데 왜 반씩 안 나올까?',
 '실손보험 2개의 비례보상은 무조건 50:50이 아닙니다. 인정 의료비, 단독 보상책임액, 분담액을 대조하고 회사별 산출내역이 다를 때 확인할 질문과 계산 예시를 안내합니다.',
 '<strong>실손 비례보상은 같은 의료비에 대한 보상책임을 보험사들이 나누는 방식으로, 보험이 두 개라고 항상 절반씩 지급하지는 않습니다.</strong> 가입 시기·보장 범위·공제·한도가 다를 수 있기 때문입니다. 영수증 합계를 나누기 전에 양쪽의 인정 의료비와 단독 보상책임액, 최종 분담액을 받아 비교하세요.'),
('standards/policyholder-insured-beneficiary.html',
 '계약자·피보험자·수익자 차이, 보험금은 누가 받나요?',
 '계약자는 계약의 당사자, 피보험자는 보장의 대상, 수익자는 해당 보험금을 받을 권리자입니다. 보험료 납입자·대리청구인·입금 계좌와 구분하는 가족보험 예시를 확인하세요.',
 '<strong>계약자는 보험계약을 맺은 사람, 인보험의 피보험자는 생명·신체 보장의 대상, 보험수익자는 해당 보험금을 받을 권리자입니다.</strong> 보험료를 낸 사람이나 서류를 대신 접수한 사람이 자동으로 보험금을 받는 것은 아닙니다. 같은 증권에서도 사망보험금과 진단·수술보험금의 수익자 항목을 따로 확인하세요.')
]

log=[]
for path,title,desc,lead in updates:
    file=ROOT/path
    raw=file.read_text(encoding='utf8')
    (OUT/(file.stem+'-before.html')).write_text(raw,encoding='utf8')
    s=BeautifulSoup(raw,'html.parser')
    s.title.string=title
    s.h1.string=title
    for m in s.select('meta[name="description"],meta[property="og:description"]'):
        m['content']=desc
    for m in s.select('meta[property="og:title"]'):
        m['content']=title
    for script in s.select('script[type="application/ld+json"]'):
        data=json.loads(script.string)
        def upd(obj):
            if isinstance(obj,dict):
                if obj.get('@type') in ('Article','BlogPosting'):
                    obj.update(headline=title,description=desc,dateModified='2026-10-27')
                for val in obj.values():upd(val)
            elif isinstance(obj,list):
                for val in obj:upd(val)
        upd(data)
        script.string=json.dumps(data,ensure_ascii=False)
    el=s.select_one('main .lead')
    el.clear(); el.append(fragment(lead))
    # This page set already has responsive tables; use the same card-label pattern.
    main=s.find('main')
    if 'cluster-reading' not in main.get('class',[]):
        main['class']=main.get('class',[])+['cluster-reading']
    if not s.select_one('link[href*="cluster-reading.css"]'):
        s.head.append(s.new_tag('link',rel='stylesheet',href='/assets/cluster-reading.css?v=20261014'))
    if 'terms-article' in main.get('class',[]):
        style=s.new_tag('style',id='responsive-label-override')
        style.string='.cluster-reading.terms-article table td::before{content:none!important}'
        s.head.append(style)
    for a in s.select('a[href]'):
        href=a['href']
        if href.startswith('/') and href.endswith('.html') and (ROOT/href.lstrip('/')).exists():
            a['href']=href[:-5]
        if 'fsc.go.kr/po010105/79180' in href:
            a['href']='https://www.fsc.go.kr/no010101/79180'
    if file.stem=='thyroid-surgery-benefit':
        replace_section(s,'갑상선암 수술비 핵심 확인','''<h2 id="treatment-route">갑상선 수술 종류에 따라 먼저 확인할 자료</h2>
<table><thead><tr><th>받은 치료</th><th>기록에서 볼 항목</th><th>연결해서 확인할 내용</th></tr></thead><tbody>
<tr><td>갑상선암 엽절제·전절제</td><td>절제 범위·수술명·시행일, 림프절 수술 동반 여부</td><td>이 글에서 수술비를 확인하고 <a href="/diagnosis-benefit/thyroid-cancer-benefit-claim">암 진단비는 별도로 대조</a></td></tr>
<tr><td>양성결절 절제</td><td>최종 진단과 실제 절제 행위</td><td><a href="/surgery-benefit/benign-thyroid-nodule-surgery-benefit">양성결절 수술비 확인 경로</a></td></tr>
<tr><td>고주파 열치료</td><td>절제술과 다른 실제 시술명·치료 목적</td><td><a href="/surgery-benefit/thyroid-nodule-rfa-surgery-benefit">고주파 치료의 수술 정의 확인</a></td></tr>
</tbody></table><p>로봇·내시경은 접근 방법에 관한 정보입니다. <a href="https://www.cancer.go.kr/lay1/program/S1T211C212/cancer/view.do?cancer_seq=3341&amp;menu_seq=3357" target="_blank" rel="noopener">국가암정보센터의 갑상선암 치료 설명</a>에서 엽절제와 전절제를 구분하듯, 기록에는 실제 절제 범위를 확인해 두세요. 이 의학적 구분만으로 보험 종수가 확정되지는 않습니다.</p>''')
        h=next(x for x in s.select('main h2') if x.get_text()=='확인 순서')
        h.insert_before(fragment('''<section id="thyroid-inquiry"><h2>보험사에 종수 근거를 물어볼 때</h2><p><strong>가상 예시:</strong> 확인서에 ‘갑상선 엽절제술’이 적혀 있고 로봇수술 비용도 발생했다면, 수술비 종수 확인에는 실제 절제술을, 실손 확인에는 영수증·세부내역서를 대조합니다. 두 담보의 결과를 같은 금액으로 예상하지 않습니다.</p><p>문의할 때는 “제 특약명은 ○○이고 수술확인서의 수술명은 ○○입니다. 적용한 수술분류표 항목·주석과 지급 횟수 규정을 알려주세요. 현재 확인서에서 부족한 정보가 있다면 필요한 항목도 안내해 주세요”처럼 적을 수 있습니다.</p></section>'''))
    elif file.stem=='type-surgery-benefit-claim':
        replace_section(s,'종수술비 보험금 청구 핵심 체크','''<h2 id="claim-start">종수술비 청구, 이 순서로 확인하세요</h2><ol><li><strong>증권:</strong> 특약명·가입일·가입금액을 확인하고 해당 계약의 약관을 준비합니다.</li><li><strong>수술확인서:</strong> 진단명·수술명·시행일을 대조합니다. 추가 자료가 필요한지 먼저 보험사에 확인합니다.</li><li><strong>분류표:</strong> 실제 시행한 수술에 해당하는 항목과 주석, 동시수술·재수술 규정을 찾습니다.</li><li><strong>산출내역:</strong> 적용 종수와 약정 금액, 감액·횟수 적용 결과를 확인합니다.</li></ol><p><a href="https://www.kbinsure.co.kr/CG205020003.ec" target="_blank" rel="noopener">KB손해보험 공식 수술비 서류 안내</a>는 진단명·수술명·수술일이 포함된 수술확인서와 필요시 수술기록지를 안내합니다. 모든 기록을 먼저 유료 발급하기보다 본인 보험사의 요구 항목을 확인하세요.</p>''')
        h=next(x for x in s.select('main h2') if x.get_text()=='종수를 안내받아도 지급액을 다시 확인하는 이유')
        h.insert_before(fragment('''<section id="tier-payment-example"><h2>종수와 지급액을 연결하는 가상 예시</h2><p>보험사가 내 계약의 해당 종수 지급액을 30만 원으로 안내했고, 지급 사유를 충족하며 감액·횟수 제한이 없다고 가정하면 그 담보는 30만 원을 기준으로 확인합니다. 실제 병원비가 100만 원이라고 해서 차액 70만 원까지 종수술비에서 지급되는 계산은 아닙니다.</p><p>증권에 적힌 ‘가입금액’이 모든 종수의 최종 지급액을 뜻하는지도 확인하세요. 상품에 따라 종수별 약정액 또는 가입금액에 적용하는 비율이 다를 수 있습니다. <a href="/standards/actual-vs-fixed-benefit">실손과 정액의 계산 차이</a>와 <a href="/claims/surgery-record-additional-request">수술기록지 추가 요청 대응</a>을 이어서 볼 수 있습니다. 이 금액은 실제 상품의 지급표가 아닙니다.</p></section>'''))
    elif file.stem=='actual-vs-fixed-benefit':
        replace_section(s,'실손보상과 정액보상, 기준이 다릅니다','''<h2 id="benefit-comparison">실손·정액 차이를 보험 조합으로 비교하세요</h2><table><thead><tr><th>내 보험 조합</th><th>지급 기준</th><th>청구할 때 확인할 자료</th></tr></thead><tbody><tr><td>실비 한 건</td><td>보장 대상 의료비에 공제·한도 등을 적용</td><td>영수증·세부내역서와 계약의 보장 범위</td></tr><tr><td>실비 두 건</td><td>같은 의료비를 계약별 보상책임에 따라 분담</td><td><a href="/standards/indemnity-proportional-compensation">회사별 산출내역과 비례보상</a></td></tr><tr><td>실비 + 정액 수술비</td><td>의료비 보장 요건과 약관상 수술 요건을 각각 확인</td><td>비용자료 + 진단명·수술명·시행일 자료</td></tr><tr><td>정액 진단비·수술비 여러 건</td><td>각 계약의 지급 사유·약정 금액·감액·횟수 규정</td><td>계약별 특약과 해당 사건을 입증하는 서류</td></tr></tbody></table><p>실비는 실손의료보험을 일상적으로 부르는 말입니다. 반면 ‘정액보험’은 한 상품의 이름보다는 보상 방식을 설명하는 말이므로, 한 증권에 실손형·정액형 특약이 함께 있는지도 확인하세요.</p><figure class="guide-image-panel"><img src="/assets/images/actual-vs-fixed-benefit-thumb.png" width="1672" height="941" loading="eager" decoding="async" alt="실손과 정액보험의 지급 기준을 비교하는 안내"></figure><div class="insurance-company-cta"><a href="/insurance-companies/">보험사별 공식 홈페이지 확인하기</a></div>''')
    elif file.stem=='indemnity-proportional-compensation':
        h=next(x for x in s.select('main h2') if x.get_text()=='실손보상은 영수증 전액 환급과 다릅니다')
        h.insert_before(fragment('''<nav class="reading-nav" aria-label="비례보상 확인 순서"><a href="#proportion-example">가상 분담 계산</a><a href="#proportion-review">산출내역이 다를 때</a></nav><section id="proportion-inputs"><h2>반씩 나누기 전에 받아야 할 숫자 3가지</h2><ol><li><strong>인정 의료비:</strong> 같은 진료일·항목이 각 계약에서 보장 대상인지 확인합니다.</li><li><strong>단독 보상책임액:</strong> 다른 실손이 없다고 보았을 때 해당 계약의 공제·한도를 반영한 금액을 확인합니다.</li><li><strong>최종 분담액:</strong> 중복계약 조항에 따라 실제로 나눈 금액과 적용 근거를 받습니다.</li></ol><p>보험사가 안내한 분담 기준금액과 책임 비율이 있어야 아래 계산 예시를 대조할 수 있습니다. 모든 계약에 같은 산식을 넣는 계산기로 사용하지 마세요.</p></section>'''))
        for h in s.select('main h2'):
            if h.get_text()=='기준금액과 분담 비율을 안내받았을 때의 계산 예시':h['id']='proportion-example'
            if h.get_text()=='두 회사의 계산이 다를 때 산출내역을 대조하는 순서':h['id']='proportion-review'
        # The medical-cost question should not open with an unrelated property example.
        for p in list(s.select('main p')):
            if p.get_text().startswith('재물보험도 같은 방식으로 수리 견적'):
                p.extract()
    else:
        h=next(x for x in s.select('main h2') if x.get_text()=='내 계약에서 확인할 순서')
        h.insert_before(fragment('''<section id="family-claim-example"><h2>부모가 보험료를 내고 자녀가 수술했다면?</h2><p><strong>가상 예시:</strong> 어머니가 계약자, 성인 자녀가 피보험자이고 수술보험금 수익자도 자녀로 지정됐다고 가정합니다. 어머니가 보험료를 내거나 청구를 도와도 그 사실만으로 수익자가 어머니로 바뀌지는 않습니다. 접수인은 어머니일 수 있지만 대리접수 절차는 별도로 확인해야 합니다.</p><table><thead><tr><th>확인하는 질문</th><th>볼 항목</th></tr></thead><tbody><tr><td>누구의 수술을 보장하나요?</td><td>피보험자와 담보의 보장 범위</td></tr><tr><td>누가 보험금을 청구할 권리가 있나요?</td><td>해당 수술보험금의 수익자 지정</td></tr><tr><td>누가 대신 접수하고 어느 계좌로 받나요?</td><td>위임·본인확인과 보험사의 계좌 요건</td></tr></tbody></table><p>수익자 변경은 계좌 변경과 다른 절차입니다. <a href="https://www.law.go.kr/법령/상법/제733조" target="_blank" rel="noopener">상법 제733조</a>의 지정·변경 권리와 함께 <a href="https://www.law.go.kr/법령/상법/제734조" target="_blank" rel="noopener">제734조의 보험사 통지 및 관련 요건</a>을 확인해야 합니다. 변경 접수 전에 지급 사유·동의 요건과 처리 완료 내역을 보험사에 확인하세요.</p></section>'''))
    # Keep the shared responsive table labels synchronized with actual headers.
    for table in s.select('main table'):
        headers=[x.get_text(' ',strip=True) for x in table.select('thead th')]
        for th in table.select('thead th'):th['scope']='col'
        for tr in table.select('tbody tr'):
            for i,td in enumerate(tr.find_all('td',recursive=False)):
                if i<len(headers):
                    td['data-label']=headers[i]
                    for label in td.select('.cell-label'):label.extract()
                    span=s.new_tag('span',attrs={'class':'cell-label','aria-hidden':'true'})
                    span.string=headers[i];td.insert(0,span)
    for a in s.select('a[href="#section-4"]'):
        if file.stem=='indemnity-proportional-compensation':
            a['href']='#proportion-review'
            a.string='산출내역이 다를 때 대조하는 순서'
    if file.stem=='indemnity-proportional-compensation':
        for nav in s.select('nav[aria-label="비례보상 확인 순서"]'):nav.extract()
    file.write_text(str(s).rstrip()+'\n',encoding='utf8')
    log.append({'path':'/'+path[:-5],'title':title,'description':desc})

# Only touched pages receive a fresh sitemap modification date.
sm=ROOT/'sitemap.xml'
text=sm.read_text(encoding='utf8')
for r in log:
    url='https://hospital.hbuby.com'+r['path']
    pat=r'(<url>\s*<loc>'+re.escape(url)+r'</loc>\s*<lastmod>)[^<]+'
    text,n=re.subn(pat,r'\g<1>2026-10-27',text)
    if n!=1:raise RuntimeError('sitemap missing '+url)
sm.write_text(text,encoding='utf8')
(OUT/'changes.json').write_text(json.dumps(log,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(log,ensure_ascii=False,indent=2))
