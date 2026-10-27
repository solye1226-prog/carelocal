"""Publish one source-reviewed Trends follow-up at a time. Push is manual."""
from pathlib import Path
from bs4 import BeautifulSoup
import json, sys, subprocess, re
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/trend5-publication-2026-10-27'
DATE = '2026-10-27'
BASE = 'https://hospital.hbuby.com'

def p(t): return '<p>' + t + '</p>'
def h(t): return '<h2>' + t + '</h2>'
def a(url,t): return f'<a href="{url}">{t}</a>'
def ul(xs): return '<ul>' + ''.join('<li>'+x+'</li>' for x in xs) + '</ul>'
def table(headers,rows):
    return '<div class="trend-table"><table><thead><tr>'+''.join('<th scope="col">'+x+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+x+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table></div>'

FSC='https://www.fsc.go.kr/no010101/87818'
SILSON='https://www.silson24.or.kr/claim/web/'
HIRA='https://www.hira.or.kr/bbsDummy.do?brdBltNo=12308&brdScnBltNo=4&pageIndex=1&pgmid=HIRAA020002000100'
ALS='https://www.mohw.go.kr/gallery.es?act=view&bid=0003&list_no=380483&mid=a10505000000'
AMB='https://e-health.go.kr/gh/heNws/selectBbsDtlViewInfo.do?bbsId=U00186&bbsNo=422117&menuId=200048'
TELE='https://m.korea.kr/briefing/pressReleaseView.do?newsId=156785554'
TRIAL='https://www.hira.or.kr/bbsDummy.do?brdBltNo=11761&brdScnBltNo=4&pgmid=HIRAA020002000100'
RARE='https://www.korea.kr/news/policyNewsView.do?newsId=148971474'
NHIS='https://www.nhis.or.kr/renewal_popup/poster/20260608_poster_longdesc_1.html'

DATA=[
dict(path='/silbi/silson24-naver-toss-in-app-claim',slug='silson24-naver-toss',cat='실비보험',title='실손24 네이버·토스 청구, 앱에서 전송한 뒤 접수까지 확인하는 법',desc='네이버·토스에서 실손24 청구를 시작할 때 참여 병원과 진료내역을 확인하는 순서입니다. 전송 완료와 보험사 접수·심사·지급을 구분하고 누락 자료와 중복 청구를 줄이는 방법을 정리합니다.',status='플랫폼 연계 서비스 이용 안내',parent='/silbi/silson24-hospital-not-found',parent_note='참여 병원을 찾았다면 플랫폼에서 청구를 시작하고 보험사 접수까지 확인하는 다음 절차를 이어서 볼 수 있습니다.',sources=[(FSC,'금융위원회 플랫폼 연계 개선 안내','10월 7일 개선 일정·네이버 지도/페이·토스 연계와 전자 전송 절차'),(SILSON,'실손24 공식 서비스·참여기관·청구이력','최신 메뉴와 참여기관, 청구 상태 안내 확인')],body=[
h('앱 안에서 신청해도 보험사 접수 확인은 따로 합니다')+p('네이버·토스에서 청구를 시작했다면 마지막 화면의 전송 결과를 확인하고, 이후 보험사의 접수 내역을 확인하세요. 화면에 청구 완료나 전송 완료가 나왔다고 보험금 지급까지 결정된 것은 아닙니다. 본인 보험계약, 다녀온 의료기관, 진료일을 정확하게 선택했는지가 먼저입니다.')+p(a(FSC,'금융위원회 안내')+'는 2026년 10월 7일부터 네이버 지도·네이버 페이·토스 앱 안에서 실손보험금 청구를 마칠 수 있도록 개선한다고 설명합니다. 앱 버전·로그인·연계 상태에 따라 실제 메뉴가 달라질 수 있으므로, 이 글은 개인 계정의 접수 화면이나 특정 버튼 위치를 대신 확인한 안내가 아닙니다.'),
h('시작할 곳과 확인할 정보를 구분하세요')+table(['시작 경로','먼저 확인할 것','다음 행동'],[['네이버 지도','병원 상세의 실손24 참여 표시·청구 연결','실제 방문한 지점과 진료일 선택'],['네이버 페이·토스','앱의 보험금 청구·실손24 관련 메뉴','수신 보험사·계약·지급계좌 대조'],['메뉴가 없거나 연계가 안 될 때','앱 업데이트·공식 서비스 안내','실손24 공식 홈페이지 또는 보험사 공식 접수 이용']])+p('앱 내부 검색에서 실손24 또는 보험금 청구를 찾아 서비스 안내를 읽으세요. 검색 결과의 광고나 개인 메시지로 받은 링크 대신 공식 앱에서 진입합니다. 마이데이터 동의로 정보가 자동 표시되더라도 병원명·날짜·보험사·계좌가 맞는지 직접 확인하세요.'),
h('병원 전체가 아니라 내 진료내역이 전송되는지 확인합니다')+p('참여 병원이라는 사실과 특정 진료내역을 선택할 수 있다는 사실은 구분해야 합니다. 영수증·세부산정내역서·처방전의 전자 전송을 이용하더라도 입원·수술 등에서 보험사가 확인하려는 사실이 모두 채워지는 것은 아닙니다. 추가 발급이 필요한지는 보험사에 요청 항목과 이유를 먼저 물어보세요.')+p('내역이 보이지 않는다면 같은 이름의 다른 지점을 고르거나 진료일을 바꿔 억지로 접수하지 마세요. '+a('/silbi/silson24-hospital-not-found','실손24 병원이 검색되지 않을 때의 확인 순서')+'에서 기관 조회 문제를 먼저 구분할 수 있습니다.'),
h('전송·접수·지급을 한 줄 기록으로 남기세요')+ul(['전송 시각과 신청한 진료일·보험사 기록','보험사 앱 또는 안내 문자에서 접수번호 확인','추가 서류 요청이 오면 서류명·제출 경로·기한 확인','동일 진료를 다른 경로로 이미 보냈다면 중복 접수 여부 문의'])+p('전송 결과가 불분명하면 같은 자료를 여러 번 보내기보다 청구이력과 수신 보험사의 접수부터 대조합니다. 시스템 이용 문제는 실손24 공식 고객지원, 접수 이후의 심사·지급 문제는 해당 보험사로 질문을 나누면 필요한 답을 받기 쉽습니다.'),
h('가상 예시: 병원 표시와 접수 내역이 다른 경우')+p('A씨가 네이버 지도에서 참여 병원을 확인하고 통원 청구를 전송한 상황을 가정합니다. 보험사 접수번호가 아직 보이지 않는다면 지급 거절로 단정하지 않고, 전송 시각·병원 지점·진료일·보험사를 대조해 문의합니다. 보험사가 수술 사실 자료를 추가 요청한 경우에도 전자 전송 실패와는 별개일 수 있습니다.'),
h('문의할 내용을 짧게 준비하세요')+'<blockquote>해당 진료일의 실손24 전송 결과와 보험사 접수 여부를 확인하고 싶습니다. 접수번호가 있는지, 추가로 필요한 자료가 있는지, 이미 접수된 동일 진료가 있는지 알려 주세요.</blockquote>'+p('본인인증 정보나 진료자료는 공개 댓글·일반 상담 메시지로 보내지 말고 해당 기관의 공식 접수 경로를 이용하세요. 기본 서류는 '+a('/claims/medical-expense-claim-documents','실비 청구서류 안내')+'와 함께 확인할 수 있습니다.')]),
dict(path='/caregiver/als-specialist-nursing-hospital-pilot',slug='als-specialist-pilot',cat='간병·돌봄',title='루게릭병 전문요양병원 시범사업, 입원 상담 전에 확인할 것',desc='루게릭병 등 중증근육성희귀질환 전문요양병원 시범사업은 11월 시행 계획과 참여기관 공모를 구분해 봐야 합니다. 입원 가능일·대상 조건·간병과 비용을 상담할 때 준비할 내용을 정리합니다.',status='11월 시행 계획·참여기관 공모 단계',parent='/caregiver/caregiver-insurance-claim-documents',parent_note='루게릭병 등 중증근육성희귀질환의 전문요양병원 시범사업을 알아본다면 사업 참여 여부·병상·간병 비용을 먼저 구분해 상담하세요.',sources=[(ALS,'보건복지부 11월 시범사업 추진 안내','사업의 목적·4대 특화서비스·11월 시행 계획'),(HIRA,'심평원 참여기관 공모 원문','기관 선정 요건과 공모 단계 확인')],body=[
h('11월 시행 계획이 모든 병원의 입원 개시를 뜻하지는 않습니다')+p(a(ALS,'보건복지부 발표')+'는 준비기간을 거쳐 2026년 11월부터 중증근육성희귀질환 전문요양병원 건강보험 시범사업을 시행할 계획이라고 설명합니다. 10월 23일 심평원에는 참여기관 공모가 올라왔습니다. 이 단계의 공고는 환자 개인의 입원 신청서나 모든 요양병원의 참여 확정 명단이 아닙니다.')+p('따라서 병원을 알아볼 때는 “시범사업 참여가 확정됐는가, 해당 서비스는 언제 시작하는가, 현재 입원 상담이 가능한가”를 따로 물어야 합니다. 루게릭병 진단만으로 어느 병원이든 같은 서비스를 받거나 빈 병상이 보장되는 것은 아닙니다.'),
h('서비스 이름을 실제 필요한 관리와 연결해 보세요')+table(['발표한 서비스','상담에서 확인할 질문'],[['환자 맞춤형 전문의료','현재 필요한 호흡·영양·재활 관리를 제공할 수 있나요?'],['단기병상','이용 목적·입원 기간·대기 절차는 무엇인가요?'],['응급상황 대응','상태 변화 시 의료진 연락과 전원은 어떻게 진행하나요?'],['지역사회 연계','퇴원 뒤 집에서 이어갈 진료·돌봄을 어떻게 연결하나요?']])+p('사업의 서비스 항목은 병원에 물어볼 출발점입니다. 가족이 인공호흡기·위루관 등 의료기기의 관리 방법을 인터넷 설명만으로 정하거나 변경해서는 안 됩니다. 현재 상태와 이동 가능 여부는 주치의·입원 상담팀이 함께 판단해야 합니다.'),
h('공모의 병원 기준을 환자 개인의 입원 조건으로 읽지 마세요')+p(a(HIRA,'참여기관 공모')+'의 환자 구성비·인력·시설 기준은 병원을 선정하기 위한 조건입니다. 그 수치를 개인에게 적용해 “이 기구를 모두 사용해야만 상담할 수 있다”거나 반대로 “이 진단이면 입원이 확정된다”고 결론내릴 수 없습니다. 선정 공고와 해당 병원의 환자 대상·진료 범위를 각각 확인하세요.'),
h('상담 전에 한 장으로 정리할 자료')+ul(['진단명과 최근 진료 병원·담당 진료과','현재 필요한 호흡·영양·이동·의사소통 지원의 종류','퇴원 또는 전원 희망일과 보호자 연락 가능 시간','의료진이 작성한 전원 관련 기록이 필요한지 확인'])+p('서류를 미리 모두 유료 발급하기보다 수신 병원이 필요한 기록과 최근 검사 범위를 먼저 알려주도록 요청하세요. 민감한 기록은 상담 창구가 지정한 안전한 제출 경로로만 보냅니다.'),
h('건강보험 수가와 가족의 총 부담액은 구분합니다')+p('건강보험 시범사업이라는 말만으로 병실료·간병·재료·이송 등 모든 비용이 면제되는 것은 아닙니다. 원무팀에 급여 본인부담, 비급여, 간병 제공 방식, 별도 준비 물품을 구분한 예상 비용을 요청하세요. 기존에 이용하던 간병 방식이 입원 뒤에도 유지되는지 확인하는 것도 필요합니다.')+p('민간 간병보험은 병원 종별·실제 간병 제공·증빙 요건을 가입 약관으로 따로 판단합니다. '+a('/caregiver/caregiver-insurance-claim-documents','간병인 사용 보험금 청구서류')+'와 대조하되, 시범사업 참여 사실만으로 개인 보험금 지급을 예상하지 마세요.'),
h('가상 예시와 입원팀 문의 문장')+p('B씨 가족이 11월 전원을 계획한다고 가정합니다. 기존 병원의 퇴원을 확정하기 전에 수신 병원의 참여 확정 여부, 입원 가능일, 필요한 의료관리, 비용 견적을 먼저 맞춥니다. 사업 시작 예정일과 가족이 실제로 입원 가능한 날이 다를 수 있기 때문입니다.')+'<blockquote>전문요양병원 시범사업 참여와 서비스 개시가 확정됐는지 궁금합니다. 환자 상태에 맞는 진료 범위, 현재 입원 대기, 필요한 전원 기록, 간병과 비급여를 나눈 예상 비용을 안내해 주세요.</blockquote>']),
dict(path='/guides/private-ambulance-quality-pilot-check',slug='private-ambulance-pilot',cat='병원 이용',title='민간구급차 인증제 시범사업, 병원 이송 예약 전 확인할 것',desc='민간구급차 품질 인증제는 10월 참여업체 접수와 12월 결과 발표 예정 단계를 구분해야 합니다. 인증 신청과 선정의 차이, 예약 전 의료진 협의·장비·견적·이송기록 확인법을 정리합니다.',status='10월 21~30일 업체 신청·12월 결과 발표 예정',parent='/guides/night-hospital-checklist',parent_note='응급 상황의 119 이용과 예정된 병원 간 이송 예약은 구분해야 합니다. 민간구급차를 예약한다면 인증 단계·환자 상태·견적을 먼저 확인하세요.',sources=[(AMB,'보건복지부 민간구급차 품질 인증제 발표','참여 접수 기간·심사 절차·12월 결과 발표 예정 안내')],body=[
h('인증 신청 업체와 인증을 받은 업체는 다릅니다')+p(a(AMB,'보건복지부·중앙응급의료센터 발표')+'는 2026년 10월 21~30일 참여업체 신청을 받고 서면·현장심사 등을 거쳐 12월 중 최종 결과를 발표할 예정이라고 설명합니다. 10월의 신청 사실을 이미 인증이 완료된 것으로 받아들이면 안 됩니다.')+p('이 사업은 업체의 법정 기준 준수와 서비스 품질을 평가하는 시범사업입니다. 인증 여부는 업체 허가, 배차 가능성, 이번 환자에게 필요한 이송 조건을 모두 대신하지 않습니다. 예약 시에는 환자 상태에 맞는 이송이 가능한지를 의료진과 먼저 정하세요.'),
h('응급 대응과 예정된 이송을 먼저 구분하세요')+p('갑자기 의식·호흡 등 상태가 나빠졌다면 업체 가격을 비교하며 예약을 기다릴 상황인지부터 판단해야 합니다. 응급 상황에서는 119에 연락해 안내를 따르세요. 이 글은 예정된 퇴원·전원 이송을 준비하는 확인 목록이며, 환자의 이송 적합성을 판단하거나 응급 대응을 대체하지 않습니다.'),
h('예약 전 세 곳의 답이 맞아야 합니다')+table(['확인할 곳','맞춰야 할 내용'],[['보내는 병원 의료진','현재 상태·이동 중 필요한 관리·출발 가능 시간'],['받는 병원','입원 또는 진료 예약·도착 창구·도착 가능 시간'],['이송업체','필요 인력과 장비 제공 여부·차량·배차·예상 비용']])+p('산소나 의료기기가 필요하다면 기구 이름만 전달하고 예약을 끝내지 마세요. 필요한 지원을 의료진이 설명하고 업체가 제공 가능 여부를 확인하도록 연결합니다. 가족이 필요한 장비·유량·처치 방법을 임의로 정하는 안내가 아닙니다.'),
h('전화 견적을 총액만으로 비교하지 마세요')+ul(['출발·도착지와 예상 경로, 날짜·시간','차량과 동승 인력, 필요한 장비 제공 범위','견적의 포함 항목과 별도 발생 가능 비용','대기·일정 변경·취소 시 조건과 최종 영수증 발급 방식'])+p('동일한 이동이라도 요청 조건을 다르게 전달하면 견적 비교가 어렵습니다. 거리나 시간만으로 전국 공통 금액을 계산하지 말고, 업체에 적용 기준과 산출 항목을 설명해 달라고 요청하세요. 인증마크를 보여주더라도 발급 주체·유효기간·대상 업체가 맞는지 확인합니다.'),
h('민간보험 청구를 생각한다면 운행 자료를 확인합니다')+p('이송 비용의 보장 여부는 본인 계약의 구급차·이송 비용 조항과 실제 이용 조건을 검토해야 합니다. 인증제 참여나 병원 간 이동만으로 실손 지급이 정해지지는 않습니다. 보험사에 필요한 증빙을 먼저 문의하고 영수증과 이송일·구간·이용 사실을 확인할 자료를 확보하세요.')+p('병원 도착 이후의 준비는 '+a('/guides/night-hospital-checklist','야간·휴일 병원 방문 전 확인사항')+'과 연결해 볼 수 있습니다. 예정된 전원이라면 수신 병원의 원무·진료 창구 안내를 우선합니다.'),
h('가상 예시: 전원 시간과 배차 시간을 맞추는 경우')+p('C씨가 퇴원일에 다른 병원으로 이동한다고 가정합니다. 가족은 업체에 출발 시간만 알리기보다 받는 병원의 도착 창구·시간을 확인하고, 보내는 병원의 준비 완료 시각과 배차를 맞춥니다. 이는 특정 업체 이용이나 인증 획득을 보장하는 사례가 아닙니다.')+'<blockquote>병원 간 예정 이송입니다. 의료진이 전달한 관리 요구를 제공할 수 있는지, 배차와 동승 인력, 견적에 포함·제외되는 비용, 발급 가능한 운행·결제 자료를 알려 주세요. 품질 인증은 신청 단계인지 최종 인증인지도 확인하고 싶습니다.</blockquote>']),
dict(path='/guides/telemedicine-first-visit-proposed-rules',slug='telemedicine-proposed',cat='병원 이용',title='비대면진료 초진·7일 처방 변경안, 지금 적용되는 기준과 구분하세요',desc='2026년 10월 입법예고한 비대면진료 초진·동일 시도·처방일수 변경안과 현재 시범사업을 구분합니다. 진료 예약 전에 대면 이력·진료 목적·처방과 약 수령을 확인하는 방법입니다.',status='10월 19일~11월 9일 입법예고·12월 24일 법 시행 예정',parent='/guides/lost-prescription-reissue-cost',parent_note='기존 처방전을 잃어버린 경우와 새 비대면진료를 받아 처방받는 경우는 다릅니다. 초진·처방일수 변경안을 현재 규칙으로 오인하지 않도록 구분해 보세요.',sources=[(TELE,'보건복지부 비대면진료 실시·처방기준 입법예고','예고안의 대상·처방일수와 12월 24일 법 시행 일정'),(TRIAL,'심평원 현재 시범사업 지침 게시 안내','2025년 10월 27일 개정 시행 지침과 첨부 원문')],body=[
h('초진 7일 처방이라는 보도를 현재 공통 규칙으로 적용하지 마세요')+p('2026년 10월에 발표된 초진·동일 시도·처방일수 기준은 '+a(TELE,'입법예고한 개정안')+'의 내용입니다. 개정 의료법은 12월 24일 시행 예정이며 시행규칙안은 10월 19일~11월 9일 의견수렴 중입니다. 발표 직후 모든 진료의 기준이 바뀌었다는 뜻이 아닙니다.')+p('지금 예약하려면 현재 시범사업 지침과 해당 의료기관의 진료 가능 여부를 확인해야 합니다. 최종 규정이 확정·시행될 때까지 예고안은 바뀔 수 있으므로, 기존 처방을 받기 위해 다른 병원을 임의로 옮기거나 약을 중단하는 근거로 삼지 마세요.'),
h('개정안에서 말하는 일반·초진은 이렇게 구분합니다')+table(['개정안 항목','예고한 내용','읽을 때 주의'],[['일반 비대면진료','같은 의료기관·6개월 이내·동일 증상 대면 이력','셋 중 한 가지만으로 재진이라 단정하지 않기'],['초진 비대면진료','해당 대면 이력 요건 미충족 시 별도 기준','주소지 등 지역·예외 대상 확인 필요'],['초진 처방일수','원칙 7일 이내, 일정 조건의 예외 제안','현재 모든 처방에 7일 제한으로 적용하지 않기']])+p('위 표는 개정안을 읽는 요약입니다. 현재 이용 가능 대상표가 아닙니다. 처음 방문한 병원인지뿐 아니라 같은 증상으로 대면진료를 언제 받았는지가 예고안의 구분에 영향을 줍니다.'),
h('현재 진료를 예약할 때 확인할 것은 따로 있습니다')+p(a(TRIAL,'심평원에 게시된 시범사업 개정 안내')+'는 2025년 10월 27일 시행 지침과 의료기관·약국용 원문을 제공합니다. 의원급 중심 운영과 병원급 예외를 안내하므로, 앱에 진료과가 보인다는 이유만으로 누구나 어느 병원에서든 이용 가능하다고 생각하면 안 됩니다.')+ul(['지금 진료받을 증상과 해당 기관의 대면진료 이력','의원이 현재 시범사업에서 해당 상황을 진료할 수 있는지','진료 방식과 필요한 본인확인·기록','처방 가능 여부, 약국 전달과 실제 약 수령 방식'])+p('진찰 뒤 처방 여부는 의료인이 판단합니다. 진료 예약·처방전 발급·약국 조제·약 수령은 서로 다른 단계이므로, 한 단계의 완료가 다음 단계 완료를 뜻하지는 않습니다.'),
h('처방전 재발급과 새 진료를 구분하세요')+p('이전에 받은 처방전을 분실한 상황이라면 원래 의료기관에 재발급 가능 여부와 약국 제출 상태부터 문의하세요. 같은 약을 받으려고 새 진료를 추가하기 전에 기존 조제 여부도 확인하는 편이 중복 처방과 비용 혼선을 줄이는 데 도움이 됩니다.')+p(a('/guides/lost-prescription-reissue-cost','처방전 분실 시 재발급·비용 확인 안내')+'에서 분실 문제를 먼저 정리할 수 있습니다. 새 증상이나 상태 변화가 있다면 분실 처리와 별개로 의료기관에 설명해야 합니다.'),
h('가상 예시: 오래전 진료를 받은 병원에 예약한다면')+p('D씨가 과거 방문한 의원에 비대면진료를 문의한다고 가정합니다. 오래전 방문했다는 사실만 전하지 말고, 현재 증상과 마지막 대면진료 시점, 필요한 약과 기존 처방 이력을 설명합니다. 의원은 현재 시범사업과 진료 가능 범위에 따라 확인하고, 이후 법 시행 시에는 확정된 새 기준을 다시 확인합니다.'),
h('예약 전 질문 문장')+'<blockquote>현재 시범사업 기준으로 제 상황에서 비대면진료가 가능한가요? 마지막 대면진료는 언제였고 지금 증상은 무엇인지 말씀드리겠습니다. 이번 안내가 현행 기준인지, 12월 시행을 앞둔 개정안인지 구분해 주세요. 처방이 가능하다면 약국 전달·수령도 확인하고 싶습니다.</blockquote>']),
dict(path='/treatment-costs/rare-disease-copayment-december-2026',slug='rare-copayment-december',cat='치료비',title='희귀질환 산정특례 7% 인하 예정, 12월 전에 확인할 비용과 등록',desc='희귀·중증난치질환 산정특례 본인부담 7% 인하 계획과 현재 10% 기준을 구분합니다. 비급여 제외, 등록내역 조회, 시행 전후 영수증과 실손 청구 시 확인할 항목을 정리합니다.',status='현재 10% 안내·2026년 12월 7% 인하 계획',parent='/treatment-costs/cancer-special-copayment-registration',parent_note='암 산정특례 5%와 희귀·중증난치질환의 인하 계획은 다른 대상입니다. 등록 질환과 시행 시점을 구분해 본인부담을 확인하세요.',sources=[(RARE,'보건복지부 건강보험 보장 확대 발표','2026년 12월 7%·2028년 상반기 5% 인하 계획'),(NHIS,'국민건강보험공단 산정특례 제도 안내','현행 비율·급여 적용 범위·등록 및 조회 절차')],body=[
h('7%는 인하 계획이며 현재 영수증 전체에 적용하는 비율이 아닙니다')+p(a(RARE,'보건복지부의 2026년 9월 발표')+'는 희귀·중증난치질환 산정특례 본인부담률을 현재 10%에서 12월 7%로 낮추고, 2028년 상반기에 5%로 추가 인하할 계획을 설명합니다. 10월 진료비를 지금부터 7%로 계산하거나 이미 시행된 할인처럼 받아들이면 안 됩니다.')+p(a(NHIS,'공단의 현행 제도 안내')+'는 희귀질환·중증난치질환 10%, 암 5%를 구분합니다. 같은 산정특례라는 이름이어도 대상 질환과 적용 범위가 다릅니다. 12월의 정확한 적용일·대상·세부 시행 기준은 시행 안내와 병원 원무팀에 다시 확인하세요.'),
h('진료비 총액에 7%를 곱하면 틀릴 수 있습니다')+table(['영수증 항목','확인할 내용'],[['특례 대상 급여','등록 질환과 관련된 적용 대상 급여인지'],['다른 질환 진료','등록 질환과 관계없는 진료가 섞였는지'],['비급여·전액본인부담·선별급여','특례 비율을 그대로 곱할 대상인지 구분'],['본인 결제금액','공적 지원·환급 등을 포함해 실제 부담한 항목 대조']])+p('산정특례는 등록된 질환 진료와 의학적 인과관계가 명확한 합병증 등의 적용 범위를 확인하는 제도입니다. 모든 질환이나 비급여 비용에 일괄 적용되지 않습니다. 치료를 미루거나 비급여 치료를 선택하는 근거로 예정 비율만 사용하지 마세요.'),
h('지금 할 일은 등록 상태를 확인하는 것입니다')+p('공단 홈페이지의 산정특례등록내역조회 또는 건강보험 25시 앱에서 본인인증 뒤 등록 내역을 확인할 수 있습니다. 질환·적용기간을 먼저 적어 두고 종료가 가까우면 주치의와 재등록 필요성을 상담하세요. 병원 접수창구에 등록 상태가 반영되어 있는지도 확인합니다.')+p('새로 등록해야 하는 상황이라면 진단확정과 등록 요건을 의료기관에서 확인하고 등록신청서 접수 절차를 진행해야 합니다. 이번 비율 인하 계획이 진단확정·등록 신청을 모두 대신하는 것은 아닙니다.'),
h('가상 계산: 같은 적용 대상 급여 100만 원을 비교한다면')+p('설명을 위해 전액이 산정특례 적용 대상 급여인 요양급여비용 100만 원을 가정합니다. 10%일 때의 본인부담은 10만 원, 향후 같은 범위에 7%가 적용된다면 7만 원으로 차이는 3만 원입니다. 차이는 3%포인트이며, 이 적용 대상 본인부담만 비교하면 30% 감소입니다. 실제 병원 결제 총액이 30% 줄어든다는 뜻은 아닙니다.')+p('비급여나 특례 제외 항목이 섞이면 위 계산과 달라집니다. 입원처럼 진료기간이 시행 전후에 걸친 경우에는 결제일만 보고 하나의 비율을 적용하지 말고, 병원이 어떤 진료기간·항목에 어떤 기준을 적용했는지 확인해야 합니다.'),
h('실손보험과 산정특례는 따로 정산합니다')+p('건강보험이 부담한 금액을 본인이 지출한 의료비처럼 실손에 청구하지 않습니다. 실손 청구는 실제 부담액과 가입 세대·약관·자기부담금·제외 항목을 확인하는 절차입니다. 인하 전 영수증을 임의로 고치거나 예정 비율로 다시 계산해 제출하지 말고 병원 발급 자료를 사용하세요.')+p('암에 관한 등록 안내는 '+a('/treatment-costs/cancer-special-copayment-registration','암 산정특례 등록과 소급 적용 안내')+'로 구분해 볼 수 있습니다. 암의 5%와 희귀질환의 7% 인하 계획을 섞지 않는 것이 핵심입니다.'),
h('시행 전후 원무팀에 이렇게 물어보세요')+'<blockquote>제 등록 질환과 적용기간을 확인하고 싶습니다. 이번 진료 중 산정특례 적용 급여와 제외 항목을 나눠 주세요. 12월 인하가 실제 시행되면 어느 진료일부터 어떤 항목에 적용되는지, 정산이나 추가 확인이 필요한지도 알려 주세요.</blockquote>'])]

CSS='''.trend5 h1{font-size:clamp(1.7rem,3vw,2.35rem);line-height:1.4;word-break:keep-all;overflow-wrap:anywhere}.trend5 p,.trend5 li{line-height:1.85}.trend5 h2{line-height:1.5;margin-top:2rem;word-break:keep-all}.trend5 .status-note{padding:16px;border-left:4px solid #1963b5;background:#edf4ff;line-height:1.8}.trend5 .trend-table{overflow-x:auto;max-width:100%;margin:20px 0}.trend5 table{width:100%;min-width:510px;border-collapse:collapse}.trend5 th,.trend5 td{padding:12px;text-align:left;vertical-align:top;border:1px solid #d5dfeb}.trend5 th{background:#edf3fa}.trend5 figure{margin:24px 0}.trend5 figure img{width:100%;height:auto;display:block;border-radius:12px}.trend5 figcaption{font-size:.85rem;color:#5b6879;margin-top:8px}.trend5 blockquote{margin:20px 0;padding:16px 20px;border-left:4px solid #1963b5;background:#f3f7fb;line-height:1.85}.trend5 a{overflow-wrap:anywhere}.trend5 .official-guide-button{min-height:48px}@media(max-width:520px){.trend5 h2{font-size:1.3rem}.trend5 th,.trend5 td{padding:10px;font-size:.94rem}.trend5 .lead{font-size:1.03rem}.trend5 .status-note{padding:12px}}'''

DATA[0]['sources'].append(('https://www.silson24.or.kr/claim/web/custSupp/custSuppFAQ?postNo=25840','실손24 접수·심사·지급 현황 FAQ','보험사 전송 뒤 진행 상태는 해당 보험사 홈페이지·앱에서 확인'))

def image(d,key,alt):
    src='/assets/images/'+d['slug']+'-'+key+'.webp'
    with Image.open(ROOT/src[1:]) as im: w,hh=im.size
    return f'<figure><img src="{src}" alt="{alt}" width="{w}" height="{hh}" loading="{"eager" if key=="thumb" else "lazy"}" decoding="async"/>'+('<figcaption>AI로 만든 설명용 장면이며 실제 환자·진료기록이나 공식 앱 화면이 아닙니다.</figcaption>' if key=='thumb' else '')+'</figure>'

def publish(i):
    d=DATA[i-1]; dest=ROOT/(d['path'][1:]+'.html')
    if dest.exists(): raise SystemExit('Already exists: '+str(dest))
    soup=BeautifulSoup((ROOT/'surgery-benefit/wound-suture-specific-rider.html').read_text(encoding='utf-8'),'html.parser')
    soup.title.string=d['title']
    for attr,key,val in [('name','description',d['desc']),('property','og:title',d['title']),('property','og:description',d['desc']),('property','og:image',BASE+'/assets/images/'+d['slug']+'-thumb.webp')]:soup.find('meta',attrs={attr:key})['content']=val
    soup.find('link',rel='canonical')['href']=BASE+d['path']
    og=soup.new_tag('meta',attrs={'property':'og:url','content':BASE+d['path']});soup.head.append(og)
    style=soup.new_tag('style');style.string=CSS;soup.head.append(style)
    schema=json.loads(soup.find('script',type='application/ld+json').string);schema.update(headline=d['title'],description=d['desc'],image=BASE+'/assets/images/'+d['slug']+'-thumb.webp',mainEntityOfPage=BASE+d['path'],datePublished=DATE,dateModified=DATE);soup.find('script',type='application/ld+json').string=json.dumps(schema,ensure_ascii=False)
    main=soup.main;cta=str(main.find('section',class_='kakao-inquiry-cta'));main.clear();main['class']=['section','article-body','insurance-series-article','cluster-reading','trend5']
    section=d['path'].split('/')[1]
    text=f'<div class="breadcrumb"><a href="/">홈</a> / <a href="/{section}/">{d["cat"]}</a></div><h1>{d["title"]}</h1><p class="lead">{d["desc"]}</p><div class="status-note"><strong>제도 진행 단계</strong><br>{d["status"]}</div>'
    text+=image(d,'thumb',d['title']+' 설명용 대표 이미지')
    if i==1:text+='<p><a href="/insurance-companies/">보험사별 공식 홈페이지 확인하기</a></p>'
    for n,part in enumerate(d['body']):
        text+=part
        if n==1:text+=image(d,'body1',['','모바일 청구 자료를 확인하는 설명 장면','전원과 돌봄 계획을 상담하는 설명 장면','예정된 환자 이송을 상담하는 설명 장면','진료 이력과 예약 정보를 준비하는 설명 장면','진료비 항목과 등록 상태를 상담하는 설명 장면'][i])
        if n==3:text+=image(d,'body2',['','청구 전송 뒤 접수 정보를 정리하는 설명 장면','입원 상담 자료를 준비하는 보호자 설명 장면','이송 장비와 운행 준비를 확인하는 설명 장면','처방전과 약 수령 절차를 상담하는 설명 장면','산정특례 등록 내역과 적용기간을 확인하는 설명 장면'][i])
    text+='<section class="official-guide-actions"><h2>공식 확인처와 상세 안내</h2><div class="official-guide-grid">'
    for url,title,scope in d['sources']:text+=f'<a class="official-guide-button" href="{url}" target="_blank" rel="noopener"><strong>{title}</strong><span>{scope} · 새 창 ↗</span></a>'
    text+='</div></section><p>작성: 케어로컬 사이트 운영자. '+a('/legal/about','작성 기준과 운영자 역할')+'을 확인할 수 있습니다. 제도 안내는 개인의 진료·입원 적합성이나 보험금 지급을 판정하지 않습니다.</p><div class="insurance-company-cta"><a href="/insurance-companies/">보험사별 공식 홈페이지 확인하기</a></div>'+cta
    main.append(BeautifulSoup(text,'html.parser'));dest.write_text(str(soup)+'\n',encoding='utf-8')
    parent=ROOT/(d['parent'][1:]+'.html');raw=parent.read_text(encoding='utf-8');(OUT/(parent.stem+'-before.html')).write_text(raw,encoding='utf-8');ps=BeautifulSoup(raw,'html.parser')
    block=BeautifulSoup('<aside class="notice" id="trend5-related"><strong>함께 확인할 다음 절차</strong><p>'+d['parent_note']+' '+a(d['path'],d['title'])+'</p></aside>','html.parser')
    anchor=ps.main.find('section',class_='official-guide-actions')
    if anchor:anchor.insert_before(block)
    else:ps.main.append(block)
    for script in ps.find_all('script',type='application/ld+json'):
        try:o=json.loads(script.string);o['dateModified']=DATE;script.string=json.dumps(o,ensure_ascii=False)
        except (ValueError,TypeError):pass
    parent.write_text(str(ps)+'\n',encoding='utf-8')
    idx=ROOT/section/'index.html';cs=BeautifulSoup(idx.read_text(encoding='utf-8'),'html.parser');(cs.main or cs.body).append(BeautifulSoup('<section class="section"><h2>제도와 이용 절차</h2><p>'+a(d['path'],d['title'])+'</p></section>','html.parser'));idx.write_text(str(cs)+'\n',encoding='utf-8')
    sm=ROOT/'sitemap.xml';raw=sm.read_text(encoding='utf-8');raw=raw.replace('</urlset>',f'  <url><loc>{BASE+d["path"]}</loc><lastmod>{DATE}</lastmod></url>\n</urlset>');raw=re.sub(r'(<loc>'+re.escape(BASE+d['parent'])+r'</loc>\s*<lastmod>)[^<]+',r'\g<1>'+DATE,raw);sm.write_text(raw,encoding='utf-8')
    subprocess.run([sys.executable,str(ROOT/'scripts/build-article-catalog.py')],check=True)
    (OUT/'manifest.json').write_text(json.dumps([{k:v for k,v in x.items() if k!='body'} for x in DATA],ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'article':str(dest.relative_to(ROOT)),'parent':str(parent.relative_to(ROOT)),'category':str(idx.relative_to(ROOT))},ensure_ascii=False))

if __name__=='__main__':publish(int(sys.argv[1]))
