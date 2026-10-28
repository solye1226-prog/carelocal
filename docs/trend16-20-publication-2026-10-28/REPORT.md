# 16~20번 순차 발행 및 네이버 수집 요청 결과

작업일: 2026-10-28 (Asia/Seoul). 신규 5편 공개, 기존 5편 내부링크 추가, 이번 대상 10개 URL의 네이버 요청 접수 완료. 접수는 실제 수집·색인 완료를 뜻하지 않는다.

## 발행 및 시행 상태

|순서|공개 글|근거 확인 결과|
|---|---|---|
|16|[자가도뇨카테터 요양비, 현재 기준과 12월 확대 계획 비교](https://hospital.hbuby.com/treatment-costs/urinary-catheter-reimbursement-update)|현행 지원 운영 중·확대안은 2026년 12월 추진 일정으로 발표|
|17|[당원병 혈당검사지·연속혈당센서 지원, 2027년 시행 계획 확인](https://hospital.hbuby.com/treatment-costs/glycogen-storage-glucose-supplies-support)|요양비는 2027년 2분기 예정·질병관리청 본인부담 지원은 별도 지침·시스템 준비|
|18|[레테브모 급여, RET 융합 폐암과 RET 변이 갑상선 수질암 차이](https://hospital.hbuby.com/treatment-costs/retevmo-ret-test-coverage)|2026년 10월 1일 급여기준 시행·암종별 검사·진행 상태와 과거 치료 대조|
|19|[리브델지 허가, 원발성 담즙성 담관염 약값·보험 확인 순서](https://hospital.hbuby.com/treatment-costs/livdelzi-approval-coverage-check)|2026년 10월 20일 국내 품목허가 확인·공급·약가·개인 급여는 별도 확인|
|20|[퀸락정 리프레티닙 허가, GIST 4차 치료와 급여 확인법](https://hospital.hbuby.com/treatment-costs/qinlock-ripretinib-coverage-check)|2026년 10월 16일 국내 허가 확인·급여·공급·실제 약값은 별도 확인|

## 기존 글 연결

- https://hospital.hbuby.com/claims/medical-expense-claim-documents → https://hospital.hbuby.com/treatment-costs/urinary-catheter-reimbursement-update
- https://hospital.hbuby.com/treatment-costs/diabetes-consumables-reimbursement-documents → https://hospital.hbuby.com/treatment-costs/glycogen-storage-glucose-supplies-support
- https://hospital.hbuby.com/guides/targeted-immunotherapy → https://hospital.hbuby.com/treatment-costs/retevmo-ret-test-coverage
- https://hospital.hbuby.com/silbi/pharmacy-prescription-claim → https://hospital.hbuby.com/treatment-costs/livdelzi-approval-coverage-check
- https://hospital.hbuby.com/guides/cancer-treatment-cost → https://hospital.hbuby.com/treatment-costs/qinlock-ripretinib-coverage-check

각 새 글에서도 관련 기존 글로 돌아가는 링크를 넣었다. 부모 글은 추가 안내 블록을 제거한 뒤 이전 main 본문 텍스트와 동일함을 대조했다. 리브델지는 암 치료가 아닌 성인 PBC 약제이므로 기획안의 표적항암 부모글 대신 처방약 실비 청구 글로 연결했다.

## 근거와 검증 범위

- 자가도뇨: 공단 현행 안내와 정부 추진계획 원문 7·15쪽을 분리. 확대안은 12월 추진 일정이며 시행 완료로 쓰지 않았다.
- 당원병: 정부 추진계획 및 질병관리청 9.9 원문·PDF 2쪽 도표 확인. 요양비 2027년 2분기 예정과 별도 본인부담 지원사업의 지침·시스템 준비를 구분.
- 레테브모: 심평원 2026-210호 10.1 시행 공고 및 보존한 원문 HWP 폐암·갑상선암 항목/주석 재확인.
- 리브델지·퀸락정: 식약처 품목 202603207·202603180 원문 확인. 국내 공급일·확정 약가·개인 급여를 확인하지 못한 부분은 미확정으로 남겼다. 허가를 급여 완료 또는 비급여 확정으로 표현하지 않았다.
- 자세한 판단과 접근 제한은 [EDITORIAL_NOTES.md](EDITORIAL_NOTES.md), [source-review.json](source-review.json).

## 품질 검수

- 공개 신규 5편의 main 본문·self canonical이 로컬과 일치. 이미지 15개 HTTP 200, 양방향 링크 확인, 기존 본문 보존 확인.
- 신규 5편을 로컬·공개 각각 360/390/1280px로 확인(30개 화면 폭 검수). 본문 폭 PC 최대 800px, 이미지 로딩 및 제목 1개, 측정 시 문서 가로 넘침 없음.
- 모바일 카드 표에서 열 이름이 사라지던 문제를 발견해 5편 모두 항목명 표시 및 min-width를 수정했다.
- 관련 기존 5편은 공개 390/1280px에서 추가 링크 표시와 넘침 여부 확인(10개 검수).
- 공개 페이지의 자동 광고는 로딩 후 스크롤 위치·빈 공간 등이 변할 수 있어 대표 첫 화면을 다시 촬영했다. 광고 설정은 변경하지 않았다.
- pnpm run check 통과: HTML 751개 내부링크, sitemap 482개 canonical, Python 5개, Node 10개. 카탈로그 457편.
- 이미지생성 스킬의 기본 내장 도구로 15개 개별 생성. WebP 자산은 assets/images/ 각 글 slug-thumb/body1/body2.webp. 프롬프트와 원본 경로는 [image-sources.json](image-sources.json).
- 공개 화면: [모바일 5편](public-mobile-contact-sheet.jpg). 개별 local/public/parent PNG와 JSON도 같은 폴더에 보관.

## 네이버 접수 결과

|대상|URL|최종 등록일|
|---|---|---|
|신규|https://hospital.hbuby.com/treatment-costs/urinary-catheter-reimbursement-update|26.10.28 13:05:07|
|신규|https://hospital.hbuby.com/treatment-costs/glycogen-storage-glucose-supplies-support|26.10.28 13:05:19|
|신규|https://hospital.hbuby.com/treatment-costs/retevmo-ret-test-coverage|26.10.28 13:05:32|
|신규|https://hospital.hbuby.com/treatment-costs/livdelzi-approval-coverage-check|26.10.28 13:05:46|
|신규|https://hospital.hbuby.com/treatment-costs/qinlock-ripretinib-coverage-check|26.10.28 13:06:10|
|기존 링크 보완|https://hospital.hbuby.com/claims/medical-expense-claim-documents|26.10.28 13:06:24|
|기존 링크 보완|https://hospital.hbuby.com/treatment-costs/diabetes-consumables-reimbursement-documents|26.10.28 13:07:02|
|기존 링크 보완|https://hospital.hbuby.com/guides/targeted-immunotherapy|26.10.28 13:07:14|
|기존 링크 보완|https://hospital.hbuby.com/silbi/pharmacy-prescription-claim|26.10.28 13:07:29|
|기존 링크 보완|https://hospital.hbuby.com/guides/cancer-treatment-cost|26.10.28 13:07:51|

- 10개 모두 최종 새 접수행과 등록일을 확인한 뒤 다음 URL로 진행했다.
- 이번 10개 요청: 접수 10 / 미시도 0 / 오류·한도·로그인 중단 0 / 남은 0.
- 기존 처방약 글 등 오늘 앞서 요청됐던 URL도 이번 작업에서 새 내부링크로 다시 변경됐으므로, 변경 이후 등록행을 새로 확인했다.
- [최종 접수 화면](naver-all10-accepted.png), [결과 원장](naver-results.json), [이번 작업 대기 목록](naver-pending.txt).
- Naver 색인 완료 수는 이번 작업에서 확인하지 않았으며, 요청 접수 수와 혼동하지 않는다. 이전 별도 작업의 대기 목록·Google 자동화·광고 설정은 이번 범위가 아니다.

## Git

- 16: b2a16b9, 모바일 표 보완 e2d54e1
- 17: 7b0cc98
- 18: 735674a
- 19: 38641b6
- 20: b997b32
- 각 글을 순서대로 push하고 이전 글의 공개 반영을 확인한 뒤 다음 글을 push했다. 사용자 기존 docs/POSTING_GUIDELINES.md 변경과 다른 미추적 파일은 보존했다.
