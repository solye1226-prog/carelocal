from pathlib import Path
from bs4 import BeautifulSoup
import json
R=Path(__file__).resolve().parents[1];O=R/'docs/surgery-tier23-examples-2026-11-03';O.mkdir(exist_ok=True)
F=R/'surgery-benefit/surgery-classification.html';old=(O/'before.html').read_text(encoding='utf8') if (O/'before.html').exists() else F.read_text(encoding='utf8');(O/'before.html').write_text(old,encoding='utf8');s=BeautifulSoup(old,'html.parser')
two=[
 ['충수절제술(맹장염 수술)','염증이 생긴 충수를 절제하는 수술','맹장염 진단만 받고 약물치료한 경우와 구분'],
 ['위·대장 내시경 용종절제','양성 용종을 내시경으로 실제 절제한 경우의 예시','관찰·검사만 한 경우는 제외. 악성종양이면 별도 수술 표도 확인'],
 ['요로결석 체외충격파쇄석술','결석을 대상으로 시행하는 ESWL','근육·힘줄 등에 시행하는 ESWT와 다름. 반복 시행의 지급 단위도 별도'],
 ['자궁·난소·난관 관혈수술','해당 장기에 시행하는 관혈수술 항목','제왕절개와 경질적 조작은 이 항목에서 제외. 암 수술은 별도 표도 확인'],
 ['전립선 관혈수술','전립선을 대상으로 한 관혈수술 항목','내시경·경요도적 수술을 모두 이 항목에 바로 넣지 않음. 시행 방법을 대조'],
 ['팔다리 뼈·관절 관혈수술','손가락·발가락을 제외한 팔다리 뼈와 관절의 관혈수술','무릎·어깨라는 부위명만으로 결정하지 않음. 힘줄·인대 수술 및 핀 제거와 구분'],
 ['뼈 이식수술','실제 뼈를 이식하는 수술','치과 처치·수술에 수반하는 경우와 내고정물 제거는 해당 근골 수술 범위에서 제외'],
 ['관혈적 고막성형술','고막을 수술적으로 성형하는 경우','고막 패치술 제외. 중이 튜브유치는 이 예시에서 1종으로 따로 분류'],
 ['망막박리 수술','망막박리에 대해 시행하는 수술','수술 시작일부터 60일 이내 반복수술을 한 번으로 계산하는 조건이 있음'],
 ['신경 관혈수술','신경에 직접 수술적 조작을 하는 관혈수술','통증 치료를 위한 신경차단·주사만으로 같은 항목이 되지는 않음']]
three=[
 ['담낭절제술(담낭 제거)','담낭·담도 관혈수술 항목에 해당하는 경우','이 약관의 복강경 주석은 해당 부위 수술 항목을 적용. 담도 내시경 수술과 구분'],
 ['갑상선·부갑상선 관혈수술','갑상선이나 부갑상선에 시행하는 관혈수술','고주파치료를 자동으로 같은 항목에 대입하지 않음. 암 근치수술은 별도 표도 확인'],
 ['척추·골반·추간판 관혈수술','척추뼈·골반뼈·디스크를 대상으로 하는 관혈수술','허리디스크라는 진단만으로 적용하지 않음. 내시경·경피적 수술은 별도 지침'],
 ['녹내장 관혈수술','녹내장에 대해 시행하는 관혈수술','백내장·수정체 수술과 다른 항목. 레이저 안구 수술도 별도로 분류'],
 ['유방절단수술','유방을 절단하는 수술 항목','유방 양성종양 절제 등 기타 유방수술과 구분. 유방암 수술 전체가 3종이라는 뜻은 아님'],
 ['넓은 범위 피부이식·일부 피판수술','25㎠ 이상 피부이식 또는 해당 피판수술','피판분리·Z flap·W flap 제외. 25㎠ 미만 피부이식은 이 예시에서 1종'],
 ['인공심박조율기 매입술','심장 박동을 조절하는 기기를 몸 안에 넣는 수술','심장 수술 전체의 공통 종수가 아님. 다른 기기·교체 행위는 실제 기록과 항목 대조'],
 ['뇌·심장의 카테터 등 경피적 수술','뇌·심장 부위에서 약관의 내시경·경피적 수술 항목에 해당하는 경우','카테터를 썼다는 사실만으로 적용하지 않음. 진단 목적 검사·흡인·천자·약물주입 등과 구분']]
def table(rows,tier):
 heads=[tier+'종 수술 예시','실제로 어떤 수술인가요?','같이 구분할 점']
 return '<table class="tier'+tier+'-table"><thead><tr>'+''.join('<th scope="col">'+x+'</th>' for x in heads)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td><span class="cell-label" aria-hidden="true">'+heads[i]+'</span>'+x+'</td>' for i,x in enumerate(row))+'</tr>' for row in rows)+'</tbody></table>'
parts=[]
for tier,name,rows in [('2','second',two),('3','third',three)]:
 parts.append('<section id="'+name+'-tier-examples"><h2>'+tier+'종 수술에는 어떤 종류가 있나요? 예시 '+str(len(rows))+'가지</h2><p class="notice"><strong>보험에 따라 종수가 다릅니다.</strong> 아래는 ABL생명 (무)ABL인터넷네개딱패키지건강보험(갱신형), 2023년 11월판의 <strong>1~5종 약관 예시</strong>입니다. 같은 수술이라도 보험사·상품·특약·가입 시기의 적용 약관에 따라 다른 종수가 적용될 수 있습니다. 과거 1~3종 계약의 공통표가 아닙니다.</p><p>일반 질병·재해 치료 수술의 예시를 수술 방법과 함께 정리했습니다. 악성종양 수술에는 별도의 분류표가 적용될 수 있어, 암이라는 진단명이나 수술 부위만으로 이 표를 적용하지 않습니다.</p>'+table(rows,tier)+'</section>')
s.find(id='first-tier-examples').insert_after(BeautifulSoup(''.join(parts),'html.parser'))
nav=s.select_one('.reading-nav');first=nav.find('a',href='#first-tier-examples');prev=first
for name,tier in [('second','2'),('third','3')]:
 a=s.new_tag('a',href='#'+name+'-tier-examples');a.string=tier+'종 수술 예시';prev.insert_after(a);prev=a
style=s.new_tag('style',id='tier23-anchor-offset');style.string='.cluster-reading #second-tier-examples,.cluster-reading #third-tier-examples{scroll-margin-top:120px}';s.head.append(style)
proof=s.find(id='policy-source-details');proof.append(BeautifulSoup('<p>2종 추가 예시 근거: 뼈이식5항·팔다리 뼈와 관절13-2항(162쪽), 충수41항(163쪽), 전립선50항·자궁/난소/난관52항·신경60항·망막박리72항(164쪽), 고막성형79항·체외충격파쇄석87항·내시경88-2항(165쪽). 근골 수술의 제외 조건과 반복수술 지침도 함께 적용합니다.</p><p>3종 추가 예시 근거: 피부이식/피판1항·유방절단3항·척추/골반/추간판9항(162쪽), 인공심박조율기28항·담낭/담도36항(163쪽), 갑상선/부갑상선57항·녹내장70항(164쪽), 뇌/심장 내시경·경피적 수술88-1항과 복강경 주석(165쪽). 악성신생물 수술 표(166쪽), 수술 정의·제외 지침(167쪽)도 구분합니다.</p>','html.parser'))
F.write_text(str(s)+'\n',encoding='utf8')
(O/'source-review.json').write_text(json.dumps({'basis':'Same dated official ABL 2023-11 historical policy downloaded and rendered earlier on2026-11-03, retained locally; not a universal current policy','two':{'count':len(two),'clauses':['41','88-2','87','52','50','13-2','5','79','72','60']},'three':{'count':len(three),'clauses':['36+laparoscopy note','57','9','70','3','1','28','88-1']},'traffic':'Familiar surgery terms and earlier user-provided traffic, not measured search-volume ranking','scope':'Existing surgery-classification page only'},ensure_ascii=False,indent=2),encoding='utf8')
print('Added',len(two),'second-tier and',len(three),'third-tier examples')
