# 발행・검수 결과 (2026-10-22)

승인된 5개 소재를 순차 발행하고 기존 글 10편에 문맥별 내부링크를 추가했다. 새 글에서 관련 기존 글로도 연결했다.

1. [퇴원 후 남은 약, 어디에 버릴까? 폐의약품 수거함·물약 배출 확인](https://hospital.hbuby.com/guides/unused-prescription-medicine-disposal)
2. [연속혈당측정기·인슐린펌프 착용 중 MRI, 검사 전에 무엇을 확인할까?](https://hospital.hbuby.com/guides/mri-cgm-insulin-pump-preparation)
3. [방문간호지시서 발급, 퇴원 소견서와 무엇이 다를까? 준비서류·비용 확인](https://hospital.hbuby.com/guides/longtermcare-home-nursing-order-documents)
4. [조영제 이상반응, 환자도 직접 보고할 수 있을까? 신고 전 준비할 정보](https://hospital.hbuby.com/guides/patient-drug-adverse-event-report)
5. [병원 폐업 환불, 소비자원에 접수하면 될까? 연락두절·피해구제 제외 사유](https://hospital.hbuby.com/treatment-costs/closed-hospital-consumer-relief-eligibility)

## 공식 근거와 표현

2번은 한국어 Dexcom G7 설명서와 제조사 펌프 안내의 해당 모델 조건을 확인했다. MRI 비용, 센서 교체 비용, 요양비, 제조사 교체를 구분하고 실비 지급을 단정하지 않았다. 5번은 소비자원 피해구제 제외 사유와 KB국민카드의 할부 항변 요건·제외 거래를 각각 대조했다. 최초 20만원 이상·3개월 이상 할부·잔여대금 등의 조건과 개별 계약 확인 필요성을 명시했다. 자세한 URL과 확인 범위는 source-review.md에 기록했다.

## 공개 검증

15페이지의 HTTP 200, 로컬과 실제 공개 head/main 일치, canonical/noindex, 이미지 45개 주소를 확인했다. 새 글 로컬/공개 및 기존 글 공개에서 360·390·1280px 총 60개 최신 검사를 모두 통과했다. 기존 글 본문은 추가 링크 구간을 제외하고 보존됐다. 사이트 링크·canonical·카탈로그·단위검사도 통과했다.

검수 중 4번 이미지가 일시 로드되지 않아 재검사했고 세 화면 크기 모두 정상 로드를 확인했다. 4번 배포에 5번 발견 목록이 먼저 포함된 문제는 즉시 별도 수정 커밋 7eb0628로 해소했다. 이후 5번 본문·이미지·발견 목록을 함께 정식 배포했으며 최종 공개 검증에서 일치했다.

## 네이버 수집 요청

오늘 앞선 작업의 사이트 일간 한도 초과 최종 응답을 근거로 반복 제출하지 않았다. 이번 변경 URL 15개를 이전 대기 목록과 중복 제거해 24개로 정리했다. 이번 신규 접수는 0건이며, 요청 대기는 실제 미색인 확정이나 색인 완료를 뜻하지 않는다.

대기 목록: naver-request-pending.txt / 상태: naver-request-status.json / 공개 확인: final-public-audit.json / 화면 검수: local-qa.json
