from pathlib import Path
from bs4 import BeautifulSoup
import json,html,re
R=Path(__file__).resolve().parents[1];O=R/'docs/surgery-table-rewrite-2026-11-03';F=R/'surgery-benefit/surgery-classification.html'
old=(O/'before.html').read_text(encoding='utf8') if (O/'before.html').exists() else F.read_text(encoding='utf8');(O/'before.html').write_text(old,encoding='utf8');s=BeautifulSoup(old,'html.parser')
url=next(a['href'] for a in s.find_all('a',href=True) if 'abllife.co.kr' in a['href'])
title='수술분류표 1종·2종·3종, 실제 수술 종류와 약관 항목 비교'
desc='백내장 1종, 충수절제술 2종, 갑상선 관혈수술 3종 등 실제 1~5종 약관의 수술분류표 예시를 정리합니다. 수술코드·분류표 항목 번호·종수 차이와 복강경·내시경 적용도 비교합니다.'
def a(path,label):return f'<a href="{path}">{label}</a>'
def table(headers,rows):
 return '<table><thead><tr>'+''.join('<th scope="col">'+h+'</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td><span class="cell-label" aria-hidden="true">'+headers[i]+'</span>'+v+'</td>' for i,v in enumerate(row))+'</tr>' for row in rows)+'</tbody></table>'
rows=[
 ['1종','백내장·수정체 관혈수술','71항 · 164쪽','눈 수술 전체를 뜻하지 않음'],
 ['1종','편도·아데노이드 절제','17항 · 162쪽','같은 날 함께 한 수술의 지급 횟수는 별도'],
 ['1종','치핵·치루 등의 근본수술','44항 · 163쪽','근치를 목적으로 하지 않은 수술 제외'],
 ['2종','충수절제술','41항 · 163쪽','충수 주위 농양 등 포함 범위는 원문 참조'],
 ['2종','뼈 이식수술','5항 · 162쪽','치과 처치·수술에 수반되는 경우 제외'],
 ['2종','관혈적 고막성형술','79항 · 165쪽','고막 패치술 제외'],
 ['3종','갑상선·부갑상선 관혈수술','57항 · 164쪽','고주파치료를 이 행에 바로 대입하지 않음'],
 ['3종','담낭·담도 관혈수술','36항 · 163쪽','개복 조건과 복강경 주석을 함께 확인'],
 ['3종','유방절단수술','3항 · 162쪽','기타 유방수술과 구분; 악성신생물 수술은 별도 표도 확인'],
 ['4종','위를 절제하는 개복수술','33항 · 163쪽','내시경 절제와 같은 행으로 보지 않음'],
 ['5종','개흉술을 수반하는 심장 내 관혈수술','26항 · 163쪽','구체적 시행 방법과 표의 조건 대조']]
base=f'<a href="{url}#page=162" target="_blank" rel="noopener">ABL생명 2023년 11월 약관 원문: 별표5, 162~167쪽</a>'
crumb=str(s.main.find(class_='breadcrumb'));meta=str(s.main.find(class_='article-meta'));figs=[str(x) for x in s.main.find_all('figure')];cta=str(s.main.find(class_='kakao-inquiry-cta'))
insurer='<div class="article-actions">'+a('/insurance-companies/','보험사별 공식 홈페이지 확인하기')+'</div>'
# Preserve the existing surgery-specific routes, while removing repeated generic explanations.
start=s.find(id='surgery-examples');links=[]
for x in start.next_siblings:
 if getattr(x,'name',None)=='h2':break
 if getattr(x,'find_all',None):
  for z in x.find_all('a',href=True):
   if z['href'].startswith('/') and z['href'] not in [p for p,l in links]:links.append((z['href'],z.get_text(' ',strip=True)))
for z in s.select('.related-topic-connections a, aside.notice a'):
 if z['href'] not in [p for p,l in links]:links.append((z['href'],z.get_text(' ',strip=True)))
body=crumb+f'<h1>{title}</h1>'+meta+'''<p class="lead">수술분류표의 1종·2종·3종은 보험에서 수술을 나눈 지급 분류입니다. 실제 약관 예시에서는 백내장 수술은 1종, 충수절제술은 2종, 갑상선 관혈수술은 3종으로 적혀 있습니다.</p><p>아래에서 수술 이름과 종수를 바로 비교할 수 있습니다. 예시는 <strong>ABL생명 (무)ABL인터넷네개딱패키지건강보험(갱신형), 2023년 11월 약관의 1~5종 분류표</strong>입니다. 과거 1~3종 특약이나 다른 상품의 공통표는 아닙니다.</p>'''
body+='''<nav class="reading-nav" aria-label="본문 바로가기"><a href="#actual-table">수술별 종수 표</a><a href="#method-difference">복강경·내시경 차이</a><a href="#surgery-code">수술코드와 종수</a><a href="#surgery-examples">수술별 상세 글</a></nav>'''
body+='<h2 id="actual-table">1종·2종·3종에는 어떤 수술이 있나요?</h2><p>다음은 해당 약관의 일반 질병·재해 치료 수술 항목을 추려 쉽게 정리한 표입니다. <strong>항목 번호와 쪽수는 원문을 찾기 위한 표시이며 병원의 수술코드가 아닙니다.</strong> 암 수술은 같은 약관의 별도 악성신생물 수술 표까지 봐야 합니다.</p><p>'+base+'</p>'+table(['종수','수술 종류 예시','약관 위치','함께 읽을 조건'],rows)
body+='<p>여기서 <strong>관혈수술</strong>은 병변을 직접 보며 수술하도록 피부를 절개하는 방식이라는 약관상의 뜻입니다. 단순히 피가 났다는 의미가 아닙니다. 1종을 “간단한 수술”, 3종을 “큰 수술”로만 외우면 위 표의 차이를 설명하기 어렵습니다. 실제 분류는 수술 부위·행위·방법과 약관의 항목에 따릅니다. 같은 3종이어도 지급액은 각 특약의 가입금액에 따라 달라집니다.</p>'+figs[0]
body+='''<h2>1~3종과 1~5종은 같은 분류표인가요?</h2><p><strong>서로 다른 분류 체계입니다.</strong> 위 표의 1·2·3종은 1~5종 체계 안의 앞 세 종류입니다. 이것을 1~3종 특약의 목록으로 바꾸어 읽으면 안 됩니다. 1~3종 계약은 그 계약의 세 종류 전체를, 1~5종 계약은 다섯 종류 전체를 대조해야 합니다.</p><p>따라서 “백내장은 항상 1종”이라고 일반화할 수는 없습니다. 이 글에서 확인한 약관의 71항은 1종이라는 구체적 예시입니다. 내 증권의 상품명·특약명·적용 약관이 같은지를 확인한 뒤 사용하세요.</p>'''
body+='<h2 id="method-difference">담낭절제술·용종절제술: 복강경과 내시경은 어떻게 다른가요?</h2><p>같은 약관 165쪽의 88항과 주석을 보면 실제 차이가 드러납니다. <strong>내시경·경피적 수술에는 별도 분류가 있고, 복강경·흉강경 수술은 해당 부위의 1~87항을 적용</strong>하도록 구분합니다.</p>'
body+=table(['실제 시행 내용','이 약관에서 읽을 항목','예시의 분류'],[
 ['복강경 담낭절제술','담낭·담도 수술 36항 + 165쪽 복강경 주석','해당 행과 주석을 함께 대조하면 3종으로 검토하는 예시'],
 ['위·대장 내시경 중 용종 절제','88-2항의 복부장기 내시경 수술 + 사용 지침','해당 조건을 충족하는 양성 용종 절제는 2종으로 검토하는 예시'],
 ['용종 절제 없이 관찰·검사만 시행','치료 목적 수술인지, 검사 제외 규정','내시경을 했다는 사실만으로 2종 수술이 되지는 않음']])
body+='<p>88항에는 수술 시작일부터 60일 안에 여러 번 시행한 경우를 한 번으로 계산하는 조건도 있습니다. 같은 약관 167쪽 사용 지침과 166쪽 악성신생물 수술 표가 적용되는 상황도 나누어 보세요. 위 예시는 수술기록이 해당 행위·조건과 일치한다는 전제이며 개인의 지급 확정 사례는 아닙니다.</p><p>'+a('/surgery-benefit/gallbladder-surgery-benefit','담낭절제술 수술비와 청구자료')+' · '+a('/claims/colonoscopy-polyp-insurance-claim','대장용종 제거 보험금과 내시경 기록')+'</p>'+figs[1]
body+='<h2 id="surgery-code">수술코드·질병코드·분류표 번호·종수 차이</h2>'+table(['표시','무엇을 뜻하나요?','어디서 확인하나요?'],[
 ['병원의 수술·행위코드','시행한 의료행위의 항목을 식별하는 코드. 보험 종수 자체는 아님','진료비 세부내역서·병원 기록의 실제 행위명과 함께 확인'],
 ['질병분류코드','어떤 질환을 진단했는지 나타내는 코드. 수술 방법까지 특정하지 않음','진단서·수술확인서 등의 진단명 항목'],
 ['약관의 71항·88-2항','이 예시 약관 안에서 수술 항목을 찾는 번호','해당 상품의 별표5'],
 ['1종·2종·3종','그 계약이 정한 수술보험금 지급 분류','수술분류표와 특약 지급표']])
body+='''<p>예를 들어 이 약관의 백내장 행에 적힌 <strong>“71”은 병원 수술코드가 아니라 분류표 항목 번호이고, “1종”이 보험의 분류 결과</strong>입니다. 병원 코드 하나를 인터넷에서 검색해 모든 계약의 종수를 확정하는 방식은 맞지 않습니다. 비슷한 수술명도 절제·봉합·재건·치환이 다를 수 있어 코드와 실제 행위명을 함께 읽어야 합니다.</p>'''
body+='''<h2>1종·2종·3종 수술비는 얼마를 받나요?</h2><p>위 분류표에는 종수가 있고, 돈은 증권과 해당 특약의 지급표에서 확인합니다. <strong>종수 × 임의의 고정금액</strong>으로 계산하는 공통 공식은 없습니다.</p><p>순수한 계산 예로, 가상의 계약에 “1종 20만 원·2종 50만 원·3종 100만 원”이라고 정해져 있고 감액·횟수 제한 없이 한 번 지급된다고 가정하면, 2종 수술의 기준금액은 50만 원입니다. 2 × 20만 원인 40만 원이 아닙니다. 이 숫자는 판매 상품의 실제 지급액이 아니라 계산 구조를 설명하기 위한 가정입니다.</p><p>한 번에 여러 수술을 했거나 같은 질환으로 재수술했다면 지급 횟수 규정을 추가로 적용합니다. 분류표에 해당한다는 사실과 최종 입금액은 구분해서 확인하세요.</p>'''
body+='<h2 id="surgery-examples">수술 종류별로 이어서 확인하기</h2><p>백내장·담낭·용종처럼 수술명으로 찾은 뒤, 실제 방법과 필요한 병원 자료를 세부 글에서 이어 볼 수 있습니다. 각 글의 설명 범위와 적용 약관을 함께 읽어 주세요.</p><ul>'+''.join('<li>'+a(p,l)+'</li>' for p,l in links)+'</ul>'
body+='''<h2 id="record-check">내 계약에 대입하는 세 가지 확인</h2><ol><li>증권에서 1~3종·1~5종 등 특약의 분류 체계를 확인합니다.</li><li>수술확인서의 실제 수술명·방법을 적용 약관의 행과 주석에 대조합니다. 이름이 다르면 수술기록의 행위와 분류 근거를 확인합니다.</li><li>가입금액과 동일일·반복수술·감액 규정을 적용해 지급액과 횟수를 확인합니다.</li></ol><p>유료 서류를 모두 먼저 발급받기보다 보험사에 기존 자료에서 부족한 항목을 확인하세요.</p><h3 id="insurer-question">분류가 다르게 안내됐을 때 문의 문구</h3><p id="inquiry-note" class="inquiry-template">“제 계약의 적용 약관과 별표 이름, 해당 항목 번호·종수·쪽수를 알려주세요. 수술확인서의 실제 수술명은 __이고 방법은 __입니다. 해당 항목에서 제외하거나 다른 종수를 적용했다면 주석·사용 지침과 그 이유도 함께 안내해 주세요.”</p>'''
body+='<p>'+a('/surgery-benefit/surgery-name-mismatch','수술명이 분류표와 다를 때')+' · '+a('/claims/surgery-claim-documents','수술비 청구서류')+' · '+a('/surgery-benefit/surgery-benefit-amount-review','수술비가 예상보다 적을 때')+'</p>'+figs[2]
body+='<section class="official-guide-actions"><h2 id="official-details">실제 수술분류표 원문 보기</h2><div class="official-guide-grid"><a class="official-guide-button" href="'+url+'#page=162" target="_blank" rel="noopener"><strong>ABL생명 예시 약관 PDF 열기</strong><span>2023년 11월판 · 별표5 162~167쪽 · 이 글의 종수 표와 주석 근거 ↗</span></a></div></section><p>이 글은 해당 판본의 예시를 설명하며 현재 판매 여부나 다른 계약의 보장을 뜻하지 않습니다. 실제 적용 약관은 본인 계약에서 확인하세요. 작성: <a href="/legal/about">케어로컬 사이트 운영자</a>.</p>'+insurer+cta
s.main.clear();s.main.append(BeautifulSoup(body,'html.parser'))
s.main.find('table')['class']='source-table'
style=s.new_tag('style',id='source-table-columns');style.string='@media(min-width:601px){.cluster-reading .source-table th:nth-child(1),.cluster-reading .source-table td:nth-child(1){width:10%}.cluster-reading .source-table th:nth-child(2),.cluster-reading .source-table td:nth-child(2){width:27%}.cluster-reading .source-table th:nth-child(3),.cluster-reading .source-table td:nth-child(3){width:20%}.cluster-reading .source-table th:nth-child(4),.cluster-reading .source-table td:nth-child(4){width:43%}}';s.head.append(style)
s.title.string=title
for key,val in [('description',desc),('og:title',title),('og:description',desc),('twitter:title',title),('twitter:description',desc)]:
 m=s.find('meta',attrs={'property' if key.startswith('og:') else 'name':key})
 if m:m['content']=val
schema=s.new_tag('script',type='application/ld+json');schema.string=json.dumps({'@context':'https://schema.org','@type':'Article','headline':title,'description':desc,'dateModified':'2026-11-03','author':{'@type':'Organization','name':'케어로컬'},'mainEntityOfPage':'https://hospital.hbuby.com/surgery-benefit/surgery-classification'},ensure_ascii=False);s.head.append(schema)
F.write_text(str(s)+'\n',encoding='utf8')
sm=R/'sitemap.xml';t=sm.read_text(encoding='utf8');t=re.sub(r'(<loc>https://hospital.hbuby.com/surgery-benefit/surgery-classification</loc>\s*<lastmod>)[^<]+',r'\g<1>2026-11-03',t);sm.write_text(t,encoding='utf8')
(O/'source-review.txt').write_text('Official ABL 2023-11 policy PDF downloaded. Printed/PDF pages162-165 rendered and visually inspected. Table clauses71=1,41=2,57=3; clause36 with clause88 laparoscopy note. Clause88 Fiberscope differs from laparoscopy. This is a 1-5 policy example, not an old1-3 universal table. No universal hospital procedure-code mapping asserted.\nSource: '+url+'\nHBUBY composition reference: direct answer, short TOC, comparison table, adjacent official PDF, detailed exceptions then related posts. No text copied.\n',encoding='utf8')
print('Rewritten',len(rows),'source-based example rows;',len(links),'existing detail routes preserved')
