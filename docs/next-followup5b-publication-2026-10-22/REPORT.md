# 후속 세부 소재 5편 발행·내부링크·네이버 요청 결과

작업일: 2026-10-22. 사이트: https://hospital.hbuby.com

## 완료 범위

- 승인된 5편을 순서대로 발행하고 각 편의 공개 본문·head가 로컬 변경과 일치하는 것을 확인했다.
- 기존 글 8편에서 새 글로 연결하는 내부링크 10개를 추가했다. 새 글은 관련 기존 글로도 연결한다.
- 기존 8편 본문은 새 연결 문단을 제외하면 원문이 보존되었음을 대조했다(`parent-preservation.json`).
- 썸네일 5장·본문 장면 10장을 built-in image_gen으로 생성하고 최종 WebP 자산 15개를 저장했다. 프롬프트 구성·장면·검수는 `source-review.md`에 기록했다.
- 카탈로그는 392 → 397편, 사이트맵은 417 → 422개 URL이다. 이 숫자는 색인 수가 아니다.

## 순차 발행

| 순서 | 포스팅 | 발행 커밋 |
|---|---|---|
| 1 | [요양병원 입원 중 다른 병원 처방약, 어디서 받아야 할까?](https://hospital.hbuby.com/guides/nursing-hospital-referral-prescription-medicine) | `2b5e940` |
| 2 | [수면 MRI 비용·실비, 촬영료와 진정 비용은 어떻게 확인할까?](https://hospital.hbuby.com/silbi/sedation-mri-cost-claim) | `f742641` |
| 3 | [회복기 재활병원 찾기, 지정 여부와 전원 조건 확인법](https://hospital.hbuby.com/guides/recovery-rehabilitation-designation-transfer-check) | `a88f7ae` |
| 4 | [조영제 부작용 경험 후 재검사, 약물안전카드·기록 준비법](https://hospital.hbuby.com/guides/contrast-reaction-drug-safety-card) | `97aa4e3` |
| 5 | [병원 폐업 후 선납 진료비, 카드 할부금이 남았다면?](https://hospital.hbuby.com/treatment-costs/closed-hospital-prepaid-card-installment) | `6cc4531` |

## 중요한 근거 처리

- 2번: KB 공식 공개 약관 PDF의 MRI 특약을 원문·렌더링으로 확인했다. 2020년 특정 상품의 예시임을 표시하고, 그 문구만으로 별도 진정 비용의 포함·제외를 확정하지 않았다. 검사 목적·실제 항목·적용 담보·제외 조항을 구분해 문의하도록 작성했다. 일반 MRI 가격이나 전국 공통 지급률을 만들지 않았다.
- 5번: 한국소비자원의 의료기관 선납치료비 주의보와 현재 KB국민카드 안내를 대조했다. 최초 결제 조건·미이행 사유·잔액·사후 할부 전환 등 예외를 설명하고, 이미 낸 돈의 반환과 남은 대금의 항변을 구분했다. 임의 연체를 안내하지 않는다.
- 나머지 글도 심평원·복지부·식약처·대학병원 자료의 실제 적용 범위로 제한했다. 세부 근거·확인 한계는 `source-review.md`에 있다.

## 검증 결과

- 각 순차 발행의 `pnpm run check` 통과: 내부 링크·canonical·Python 검사·카탈로그 일치·Node 분석 기능 검사.
- 신규 글의 로컬 15건, 공개 15건, 수정 기존 글의 공개 24건: 실제 360·390·1280px의 고유 화면 검사 **54건 통과**. 요청 폭과 실제 `innerWidth` 일치 및 문서 가로 넘침 여부를 기록했다(`viewport-qa.json`).
- 신규 5편은 실제 스크롤로 지연 이미지를 로드해 확인했다. 모바일 표의 카드 전환과 한글 제목·표·문의 문안, 데스크톱 배치를 육안 검토했다. 5번 FAQ 열림도 실제 클릭 확인했다. 모든 버튼을 클릭 검사했다는 뜻은 아니다.
- 공개 13편의 HTTP·canonical·noindex 없음·정확한 head/main 반영 확인. 해당 페이지 이미지 URL 39개 정상 응답 확인(`final-public-audit.json`).
- 공개 첫 화면에서 자동 광고용 예약 여백이 생기는 경우를 관찰했다. 본문 가로 넘침과 별개이며 이 작업에서 광고 설정은 변경하지 않았다.
- 기존 사용자 변경 `docs/POSTING_GUIDELINES.md`는 발행 커밋에 포함하지 않았다.

## 네이버 수집 요청: 7개 접수, 6개 한도 대기

요청 대상은 신규 5편 + 수정 기존 글 8편 = 13개다. 새 등록 시각이 있는 요청 내역으로 **7개 접수**를 확인했다. 신규 5편 모두 포함하며 접수 시간은 2026-10-22 10:12:40~10:15:43(KST)이다.

8번째 대상 `/guides/iol-mri-device-information-check` 요청에서 네이버가 **“사이트별 일간 최대 요청 수를 초과하였습니다.”**라고 응답하여 추가 요청을 중단했다. 이후 반복 제출하지 않았다. 이 URL은 접수 완료로 세지 않았다.

- 접수 증거: `naver-request-status.json`, `naver-accepted-receipts.png`
- 한도 응답 원문: `naver-quota-exceeded.txt` (브라우저 alert 상태에서는 스크린샷 API가 제공되지 않아 접근성 응답을 저장함)
- 남은 URL: `naver-request-pending.txt`
- `indexingConfirmed: false`. 요청 접수는 실제 수집·색인 완료를 뜻하지 않는다.

### 미접수 대기 6개

1. https://hospital.hbuby.com/guides/iol-mri-device-information-check
2. https://hospital.hbuby.com/silbi/mri-silbi-claim
3. https://hospital.hbuby.com/silbi/knee-surgery-rehabilitation-hospital-transfer-claim
4. https://hospital.hbuby.com/guides/hira-medication-history-before-admission
5. https://hospital.hbuby.com/treatment-costs/surgery-deposit-cancellation-refund-records
6. https://hospital.hbuby.com/claims/closed-hospital-records-request

한도가 풀린 뒤 이 목록만 다시 대조해 제출할 수 있다. 이번 턴에서는 별도 자동 재실행 일정을 만들지 않았다.
