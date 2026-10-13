# 최근 30편 품질 검토 및 공식 버튼 보완 — 2026-10-13

## 범위와 결과

Git의 신규 HTML 발행 커밋을 역순으로 추적한 최근 30편. 사이트 전체 카탈로그는 267편이며 이번 작업은 신규 발행이 아닌 기존 글 보완이다.

- 30편에 주제별 공식 상세 안내 버튼 32개. 새 창 및 PDF·기관·지역 범위 표시.
- 치아·해외진료·환불·계좌 글 10편의 공통 체크리스트를 상황별 질문·서류·예시로 교체.
- 무릎 지원기관의 2026-07-16 예산 소진 관련 신규 접수 사전 종료 공지를 반영. 현재 재개를 추정하지 않음.
- 전동휠체어의 접속 실패 출처를 공단 부담금액 상세 안내로 대체. 보청기 출처의 오래된 보조자료를 공단 지급 절차로 교체.
- 보험사 제출서류 안내가 환불 정산·심사 중 계좌 변경·재치료 보장 규칙 자체의 근거는 아니라는 한계를 명시.
- 제목·발행일·90개 기존 이미지·카카오 문의 블록 보존 검사 30/30 통과.

## 검증 방법과 한계

- 공식 공개 원문과 본문의 핵심 수치·대상·서류·절차를 대조. 지역 조건을 전국 조건으로 전용하지 않았는지 확인.
- 출처 40개 최초 HTTP 검사 중 39개 응답 성공. 부산시 URL은 연결 실패하여 활성 본문에서 교체. 복지로는 HTTP 200만으로 판단하지 않고 Chrome에서 2026 서비스 본문과 선정기준을 확인. 추가 공단 대체 출처는 별도 라이브 확인.
- 틀니 65세·30%·7년, 복지용구 160만원·15%·감경 6/9%, 산소기 12/20만원·90%, 양압기 90일·30일 중21일·4시간(12세 이하3시간)·지원50/80%, 서울대병원 영상 CD/DVD 1/2만원을 해당 기관 원문과 대조.
- 동일한 제목 변형만으로 같은 답을 반복하는지 검토. 특히 보청기/전동휠체어, 센서/소모품, 임플란트 서류/청구 날짜, 병원비 정정/지급 후 환불은 다른 절차를 다루도록 구분. 제목 문자열 유사도는 후보 탐색에만 사용하고 중복 판정 근거로 단독 사용하지 않음.
- 360·390·1280px Chrome 실제 렌더링 90건: 가로 넘침, 이미지 로드, 버튼 화면 범위·최소48px 높이 확인. 모바일 스크린샷 시각 확인.
- 렌더링 검사는 광고 네트워크 요청을 제외한 편집 콘텐츠 기준. 개인화·자동광고 배치는 이번 검증 범위에 포함하지 않음. 보험금·지원 승인 또는 검색 색인·순위·수익을 보장하는 검토가 아님.

## 글별 검토 범위

|번호|글|구분한 핵심 질문|보완|
|---|---|---|---|
|1|[복막투석 소모성재료 요양비, 처방전·등록업소·청구서류 확인](https://hospital.hbuby.com/treatment-costs/peritoneal-dialysis-supplies-reimbursement)|복막투석 관류액·자동투석 재료 요양비|상세 안내 버튼|
|2|[노인 눈수술비 지원, 백내장 수술 전에 신청·선정 순서 확인](https://hospital.hbuby.com/treatment-costs/senior-eye-surgery-cost-aid-application)|공공 눈수술 지원의 신청·선정 순서|상세 안내 버튼|
|3|[무릎 인공관절 수술비 지원, 수술 전에 보건소에 신청해야 할까?](https://hospital.hbuby.com/treatment-costs/senior-knee-surgery-aid-before-operation)|공공 무릎수술 지원과 지자체 자체사업|상세 안내 버튼·접수 종료 공지|
|4|[치매검사비 지원 신청, 병원 예약 전에 치매안심센터 의뢰 확인](https://hospital.hbuby.com/treatment-costs/dementia-test-cost-support-referral)|검사비 지원과 센터 의뢰|상세 안내 버튼|
|5|[복지용구 지원 신청, 연 160만원 한도와 구입·대여 비용 확인](https://hospital.hbuby.com/caregiver/longterm-care-welfare-equipment-limit)|장기요양 복지용구 구입·대여 한도|상세 안내 버튼|
|6|[전동휠체어 건강보험 지원, 구입 전 급여 승인부터 확인하세요](https://hospital.hbuby.com/treatment-costs/powered-wheelchair-insurance-preapproval)|장애인 전동휠체어 사전 승인|상세 안내 버튼·불안정 출처 대체|
|7|[연속혈당측정기 건강보험, 기기와 센서 지원을 따로 확인하세요](https://hospital.hbuby.com/treatment-costs/continuous-glucose-monitor-device-sensor-support)|연속혈당측정 기기와 센서 분리|상세 안내 버튼|
|8|[당뇨 소모품 지원 신청, 혈당검사지·채혈침 구입 전 확인할 서류](https://hospital.hbuby.com/treatment-costs/diabetes-consumables-reimbursement-documents)|당뇨 소모품 처방·구입 증빙|상세 안내 버튼|
|9|[틀니 건강보험 적용, 65세·등록·7년 기준과 본인부담 확인](https://hospital.hbuby.com/treatment-costs/denture-insurance-registration-cost)|틀니 등록·제작·유지관리|상세 안내 버튼|
|10|[보청기 지원금 신청, 구입 전에 장애등록·처방·급여제품을 확인하세요](https://hospital.hbuby.com/treatment-costs/hearing-aid-subsidy-before-purchase)|보청기 건강보험과 지역 지원 구분|상세 안내 버튼|
|11|[퇴원 후 가정간호 신청, 상처 소독·관 관리가 필요하면 퇴원 전에 확인](https://hospital.hbuby.com/guides/home-nursing-before-discharge)|의사 처방에 따른 가정간호 의뢰|상세 안내 버튼|
|12|[퇴원 후 휠체어 무료대여, 주민센터·보건소에 전화하기 전 준비](https://hospital.hbuby.com/guides/temporary-wheelchair-free-rental)|단기 무료대여와 구입 지원 구분|상세 안내 버튼|
|13|[가정 산소치료기 대여비 지원, 처방전과 요양비 청구서류 확인](https://hospital.hbuby.com/treatment-costs/home-oxygen-rental-reimbursement)|산소기 대여료 요양비|상세 안내 버튼|
|14|[양압기 건강보험 신청, 등록·처방전·순응기간을 먼저 확인하세요](https://hospital.hbuby.com/treatment-costs/cpap-insurance-registration-adherence)|양압기 등록·순응기간·사용기록|상세 안내 버튼|
|15|[간호·간병통합서비스 비용, 입원 전에 병원과 보험사에 확인할 항목](https://hospital.hbuby.com/caregiver/integrated-nursing-care-cost-check)|통합병동 비용과 개인간병 담보 구분|상세 안내 버튼|
|16|[진단서 인터넷 발급, 처음 받는 진단서와 사본 재발급은 다릅니다](https://hospital.hbuby.com/claims/medical-certificate-online-first-issue)|진단서 최초 작성과 사본 재발급|상세 안내 버튼|
|17|[처방전 분실 재발급 비용, 약을 잃어버린 경우와 어떻게 다를까?](https://hospital.hbuby.com/guides/lost-prescription-reissue-cost)|처방전만 분실·만료·조제약 분실 구분|상세 안내 버튼|
|18|[병리 슬라이드 대출, 조직검사 결과지와 다른 점·비용·반납 확인](https://hospital.hbuby.com/guides/pathology-slide-loan-return)|슬라이드 재판독 자료 대출·반납|상세 안내 버튼|
|19|[폐업한 병원 진료기록 발급, 포털에서 안 나오면 어디에 문의할까?](https://hospital.hbuby.com/claims/closed-hospital-records-request)|폐업 후 진료기록 보관처 추적|상세 안내 버튼|
|20|[CT·MRI 영상 CD 발급, 다른 병원에 갈 때 판독지도 필요할까?](https://hospital.hbuby.com/guides/ct-mri-image-cd-transfer)|전원용 영상·판독지·매체 발급|상세 안내 버튼|
|21|[보험금 받은 뒤 병원비를 환불받으면 어떻게 할까?](https://hospital.hbuby.com/silbi/hospital-bill-correction-silbi-claim)|지급 후 병원비 환불 정산|상세 안내 버튼·상황별 체크리스트|
|22|[보험금 심사 중 지급 계좌를 바꿀 수 있을까?](https://hospital.hbuby.com/claims/insurance-claim-bank-account-change)|기존 청구 건의 지급 계좌 변경|상세 안내 버튼·상황별 체크리스트|
|23|[귀국 후 같은 증상으로 국내 병원에 갔다면 어디에 청구할까?](https://hospital.hbuby.com/silbi/post-travel-domestic-followup-silbi)|귀국 후 국내 치료와 해외 비용 분리|상세 안내 버튼·상황별 체크리스트|
|24|[해외 진료서에 진단명이 빠져 있다면 어떻게 할까?](https://hospital.hbuby.com/claims/overseas-medical-note-diagnosis-claim)|현지 진료서의 누락 내용 보완|상세 안내 버튼·상황별 체크리스트|
|25|[해외 약국에서 약을 샀다면 어떤 서류가 필요할까?](https://hospital.hbuby.com/claims/overseas-pharmacy-prescription-claim)|해외 약국 처방·구입 증빙|상세 안내 버튼·상황별 체크리스트|
|26|[해외 병원비 카드 전표만으로 청구할 수 있을까?](https://hospital.hbuby.com/claims/overseas-hospital-card-slip-insurance)|카드 전표와 병원 발급 내역 구분|상세 안내 버튼·상황별 체크리스트|
|27|[같은 치아를 다시 치료했다면 보험금을 또 청구할 수 있을까?](https://hospital.hbuby.com/claims/same-tooth-repeat-dental-treatment-claim)|동일 치아 재치료·이전 지급 이력|상세 안내 버튼·상황별 체크리스트|
|28|[발치는 먼저, 임플란트는 나중에 했다면 언제 청구할까?](https://hospital.hbuby.com/claims/dental-extraction-implant-dates)|발치·식립·보철 날짜와 청구 단계|상세 안내 버튼·상황별 체크리스트|
|29|[크라운 치료를 받았다면 치아보험에 무엇을 제출할까?](https://hospital.hbuby.com/claims/dental-crown-insurance-claim-documents)|크라운 치아번호·재료·치료 서류|상세 안내 버튼·상황별 체크리스트|
|30|[임플란트 보험금 청구 전에 무엇을 확인할까?](https://hospital.hbuby.com/claims/dental-implant-insurance-claim-documents)|임플란트 발거·보철 자료|상세 안내 버튼·상황별 체크리스트|

## 증거 파일

- `OFFICIAL_BUTTONS_2026-10-13.json`: 30편 버튼 문구·URL 대응표
- `QUALITY_30_SOURCES_2026-10-13.json`: 출처 응답·예외 처리
- `QUALITY_30_LOCAL_2026-10-13.json`: 90개 로컬 화면 검사
- 공개 배포 후 `QUALITY_30_PUBLIC_2026-10-13.json`으로 실제 반영 검사 기록 예정.
