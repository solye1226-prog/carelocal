# 수술비·청구서류 보완 및 신규 발행 보고

작업 시작: 2026-10-21 / 재개·공개 검증: 2026-10-22 (Asia/Seoul)

## 현재 결과

- 기존 대표 글 5편 보완 및 공개 반영 확인. 신규 5편 순차 발행 완료. 관련 기존 글 2편은 문맥 내부링크만 추가.
- 12개 페이지의 공개 head·main이 로컬 원본과 일치함을 확인. 이미지 36개 정상 응답, 자기 canonical 및 noindex 부재 확인.
- 신규 5편과 기존 대표 5편의 PC·모바일 검수 기록은 local-qa.json 참조. 요청 크기와 실제 너비가 일치한 최종 통과 행만 유효함.
- 네이버 수집 요청은 아직 미실행: 2026-10-22 세션 로그아웃. 관리 계정 로그인 후 naver-request-targets.json 12개를 순차 요청할 것.
- 이번 작업에서 Google 색인 요청·광고 설정은 변경하지 않음.

## 기존 대표 5편 보완

1. 담낭 수술비: 접근 방법·절제 범위·별도 행위를 구분하는 표와 가상 예시.
2. 백내장 수술비: 양쪽 눈 수술일과 지급 단위를 구분, 인공수정체 재수술 글 연결.
3. 치핵 수술비: 진단과 실제 수술을 구분, PPH·동시수술 질문 연결.
4. 수술분류표: 계약·분류표·지급 단위·금액 확인 순서 보강.
5. 수술비 청구서류: 추가 요청 사유별 대응과 병원 FAQ의 정확한 상세 링크 보강.

## 신규 5편

1. [인공수정체 탈구 재수술 보험금, 처음 백내장 수술과 기록을 나누는 법](https://hospital.hbuby.com/surgery-benefit/iol-dislocation-reoperation-insurance)
2. [PPH 치핵 수술 보험금, 절제술·고무밴드 결찰술과 무엇이 다를까?](https://hospital.hbuby.com/surgery-benefit/hemorrhoid-pph-stapled-surgery-claim)
3. [카티스템과 절골술을 함께 받았다면? 수술비·실비 청구 기록 나누기](https://hospital.hbuby.com/surgery-benefit/cartistem-high-tibial-osteotomy-claim)
4. [담낭 아전절제술 보험금 청구, 전절제·개복 전환과 기록 구분하기](https://hospital.hbuby.com/surgery-benefit/subtotal-cholecystectomy-insurance-documents)
5. [치핵·치루 동시수술 보험금, 두 수술명과 지급 단위 확인법](https://hospital.hbuby.com/surgery-benefit/hemorrhoid-fistula-same-day-claim)

## 배포 및 검증

- 어제 누락돼 보이던 후속 커밋들이 밤사이 Cloudflare 배포 목록에 도착함. 연결 재설치·권한 확대 없이 기존 자동 배포로 반영됨. 지연의 근본 원인을 확정한 것은 아님.
- 신규 발행 순서: c0bc801 → e6b49e2 → 257eedb → b5c0421 → 5c41279. 각 페이지의 공개 원문 일치를 확인한 뒤 다음 발행으로 진행.
- 미래 글은 단계별 카테고리·사이트맵·카탈로그·부모 문맥 링크에서 제외하여 아직 공개되지 않은 글로 연결되지 않도록 처리.
- 공식 의료 자료는 행위 명칭·기록 구분의 근거로 사용하며 보험 지급 기준으로 일반화하지 않음. 실제 수가코드·공통 종수·지급 횟수는 임의로 제시하지 않음.
- 링크·canonical·카탈로그 및 기존 테스트 전체 통과. 최종 사이트맵 날짜 보정 후 전체 점검도 다시 통과.

## 증거

- final-public-audit.json: 공개 본문·canonical·이미지 검사
- publication.json: 개별 신규 글의 공개 본문 반영 확인
- local-qa.json: 화면 크기별 검증 (실패 후 재검증 이력 포함)
- naver-request-targets.json: 수집 요청 대상 12개
- same-day-table-mobile.png: 모바일 표 표시 검수
- source-notes.json / duplicate-check.json: 근거·중복 의도 검토
