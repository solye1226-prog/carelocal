# 네이버 유입 검색어 기반 1차 보완·후속 10개 발행

작업일: 2026-10-08 (Asia/Seoul). 사용자 제공 전일 네이버 검색어 TOP 30을 **이미 케어로컬에 유입된 질문**으로 해석했다. 이 자료만으로 새 키워드의 검색량이나 성과 개선을 예측하지 않는다. 같은 답을 반복하는 URL은 만들지 않고, 독자가 기존 글을 읽은 뒤 만날 수 있는 다음 상황을 분리했다.

## 1차 보완

| 기존 글 | 추가한 빠른 답 |
|---|---|
| `/claims/surgery-claim-documents` | 수술확인서의 진단명 누락, 수술기록지 추가 요청, 대체자료를 먼저 보험사에 문의 |
| `/surgery-benefit/gallbladder-surgery-benefit` | 담낭절제술과 ERCP를 분리하고 가입 약관의 동시수술 규정 확인 |
| `/surgery-benefit/hemorrhoid-surgery-benefit` | 치질·치핵 표현과 고무밴드 결찰술·치핵절제술 구분 |
| `/surgery-benefit/surgery-classification` | 1~3종 문의는 병원비가 아니라 실제 수술명과 가입 당시 분류표로 확인 |

보완 커밋: `6c76394`. 4개 글의 `dateModified`와 사이트맵 변경일을 실제 편집일로 갱신했다.

## 새 글과 순차 발행

| 순서 | 새 URL | 검색 의도상 기존 글과 다른 질문 | 커밋 | 대표 이미지 |
|---:|---|---|---|---|
| 1 | `/claims/surgery-certificate-missing-diagnosis` | 수술확인서에 진단명이 빠진 경우의 보완 순서 | `a912d58` | `assets/images/surgery-certificate-missing-diagnosis-thumb.webp` |
| 2 | `/claims/surgery-record-additional-request` | 보험사가 수술기록지를 추가로 요청한 경우의 발급 범위 | `a0b29c3` | `assets/images/surgery-record-additional-request-thumb.webp` |
| 3 | `/claims/surgery-certificate-unavailable` | 수술확인서를 발급받기 어려울 때 인정 가능한 대체자료 문의 | `2712ffb` | `assets/images/surgery-certificate-unavailable-thumb.webp` |
| 4 | `/surgery-benefit/gallbladder-ercp-combined-claim` | 담낭절제술과 ERCP 두 행위의 수술비 지급 단위 | `d920465` | `assets/images/gallbladder-ercp-combined-claim-thumb.webp` |
| 5 | `/claims/gallbladder-pathology-request` | 담낭 수술 후 조직검사 결과지 보완 요청의 목적 | `ee4e32a` | `assets/images/gallbladder-pathology-request-thumb.webp` |
| 6 | `/surgery-benefit/hemorrhoid-ligation-benefit` | 치핵 결찰술과 절제술의 행위 구분 및 수술비 약관 | `4f39dc5` | `assets/images/hemorrhoid-ligation-benefit-thumb.webp` |
| 7 | `/surgery-benefit/hemorrhoid-repeat-surgery-benefit` | 치핵 반복 치료의 실제 행위·부위·지급 횟수 | `17b4200` | `assets/images/hemorrhoid-repeat-surgery-benefit-thumb.webp` |
| 8 | `/claims/silbi-fixed-surgery-same-claim` | 실손의료비와 정액 수술비를 함께 접수할 때 담보별 서류 | `0e7c877` | `assets/images/silbi-fixed-surgery-claim-thumb.webp` |
| 9 | `/surgery-benefit/surgery-benefit-amount-review` | 예상보다 적은 수술비의 가입금액·종수·지급내역 대조 | `1b87633` | `assets/images/surgery-benefit-amount-review-thumb.webp` |
| 10 | `/claims/surgery-record-certificate-mismatch` | 수술확인서와 수술기록지 자체의 기재 차이 확인 | `3bcd8b3` | `assets/images/surgery-record-mismatch-thumb.webp` |

상단 보험사 공식 접수처 CTA를 10개 글에 추가한 후속 커밋: `a2b4375`. 각 새 글은 대표 이미지 1장과 서로 다른 본문 장면 이미지 2장을 사용한다. 설명용 이미지는 실제 환자나 의료기록이 아니라고 본문에 표시했다.

## 공식 근거와 적용 범위

- [삼성화재 보험금 청구 필요서류](https://direct.samsungfire.com/m/claim/MP040202_001.html?tab=1): 수술 청구에서 진단명·질병분류기호·수술명·수술일이 포함된 서류, 실손 비용 자료를 확인한 **한 보험사 예시**. 모든 보험사에 일반화하지 않았다.
- [의료법 제21조](https://law.go.kr/lsLinkCommonInfo.do?lsJoLnkSeq=1022124333): 본인 진료기록 열람·사본 발급 요청의 근거. 보험사 전용 수술확인서 양식 발급 의무로 해석하지 않았다.
- [질병관리청 담석증](https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=6735) 및 [ERCP](https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=5251): 담낭절제술과 담도 내시경 치료 행위를 구분했다. 민간보험 지급 기준은 개별 약관에 남겨 두었다.
- [질병관리청 치핵](https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=5818): 고무밴드 결찰술·치핵절제술의 치료 방법 차이를 확인했다.
- [손해보험협회 실손 청구서류 안내](https://consumer.knia.or.kr/m/consumer/insurance-guide/0202.do): 실손 비용 서류를 확인했다. 정액 수술비의 종수·금액 근거로 사용하지 않았다.

조사 확인일: 2026-10-08. 실제 지급·분류·제출서류는 보험사, 상품, 특약, 가입 시기와 개인 기록에 따라 달라진다고 모든 글에 설명했다.

## 생성 이미지 프롬프트 기록

기본 제공 ImageGen으로 원본 PNG를 만들고 `cwebp`로 1200×675 WebP로 압축해 위 파일에 저장했다. 프롬프트의 공통 조건은 **Korean insurance editorial photography, wide 16:9, natural daylight, navy/blue accents, no legible text, numbers, logos, personal data, fake medical values or watermark**였다. 개별 장면 요청은 다음과 같다.

1. 병원 수술확인서와 보험 청구 체크리스트를 비교하는 성인.
2. 수술기록 사본 요청서와 휴대폰을 확인하는 성인.
3. 병원 접수창구에서 수술확인서 발급을 상담하는 성인.
4. 담낭 수술과 ERCP의 별도 기록을 상징하는 두 병원 폴더.
5. 담낭 수술 뒤 병리결과 봉투를 확인하는 성인(결과 내용은 비표시).
6. 치핵 치료 기록과 보험 약관을 비교하는 성인(치료 장면 비표시).
7. 서로 다른 치료일의 병원 기록 두 묶음을 비교하는 성인.
8. 병원 영수증·보험 약관·휴대폰 청구 화면을 비교하는 성인.
9. 보험금 지급내역과 약관·계산기를 비교하는 성인.
10. 수술확인서와 수술기록지 두 문서를 나란히 비교하는 성인.

## 검증

- 각 글을 생성한 뒤 카탈로그를 갱신하고 `pnpm run check`를 통과시킨 뒤 **한 건씩** `main`에 커밋·푸시했다. 최종 카탈로그 227개, 사이트맵 252 URL.
- 공개 도메인의 새 10개 URL 모두 HTTP 200, 의도한 제목, self-canonical, 공개 카탈로그·사이트맵 포함 확인.
- 공개 페이지의 실제 Chrome 모바일 뷰포트 360px·390px, 10개×2에서 H1·대표 이미지 로딩과 가로 넘침 없음 확인. 대표 화면 스크린샷은 작업용 시각화 폴더에 저장했다.
- 이 검증은 네이버 색인, 검색 순위, 클릭 상승 또는 보험금 지급을 증명하지 않는다. 색인 요청은 하지 않았다.
