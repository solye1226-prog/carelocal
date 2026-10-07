# 검색어 기반 기존 글 보강 기록

확인일: 2026-10-07 (KST). 사용자가 제공한 ‘검색 키워드 TOP 30’ 화면에서 보이는 상위 10개 검색어를 참고했다. 화면에는 집계 기간·도착 페이지·평균 순위가 보이지 않으므로 검색어별 클릭을 특정 URL의 성과로 단정하지 않는다. 같은 검색 의도에 새 URL을 만들지 않고 기존 글을 순서대로 보강한다. 검색 지표 개선은 보장하지 않는다.

## 1. 수술분류표

- 대상: `/surgery-benefit/surgery-classification`
- 중복 확인: 이 URL이 1종·2종·3종 분류표의 대표 글이며 3종 세부 글과 별도 역할을 유지한다.
- 변경: 병명만 보고 종수를 고르지 않는 가상 담낭절제술 예시를 자료 확인 표 바로 뒤에 추가했다. 모바일 H1을 짧게 하고 줄바꿈을 조정했다. 기존 SEO 제목·canonical과 관련 글은 유지했다.
- 근거: 가입 당시 약관의 분류표가 계약 기준이며, [삼성화재 수술 청구서류 안내](https://direct.samsungfire.com/m/claim/MP040202_001.html?tab=1)는 진단명·수술명·수술일자를 포함한 서류를 안내한다. 한 회사의 서류 안내를 종수 공통 기준으로 일반화하지 않았다.
- 검사: `pnpm run check` 통과. 로컬 360×800, 390×1000, 1280×900에서 본문 가로 넘침 없음. `.deploy/classification-update-360-v2.png` 첫 화면 확인.
- 발행 커밋: `8fbd0ad`. 공개 URL HTTP 200, 가상 예시와 새 H1 반영 확인. 공개 360px·390px 첫 화면에서 본문 가로 넘침 없음. `.deploy/classification-public-360.png`, `.deploy/classification-public-390.png`.

## 2. 보험금 청구서류

- 대상: `/claims/insurance-claim-documents`
- 중복 확인: 실비·진단비·수술비·입원비 서류를 한 페이지에서 분기하는 대표 글이며 세부 청구서류 글로 연결한다.
- 변경: SEO 제목과 H1을 검색 질문에 맞게 명확히 하고 도입을 짧게 정리했다. OG 제목·이미지 주소, Article 수정일, 모바일 H1 줄바꿈을 맞췄다. 기존 서류 비교표와 상세 근거는 유지했다.
- 공식 확인: [삼성화재 청구서류 안내](https://direct.samsungfire.com/m/claim/MP040202_001.html?tab=1)는 수술·실손·입원·진단 청구에 서로 다른 서류를 제시하며 상품에 따른 추가 요청 가능성을 명시한다. 이 회사의 항목을 모든 보험사 필수 목록으로 단정하지 않는다.
- 로컬 모바일: 360×800·390×1000에서 제목·도입·첫 비교표 진입을 확인했고 본문 가로 넘침 없음. `.deploy/claim-documents-update-360.png`, `.deploy/claim-documents-update-390.png`.
- 발행 커밋: `355b254`. 공개 URL HTTP 200, 새 제목·도입 반영 확인. 공개 360px·390px 첫 화면에서 본문 가로 넘침 없음.

## 3. 3종 수술분류표

- 대상: `/surgery-benefit/third-tier-surgery-classification`
- 중복 확인: 대표 수술분류표 글은 전체 분류 체계, 이 글은 3종 해당 여부와 지급 조건을 다룬다.
- 변경: H1과 도입을 질문형으로 간결하게 정리하고 계약 특약명 → 적용 분류표 → 실제 수술 행위 → 지급·횟수 조건의 확인 순서를 첫 화면에 추가했다. Article 수정일과 사이트맵 수정일을 갱신했다.
- 로컬 확인: `pnpm run check` 통과. 360px·390px 첫 화면 확인, 가로 넘침 없음. `.deploy/third-tier-local-360.png`, `.deploy/third-tier-local-390.png`.
- 발행 커밋: `61a4242`. 공개 URL HTTP 200, 새 H1·확인 순서 반영 확인. 공개 360px·390px 첫 화면에서 본문 가로 넘침 없음.

## 4. 카티스템 실비

- 대상: `/silbi/cartistem-silbi-claim`
- 중복 확인: 이 글은 카티스템 치료의 실손 청구 판단을 다루며, 치료비 구성 글·일반 재료대 실비 글과 연결한다.
- 변경: 첫 화면에서 항목별 비용과 가입 실손 약관을 대조하는 답이 바로 보이도록 H1·도입을 정리했다. Article 수정일과 사이트맵 수정일을 갱신했다.
- 로컬 확인: `pnpm run check` 통과. 360px·390px 첫 화면 확인, 가로 넘침 없음. `.deploy/cartistem-local-360.png`, `.deploy/cartistem-local-390.png`.
- 발행 커밋: `276ea95`. 공개 URL HTTP 200, 새 H1·도입 반영 확인. 공개 360px·390px 첫 화면에서 본문 가로 넘침 없음.

## 5. 백내장 수술 몇 종

- 대상: `/surgery-benefit/cataract-surgery-benefit`
- 중복 확인: 백내장 수술의 종수·렌즈·양안 지급 횟수를 구분하는 대표 글이며 청구서류 상세 글과 역할을 나눈다.
- 변경: 첫 화면에 모든 계약에 공통인 종수가 없다는 답과 실제 수술명·가입 당시 약관의 대조 방법을 배치했다. Article 수정일과 사이트맵 수정일을 갱신했다.
- 로컬 확인: `pnpm run check` 통과. 360px·390px 첫 화면 확인, 가로 넘침 없음. `.deploy/cataract-benefit-local-360.png`, `.deploy/cataract-benefit-local-390.png`.
- 발행 커밋: `6e48a53`. 공개 URL HTTP 200, 새 H1·도입 반영 확인. 공개 360px·390px 첫 화면에서 본문 가로 넘침 없음.

## 6. 백내장 수술 보험금 청구서류

- 대상: `/claims/cataract-surgery-claim-documents`
- 중복 확인: 백내장 청구서류에 집중한 글이며 종수 판단 글과 분리한다.
- 변경: 실손은 영수증·세부내역서, 수술비 특약은 진단명·수술명·수술일 자료라는 구분을 첫 화면에 배치했다. Article 수정일과 사이트맵 수정일을 갱신했다.
- 로컬 확인: `pnpm run check` 통과. 360px·390px 첫 화면 확인, 가로 넘침 없음. `.deploy/cataract-docs-local-360.png`, `.deploy/cataract-docs-local-390.png`.
- 발행 커밋: `366e1f4`. 공개 URL HTTP 200, 새 H1·도입 반영 확인. 공개 360px·390px 첫 화면에서 본문 가로 넘침 없음.

## 7. 보험 수술분류표와 수술코드

- 대상: `/surgery-benefit/surgery-code-insurance-guide`
- 중복 확인: 대표 분류표 글과 달리 진단코드·진료행위코드·보험 분류표의 역할 차이를 다룬다.
- 변경: 코드만으로 종수를 정할 수 없다는 답과 서류별 역할을 첫 화면에 배치했다. Article 수정일과 사이트맵 수정일을 갱신했다.
- 로컬 확인: `pnpm run check` 통과. 360px·390px 첫 화면 확인, 가로 넘침 없음. `.deploy/surgery-code-local-360.png`, `.deploy/surgery-code-local-390.png`.
- 발행 커밋: `2492f15`. 공개 URL HTTP 200, 새 H1·서류 역할 문장 반영 확인. 공개 360px·390px 첫 화면에서 본문 가로 넘침 없음.

## 8. 수술확인서와 수술기록지

- 대상: `/claims/surgery-claim-documents`
- 중복 확인: 수술비 청구서류 대표 글에서 두 서류의 역할을 다루며, 수술명 불일치 글은 별도 상황에 한정한다.
- 변경: 검색 질문을 H1에 반영하고 기본 확인 서류와 추가 수술기록지의 구분을 첫 화면에 명확히 했다. OG 이미지 절대 주소, Article·사이트맵 수정일을 갱신했다.
- 로컬 확인: `pnpm run check` 통과. 360px·390px 첫 화면 확인, 가로 넘침 없음. `.deploy/surgery-docs-local-360.png`, `.deploy/surgery-docs-local-390.png`.
- 발행 커밋: `306c863`. 공개 URL HTTP 200, 새 H1·도입 반영 확인. 공개 360px·390px 첫 화면에서 본문 가로 넘침 없음.

## 9. 수술확인서 수술명과 약관의 이름이 다를 때

- 대상: `/surgery-benefit/surgery-name-mismatch`
- 중복 확인: 대표 청구서류 글과 달리 병원 기록명과 약관 항목명이 일치하지 않는 상황에 집중한다.
- 변경: 실제 시행 행위를 대조하고 보험사에 적용한 분류표 항목·조항을 묻는 질문을 첫 화면에 추가했다. Article 수정일과 사이트맵 수정일을 갱신했다.
- 로컬 확인: `pnpm run check` 통과. 360px·390px 첫 화면 확인, 가로 넘침 없음. `.deploy/name-mismatch-local-360.png`, `.deploy/name-mismatch-local-390.png`.
- 발행 커밋: `3a33fb1`. 공개 URL HTTP 200, 새 H1·질문 문장 반영 확인. 공개 360px·390px 첫 화면에서 본문 가로 넘침 없음.

## 10. 종수술비 보험금 청구

- 대상: `/surgery-benefit/type-surgery-benefit-claim`
- 중복 확인: 대표 분류표 글은 항목을 찾는 법, 이 글은 가입 특약 확인부터 청구 접수까지의 순서에 집중한다.
- 변경: 계약 확인 → 수술서류·분류표 대조 → 공식 경로 접수의 순서를 첫 화면에 배치하고 접수 순서의 병원 서류 항목을 구체화했다. Article 수정일과 사이트맵 수정일을 갱신했다.
- 로컬 확인: `pnpm run check` 통과. 360px·390px 첫 화면 확인, 가로 넘침 없음. `.deploy/type-claim-local-360.png`, `.deploy/type-claim-local-390.png`.
- 발행 커밋: `aff626a`. 공개 URL HTTP 200, 새 H1·접수 순서 반영 확인. 공개 360px·390px 첫 화면에서 본문 가로 넘침 없음. `.deploy/type-claim-public-360.png`, `.deploy/type-claim-public-390.png`.

## 최종 공개 확인

- 위 10개 공개 URL 모두 HTTP 200이고 각 문서의 H1 및 self-canonical을 확인했다.
- 공개 360px 화면에서 10개 문서 모두 가로 넘침이 없었다. 각 글 발행 직후 390px 첫 화면도 확인했다.
- 사이트 검사 `pnpm run check`는 마지막 글 수정 후 통과했다. 검색 노출·색인·광고 표시·순위 변동은 이 확인으로 입증되지 않는다.
