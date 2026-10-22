# 후속 세부 소재 5편 발행 결과 — 2026-10-22

## 발행 완료

승인된 최신 계획의 순서로 각 글을 개별 커밋·배포했다. 각 글의 공개 head/main 일치 확인 후 다음 글을 발행했다.

| 순서 | 글 | 발행 커밋 |
|---|---|---|
|1|[입원 지참약 관리](https://hospital.hbuby.com/guides/inpatient-personal-medicine-handover)|ab3c58e|
|2|[MRI 전 약물패치](https://hospital.hbuby.com/guides/mri-transdermal-patch-check)|1a60568|
|3|[퇴원 후 방문재활](https://hospital.hbuby.com/guides/postdischarge-home-rehabilitation-consultation)|1ae31d5|
|4|[조영제 부작용 피해구제](https://hospital.hbuby.com/claims/contrast-adverse-reaction-relief-documents)|281b0a0|
|5|[병원 환불 내용증명 반송](https://hospital.hbuby.com/treatment-costs/hospital-refund-notice-delivery-records)|cc8999d|

각 글에 준비 표, 체크리스트, 가상 예시, 문의 문장, 공식 원문 버튼과 설명용 생성 이미지 3개를 포함했다. 2번은 안전 확인과 실손 적용을 분리했고, 5번은 현행 카드사 안내의 최초 할부 조건·잔여대금·불이행·제외 거래를 확인했다. 상세 근거는 source-review.md에 기록했다.

## 기존 글 연결

기존 글 10편에 문맥 설명과 신규 글 링크를 각각 1개 추가했다. 신규 글에서도 관련 기존 글로 이동한다. 기존 main 본문은 새 연결 섹션을 제거한 뒤 공백 정규화 텍스트가 백업과 동일한지 10편 모두 확인했다(parent-preservation.json). 원래 정보를 삭제하거나 별도 개편하지 않았다.

## 검증

- 발행마다 pnpm run check 통과: 내부링크·canonical·카탈로그·정규 URL 단위검사·분석 스크립트 검사.
- 신규5 + 수정10 공개 페이지: HTTP200, 정확한 head/main, 자기 canonical, noindex 없음 확인.
- 공개 이미지 URL45개 정상 응답. 신규 생성 이미지15개는 assets/images/의 각 슬러그-thumb/body1/body2.webp에 저장했다. 원본은 생성 폴더에 남겼다. 정확한 프롬프트는 image-prompts.json에 보관했다.
- 실제 너비360/390/1280px: 신규 로컬15회, 신규 공개15회, 기존 공개30회, 합계60회 검사. viewport 실제값·가로넘침·신규 이미지3개 로딩 확인. 390px 표의 카드형 표시와 한글 이미지를 직접 확인했다(local-qa.json 및 PNG).
- 마지막 검수 중 한 탭의 일시적 연결 종료가 있었으나 새 탭과 새 검사 함수로 복구했다. 이전 탭에 묶인 함수 결과를 사용하지 않았고, 남은 검사도 실제 크기로 완료했다.
- 카탈로그402편, 사이트맵427 URL. 이 수치는 발행·등재 수이며 색인 수가 아니다.

## 네이버 — 접수 미완료

오늘 앞선 배치에서 `사이트별 일간 최대 요청 수를 초과하였습니다.` 최종 응답을 이미 확인했다. 근거는 ../next-followup5b-publication-2026-10-22/naver-quota-exceeded.txt 및 같은 폴더의 naver-request-status.json이다. 같은 날 반복 요청을 하지 않았다.

이번 신규·수정15 URL과 이전 대기6 URL을 합쳐 중복4개를 제거했고 **총17 URL 대기**로 저장했다. 이번 작업에서 새로 접수한 URL은0개다. 이 목록은 미색인 확정 목록이 아니라 최신 변경 내용의 수집 요청을 기다리는 목록이다. 한도가 풀린 후 기존 접수 이력·현재 상태를 대조해 필요한 URL만 요청해야 한다. 접수와 실제 수집·색인 완료는 구분한다.

- naver-request-pending.txt: 중복 제거된 전체17개
- naver-request-status.json: 미접수 사유·기존 증거·각 URL
- final-public-audit.json: 제출 대상 공개 응답 검증

## 작업 경계

기존 docs/POSTING_GUIDELINES.md 변경은 보존하고 이번 커밋에서 제외했다. 광고·다른 사이트·자동화 설정은 변경하지 않았다. 외부 원문 HTML은 내부 검사가 사이트 페이지로 오인하지 않도록 .source 확장자로 보관했으며 공개 배포에 넣지 않았다. 공개 사이트의 기존 AdSense 자동광고 예약 공간은 이번 글 배포 범위에서 별도로 바꾸지 않았다.
