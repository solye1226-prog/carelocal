# 도수치료 실비 청구 발행 기록

작성일: 2026-10-05
대상: https://hospital.hbuby.com/silbi/manual-therapy-silbi-claim
제목: 도수치료 실비 청구, 가입 세대별로 무엇을 확인할까?

## 범위와 중복 점검

카탈로그와 silbi HTML에서 도수치료를 검색했습니다. 기존 generation-comparison은 전체 세대 구조, current-silbi는 5세대 구조를 설명합니다. 이번 글은 실제 도수치료 청구의 특약·공제·횟수·추가자료 문의 절차에 집중합니다. 가입 세대를 전체 보험금의 지급표로 사용하지 않습니다.

## 공식 근거와 검토

- 금융위원회 2017년 출시 안내 https://www.fsc.go.kr/po010106/72654 : 기본형과 도수·체외충격파·증식치료 특약 분리, 연간 350만원·50회, max(2만원,30%) 확인. 출시 구조로 범위를 표시하고 실제 계약을 우선.
- 금융위원회 4세대 출시 안내 https://www.fsc.go.kr/no010101/76157 : web 도구 접근 실패 뒤 실제 브라우저에서 본문 열람. 10회마다 병적 완화 효과 확인 시 최대 50회 설명을 확인. 모든 10회에 유료 진단서가 필수라고 쓰지 않음.
- 금융위원회 5세대 출시 자료 https://www.fsc.go.kr/no010101/86831 : 비중증 비급여의 근골격계 물리치료 등 제외 확인. 공식 정책영상 본문 https://www.fsc.go.kr/no010107/86856 에서 도수치료 명시를 확인. 중증·비중증 구분을 유지하고 모든 특약에 동일 제외라고 일반화하지 않음.
- 삼성화재 다이렉트 https://direct.samsungfire.com/m/claim/MP040202_001.html?tab=1 : 실손 통원 영수증·처방전·비급여 세부내역서와 추가 요청 가능 안내 확인. 회사 예시라고 표시하고 원본 제출 금액 조건을 타사에 일반화하지 않음.
- 삼성화재 PDF 후보는 검색했으나 해당 조항의 실제 페이지 확인을 완료하지 않아 본문 근거에 사용하지 않음.
- 1·2세대 전액 보장, 신규 검사 필수, 치료 횟수 목표, 지급 보장 표현 없음. 가상 10만원 계산은 명시적인 가정이고 모든 세대에 적용하지 않음.
- 실제 자격·환자 기록·의료 경험을 만들지 않음. 작성 주체는 조직 케어로컬.

## 편집 및 이미지

상단·하단 보험사 공식 홈페이지 CTA, 하단 카카오 문의와 민감정보 전송 금지 안내를 유지합니다. 새 글은 현재 공개된 청구서류·공제·보완자료·세대 안내로 연결합니다. /silbi/와 기존 세대 비교 글에서 새 글 유입 링크를 추가했습니다.

built-in image_gen 사용. 썸네일 최초 결과의 3세대 이후 묶음과 불필요한 홍보 문구를 편집으로 제거했습니다. 세 장은 AI 설명용이며 실제 문서가 아닙니다. WebP 품질 84, 1672x941.
- assets/images/manual-therapy-silbi-thumb.webp
- assets/images/manual-therapy-silbi-policy.webp
- assets/images/manual-therapy-silbi-inquiry.webp

## 로컬 검증

- 전체 pnpm run check 통과: 170 HTML 링크, 168 sitemap canonical, 143개 카탈로그, Python 5개 및 Node 10개 테스트.
- JSON-LD 파싱, 이미지 3개, 혼입 일본어 문자 없음 확인.
- 실제 390x1000 / 360x800 / 1280x900 화면 검토. 문서 폭 375 / 345 / 1265px로 문서 가로 넘침 없음.
- 질문 버튼 높이 45.09px. 세대별 링크 이동, 표 ArrowRight scrollLeft 40, 헤더 table-header-group 확인.
- 본문 이미지 클릭·스크롤 후 3장 loaded=true, 1672x941 확인. 두 번째 FAQ 펼침 확인.
- 사용자 POSTING_GUIDELINES 변경과 기존 미추적 파일은 커밋 대상에서 제외.

## 공개 확인

- 콘텐츠 커밋 81a3236을 main에 push한 뒤 공개 URL의 제목·canonical·본문 반영 확인.
- 공개 390x1000 / 360x800 / 1280x900 화면에서 문서 가로 넘침 없음.
- 세대별 질문 링크 이동, 표 키보드 가로 스크롤 및 헤더 표시, 이미지 3장 로딩, 두 번째 FAQ 펼침을 실제 검증.
- /silbi/ 목록과 /silbi/generation-comparison의 새 글 유입 링크 공개 반영 확인.
- 증거: docs/manual-therapy-public-mobile-2026-10-05.png, docs/manual-therapy-public-360-2026-10-05.png.
- 질문 링크 클릭 때 기존 전면 광고가 표시돼 광고 닫기 버튼으로 닫고 검증을 계속함. 광고 내용은 클릭하지 않았음.
- 색인 요청·광고 설정 변경은 하지 않았음.

## 이미지 프롬프트

1. Use case: infographic-diagram. Asset: Korean insurance guide thumbnail, wide 16:9. Navy blue vivid blue white and yellow accents. Large perfectly readable Korean text exactly '도수치료 실비 청구' with smaller subtitle exactly '세대별 확인 기준'. Left clear title, right realistic Korean adult at desk comparing generic insurance documents and receipt, smartphone nearby. Editorial card-news, balanced bold typography. No treatment manipulation scene, no diagnosis, no medical amounts, no insurer logos or real app UI, no tiny text, no watermark.

2. Use case: photorealistic-natural. Wide 16:9 overhead Korean household desk scene. Adult hands compare a generic insurance policy booklet with a blank checklist on tablet, blue folder, yellow pen. Clean natural daylight, navy blue white accents, realistic anatomy. No readable personal information, no numbers or diagnosis, no logos, no text labels, no watermark. This illustrates checking coverage and deductible before manual therapy insurance claim, not actual patient documents.

3. Use case: photorealistic-natural. Wide 16:9 Korean home office scene. Adult preparing an insurer inquiry, smartphone held beside neatly arranged generic hospital receipt sheets and notebook, calendar with blank squares. Different angle from overhead: side view with warm daylight, blue folder and restrained yellow accent. No readable screen or document text, no personal information, no diagnosis, no amounts, no logos, no watermark. Illustrates asking what additional medical records are necessary before paid document issuance.

썸네일 편집: Edit the supplied insurance thumbnail. Preserve the large correct text '도수치료 실비 청구' and '세대별 확인 기준', navy/blue/yellow colors, adult comparing generic papers, and wide layout. Remove all three small portrait badges and their labels '1세대', '2세대', '3세대 이후'. Remove the handwritten sales-like text on the right and text on the framed wall artwork, leaving clean neutral decor. Remove bottom checklist words. Use the freed lower-left area as quiet navy negative space. No new text, no labels, no numeric amounts. Do not change anatomy or headline text.
