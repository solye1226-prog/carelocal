"""Publish source-reviewed topics 6-10 one at a time; push remains explicit."""
from pathlib import Path
from bs4 import BeautifulSoup
import json,sys,subprocess,re
from PIL import Image
from publish_trend5_20261027 import p,h,a,ul,table,CSS
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/trend6-10-publication-2026-10-27'
BASE='https://hospital.hbuby.com'
DATE='2026-10-27'
COVID='https://nip.kdca.go.kr/irhp/covd/goCov19Vcnt.do?menuCd=47&menuLv=4'
WEG='https://nedrug.mfds.go.kr/pbp/CCBBB01/getItemDetail?itemSeq=202301388'
MOU='https://nedrug.mfds.go.kr/pbp/CCBBB01/getItemDetail?itemSeq=202301983'
MFDS='https://e-health.go.kr/gh/heNws/selectBbsDtlViewInfo.do?bbsId=U00186&bbsNo=422005&menuId=200048'
RESIN='https://www.korea.kr/news/policyNewsView.do?newsId=148971474'
PLAN='https://www.korea.kr/common/download.do?fileId=198572688&tblKey=GMN'
HIRA='https://www.hira.or.kr/bbsDummy.do?brdBltNo=47596&brdScnBltNo=4&pgmid=HIRAA010006011500'
LAW='https://www.law.go.kr/admRulLsInfoP.do?admRulSeq=2100000286910'
AMEND='https://www.kha.or.kr/kha_home/notice_list.do?articleNo=47640&mode=view'
BIO='https://www.biobigdata.kr/guide/generalParticipantGuide.do?key=2601190045#instSearchStatus'
KDCA='https://www.kdca.go.kr/kdca/2848/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGa2RjYSUyRjQyJTJGMzEyOTY3JTJGYXJ0Y2xWaWV3LmRvJTNG'
DATA=[
dict(path='/guides/covid-vaccine-2026-high-risk-documents',slug='covid-high-risk-2026',cat='병원 이용',title='코로나19 무료접종 고위험군, 대상과 증빙서류 확인 순서',desc='2026~2027절기 코로나19 무료접종의 면역저하자·시설 입소자 대상과 서류 예외를 정리합니다. 12세 미만 별도 일정, 접종기관 조회와 방문 전 문의할 항목을 확인하세요.',status='12세 이상 고위험군 접종 시행·12세 미만은 별도 일정 안내 예정',parent='/guides/flu-vaccination-2026',parent_note='독감과 코로나19는 지원 대상과 시작 일정이 다릅니다. 코로나19 고위험군의 증빙서류와 12세 미만 안내를 별도로 확인하세요.',sources=[(COVID,'질병관리청 코로나19 예방접종 안내','연령·고위험군·절기 일정·증빙 예외와 지정기관 확인')],body=[
h('고위험군은 진료명과 접종 지원 기준을 함께 확인합니다')+p('코로나19 무료접종을 알아보는 면역저하자나 감염취약시설 입소자라면, 방문할 접종기관에 대상 여부와 필요한 증빙을 먼저 문의하세요. 만성질환이 있다는 설명만으로 지원 대상 면역저하자라고 단정하거나, 접종 서류용 진단서를 먼저 유료 발급할 필요는 없습니다.')+p(a(COVID,'질병관리청의 2026~2027절기 안내')+'는 65세 이상과 면역저하자·감염취약시설 입소자 등을 구분합니다. 고위험군 여부는 자신의 질환·치료 상황과 공식 대상 기준을 의료진이 확인하도록 해야 합니다. 지원 대상이라는 말은 개인의 접종 적합성을 미리 판정한 결과가 아닙니다.'),
h('12세 이상 일정과 12세 미만 일정을 나눠 보세요')+table(['구분','공식 일정·대상 안내','방문 전 확인'],[['70세 이상','2026년 10월 12일부터','접종기관 운영일과 백신 보유'],['65~69세','2026년 10월 15일부터','1961년 12월 31일 이전 출생 기준 대조'],['12세 이상 면역저하자·시설 입소자','2026년 10월 12일~2027년 6월 30일','접종일 생년월일·해당 위험군·증빙'],['12세 미만 고위험군','백신 긴급 도입 후 별도 일정 안내 예정','성인 시작일을 그대로 적용하지 않기']])+p('12세 미만 가족을 위해 예약한다면 먼저 소아 대상 도입·접종 개시 안내가 나왔는지 확인하세요. 연령 기준과 의료기관에서 실제 예약을 받을 수 있는 날짜는 따로 확인해야 합니다.'),
h('증빙은 필요할 수 있지만 예외도 있습니다')+p('공식 안내에는 진단서·소견서, 시설 입소 확인 자료 등의 예가 있습니다. 다만 의사가 면역저하자로 판단하는 경우나 시설 계약의사 방문·자체 접종 등에서는 증빙이 불필요할 수 있습니다. 모든 사람이 새 진단서를 제출해야 한다는 뜻은 아닙니다.')+ul(['의료기관에 현재 질환·치료 약과 마지막 접종 시점을 설명하기','기존 소견서 등 보유 자료로 확인 가능한지 먼저 묻기','별도 자료가 필요하면 서류명·필요 항목·발급기관 확인하기','시설 입소자는 시설 담당자에게 단체 접종·확인 절차 문의하기'])+p('진료기록 전체를 공개 댓글이나 일반 메시지로 보내지 마세요. 필요한 항목이 정해진 뒤 의료기관이 안내한 제출 경로를 이용합니다.'),
h('지정기관 조회 후 전화로 예약 가능 여부를 맞춥니다')+p('주소지와 관계없이 지정의료기관·보건소를 이용할 수 있다는 안내와, 특정 기관이 오늘 접종 가능한지는 다릅니다. 예방접종도우미에서 지정기관을 찾은 다음 운영 시간·예약 방식·백신 보유를 확인하세요. 가족의 나이와 위험군까지 전달해야 잘못된 예약을 줄일 수 있습니다.')+p('약을 복용 중이라면 접종을 위해 임의로 중단하지 말고 진료 의료진과 상담합니다. 접종 간격이나 추가 접종 횟수는 이전 접종 이력·상태에 따라 의료기관에서 확인할 항목입니다. 독감 지원은 '+a('/guides/flu-vaccination-2026','2026 독감 무료접종 대상 안내')+'에서 따로 비교하세요.'),
h('가상 예시: 치료 중인 가족의 서류를 준비한다면')+p('A씨가 면역 관련 치료를 받는 가족의 접종을 문의한다고 가정합니다. A씨는 먼저 접종기관에 약 이름과 치료 상황을 설명하고, 기존 진료 자료로 대상 확인이 가능한지 묻습니다. 의료기관이 추가 자료가 필요하다고 안내한 뒤 해당 항목을 발급받습니다. 질환 이름만 보고 대상이라고 확정하거나 새 진단서 비용부터 지출하지 않는 순서입니다.'),
h('접종기관에 이렇게 문의하세요')+'<blockquote>가족의 생년월일과 현재 치료 내용을 말씀드리겠습니다. 이번 절기 무료접종 고위험군에 해당하는지, 기존 자료로 확인 가능한지, 별도 증빙이 필요하다면 어떤 항목인지 알려 주세요. 해당 연령의 접종 개시 여부와 예약 가능일도 확인하고 싶습니다.</blockquote>']),
dict(path='/guides/glp1-pregnancy-planning-official-guide',slug='glp1-pregnancy-plan',cat='병원 이용',title='위고비·마운자로 임신 계획, 중단 시점과 피임 안내가 다른 이유',desc='식약처 허가사항에서 위고비와 마운자로의 계획 임신 전 중단 기간은 다릅니다. 제품명·마지막 투여일·피임약을 정리해 처방의와 상담할 때 확인할 내용을 안내합니다.',status='제품별 현행 허가사항 적용·임신 계획은 처방 의료진과 상담',parent='/guides/inpatient-personal-medicine-handover',parent_note='입원 시 가져가는 약에 위고비·마운자로가 있다면 제품명과 마지막 투여일을 정확히 알리세요. 임신 계획이 있는 경우의 제품별 허가사항도 확인할 수 있습니다.',sources=[(WEG,'의약품안전나라 위고비 허가사항','세마글루티드의 임신·계획 임신 전 중단 안내'),(MOU,'의약품안전나라 마운자로 허가사항','터제파타이드의 임신·중단·경구피임약 관련 주의'),(MFDS,'식약처 GLP-1 계열 비만치료제 안전사용 안내','의사 처방과 임신 계획 상담 필요성')],body=[
h('같은 비만치료제로 묶어 중단 기간을 정하지 마세요')+p('계획 임신 전 중단 기간은 위고비가 최소 2개월, 마운자로가 최소 1개월로 허가사항이 다릅니다. 이 숫자는 제품별 상담의 기준이며, 마지막 투여 후 그 기간이 지났다는 이유만으로 개인의 임신 안전성이 보장되는 것은 아닙니다. 제품명과 마지막 투여일을 확인해 처방의·산부인과와 계획을 맞추세요.')+p('식약처는 전문의약품인 GLP-1 계열 치료제를 처방과 상담 아래 사용하도록 안내합니다. 다른 사람의 약, 해외 구매품, 성분을 확인하지 못한 주사제에 이 글의 기간을 그대로 적용해서는 안 됩니다.'),
h('두 제품의 허가사항을 나란히 확인합니다')+table(['제품·성분','계획 임신 전 안내','함께 확인할 점'],[['위고비·세마글루티드','최소 2개월 전 중단','치료 중 피임, 임신 확인 시 사용 중단·의료진 연락'],['마운자로·터제파타이드','최소 1개월 전 중단','경구 호르몬 피임약 사용 여부·투여 시작과 증량 시점']])+p('위 표는 '+a(WEG,'위고비')+'와 '+a(MOU,'마운자로')+'의 국내 허가사항을 구분한 것입니다. 용량별 투여법이나 개인의 중단·재시작 처방을 제공하는 표가 아닙니다. 당뇨병 치료를 함께 받고 있다면 혈당 관리 계획도 의료진과 정해야 합니다.'),
h('마운자로의 피임약 주의와 임신 전 중단은 다른 기준입니다')+p('마운자로 허가사항은 경구 호르몬 피임약을 사용하는 경우 투여 시작 후 4주, 각 용량 증량 후 4주 동안 비경구 피임법으로 전환하거나 차단 피임법을 추가하도록 권고합니다. 이 기간은 계획 임신 전 최소 1개월 중단 안내와 목적이 다릅니다.')+p('피임약 이름을 적어 처방의나 약사에게 알려 주세요. 약을 임의로 바꾸거나 피임약만 중단하는 방식으로 해결하지 말고 어떤 방법을 언제까지 사용할지 상담합니다. 위고비에 마운자로의 피임약 문구를 똑같이 옮겨 적용하지도 않습니다.'),
h('이미 임신을 확인했다면 계획 임신의 대기 기간으로 해석하지 마세요')+p('두 제품의 허가사항은 임신 중 사용하지 않도록 안내합니다. 임신을 확인했다면 다음 투여를 그대로 이어가기보다 제품·용량·마지막 투여일을 알리고 처방의와 산부인과에 신속히 연락해 필요한 평가를 받으세요. “몇 주 더 사용한 뒤 끊어도 된다”는 의미가 아닙니다.')+p('노출 이력이 있다는 사실만으로 태아 이상을 확정할 수도 없습니다. 인터넷 사례로 결과를 예측하거나 다른 필수 약까지 한꺼번에 끊지 말고, 각 약의 사용 이력과 임신 시점을 의료진에게 전달합니다.'),
h('상담 메모에는 날짜와 제품을 정확히 적습니다')+ul(['약 상자·처방전에 적힌 정확한 제품명과 성분','현재 용량, 마지막 투여일, 최근 증량 날짜','임신 계획 여부 또는 확인한 임신 정보','경구 피임약 등 함께 쓰는 약과 당뇨병 치료 여부','중단 뒤 진료·혈당 관리·재평가 계획을 물을 질문'])+p('입원이나 다른 진료를 앞뒀다면 관련 약을 빠뜨리지 말고 '+a('/guides/inpatient-personal-medicine-handover','입원 시 개인약 인계 안내')+'처럼 의료진에게 전달하세요. 약을 가져가는 절차와 계속 투여해도 된다는 판단은 구분합니다.'),
h('가상 상담 문장')+'<blockquote>현재 사용 중인 제품은 ○○이고 마지막 투여일은 ○월 ○일입니다. 임신을 계획하고 있어 허가사항의 중단 기간과 이후 관리 계획을 상담하고 싶습니다. 경구 피임약도 사용 중인데, 시작·증량 뒤 추가 피임이 필요한지 함께 확인해 주세요.</blockquote>'+p('수유 중 사용 가능 여부는 별도 허가사항과 개인 상황을 확인할 질문입니다. 임신 전 중단 기간을 수유 안내에 그대로 대입하지 마세요.')]),
dict(path='/silbi/age13-composite-resin-coverage-update',slug='age13-resin-update',cat='실비보험',title='13세 레진 건강보험 확대 발표, 치료 전 나이·시행일 확인법',desc='13세 광중합형 복합레진 건강보험 확대 추진 발표와 현재 안내되는 5~12세 기준을 구분합니다. 영구치·충치 치료 여부, 실제 적용일·급여 항목·민간보험을 확인하는 순서입니다.',status='13세 확대 추진 발표·정확한 적용일과 최종 급여 기준은 치료 전 확인',parent='/silbi/dental-covered-medical-expense-claim',parent_note='치과 급여 실비와 13세 레진 급여 확대 발표는 구분해 확인해야 합니다. 치료일의 나이·치아·급여 기준을 먼저 대조하세요.',sources=[(RESIN,'정부 건강보험 보장 확대 발표','5~12세에서 5~13세 확대 방향 안내'),(PLAN,'보건복지부 의료혁신 추진방안 원문 PDF','인쇄 17쪽·PDF 19쪽의 레진 확대 추진 및 2027년 재정 소요'),(HIRA,'심평원 광중합형 복합레진 급여 안내','기존 5~12세 충치 레진 기준 확인')],body=[
h('13세 확대 발표를 오늘 바로 적용되는 급여로 읽지 마세요')+p('13세 자녀의 충치 레진 비용을 알아본다면 치과에 치료 예정일의 적용 나이와 급여 시행 기준부터 확인하세요. 정부는 광중합형 복합레진의 지원 연령을 13세까지 넓히는 방향을 발표했지만, 발표 사실만으로 지금 모든 13세 치료가 건강보험으로 처리되는 것은 아닙니다.')+p(a(RESIN,'정부 발표')+'는 기존 5~12세에서 5~13세로 확대한다고 설명합니다. '+a(PLAN,'보건복지부 추진방안 원문')+'에는 확대 추진과 2027년 예상 재정 소요가 제시돼 있습니다. 이 자료만으로 레진의 정확한 적용 개시일을 확정할 수 없어, 이 글에서는 특정 날짜부터 시행됐다고 안내하지 않습니다.'),
h('나이뿐 아니라 치아와 치료 목적도 맞아야 합니다')+table(['확인 항목','치과에 물을 내용'],[['치료일의 만 나이','학년이나 세는나이가 아닌 실제 적용 나이'],['치아 종류','유치인지 영구치인지, 해당 치아가 대상인지'],['치료 목적·방법','충치에 대한 광중합형 복합레진 충전인지'],['시행 기준','13세 확대가 치료일에 실제 시행되는지'],['비용 항목','급여·비급여와 별도 검사·치료 항목']])+p(a(HIRA,'심평원의 기존 급여 안내')+'는 일반적인 5~12세 충치 치료를 설명합니다. 구체적인 급여 기준은 치아·상태·시술을 함께 보며, 5세 미만에 조기 맹출한 영구치 등 별도 예외도 있을 수 있습니다. 이 표를 모든 연령의 급여를 확정하는 판정표로 사용하지 마세요.'),
h('레진이라는 말 하나로 모든 수복을 묶지 않습니다')+p('광중합형 복합레진의 연령 확대는 미용 목적의 치아 모양 수정이나 모든 유치 치료, 인레이·크라운까지 일괄 지원한다는 뜻이 아닙니다. 상담할 때 “레진 하나 얼마인가요”만 묻기보다 어느 치아의 어떤 충치를 어떤 방식으로 치료하는지 확인하세요.')+p('추가적인 신경치료 등이 필요하면 치료 구성과 비용이 달라질 수 있습니다. 치료 시기는 치과의사가 상태를 보고 판단해야 합니다. 예정된 급여 확대를 기다리려고 필요한 진료를 임의로 미루지 마세요.'),
h('견적과 영수증을 항목별로 대조합니다')+ul(['치아 위치와 시행할 치료명 메모','치료 예정일 기준 급여 여부와 근거 문의','급여 본인부담·비급여·다른 치료 비용을 나눈 설명 요청','치료 뒤 영수증과 세부내역서의 실제 처리 항목 대조'])+p('정부 발표에 있는 평균적 예상 혜택을 개인에게 지급되는 현금이나 한 치아의 정해진 할인액으로 해석하지 않습니다. 필요한 치료 개수와 병원 청구 항목을 확인해야 실제 부담을 이해할 수 있습니다.'),
h('민간보험은 건강보험 적용과 따로 확인합니다')+p('건강보험 급여가 되었다는 사실만으로 치아보험이나 실손보험 지급이 자동 결정되지는 않습니다. 치아보험은 가입 특약·면책·감액·보철 및 보존치료 정의 등을, 실손은 해당 계약의 치과 급여 보장 범위와 자기부담금을 따로 확인합니다.')+p('기본 구분은 '+a('/silbi/dental-covered-medical-expense-claim','치과 건강보험 급여의 실비 청구 안내')+'에서 볼 수 있습니다. 보험사가 요구하는 자료를 확인한 뒤 필요한 서류만 발급받고, 정부 급여 확대 발표를 민간보험 약관 변경으로 받아들이지 마세요.'),
h('가상 예시: 생일과 치료일이 가까운 경우')+p('B씨 자녀가 곧 13세가 된다고 가정합니다. 보호자는 생일 전후의 치료일과 해당 치아의 상태를 알리고, 진료일에 적용되는 급여 기준을 치과에 확인합니다. 확대 발표를 보고 예약일만 바꾸면 지원이 확정된다고 생각하지 않고, 시행 공고와 의료진 판단을 함께 확인하는 사례입니다.')+'<blockquote>아이의 생년월일과 치료 예정일을 기준으로 이번 치아의 광중합형 복합레진 급여 여부를 알고 싶습니다. 13세 확대가 실제 시행 중인지, 적용되지 않는다면 어떤 기준 때문인지, 급여와 비급여를 나눠 설명해 주세요.</blockquote>']),
dict(path='/checkups/cervical-screening-report-2027-change',slug='cervical-report-2027',cat='건강검진',title='2027 자궁경부암 검진 결과 기록지 개정, 5가지 판정 읽는 법',desc='2027년 1월 1일 시행되는 국가 자궁경부암 검진 판정 기준·기록지 개정을 정리합니다. 저위험·고위험·암 의심·판정불가를 확진과 구분하고 결과표에서 권고사항을 확인하는 방법입니다.',status='고시 2026-214호 개정·2027년 1월 1일 시행 예정',parent='/checkups/cervical-screening-ascus-followup',parent_note='현재 ASC-US 결과의 후속 진료 안내와 2027년 국가검진 기록지 개정은 다른 질문입니다. 개정 판정 구분과 권고사항을 따로 확인하세요.',sources=[(LAW,'국가법령정보센터 암검진 실시기준','고시 2026-214호·시행일·별표 2와 별지 제14호'),(AMEND,'보건복지부 개정 고시 원문·신구조문','대한병원협회가 게시한 공문·붙임 원문 확인')],body=[
h('2027년 기록지 개정이 현재 결과의 확진을 바꾸지는 않습니다')+p('2027년 국가 자궁경부암 검진에서는 개정된 판정 기준과 기록지를 확인하게 됩니다. 저위험·고위험·자궁경부암 의심 등의 구분을 읽을 때는 세포검사 소견, 최종 판정, 의료진 권고를 나눠 보세요. 고위험이나 암 의심이라는 문구만으로 암 확진을 뜻하지는 않습니다.')+p(a(LAW,'암검진 실시기준 고시 2026-214호')+'의 시행일은 2027년 1월 1일입니다. 별표 2의 판정 기준과 별지 제14호 자궁경부암 검진 결과 기록지가 개정됩니다. 이 기록지는 의료기관의 기록 서식이므로 개인에게 전달되는 결과 통보서의 모든 칸이 동일하다고 가정하지 마세요.'),
h('개정 최종 판정은 다섯 구분으로 읽습니다')+table(['최종 판정 구분','결과에서 확인할 것'],[['정상: 상피내병변 또는 악성소견 없음','추가 소견과 권고를 함께 읽기'],['저위험: 비정형세포 또는 저등급병변','전문의 상담·필요 검사 안내 확인'],['고위험: 전암성병변 의심','의료진이 권한 추가 평가·일정 확인'],['자궁경부암 의심','신속한 전문의 진료 등 권고 확인'],['판정불가: 재검진 권고','검체 상태 등 사유와 재검 방법 문의']])+p('표의 행동은 결과표를 확인하는 순서입니다. 각 분류에 모든 사람에게 동일한 검사나 대기 기간을 지정한 것은 아닙니다. 이전 검사·HPV 결과·증상·개인 상태에 따라 의료진이 후속 계획을 정합니다.'),
h('유형별 진단과 최종 판정을 혼동하지 마세요')+p(a(AMEND,'개정 고시의 원문 서식')+'에는 유형별 진단과 최종 판정, 권고사항이 구분되어 있습니다. 유형별 진단의 세부 항목 번호를 최종 판정 번호로 옮기거나, 이전 ASC-US라는 약어 하나만 보고 새 판정을 스스로 확정하지 마세요.')+p('반응성 세포변화나 감염성 소견이 적혔다고 곧바로 암이라는 뜻도 아닙니다. 검체가 충분하지 않아 판정불가가 된 경우에도 암 확인과는 구분해야 합니다. 어느 항목이 최종 판정이고 어떤 소견이 추가 설명인지 병원에 질문하세요.'),
h('권고사항에서 실제 다음 행동을 찾습니다')+p('개정 기록지의 권고는 추가조치 불필요, 전문의 상담 및 필요 검사, 신속한 전문의 진료 및 그에 따른 치료, 판정불가에 따른 재검진 등의 항목으로 구분됩니다. 문구만 보고 스스로 치료를 시작하거나 검진만 반복하지 말고 해당 결과의 후속 안내를 받으세요.')+ul(['검사일과 검체·검사 종류 확인','최종 판정과 유형별 소견을 분리해 기록','권고된 진료과·검사·일정과 예약 방법 문의','이전 결과와 관련 검사 자료를 의료진에게 전달'])+p('현재 ASC-US 결과를 받은 경우에는 '+a('/checkups/cervical-screening-ascus-followup','ASC-US와 HPV 후속 검사 확인 안내')+'를 함께 볼 수 있습니다. 2027년 양식을 기다리며 이미 권고받은 진료를 미루지 마세요.'),
h('기존 결과표를 새 분류로 다시 쓰는 작업은 아닙니다')+p('2026년에 받은 결과를 새 구분으로 자동 변환해 해석하거나 병원에 확진서로 바꾸어 달라고 요청할 근거는 아닙니다. 보험 청구에서도 검진의 의심 소견과 조직검사 등으로 확인한 진단은 구분합니다. 필요한 진료와 서류는 해당 의료진·보험사의 공식 안내를 따르세요.'),
h('가상 예시: 판정불가라고 적혀 있다면')+p('C씨가 판정불가·재검진 권고라는 결과를 받았다고 가정합니다. C씨는 암이 확정됐다고 단정하지 않고, 검체나 판독 관련 사유와 재검진 방법을 문의합니다. 이전 검사 결과를 함께 전달하고 의료진의 안내로 다음 일정을 정하는 사례입니다.')+'<blockquote>결과의 최종 판정과 세부 소견이 각각 무엇을 뜻하는지 설명해 주세요. 지금 필요한 후속 검사와 예약 시점, 가져갈 이전 결과가 있는지 확인하고 싶습니다.</blockquote>']),
dict(path='/checkups/national-biobank-noncheckup-participation',slug='biobank-general-participation',cat='건강검진',title='건강검진 비대상자도 바이오빅데이터 참여, 신청 전 확인할 것',desc='국가통합바이오빅데이터 일반참여자 모집이 건강검진 비대상자까지 확대됐습니다. 만 19세 이상 대한민국 국적 기준, 모집기관·동의서·검체 기증 절차와 검진의 차이를 정리합니다.',status='건강검진 비대상자 모집 확대·일반참여자 공식 안내 운영 중',parent='/checkups/health-checkup-target-2026',parent_note='국가건강검진 대상 확인과 바이오빅데이터 연구 참여는 별개입니다. 검진 비대상자의 일반참여자 신청·동의 절차를 확인하세요.',sources=[(KDCA,'질병관리청 일반참여자 모집 확대 발표','2026년 10월 15일·건강검진 비대상자 참여 확대'),(BIO,'국가통합바이오빅데이터 일반참여자 안내','자격·모집기관 검색·설명 및 동의·검체 기증 안내')],body=[
h('검진 대상이 아니어도 연구 참여를 알아볼 수 있습니다')+p('국가통합바이오빅데이터는 건강검진 비대상자도 일반참여자 모집기관에 참여를 문의할 수 있도록 범위를 넓혔습니다. 현재 일반참여자 공식 안내의 기본 대상은 만 19세 이상 대한민국 국적자입니다. 검진 대상 여부와 실제 연구 참여 가능 여부는 모집기관에서 확인하세요.')+p(a(KDCA,'질병관리청의 모집 확대 발표')+'와 '+a(BIO,'사업의 일반참여자 안내')+'는 연구 설명·동의와 자료 수집·검체 기증을 안내합니다. 연구 참여를 신청하면 무료 종합검진이나 질병 진단·치료를 모두 받을 수 있다는 뜻은 아닙니다.'),
h('국가건강검진과 연구 참여는 목적이 다릅니다')+table(['구분','국가건강검진','바이오빅데이터 연구 참여'],[['주된 확인','해당 연도 검진 대상과 검사항목','일반참여자 자격과 모집기관'],['진행 방식','지정기관 검진 예약·수검','연구 설명·동의·자료 및 검체 기증'],['마지막 확인','검진 결과와 필요한 진료','참여 절차와 동의 범위·안내받을 결과'],['서로 대신하는지','연구 참여만으로 수검 완료가 되지는 않음','검진 비대상자도 참여 문의 가능']])+p('올해 검진 대상 확인이 목적이라면 '+a('/checkups/health-checkup-target-2026','2026 국가건강검진 대상 조회 안내')+'를 먼저 보세요. 연구 참여를 선택했다고 필요한 검진이나 진료가 자동으로 대체되지 않습니다.'),
h('공식 사이트에서 일반참여자 모집기관을 찾습니다')+p('사업 사이트에는 일반참여자와 중증질환자·희귀질환자 경로가 나뉘어 있습니다. 질환별 경로의 연령·진단 요건을 일반참여자에게 그대로 적용하지 마세요. 일반참여자 안내에서 지역별 모집기관을 찾고 현재 예약·모집 상황을 전화로 확인합니다.')+ul(['일반참여자로 신청 가능한지와 예약 가능일','방문할 모집기관·연구 담당 창구·준비할 확인 자료','설명과 동의, 채혈·채뇨 등 실제 방문 절차','식사·복용약 등 방문 전 준비를 의료기관에 질문'])+p('모든 병원이 참여기관인 것은 아닙니다. 채혈을 한다는 이유로 임의로 금식 시간을 정하거나 약을 끊지 말고 해당 기관의 지시를 확인하세요.'),
h('동의서에서는 자료와 검체의 사용 범위를 읽습니다')+p('공식 페이지는 연구 설명문, 개인정보 수집·이용 동의, 인체유래물 등 기증 동의, 참여 동의 관련 자료를 제공합니다. 방문 전 내용을 읽고 이해되지 않는 부분을 연구 담당자에게 물어보세요. 신청 버튼을 눌렀다는 이유만으로 모든 동의의 의미를 이해한 것이 되지는 않습니다.')+ul(['어떤 건강·유전 정보와 검체를 수집하는가','연구 이용·보관·제공의 범위는 어디까지인가','철회하려면 누구에게 어떤 방식으로 요청하는가','어떤 결과를 어떤 방식으로 안내받을 수 있는가'])+p('모든 유전체 분석 결과를 개인에게 돌려받거나 참여 철회 시 이미 이용된 자료까지 모두 회수할 수 있다고 가정하지 마세요. 실제 동의서의 범위와 예외를 확인하는 질문입니다. 주민등록번호나 진료자료를 공개 댓글에 올리지 않습니다.'),
h('가상 예시: 올해 국가검진 대상이 아닌 직장인')+p('D씨는 올해 국가건강검진 비대상자이지만 연구 참여에 관심이 있다고 가정합니다. 공식 사이트에서 일반참여자 자격과 지역 모집기관을 확인하고, 예약 시 검진 비대상자 참여 절차를 문의합니다. 설명을 들은 뒤 동의 여부를 스스로 결정하며, 별도로 필요한 진료는 평소 의료기관에서 받습니다.'),
h('신청 전 질문 문장')+'<blockquote>올해 국가건강검진 비대상자이고 일반참여자 참여를 알아보고 있습니다. 현재 모집과 예약이 가능한지, 방문 준비와 소요 절차, 개인정보·검체 동의 범위 및 철회 방법, 개인에게 안내되는 결과가 무엇인지 설명해 주세요.</blockquote>'+p('참여 여부는 충분히 설명을 듣고 자발적으로 결정할 사항입니다. 이 글이나 연결된 정보만으로 사용자의 신청·개인정보 입력·동의가 대신 이루어지지는 않습니다.')])]

def image(d,key):
 src='/assets/images/'+d['slug']+'-'+key+'.webp'
 with Image.open(ROOT/src[1:]) as im:w,hh=im.size
 return f'<figure><img src="{src}" width="{w}" height="{hh}" alt="{d["title"]} 관련 상담 설명 장면" loading="{"eager" if key=="thumb" else "lazy"}" decoding="async">'+('<figcaption>AI로 만든 설명용 이미지이며 실제 환자·진료기록이나 공식 서비스 화면이 아닙니다.</figcaption>' if key=='thumb' else '')+'</figure>'

def publish(n):
 d=DATA[n-6];dest=ROOT/(d['path'][1:]+'.html')
 if dest.exists():raise SystemExit('Already exists: '+str(dest))
 soup=BeautifulSoup((ROOT/'surgery-benefit/wound-suture-specific-rider.html').read_text(encoding='utf-8'),'html.parser')
 soup.title.string=d['title']
 for attr,key,val in [('name','description',d['desc']),('property','og:title',d['title']),('property','og:description',d['desc']),('property','og:image',BASE+'/assets/images/'+d['slug']+'-thumb.webp')]:soup.find('meta',attrs={attr:key})['content']=val
 soup.find('link',rel='canonical')['href']=BASE+d['path']
 og=soup.new_tag('meta',attrs={'property':'og:url','content':BASE+d['path']});soup.head.append(og)
 style=soup.new_tag('style');style.string=CSS;soup.head.append(style)
 schema=json.loads(soup.find('script',type='application/ld+json').string);schema.update(headline=d['title'],description=d['desc'],image=BASE+'/assets/images/'+d['slug']+'-thumb.webp',mainEntityOfPage=BASE+d['path'],datePublished=DATE,dateModified=DATE);soup.find('script',type='application/ld+json').string=json.dumps(schema,ensure_ascii=False)
 main=soup.main;cta=str(main.find('section',class_='kakao-inquiry-cta'));main.clear();main['class']=['section','article-body','insurance-series-article','cluster-reading','trend5']
 section=d['path'].split('/')[1]
 text=f'<div class="breadcrumb"><a href="/">홈</a> / <a href="/{section}/">{d["cat"]}</a></div><h1>{d["title"]}</h1><p class="lead">{d["desc"]}</p><div class="status-note"><strong>이용·시행 단계</strong><br>{d["status"]}</div>'+image(d,'thumb')
 if n==8:text+='<p>'+a('/insurance-companies/','보험사별 공식 홈페이지 확인하기')+'</p>'
 for i,part in enumerate(d['body']):
  text+=part
  if i==1:text+=image(d,'body1')
  if i==3:text+=image(d,'body2')
 text+='<section class="official-guide-actions"><h2>공식 확인처와 상세 안내</h2><div class="official-guide-grid">'
 for url,title,scope in d['sources']:text+=f'<a class="official-guide-button" href="{url}" target="_blank" rel="noopener"><strong>{title}</strong><span>{scope} · 새 창 ↗</span></a>'
 text+='</div></section><p>작성: 케어로컬 사이트 운영자. '+a('/legal/about','작성 기준과 운영자 역할')+'을 확인할 수 있습니다. 개인의 진단·치료 적합성은 의료진에게, 보험 보장은 해당 계약의 공식 안내에서 확인하세요.</p>'
 if n==8:text+='<div class="insurance-company-cta">'+a('/insurance-companies/','보험사별 공식 홈페이지 확인하기')+'</div>'+cta
 main.append(BeautifulSoup(text,'html.parser'));dest.write_text(str(soup)+'\n',encoding='utf-8')
 parent=ROOT/(d['parent'][1:]+'.html');raw=parent.read_text(encoding='utf-8');(OUT/(parent.stem+'-before.html')).write_text(raw,encoding='utf-8');ps=BeautifulSoup(raw,'html.parser')
 block=BeautifulSoup('<aside class="notice" id="trend610-related"><strong>함께 확인할 내용</strong><p>'+d['parent_note']+' '+a(d['path'],d['title'])+'</p></aside>','html.parser')
 anchor=ps.main.find('section',class_='official-guide-actions')
 if anchor:anchor.insert_before(block)
 else:ps.main.append(block)
 for script in ps.find_all('script',type='application/ld+json'):
  try:o=json.loads(script.string);o['dateModified']=DATE;script.string=json.dumps(o,ensure_ascii=False)
  except(ValueError,TypeError):pass
 parent.write_text(str(ps)+'\n',encoding='utf-8')
 idx=ROOT/section/'index.html';cs=BeautifulSoup(idx.read_text(encoding='utf-8'),'html.parser');(cs.main or cs.body).append(BeautifulSoup('<section class="section"><h2>제도와 이용 절차</h2><p>'+a(d['path'],d['title'])+'</p></section>','html.parser'));idx.write_text(str(cs)+'\n',encoding='utf-8')
 sm=ROOT/'sitemap.xml';raw=sm.read_text(encoding='utf-8');raw=raw.replace('</urlset>',f'  <url><loc>{BASE+d["path"]}</loc><lastmod>{DATE}</lastmod></url>\n</urlset>');raw=re.sub(r'(<loc>'+re.escape(BASE+d['parent'])+r'</loc>\s*<lastmod>)[^<]+',r'\g<1>'+DATE,raw);sm.write_text(raw,encoding='utf-8')
 subprocess.run([sys.executable,str(ROOT/'scripts/build-article-catalog.py')],check=True)
 (OUT/'manifest.json').write_text(json.dumps([{k:v for k,v in x.items() if k!='body'} for x in DATA],ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps({'n':n,'article':str(dest.relative_to(ROOT)),'parent':str(parent.relative_to(ROOT))},ensure_ascii=False))

if __name__=='__main__':publish(int(sys.argv[1]))
