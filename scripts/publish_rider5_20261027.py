"""Publish one verified rider explainer per invocation; never push automatically."""
from pathlib import Path
from bs4 import BeautifulSoup
import json, html, sys, subprocess, re
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/rider5-publication-2026-10-27'
BASE='https://hospital.hbuby.com'
DATE='2026-10-27'
HEALTH='https://www.kbinsure.co.kr/pop/CR301010002.ec?pdcd=25434'
CANCER='https://www.kbinsure.co.kr/pop/CR301010002.ec?pdcd=25290'
def p(t): return '<p>'+t+'</p>'
def h(t): return '<h2>'+t+'</h2>'
def table(headers,rows):
 return '<table><thead><tr>'+''.join('<th scope="col">'+x+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td><span class="cell-label">'+headers[i]+'</span>'+x+'</td>' for i,x in enumerate(row))+'</tr>' for row in rows)+'</tbody></table>'
def ul(items): return '<ul>'+''.join('<li>'+x+'</li>' for x in items)+'</ul>'
def link(path,label): return f'<a href="{path}">{label}</a>'
DATA=[
dict(path='/surgery-benefit/116-disease-vs-tier-surgery-benefit',slug='116-disease-vs-tier',title='116대 질병수술비와 종수술비 차이, 같은 수술이면 둘 다 확인할까?',desc='116대 질병수술비의 질병군과 종수술비의 수술분류는 다른 기준입니다. 현행 공개 약관의 감액·수술 정의·반복수술 제한을 구분하고 담보별 검토를 요청하는 방법을 정리합니다.',parent='/surgery-benefit/type-surgery-benefit-claim',pdf=HEALTH,page=361,source='KB 5.10.10 플러스 건강보험(연만기갱신형)(무배당)(26.09), 2026년 10월 1일 적용 약관',pages='특별약관 73-1~73-6, 본문 359~367쪽(PDF 361~369쪽)',body=[
h('116대는 질병 묶음, 종수술비는 수술 항목을 확인합니다')+p('116대 질병수술비에 해당한다고 종수술비의 1종·2종·3종이 정해지는 것은 아닙니다. 먼저 진단된 질병이 가입 담보의 질병분류표에 들어가는지 확인하고, 별도로 실제 수술이 종수술비의 분류표 어느 항목에 해당하는지 대조해야 합니다. 같은 수술 자료를 쓰더라도 심사하는 기준은 서로 다릅니다.')+p('이 글은 KB손해보험의 공개된 특정 판본을 읽는 예시입니다. 가입 시기·상품·특약 이름이 다르면 질병 수, 보장 범위와 지급 제한도 달라질 수 있습니다. 아래 예시의 금액 비율을 오래된 계약이나 다른 회사 계약에 그대로 적용하지 마세요.'),
h('Ⅰ~Ⅵ를 1~6종 수술로 읽지 마세요')+table(['확인 대상','판단 기준','찾을 자료'],[['116대 질병수술비','특약별 질병군과 직접 치료 목적의 수술','각 특약의 질병분류표·수술 정의'],['종수술비','가입한 수술분류표의 해당 행위와 등급','수술명·수술기록·해당 분류 항목'],['함께 가입한 경우','담보별 지급사유를 각각 충족하는지','가입 담보 목록과 각 심사 결과']])+p('확인한 116대 특약은 Ⅰ~Ⅵ로 나뉩니다. 이 로마 숫자는 해당 상품의 질병군별 특약 구분이며 수술 난이도 순위가 아닙니다. 예를 들어 Ⅳ의 49대질병 목록에는 담낭담도질환·담석증 등이 보이지만, 질병 이름만으로 지급을 확정할 수는 없습니다. 분류표의 범위와 실제 수술 여부까지 확인합니다.'),
h('감액과 반복수술 제한도 해당 특약에서 읽습니다')+p('확인한 Ⅰ의 지급표는 최초 계약일부터 1년 미만이면 가입금액의 50%, 1년 이상이면 100%이며 갱신 계약은 100%로 구분합니다. 같은 상품 안에서도 본인이 가입한 세부 특약의 표를 다시 확인해야 합니다. 현재 판매 약관이 본인의 계약 약관을 바꾸는 것은 아닙니다.')+p('Ⅰ·Ⅱ 등에는 약관이 정한 레이저수술에 대해 수술개시일부터 60일 이내 여러 수술을 한 번으로 보는 규정이 있습니다. 이것을 모든 수술이나 모든 담보의 공통 규칙으로 넓히면 안 됩니다. 복수 수술이라면 부위·시행일·행위별로 어떤 조항을 적용했는지 질문하세요.'),
h('수술확인서만으로 판단하기 어려운 지점')+p('약관의 수술 정의와 제외 문구를 함께 봅니다. 진단을 위한 검사나 주사·흡인·천자와 같은 처치가 일상 표현으로는 수술처럼 들려도, 가입 담보의 정의에는 맞지 않을 수 있습니다. 반대로 병원의 통칭만 듣고 제외라고 단정해서도 안 됩니다. 실제 시행 기록을 근거로 보험사에 검토를 요청하세요.')+p('병명·질병코드, 정확한 수술명, 시행일, 치료 목적이 확인되는 자료를 먼저 모읍니다. 세부 기록이 필요하다는 요청이 오면 어떤 사실을 확인하려는지부터 물어본 뒤 병원에 발급을 문의하면 불필요한 서류 발급을 줄일 수 있습니다.'),
h('가상 예시: 한 수술을 두 담보에 대조한다면')+p('A씨가 담석증 관련 수술을 받고 질병수술비와 종수술비를 함께 가입한 상황을 가정합니다. 116대 담보는 해당 질병군·수술 정의·감액 여부를 보고, 종수술비는 수술기록과 분류표 항목을 따로 검토합니다. 한쪽 지급 결과가 다른 쪽 결과를 대신하지 않습니다. 이 예시는 지급액이나 종수를 확정한 사례가 아닙니다.'),
h('접수 전에 확인할 네 가지')+ul(['보험증권에서 두 담보의 정확한 이름과 가입금액 확인','가입 당시 약관 판본과 질병·수술 분류표 확보','진단명·수술명·시행일이 같은 사건을 가리키는지 대조','감액, 동일 수술, 반복수술 제한을 담보별로 질문'])+h('문의 문장')+'<blockquote>이번 수술에 대해 116대 질병수술비의 해당 질병군과 종수술비의 분류 항목을 각각 알려 주세요. 지급 또는 제외 근거 조항, 감액 여부와 추가로 필요한 자료를 담보별로 구분해 주세요.</blockquote>'+p('종수술비 접수 자료를 더 자세히 확인하려면 '+link('/surgery-benefit/type-surgery-benefit-claim','종수술비 청구와 수술분류표 대조 안내')+'로 이어서 보세요.')]),
dict(path='/diagnosis-benefit/brain-heart-major-treatment-vs-diagnosis',slug='brain-heart-treatment',title='뇌·심장 주요치료비, 진단비와 다른 지급 요건과 연간 한도 확인법',desc='뇌·심장 주요치료비는 진단만으로 지급되는 진단비와 다릅니다. 약관 원문으로 직접치료 범위, 진단일부터 계산하는 연간 기준, 10년 보장과 감액 구조를 확인합니다.',parent='/diagnosis-benefit/cerebrovascular-benefit-claim-documents',pdf=HEALTH,page=613,source='KB 5.10.10 플러스 건강보험(연만기갱신형)(무배당)(26.09), 2026년 10월 1일 적용 약관',pages='특별약관 199, 본문 611~614쪽(PDF 613~616쪽)',body=[
h('진단비와 주요치료비는 확인할 사건이 다릅니다')+p('진단비가 약관에 정한 질병의 진단확정을 중심으로 본다면, 이 글에서 확인한 주요치료비는 대상 질병의 진단에 더해 정해진 주요치료를 실제로 받았는지를 봅니다. 진단서를 제출했다는 이유만으로 이후 10년의 치료비가 자동으로 지급되는 것은 아닙니다.')+p('확인 대상은 KB손해보험의 2대질병(뇌,심장)주요치료비(진단후10년,연간1회한)(감액있음)(맞춤고지) 갱신 특약입니다. 이름이 비슷한 다른 상품까지 같은 지급 조건이라고 볼 수 없으며, 가입 당시 약관과 보장 개시를 먼저 대조해야 합니다.'),
h('이 예시의 주요치료 범위')+table(['구분','약관에서 확인한 범위','접수 시 질문'],[['수술','해당 질병의 직접 치료 목적이며 수술 정의에 맞는 경우','시술명·시행 방법이 정의에 포함되는지'],['혈전용해치료','약관의 약물·치료 정의에 맞는 경우','투약명과 실제 치료 기록이 필요한지'],['중환자실 치료','약관에서 정한 종합병원 중환자실 치료','병원급·중환자실 입실 및 치료 사실 확인']])+p('항응고제나 경구 약제의 사용을 곧바로 혈전용해치료로 보면 안 됩니다. 혈전용해제를 쓰지 않은 기계적 혈전제거술은 이 약관의 혈전용해치료 정의와 구별됩니다. 다만 수술에 해당하는지는 수술 조항에서 별도로 검토할 문제이므로, 한 정의의 제외 문구로 담보 전체를 단정하지 않습니다.'),
h('연간은 1월 1일이 아니라 최초 진단일에서 시작합니다')+p('이 특약의 연간 계산은 최초 진단확정일을 기준으로 합니다. 진단 후 10년이라는 보장 기간 안에서 실제 주요치료가 있는 연도의 요건을 확인하며, 연간 1회·최대 10회 구조입니다. 보장 기간만 지나면 매년 받는 연금처럼 이해하면 안 됩니다.')+p('뇌 또는 심장 질환으로 나중에 다른 진단을 받았다고 새로 10년이 시작되는 것도 아닙니다. 최초 진단일, 연차 구간, 해당 치료일을 한 표에 놓고 확인하세요. 마지막 연차의 종료 시점도 특약의 별도 규정을 읽어야 하므로 달력 연도나 단순 만 나이로 계산하지 않습니다.'),
h('첫 진단 시점에 따른 감액이 이후에도 이어질 수 있습니다')+p('이 예시에서 특히 주의할 부분은 최초 계약일부터 1년 미만에 대상 질병이 진단된 경우입니다. 해당 감액 구간에 진단되면 지급기간 동안 가입금액의 50%를 적용하는 구조가 적혀 있습니다. 치료를 1년 뒤에 받았다는 이유만으로 100%가 된다고 읽으면 잘못된 예상이 생길 수 있습니다.')+p('이는 이 특약의 조건을 설명한 것입니다. 다른 계약의 감액 기간·비율·갱신 조건을 정하는 공통 규정이 아니므로, 보험사에 최초 진단일에 적용되는 지급표를 확인하세요.'),
h('가상 예시: 진단일과 치료일을 따로 적기')+p('B씨의 첫 대상 질병 진단일이 2026년 4월 15일이었다고 가정합니다. 이후 치료를 정리할 때는 2026년 1월~12월로 묶지 않고 그 진단일에서 출발하는 연차를 확인합니다. 같은 연차의 여러 치료가 각각 새 보험금이 되는지, 이미 해당 연차에 지급된 내역이 있는지를 함께 묻습니다. 실제 지급은 가입 시점·치료 종류 등 모든 요건을 심사해야 합니다.'),
h('청구 자료와 문의 순서')+ul(['정확한 특약명, 최초 계약일·갱신 여부 확인','최초 진단확정일과 질병분류표 확인','수술·투약·중환자실 치료일 및 실제 시행 자료 정리','해당 연차의 이전 지급 내역과 감액표 대조'])+'<blockquote>이 특약의 최초 진단일과 연간 구간을 어떻게 산정했는지, 이번 치료가 어느 주요치료 정의에 해당하는지 알려 주세요. 첫 진단 시점에 따른 감액이 이후 지급에도 적용되는지 근거 조항과 함께 확인해 주세요.</blockquote>'+p('진단 사실을 입증하는 서류는 '+link('/diagnosis-benefit/cerebrovascular-benefit-claim-documents','뇌혈관질환 진단비 청구서류 안내')+'에서 확인하고, 주요치료 자료는 별도로 추가합니다.')]),
dict(path='/diagnosis-benefit/integrated-cancer-metastasis-vs-rediagnosis',slug='integrated-cancer',title='통합암진단비 전이암 포함, 재진단암과 같은 뜻일까?',desc='통합암진단비 전이암 포함은 재진단암 담보와 다른 구조입니다. 세부 암 그룹 최초 1회와 소멸 조건, 같은 그룹 전이와 다른 그룹 진단, 재진단 대기기간을 약관 원문으로 구분합니다.',parent='/claims/cancer-diagnosis-benefit-documents',pdf=CANCER,page=437,source='KB 9회주는 암보험Plus(무배당)(26.07), 2026년 8월 1일 적용 약관',pages='특별약관 119 본문 435~440쪽(PDF 437~442쪽), 비교용 특별약관 25 본문 233쪽부터(PDF 235쪽부터)',body=[
h('전이암 포함이라는 문구만으로 재지급을 판단하지 않습니다')+p('통합암진단비에 전이암이 포함돼 있어도 암 진단을 받을 때마다 다시 지급한다는 뜻은 아닙니다. 암을 어떤 세부 보장 그룹으로 묶는지, 그 그룹에서 이미 보험금이 지급됐는지, 각 그룹이 언제 소멸하는지까지 확인해야 합니다. 재진단암은 별도의 보장개시와 진단 요건을 가진 담보입니다.')+p('여기서는 KB손해보험의 통합암진단비Ⅱ(전이암포함)(유사암제외)를 읽고, 같은 약관집의 재진단암진단비와 구조를 비교합니다. 같은 회사라도 다른 버전의 통합암·재진단암 담보에는 다른 기준이 있을 수 있습니다.'),
h('핵심은 장기 개수가 아니라 세부 보장 그룹입니다')+p('확인한 통합암 특약은 9개의 세부 보장을 두고 각각 최초 1회 지급하는 구조입니다. 해당 그룹의 보험금 지급사유가 발생하면 그 세부 보장은 소멸합니다. 새로운 부위가 발견됐더라도 이미 사용한 같은 그룹이면 추가 지급으로 연결되지 않을 수 있습니다.')+table(['상황','먼저 볼 항목','자동으로 결론 내리면 안 되는 말'],[['다른 장기에서 암 확인','같은 그룹인지 다른 그룹인지','장기가 다르니 무조건 새 지급'],['전이암 진단','전이암 분류와 해당 그룹의 지급 이력','전이암 포함이니 매번 지급'],['재발·잔존암 관련 진단','가입 담보와 재진단 정의·보장개시','암이 다시 보이면 통합암 재지급']]),
h('가상 예시: 같은 그룹과 미사용 그룹을 나눕니다')+p('C씨가 과거 암 진단으로 A그룹 보험금을 받았고 이후 다른 부위에서 암이 확인된 상황을 가정합니다. 두 번째 진단이 약관상 A그룹에 속하면 그 그룹의 최초 1회 조건부터 확인해야 합니다. 반대로 아직 지급사유가 발생하지 않은 B그룹에 속한다면 B그룹의 요건을 별도로 검토합니다. 전이인지 새 원발암인지는 환자가 추측하지 않고 진료·병리 자료와 해당 분류 규정으로 확인합니다.')+p('이 예시는 그룹 구조를 설명하기 위한 가상 사례이며 지급 승인 사례가 아닙니다. 진단명이나 코드 한 줄만으로 이전 암과의 관계, 세부 그룹, 보장개시일 충족 여부를 결정하지 않습니다.'),
h('재진단암은 시간 요건을 따로 읽습니다')+p('비교한 재진단암 특약 25는 첫 암 진단 또는 직전 재진단암 진단에서 정한 2년 경과 후의 보장개시 구조를 둡니다. 제외되는 암과 새로운 원발암·전이암·재발암·잔존암 등의 정의도 별도로 확인해야 합니다. 따라서 통합암의 미사용 그룹 확인과 재진단암의 시간·진단 요건 확인은 같은 절차가 아닙니다.')+p('다른 이름의 신재진단암이나 횟수 제한형 담보는 기간이 다를 수 있습니다. 이 글의 2년을 모든 재진단암 상품의 공통 대기기간으로 적용하지 마세요. 보험증권에 적힌 정확한 이름과 특별약관 번호를 연결하는 것이 먼저입니다.'),
h('감액도 모든 그룹에 똑같이 적용되는지 확인합니다')+p('확인한 통합암 지급표에서는 최초 계약 1년 미만의 감액이 특정소액암Ⅱ 그룹에 표시돼 있고 나머지 그룹과 구별됩니다. 상품 설명의 짧은 문구만 보고 모든 암에 일률적으로 50%라고 계산하면 안 됩니다. 각 세부 보장의 가입금액과 지급표, 암 보장개시일을 따로 보세요.'),
h('이전 지급 내역과 병리 자료를 함께 정리하세요')+ul(['가입한 통합암·재진단암 특약 이름과 판본','과거 진단일·암 부위·세부 보장 그룹 및 지급 내역','이번 진단확정 자료와 원발·전이 관계를 확인할 기록','그룹별 소멸 여부와 별도 재진단 보장개시일'])+'<blockquote>이전 진단과 이번 진단을 각각 어느 세부 그룹으로 분류했는지 알려 주세요. 해당 그룹의 최초 1회·소멸 조건과 재진단암 담보의 별도 보장개시 요건을 구분해 검토해 주세요.</blockquote>'+p('발급 자료의 기본 구성은 '+link('/claims/cancer-diagnosis-benefit-documents','암 진단비 청구서류와 병리결과 확인 안내')+'로 연결해 확인할 수 있습니다.')]),
dict(path='/diagnosis-benefit/reproductive-cancer-radiation-rider-check',slug='reproductive-radiation',title='남녀생식기암 항암방사선치료비, 중입자치료를 받으면 무엇을 확인할까?',desc='남녀생식기암 항암방사선치료비의 대상 암, 항암방사선 정의, 최초 1회와 특약 소멸을 확인합니다. 중입자치료라는 치료 이름만으로 지급 여부를 단정하지 않는 약관 대조법입니다.',parent='/guides/heavy-ion-therapy',pdf=CANCER,page=311,source='KB 9회주는 암보험Plus(무배당)(26.07), 2026년 8월 1일 적용 약관',pages='특별약관 63·64, 본문 309~312쪽(PDF 311~314쪽)',body=[
h('치료 방법과 가입한 담보를 연결해야 합니다')+p('중입자치료 비용이 궁금하더라도 먼저 본인이 가입한 담보가 무엇인지 확인해야 합니다. 일반 항암방사선치료비, 중입자치료 전용 담보, 남녀생식기암 항암방사선치료비는 같은 이름의 보장이 아닙니다. 치료 방법이 비슷해 보인다는 이유로 서로의 지급 조건을 복사하지 않습니다.')+p('이 글은 KB손해보험 공개 약관의 남성생식기암 항암방사선치료비와 여성생식기암 항암방사선치료비를 예시로 설명합니다. 상품 안내에는 중입자치료를 포함한 설명이 있으나 실제 청구는 가입한 판본의 대상 암·치료 정의·보장개시 요건을 대조해야 합니다.'),
h('대상 암의 범위부터 구분합니다')+table(['확인 항목','남성생식기암 특약 예시','여성생식기암 특약 예시'],[['대상 부위','전립선·음경·고환 관련 분류','자궁·난소·외음·질·태반 관련 분류'],['정확한 기준','해당 특약의 암 정의와 분류표','해당 특약의 암 정의와 분류표'],['공통 질문','그 암의 직접 치료를 위한 방사선인지','그 암의 직접 치료를 위한 방사선인지']])+p('위 부위 설명은 분류표를 찾기 위한 요약입니다. 진단서의 표현과 약관의 세부 분류가 일치하는지 확인해야 하며 생식기 주변에서 발생했다는 이유만으로 대상 암이라고 단정하지 않습니다. 원발 부위나 다른 암과의 관계가 불명확하면 의료기록을 근거로 보험사에 확인합니다.'),
h('방사선치료의 정의와 실제 시행 내용을 확인합니다')+p('확인한 약관은 방사선종양학과 전문의가 암의 직접 치료를 목적으로 고에너지 전리 방사선을 조사하는 치료를 정의합니다. 상담 예약, 검사, 치료 계획 수립과 실제 방사선 시행은 구분해서 정리하세요. 치료를 고려하고 있다는 사실만으로 보험금 지급사유가 생기는 것은 아닙니다.')+p('중입자치료를 받을 수 있는지는 의료진이 판단할 사항입니다. 보험 보장 여부 때문에 치료 방법을 정하거나 이 글을 치료 적합성 판단 자료로 사용하지 마세요. 이 글이 다루는 것은 치료가 시행된 뒤 계약의 어떤 항목을 확인할지입니다.'),
h('여러 회차 치료와 보험금 여러 번은 다릅니다')+p('이 예시 특약은 해당 항암방사선치료비를 최초 1회 지급하는 구조입니다. 남성 특약의 소멸 조항처럼 지급사유가 발생하면 해당 특약이 소멸하는 규정도 함께 읽어야 합니다. 방사선치료를 여러 날에 나누어 받았다고 방문 횟수마다 같은 보험금이 반복 지급되는 것으로 계산하지 않습니다.')+p('최초 암 보장개시일, 과거 같은 담보의 지급 여부, 갱신·부활 관련 조건도 확인합니다. 현재 안내에 보이는 보장 내용과 자신의 가입 계약에 실제 포함된 보장을 구별하세요.'),
h('가상 예시: 12회 치료 계획이 있다면')+p('D씨가 대상 암으로 진단받아 방사선치료를 12회 계획한 경우를 가정합니다. 확인한 최초 1회형 특약이라면 12회를 곱해 보험금을 예상하지 않고, 보장개시 이후 대상 암의 직접치료가 실제 시행됐는지와 과거 지급 이력을 대조합니다. 다른 항암·통원 담보는 각각의 지급 요건을 따로 살펴봅니다. 실제 지급액을 약속한 예시는 아닙니다.'),
h('자료를 요청하기 전에 보험사에 확인할 질문')+ul(['남성·여성생식기암 또는 별도 중입자 담보 중 실제 가입 담보','진단확정 자료와 해당 암 분류표의 연결','치료 방법·실제 시행일·직접치료 목적을 확인할 자료','최초 1회 지급·소멸 및 과거 지급 이력'])+'<blockquote>이번 치료를 가입한 특약의 항암방사선 정의로 검토할 때 필요한 자료를 알려 주세요. 대상 암 분류, 실제 치료 개시, 최초 1회와 특약 소멸 조건을 구분해 확인해 주세요.</blockquote>'+p('치료 전반과 비용 정보를 확인하려면 '+link('/guides/heavy-ion-therapy','중입자치료 기본 안내')+'를 함께 보되, 보장 판단은 이 글의 계약 대조 순서로 별도 확인하세요.')]),
dict(path='/diagnosis-benefit/three-disease-outpatient-daily-hospital-tier',slug='outpatient-hospital-tier',title='3대질병 통원일당, 상급종합병원과 종합병원은 왜 따로 확인할까?',desc='암·뇌혈관·허혈성심장질환 통원일당은 병원급과 직접치료 목적을 따로 확인해야 합니다. 현행 공개 약관의 1일 제한, 연간 기준과 병원 지정 변경을 구분합니다.',parent='/standards/actual-vs-fixed-benefit',pdf=CANCER,page=317,source='KB 9회주는 암보험Plus(무배당)(26.07), 2026년 8월 1일 적용 약관',pages='암 통원 특별약관 22·23·26, 뇌혈관·허혈성심장 통원 특별약관 65~70; 본문 227쪽·239쪽·312~320쪽 등',body=[
h('같은 질병으로 통원해도 담보의 병원급 조건을 봅니다')+p('3대질병 통원일당이라는 묶음 표현을 보더라도 암·뇌혈관·허혈성심장질환의 세부 담보와 병원급을 따로 확인해야 합니다. 상급종합병원 한정, 종합병원 한정, 병원·의원까지 포함하는 담보는 조건이 다를 수 있습니다. 대학병원이라는 별칭이나 건물 크기만으로 병원급을 정하지 않습니다.')+p('확인한 KB손해보험 약관집에도 질병별·병원급별 통원 특약이 나뉘어 있습니다. 아래 설명은 해당 판본을 읽는 예시이며 모든 상품의 통원일당이 같은 구조라는 뜻은 아닙니다. 실비처럼 실제 진료비를 계산하는 담보인지 정액 일당인지도 먼저 구분하세요.'),
h('정리할 자료는 병원·날짜·치료 목적입니다')+table(['확인 대상','대조할 자료','놓치기 쉬운 점'],[['병원급','통원일 당시 의료기관 분류·지정 정보','병원 이름만 보고 추정'],['직접치료','통원확인 자료와 실제 진료·치료 내용','진단명만으로 모든 방문 포함 판단'],['지급 일수','통원일과 같은 날 지급 이력','하루 여러 방문을 각각 합산'],['연간 한도','정확한 특약과 계산 시작일','모든 담보에 같은 한도 적용']]),
h('상급종합병원 여부는 방문일 기준으로 확인합니다')+p('보건복지부는 상급종합병원 지정 제도를 운영하고 지정 정보를 공개합니다. 약관이 정한 상급종합병원 또는 종합병원의 정의와 해당 기관의 지위를 대조하세요. 오늘의 분류만 확인하면 과거 통원일 당시 상태를 놓칠 수 있습니다.')+p('확인한 종합병원 암 통원 특약은 병원 지정이 적용되거나 취소되는 경우의 날짜 처리도 규정합니다. 같은 병원에 계속 다녔더라도 적용일 전후로 결과가 달라질 수 있으므로, 기관명·통원일·지정 적용일을 함께 질문하는 편이 정확합니다.'),
h('암과 뇌·심장 담보의 횟수 제한을 섞지 않습니다')+p('확인한 뇌혈관·허혈성심장질환 통원 특약에는 1일 1회, 연간 30일 한도 구조가 표시돼 있습니다. 이때 연간은 계약일을 기준으로 매년 도래하는 구간입니다. 최초 진단일 기준으로 연차를 계산하는 다른 주요치료비 담보와 혼동하지 마세요.')+p('반면 이 약관집의 암직접치료통원일당에는 1일 1회 규정이 있으나, 이를 근거로 모든 암 통원 담보에 연간 30일 제한이 있다고 일반화할 수 없습니다. 세 질병을 한 상품 안내에서 봤더라도 각 특별약관의 횟수·기간 표를 따로 읽어야 합니다.'),
h('검사나 경과 관찰 방문도 목적을 확인합니다')+p('통원 사실과 직접치료 목적은 별개입니다. 확인한 암 통원 규정은 합병증이나 새 질병의 치료가 병행될 때 의사의 소견에 따라 암 치료가 주된 목적인지를 봅니다. 진단코드가 찍혀 있다는 이유만으로 모든 방문이 포함된다고 말할 수 없습니다.')+p('검사만 있었다고 일률적으로 제외라고 단정하는 것도 피하세요. 실제 진료 목적과 기록, 해당 특약의 정의를 확인해 달라고 요청합니다. 의료기록을 보험금에 맞춰 바꾸는 것이 아니라 이미 시행한 사실을 정확히 확인하는 절차입니다.'),
h('가상 예시: 같은 날 두 번 방문했다면')+p('E씨가 같은 날 오전·오후에 두 차례 외래 진료를 받았다고 가정합니다. 1일 1회형 담보를 방문 횟수대로 두 번 계산하지 않고, 해당 날짜의 치료 목적과 병원급, 같은 담보의 지급 이력을 확인합니다. 실비 청구는 실제 비용·공제·한도 등 별도의 계산을 하므로 통원일당의 횟수 규칙을 그대로 옮기지 않습니다.'),
h('보험사에 보낼 확인 문장')+'<blockquote>통원일 당시 이 병원이 가입 특약의 병원급 조건에 맞는지, 이번 방문이 직접치료에 해당하는지 알려 주세요. 해당 질병의 1일 제한과 연간 계산 시작일·남은 일수를 근거 조항과 함께 확인해 주세요.</blockquote>'+ul(['특약 이름과 병원급 조건 확인','날짜별 통원 목적 및 병원 정보 정리','동일일 중복과 연간 지급 내역 확인','추가자료의 명칭과 필요한 확인 항목 문의'])+p('비용을 보상하는 실손과 정액 담보를 구분하려면 '+link('/standards/actual-vs-fixed-benefit','실손보험과 정액보험 차이')+'로 이어서 확인하세요.')])
]

def img(d,part,alt):
 from PIL import Image
 fn=d['slug']+'-'+part+'.webp'
 w,hh=Image.open(ROOT/'assets/images'/fn).size
 return f'<figure class="guide-image-panel"><img src="/assets/images/{fn}" width="{w}" height="{hh}" loading="{"eager" if part=="thumb" else "lazy"}" decoding="async" alt="{html.escape(alt)}"><figcaption>이해를 돕는 생성 이미지이며 실제 환자·개인 의료기록이 아닙니다.</figcaption></figure>'

def publish(i):
 d=DATA[i-1]; path=ROOT/(d['path'][1:]+'.html')
 if path.exists(): raise SystemExit('Already exists: '+str(path))
 template=BeautifulSoup((ROOT/'surgery-benefit/wound-suture-specific-rider.html').read_text(encoding='utf8'),'html.parser')
 template.title.string=d['title']
 for name,key,val in [('name','description',d['desc']),('property','og:title',d['title']),('property','og:description',d['desc']),('property','og:image',BASE+'/assets/images/'+d['slug']+'-thumb.webp')]: template.find('meta',attrs={name:key})['content']=val
 template.find('link',rel='canonical')['href']=BASE+d['path']
 schema=json.loads(template.find('script',type='application/ld+json').string)
 schema.update(headline=d['title'],description=d['desc'],image=BASE+'/assets/images/'+d['slug']+'-thumb.webp',datePublished=DATE,dateModified=DATE,mainEntityOfPage=BASE+d['path'])
 template.find('script',type='application/ld+json').string=json.dumps(schema,ensure_ascii=False)
 main=template.main; cta=str(main.find('section',class_='kakao-inquiry-cta')); main.clear()
 cat='수술비' if i==1 else '진단비'; section=d['path'].split('/')[1]
 s=f'<div class="breadcrumb"><a href="/">홈</a> / <a href="/{section}/">{cat}</a></div><h1>{d["title"]}</h1><p class="lead">{d["desc"]}</p><p class="article-meta">작성·근거 확인: 2026년 10월 27일 · 케어로컬</p>'
 s+='<nav class="reading-nav" aria-label="본문 바로가기"><a href="#contract">약관 대조</a><a href="#sources">공식 원문</a></nav>'+img(d,'thumb',d['title']+' 설명용 표지')
 s+='<div class="notice" id="contract">현재 공개된 특정 상품 약관을 읽는 예시입니다. 내 계약에는 가입 당시 판본을 적용하며, 회사·상품·특약별 차이가 있습니다. 지급을 보장하거나 치료·가입을 권하는 글이 아닙니다.</div>'
 for j,part in enumerate(d['body']):
  s+=part
  if j==1:s+=img(d,'body1','진단·치료 자료와 가입 담보를 비교하는 설명용 장면')
  if j==3:s+=img(d,'body2','날짜별 기록과 약관 조건을 정리하는 설명용 장면')
 s+='<section class="official-guide-actions"><h2 id="sources">직접 확인할 공식 원문</h2><p>'+d['source']+'을 확인했습니다. '+d['pages']+'. PDF 뷰어 쪽수와 인쇄된 본문 쪽수가 2쪽 차이 납니다. 판매 안내보다 지급사유·정의·소멸 조항을 함께 읽으세요.</p><div class="official-guide-grid">'
 s+=f'<a class="official-guide-button" href="{d["pdf"]}#page={d["page"]}" target="_blank" rel="noopener"><strong>KB손해보험 공식 약관 PDF 열기</strong><span>{d["pages"]} · 내 계약의 판본과 대조 · 새 창 ↗</span></a>'
 s+='<a class="official-guide-button" href="https://www.kbinsure.co.kr/CG205020003.ec" target="_blank" rel="noopener"><strong>KB손해보험 담보별 청구서류</strong><span>회사별 서류 예시입니다. 본인 보험사에 필요한 자료를 확인하세요. · 새 창 ↗</span></a>'
 if i==5:s+='<a class="official-guide-button" href="https://www.mohw.go.kr/menu.es?mid=a10702030300" target="_blank" rel="noopener"><strong>보건복지부 상급종합병원 지정 안내</strong><span>방문일 당시 지정 정보와 약관의 병원 정의를 확인하세요. · 새 창 ↗</span></a>'
 s+='</div></section><p>작성: 케어로컬 사이트 운영자. '+link('/legal/about','작성 기준과 운영자 역할')+'을 확인할 수 있습니다. 개별 지급 판단은 가입 약관과 실제 진료자료를 토대로 해당 보험사가 확인합니다.</p><div class="insurance-company-cta"><a href="/insurance-companies/">보험사별 공식 홈페이지 확인하기</a></div>'+cta
 main.append(BeautifulSoup(s,'html.parser'))
 path.write_text(str(template)+'\n',encoding='utf8')
 parent=ROOT/(d['parent'][1:]+'.html'); raw=parent.read_text(encoding='utf8')
 OUT.mkdir(exist_ok=True,parents=True); (OUT/(parent.stem+'-before.html')).write_text(raw,encoding='utf8')
 ps=BeautifulSoup(raw,'html.parser')
 anchor=ps.main.find('section',class_='official-guide-actions')
 block=BeautifulSoup('<aside class="notice"><strong>연결해서 확인할 세부 기준</strong><p>'+link(d['path'],d['title'])+'에서 이번 질문의 별도 지급 조건과 약관 원문을 확인할 수 있습니다.</p></aside>','html.parser')
 if anchor:anchor.insert_before(block)
 else:ps.main.append(block)
 for script in ps.find_all('script',type='application/ld+json'):
  try:
   obj=json.loads(script.string); obj['dateModified']=DATE; script.string=json.dumps(obj,ensure_ascii=False)
  except (ValueError,TypeError):pass
 parent.write_text(str(ps)+'\n',encoding='utf8')
 # Category discovery link, without duplicating an existing link.
 idx=ROOT/section/'index.html'; cs=BeautifulSoup(idx.read_text(encoding='utf8'),'html.parser')
 sec=BeautifulSoup('<section class="section"><h2>새로 확인한 약관 세부 기준</h2><p>'+link(d['path'],d['title'])+'</p></section>','html.parser')
 (cs.main if cs.main else cs.body).append(sec)
 idx.write_text(str(cs)+'\n',encoding='utf8')
 sm=ROOT/'sitemap.xml'; raw=sm.read_text(encoding='utf8')
 raw=raw.replace('</urlset>',f'  <url><loc>{BASE+d["path"]}</loc><lastmod>{DATE}</lastmod></url>\n</urlset>')
 sm.write_text(raw,encoding='utf8')
 subprocess.run([sys.executable,str(ROOT/'scripts/build-article-catalog.py')],check=True)
 (OUT/'manifest.json').write_text(json.dumps([{k:v for k,v in x.items() if k!='body'} for x in DATA],ensure_ascii=False,indent=2)+'\n',encoding='utf8')
 print(json.dumps({'article':str(path.relative_to(ROOT)),'parent':str(parent.relative_to(ROOT)),'category':str(idx.relative_to(ROOT))},ensure_ascii=False))

if __name__=='__main__': publish(int(sys.argv[1]))
