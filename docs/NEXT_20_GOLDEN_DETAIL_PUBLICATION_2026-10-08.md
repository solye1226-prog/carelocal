# 보험 청구 세부키워드 후속 20개 발행 기록

작업일: 2026-10-08 (Asia/Seoul). 공개 사이트: https://hospital.hbuby.com/. 전일 네이버 유입 검색어의 **기존 케어로컬 방문 의도**와 기발행 글의 다음 문제를 참고했다. `황금키워드`는 이 작업에서 실비보험·보험금 청구·치아보험·해외 의료비라는 **넓은 주제 축**을 뜻한다. 원본 황금키워드 목록과 검색량·광고 단가 자료는 이 저장소에서 확인되지 않았으므로, 아래 소재를 데이터로 검증된 고수익 키워드라고 주장하지 않는다. 각 글은 `넓은 축 + 실제 상황 + 확인 행동`의 세부키워드로 범위를 좁혔다.

| 순서 | 넓은 주제 축 → 세부키워드 | 공개 URL | 기존 글과 분리한 질문 |
|---:|---|---|---|
| 1 | 보험금 청구 → 미성년자 부모 청구 서류 | `/claims/minor-child-insurance-claim-documents` | 수익자·가족관계·지급계좌 |
| 2 | 보험금 청구 → 성인 가족 대리 위임장 | `/claims/family-proxy-insurance-claim-form` | 병원 기록 대리 발급과 다른 보험사 위임 |
| 3 | 보험금 청구 → 사진 접수 뒤 원본 요청 | `/claims/insurance-claim-original-documents-request` | 요청 범위·제출 경로·접수 확인 |
| 4 | 실손보험 → 여러 보험사 서류 전송 | `/silbi/multiple-silbi-insurers-document-forwarding` | 서류 전송과 회사별 심사·지급 분리 |
| 5 | 실비보험 → 입원 중간정산 청구 | `/silbi/hospital-interim-bill-silbi-claim` | 선지급 가능성과 최종 정산 |
| 6 | 실비보험 → 납입확인서와 법정 영수증 | `/silbi/hospital-receipt-vs-payment-certificate` | 연말정산 서류를 청구 영수증으로 쓸 수 있는지 |
| 7 | 실비보험 → 비급여 세부내역서 | `/silbi/noncovered-itemized-bill-silbi-documents` | 항목별 비용과 비급여 담보 확인 |
| 8 | 실비보험 → 처방전 진단명 코드 누락 | `/silbi/outpatient-prescription-diagnosis-code` | 대체자료·재발급 확인 |
| 9 | 보험금 청구 → 수익자와 계좌 명의 불일치 | `/claims/insurance-beneficiary-bank-account-mismatch` | 청구 전 명의 확인 |
| 10 | 실비보험 → 병원비 정정 후 청구 | `/silbi/corrected-hospital-bill-insurance-claim` | 접수액과 최종 납부액 대조 |
| 11 | 치아보험 → 임플란트 청구서류 | `/claims/dental-implant-insurance-claim-documents` | 발치 원인·치아번호·보철 담보 |
| 12 | 치아보험 → 크라운 청구서류 | `/claims/dental-crown-insurance-claim-documents` | 보존치료 재료와 치아번호 |
| 13 | 치아보험 → 발치일·임플란트 완료일 | `/claims/dental-extraction-implant-dates` | 단계별 날짜와 특약 판단 시점 |
| 14 | 치아보험 → 같은 치아 재치료 | `/claims/same-tooth-repeat-dental-treatment-claim` | 이전 치료·지급 이력과 횟수 규정 |
| 15 | 해외 의료비 → 카드 전표만 있는 병원비 | `/claims/overseas-hospital-card-slip-insurance` | 결제 증빙과 진료비 내역 구분 |
| 16 | 해외 의료비 → 약국 처방전·약제비 | `/claims/overseas-pharmacy-prescription-claim` | 해외 진료와 처방약 구매 연결 |
| 17 | 해외 의료비 → 진단명 누락 소견서 | `/claims/overseas-medical-note-diagnosis-claim` | 보완할 정보와 현지 병원 자료 |
| 18 | 실비보험 → 귀국 뒤 국내 재진료 | `/silbi/post-travel-domestic-followup-silbi` | 해외 여행자보험과 국내 실손 구분 |
| 19 | 보험금 청구 → 접수 후 계좌 변경 | `/claims/insurance-claim-bank-account-change` | 지급 전 단계와 변경 절차 |
| 20 | 실비보험 → 보험금 지급 뒤 병원비 환불 | `/silbi/hospital-bill-correction-silbi-claim` | 기존 지급액과 최종 실제 납부액 정산 |

## 중복 의도와 출처

- 게시 전 `assets/article-catalog.json`과 관련 HTML 본문을 확인했다. 같은 넓은 검색어라도 **새로 해결할 행동**이 다르면 분리했다. 예: 기존 해외 병원비 글은 귀국 전 서류 준비 전반, 15~17번은 카드 전표·약국·진단명 보완 각각의 접수 문제다. 치아보험 면책기간 글, 국민건강보험 임플란트 급여 글과 11~14번의 민간 치아보험 청구는 범위가 다르다.
- [삼성화재 질병·상해·여행·치아 보험금 청구 필요서류](https://direct.samsungfire.com/claim/PP040202_001.html?pcMode=true)에서 공통·대리 청구 서류, 실손 입원·통원 서류, 수술 서류, 원본 제출 안내, 실손 청구대행·선지급 서비스, 해외 진료·약제비 증빙, 치과치료확인서의 치아번호·원인·치료일과 엑스레이 항목을 확인했다. **삼성화재의 항목과 금액 기준은 다른 보험사에 일반화하지 않았다.** 개별 상품 약관, 특약과 공식 접수처가 최종 기준이다.
- 병원비 정정·지급 후 환불, 계좌 변경은 위 자료가 절차를 확정하지 않는다. 해당 글은 사실관계를 정리해 보험사에 문의할 항목을 제시할 뿐, 특정 변경 절차나 지급 결과를 보장하지 않는다.

## 이미지 제작

기본 제공 ImageGen으로 **각 글의 서로 다른 대표 장면 20개**를 만들고 눈으로 샘플을 확인한 뒤, 1200×675 WebP로 변환해 `assets/images/<slug>-thumb.webp` 또는 이미지 교정 후 `-thumb-v2.webp`·`-thumb-v3.webp`에 저장했다. 각 글은 대표 이미지와 관련 기존 본문 이미지 두 장을 사용한다. 이미지가 실제 환자·기록이 아님을 글에 표시했다. 공통 프롬프트: `Editorial photorealistic natural image for a Korean insurance information website, landscape 16:9, natural daylight, navy and soft blue accents, no readable text, no logos, no medical data, no watermark, no dramatic illness.` 최종 게시물에 연결된 개별 장면은 순서대로 다음과 같다. 초기 생성 시 사용했지만 주제와 맞지 않은 오래된 병원 기록 및 재활치료 장면 두 개는 공개 글에서 제외했다.

1. 부모가 아이의 병원 청구서류를 검토하는 장면.
2. 가족이 보험 청구 위임장을 비교하는 장면.
3. 보험사 원본 제출용 병원 서류를 정리하는 장면.
4. 보험증권 두 묶음과 병원 영수증을 비교하는 장면.
5. 입원 중간정산 영수증과 약관을 검토하는 장면.
6. 통원 영수증과 연간 납입확인서를 비교하는 장면.
7. 비급여 세부내역서와 보험 청구 화면을 대조하는 장면.
8. 처방전과 통원 영수증을 검토하는 장면.
9. 수익자와 계좌 명의 관련 자료를 확인하는 장면.
10. 정정된 병원비 자료를 확인하는 장면.
11. 치과 임플란트 청구 자료를 정리하는 장면.
12. 크라운 치료 자료를 확인하는 장면.
13. 발치일과 임플란트 완료일 기록을 비교하는 장면.
14. 같은 치아의 두 치료 기록을 비교하는 장면.
15. 해외 병원 청구서와 카드 전표를 정리하는 장면.
16. 해외 약국 영수증과 처방전을 정리하는 장면.
17. 해외 의사 소견서와 진료 자료를 검토하는 장면.
18. 귀국 후 국내 진료비와 해외 진료비를 비교하는 장면.
19. 보험금 청구 계좌를 변경하면서 서류와 휴대전화를 확인하는 장면.
20. 병원비 환불 영수증과 이미 지급된 보험금 자료를 비교하는 장면.

## 배포·검증

- 1번부터 20번까지 각 글을 생성한 다음 카탈로그·사이트맵을 갱신하고 `pnpm run check`를 통과시켜 **각각 `main`에 커밋·푸시**했다. 마지막 본문 커밋 `87a7217`. 카테고리 진입 링크는 후속 커밋 `a9f8831`, 대표 이미지 주제 정합성 교정은 `dcec09b`.
- 각 공개 URL은 HTTP 200과 본문 canonical·대표 이미지 경로를 확인했다. 카탈로그 227→247개, 사이트맵 252→272 URL. 카테고리 `/claims/`, `/silbi/`에서 새 글로 진입할 수 있도록 연결했다.
- 이미지 교정 배포 뒤 공개 20개 HTML의 제목·canonical·OG 이미지 URL을 로컬 원고와 1:1 대조했다. 20개 대표 WebP 응답과 두 카테고리의 새 링크도 공개 도메인에서 확인했다.
- Chrome CDP 실제 모바일 폭 360px·390px에서 20글×2회 검사했다. 전 회차 H1, canonical, 본문 이미지 3장 로딩, 가로 넘침 없음. 이미지 장면 연결을 교정한 뒤 40회 전체 재검사도 통과했다. 대표 장면 7장을 육안으로 확인했다. 스크린샷과 측정 JSON은 작업 시각화 폴더에 보관했다.
- 네이버·구글 개별 색인, 순위, 클릭, 광고 수익은 별도이며 이 작업에서 검증하거나 보장하지 않는다. 색인 요청과 광고 설정 변경은 하지 않았다.
