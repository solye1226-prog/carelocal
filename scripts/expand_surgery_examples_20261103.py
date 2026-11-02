from pathlib import Path
from bs4 import BeautifulSoup
import json
R=Path(__file__).resolve().parents[1];O=R/'docs/surgery-table-examples-2026-11-03';O.mkdir(exist_ok=True)
F=R/'surgery-benefit/surgery-classification.html';old=(O/'before.html').read_text(encoding='utf8') if (O/'before.html').exists() else F.read_text(encoding='utf8');(O/'before.html').write_text(old,encoding='utf8');s=BeautifulSoup(old,'html.parser')
def table(head,rows,cls):
 return '<table class="'+cls+'"><thead><tr>'+''.join('<th scope="col">'+x+'</th>' for x in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td><span class="cell-label" aria-hidden="true">'+head[i]+'</span>'+v+'</td>' for i,v in enumerate(row))+'</tr>' for row in rows)+'</tbody></table>'
common=[
 ['백내장 수술','1종','수정체를 수술한 경우의 예시. 녹내장·망막 수술과 구분'],
 ['편도·아데노이드 절제','1종','편도 절제와 같은 날 시행한 다른 수술의 지급 횟수는 별도'],
 ['치핵·치루 근본수술','1종','약물·단순 처치가 아니라 근치를 목적으로 한 수술'],
 ['충수절제술(맹장염 수술)','2종','진단명만이 아니라 충수를 절제한 실제 기록 확인'],
 ['위·대장 내시경 용종절제','2종으로 검토','양성 용종을 실제 절제하고 해당 내시경 수술 조건을 충족한 경우. 검사만 한 경우·악성종양 수술과 구분'],
 ['갑상선·부갑상선 관혈수술','3종','절개 수술의 항목. 고주파치료·암 근치수술은 각각의 분류를 추가 확인'],
 ['담낭절제술(담낭 제거)','3종으로 검토','이 약관은 복강경 수술도 해당 부위의 항목을 적용한다는 주석이 있음'],
 ['척추·추간판 관혈수술','3종','허리디스크 진단만으로 적용하지 않음. 내시경·경피적 수술은 별도 지침 확인']]
ones=[
 ['백내장·수정체 수술','백내장 때문에 수정체에 시행한 관혈수술','다른 눈 수술까지 모두 1종인 것은 아님'],
 ['편도·아데노이드 절제술','편도나 아데노이드를 절제하는 수술','두 부위를 함께 수술한 경우 두 번 지급되는지는 별도 규정'],
 ['치핵·치루 근본수술','치질로 검색하는 수술 중 치핵·치루 등의 근본수술','단순 처치·비근치 목적 수술은 이 항목에서 제외'],
 ['탈장 근본수술','탈장을 근본적으로 교정하는 수술','다른 복부 수술을 모두 탈장 항목으로 볼 수는 없음'],
 ['하지정맥류 근본수술','다리 정맥류를 근본적으로 치료하는 수술','레이저·고주파 등 방법에 따라 내시경·경피적 지침과 실제 행위를 추가 대조'],
 ['안검하수 수술','눈꺼풀 처짐에 대한 안검하수증 수술','안검내반증은 해당 항목에서 제외. 미용 목적 제외 규정도 별도'],
 ['작은 범위의 피부이식','이식 면적이 25㎠ 미만인 피부이식수술','이 예시 약관은 25㎠ 이상 이식과 피판수술에 다른 항목을 둠'],
 ['힘줄·인대·연골 등의 관혈수술','근육·힘줄·인대·연골을 대상으로 한 관혈수술','뼈·관절 수술과 같은 항목이 아님. 수술 부위가 같아도 실제 행위를 구분'],
 ['중이 내 튜브유치술','가운데귀에 튜브를 두는 수술','고막 패치술은 제외. 반복수술 지급 단위 규정도 확인'],
 ['코뼈(비골) 수술','코뼈 자체를 대상으로 시행하는 수술','비중격만곡증·수면 중 무호흡 수술은 이 항목에서 제외. 미용 목적 제외 규정도 별도']]
oldtable=s.select_one('.source-table');intro=oldtable.find_previous('h2');nodes=[]
for x in intro.next_siblings:
 if x is oldtable:break
 nodes.append(x)
for x in nodes:x.extract()
intro.insert_after(BeautifulSoup('<p>실제 검색 유입이 있었던 백내장·담낭·용종·치핵을 중심으로, 수술명과 시행 방법을 연결한 예시입니다.</p><p class="notice"><strong>보험에 따라 분류가 다릅니다.</strong> 아래는 ABL생명 2023년 11월판의 <strong>1~5종 수술분류표</strong>를 설명한 예시입니다. 보험사·상품·특약·가입 시기의 적용 약관에 따라 종수가 달라질 수 있으며, 과거 1~3종 계약의 공통표로 사용하면 안 됩니다.</p>','html.parser'))
oldtable.replace_with(BeautifulSoup(table(['사람들이 찾는 수술','이 약관의 예시','방법·조건에서 달라지는 점'],common,'source-table'),'html.parser'))
pos=s.select_one('.source-table')
detail='<section id="first-tier-examples"><h2>1종 수술에는 어떤 종류가 있나요? 예시 10가지</h2><p>위 세 가지 외에도 탈장·하지정맥류·안검하수 등 다양한 수술이 이 예시 약관의 1종 항목에 들어 있습니다. <strong>같은 수술 이름이라도 다른 보험에서 같은 종수라는 뜻은 아닙니다.</strong> 아래의 방법과 제외 조건까지 함께 읽어 주세요.</p>'+table(['1종 수술 예시','실제로 어떤 수술인가요?','같이 구분할 점'],ones,'first-tier-table')+'</section>'
pos.insert_after(BeautifulSoup(detail,'html.parser'))
# Keep provenance available without making page numbers the main reader task.
sourceurl=next(x['href'].split('#')[0] for x in s.find_all('a',href=True) if 'abllife.co.kr' in x['href'])
evidence='''<section id="example-evidence"><h2>수술 이름만 나열하지 않고 방법까지 보는 이유</h2><p><strong>백내장과 녹내장:</strong> 같은 눈 수술이지만 이 약관은 백내장·수정체 수술은 1종, 녹내장 관혈수술은 3종으로 나눕니다. “눈 수술”이라는 말만으로 같은 종수를 적용할 수 없습니다.</p><p><strong>피부이식의 범위:</strong> 이 약관은 25㎠ 미만 피부이식은 1종, 25㎠ 이상 피부이식은 3종으로 구분합니다. 같은 피부이식도 면적이 분류의 근거가 됩니다. 피판수술에는 별도의 제외 조건도 있습니다.</p><p><strong>고막성형과 튜브유치:</strong> 귀 수술 중 관혈적 고막성형은 2종, 중이 내 튜브유치는 1종으로 나뉩니다. 고막 패치술은 이 두 항목에서 제외되어 있어 “귀를 치료했다”는 설명만으로 같은 항목을 선택할 수 없습니다.</p><p>이 차이는 특정 개인에게 보험금을 지급했다는 사례가 아니라, 아래 약관 원문에 서로 다른 분류가 적혀 있다는 근거입니다. 개인 계약에서는 적용되는 표와 실제 수술기록을 대조해야 합니다.</p></section>'''
s.find(id='first-tier-examples').insert_after(BeautifulSoup(evidence,'html.parser'))
proof=s.new_tag('details',id='policy-source-details');proof.append(BeautifulSoup('<summary>예시의 약관 근거와 원문 위치 보기</summary><p><a href="'+sourceurl+'#page=162" target="_blank" rel="noopener">ABL생명 예시 약관 원문 PDF</a> · (무)ABL인터넷네개딱패키지건강보험(갱신형), 2023년 11월판, 별표5.</p><p>1종 예시의 근거: 피부이식 2항, 근육·힘줄·인대·연골 14항, 편도17항(162쪽); 하지정맥류23항, 탈장39항, 치핵·치루44항(163쪽); 경질적 수술53항, 안검하수63항, 백내장71항(164쪽); 중이 튜브82항(165쪽). 비교 근거는 피부이식1항, 녹내장70항, 고막성형79항입니다.</p><p>대표 수술 표의 2·3종 근거: 충수41항, 담낭36항, 갑상선57항, 척추·추간판9항, 내시경88-2항과 복강경 주석. 내시경·경피적 수술의 반복수술 조건과 사용 지침도 함께 확인했습니다.</p>','html.parser'))
s.find(id='official-details').parent.insert_before(proof)
style=s.find(id='source-table-columns');style.string='@media(min-width:601px){.cluster-reading .source-table th:nth-child(1),.cluster-reading .source-table td:nth-child(1){width:32%}.cluster-reading .source-table th:nth-child(2),.cluster-reading .source-table td:nth-child(2){width:18%}.cluster-reading .source-table th:nth-child(3),.cluster-reading .source-table td:nth-child(3){width:50%}}'
nav=s.select_one('.reading-nav');z=s.new_tag('a',href='#first-tier-examples');z.string='1종 수술 10가지';nav.insert(1,z)
style.string='.cluster-reading #first-tier-examples{scroll-margin-top:120px}'+style.get_text()
rendered=str(s).replace('피부이식 2항, 근육','피부이식 2항, 코뼈7항, 근육').replace('경질적 수술53항, ','').replace('실제 검색 유입이 있었던 백내장·담낭·용종·치핵을 중심으로, 수술명과 시행 방법을 연결한 예시입니다.','백내장·담낭절제·용종절제·치핵 등 익숙한 수술을 중심으로, 수술 종류와 시행 방법을 연결한 예시입니다.').replace('사람들이 찾는 수술','수술 종류')
F.write_text(rendered+'\n',encoding='utf8')
e={'source':'ABL official 2023-11 policy downloaded and visually reviewed earlier on 2026-11-03; same retained local PDF','new_download':'Web tool returned overseas-access restriction. No access workaround attempted. Fixed historical PDF already on disk used.','first_tier_count':len(ones),'representative_count':len(common),'clauses':[2,7,14,17,23,39,44,63,71,82],'traffic_basis':'User-provided historical Naver keyword screenshots, not newly measured search volume','scope':'Only existing surgery-classification page; no new posts or indexing submissions'}
(O/'source-review.json').write_text(json.dumps(e,ensure_ascii=False,indent=2),encoding='utf8')
print('Expanded first-tier examples:',len(ones))
