# 후속 세부 소재 5편 발행 보고

작업일: 2026-10-22 (Asia/Seoul)

## 발행 및 링크

- 계획한 신규 5편을 순서대로 발행. 기존 382편에서 387편으로 증가.
- 기존 11편에 문맥 내부링크를 추가. 신규 글도 해당 대표 글과 관련 기준으로 연결.
- 총 16개 공개 페이지의 head·main 원본 일치, 자기 canonical, noindex 부재를 확인. 이미지 48개 정상 응답.
- 신규 5편 각각 360·390·1280px 실제 너비 검증. 실패 이력은 보존하되 각 기대 너비의 마지막 PASS만 완료 근거로 사용.
- 링크·canonical·카탈로그·기존 테스트를 각 발행 전에 통과함.

## 신규 글

1. [담도 배액술 PTBD 수술비, ERCP·담낭절제술과 청구 기록은 어떻게 다를까?](https://hospital.hbuby.com/surgery-benefit/ptbd-biliary-drainage-insurance)
2. [치루 세톤 수술 보험금, 설치·조임·제거 기록을 어떻게 나눌까?](https://hospital.hbuby.com/surgery-benefit/anal-fistula-seton-staged-claim)
3. [백내장 렌즈 카드를 잃어버렸다면? 인공수정체 종류·수술 기록 확인법](https://hospital.hbuby.com/claims/iol-implant-card-lost-records)
4. [카티스템·절골술 후 재활병원으로 옮겼다면? 실비 청구서류 나누는 법](https://hospital.hbuby.com/silbi/knee-surgery-rehabilitation-hospital-transfer-claim)
5. [수술이 취소됐는데 검사비·마취비가 나왔다면? 실비 청구 전 정산 확인](https://hospital.hbuby.com/silbi/cancelled-surgery-test-anesthesia-claim)

## 4·5번 약관 검증

- 4번: 삼성화재 다이렉트 실손의료비보험 2605.1 계약전환용의 PDF46쪽(인쇄45쪽) 용어 정의를 확인. 입원의 치료 필요성·재택치료 곤란·관리·체류 조건과 재활 비용 용어를 상품 예시로 소개. 입원 필요성과 보장 여부를 병원 이름 또는 체류 시간만으로 보장하지 않음.
- 5번: 현대해상 다이렉트 실손 Hi2407의 질병급여 지급사유(PDF41쪽), 비용 용어(PDF62~63쪽)를 확인. 실제 검사·마취 비용과 정액 수술비를 구분. 수술 취소 전용 일괄 보장 규정으로 소개하지 않음.
- 두 글 모두 상품·버전·해당 PDF 페이지와 공식 원문 링크를 본문 가까이 표시. 개인 계약의 비급여·제외·공제 조건은 별도 확인하도록 안내.
- 약관 관련 페이지를 렌더링해 표 머리말과 정의의 연결을 시각적으로 확인. 공식 PDF 원본은 내부 작업 폴더에만 보존.

## 연결한 기존 글

- https://hospital.hbuby.com/surgery-benefit/subtotal-cholecystectomy-insurance-documents
- https://hospital.hbuby.com/surgery-benefit/gallbladder-ercp-combined-claim
- https://hospital.hbuby.com/surgery-benefit/hemorrhoid-fistula-same-day-claim
- https://hospital.hbuby.com/surgery-benefit/anal-fistula-surgery-benefit
- https://hospital.hbuby.com/surgery-benefit/iol-dislocation-reoperation-insurance
- https://hospital.hbuby.com/claims/cataract-multifocal-lens-silbi
- https://hospital.hbuby.com/surgery-benefit/cartistem-high-tibial-osteotomy-claim
- https://hospital.hbuby.com/silbi/cartistem-silbi-claim
- https://hospital.hbuby.com/surgery-benefit/hemorrhoid-pph-stapled-surgery-claim
- https://hospital.hbuby.com/silbi/cataract-preoperative-test-claim
- https://hospital.hbuby.com/claims/surgery-claim-documents

## 이미지 및 증거

- 내장 imagegen으로 원본15장 제작, WebP로 변환하여 assets/images/에 글 slug별 thumb·body1·body2 저장.
- 최종 프롬프트: image-prompts.json. 검수 연락시트: image-contact-sheet.jpg.
- 자료 비교표·문의 문장·FAQ·공식 자료 버튼 포함. 생성 이미지 및 가상 예시를 구분하고 개인정보 전송을 권하지 않음.
- final-public-audit.json / publication.json: 실제 공개 본문 반영 증거.
- local-qa.json: 화면 크기별 검사. rehab-interaction.json: FAQ·이미지·약관 링크 검증.
- duplicate-check.json / source-notes.json / editorial-review.json: 검색 의도·출처·편집 검토.

## 네이버 수집 요청

신규 5편 + 내부링크를 추가한 기존 11편 = 총 16개 수집 요청 접수 완료. 2026-10-22 08:53:30~08:56:57 KST 등록 행을 각각 확인하고 최종 목록 1·2페이지에서 전체 URL을 대조함. 남은 요청 0개. 실제 수집·색인 완료를 뜻하지 않음.

- naver-request-status.json: 16개 접수, indexingConfirmed=false
- naver-receipt-1.txt~16.txt: 개별 최종 접수 등록행
- naver-final-page1.txt 및 naver-final-page2.txt: 최종 목록 대조
- naver-final-page1.png 및 naver-final-page2.png: 접수 화면 증거

광고 설정과 Google 색인 요청은 변경하지 않았음.
