# 수면다원검사 글 발행 기록 — 2026-10-05

- 제목: 수면다원검사 비용과 실비 청구 전 확인할 사항
- 공개 URL: https://hospital.hbuby.com/silbi/sleep-study-cost-insurance
- 사용자 요청: 다음 글 진행. 후보 순서 4의 새 글을 작성·발행.
- 중복 점검: 기존 HTML·카탈로그의 수면다원검사, 수면무호흡증, polysomno 검색에서 같은 주제 없음.
- 범위: 급여 조건, 총비용 문의, 실비 약관·청구자료, 재검사와 입원·통원 판단 확인. 특정 계약의 지급이나 개인 진단을 확정하지 않음.

## 공식 근거 확인

2026-10-05 원문 확인.
- 심평원 FAQ(2026-09-15): https://www.hira.or.kr/bbsDummy.do?brdBltNo=47808&brdScnBltNo=4&pgmid=HIRAA010006011130
  - 증상만으로 급여 확정 불가. 진찰·관련 병력 등 조합과 검사·시설·인력 조건 확인.
- 심평원 나629 기준(2023-293, 2024-01-01 시행): https://www.hira.or.kr/rc/insu/insuadtcrtr/InsuAdtCrtrPopup.do?mtgHmeDd=20231229&mtgMtrRegSno=0019&sno=6
  - 팝업의 최신 기준 블록 사용. 아래의 과거 기준과 혼합하지 않음.
  - 진단 1회, 양압기 적정압력 측정과 처치·수술 후 각 1회. 6개월 이후에도 급격한 상태 변화와 임상적 필요에 따른 사례별 인정.
- 질병관리청: https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=6308
  - 건강보험 본인부담률 20% 설명. 급여 조건을 충족한 검사 항목으로 한정하고 총 영수증·실비 공제와 구분.
- 삼성화재 다이렉트: https://direct.samsungfire.com/m/claim/MP040202_001.html?tab=1
  - 입원·통원 자료와 상품·사고별 추가서류 안내. 회사 사례를 모든 보험사 공통 의무로 일반화하지 않음.
- 병원 가격 검색 결과는 원문 확인에 실패하여 사용하지 않음. 60만원×20%=12만원은 가상 계산이라고 명시.
- 의료 이미지·원문 전체를 복사하지 않고 사실을 요약. 경험·자격·심사 결과를 창작하지 않음.

## 변경과 로컬 검증

- 새 HTML, 대표 이미지와 본문 이미지 총 3장, 실비 허브 및 급여·비급여 기존 글의 유입 링크.
- sitemap, article-catalog 갱신. 카탈로그 144개.
- 글 전용 모바일 CSS, 질문별 2열 링크, 가로 스크롤 표와 헤더 보존.
- 상하단 보험사 CTA 및 하단 카카오 문의·민감정보 안내.
- pnpm run check PASS: 171 HTML 링크, 169 sitemap canonical, Python 5개·Node 10개 테스트.
- 실제 브라우저 390×1000, 360×800, 1280×900 확인. 문서 너비는 각각 375/345/1265로 viewport 초과 없음.
- 390 화면의 표 폭 345, 콘텐츠 540, 키보드 좌우 스크롤 39 확인. 헤더 3개.
- 이미지 3장 모두 1672×941 로드 확인. FAQ 펼침 확인.

## 이미지 파일과 생성 프롬프트

설명용 AI 이미지임을 본문에 표시. WebP quality 84.
- assets/images/sleep-study-thumb.webp
  - 원본: C:/Users/Solemee/.codex/generated_images/01a10aab-8d8f-7252-90a9-c3f3197c11f6/exec-df996c7a-370d-4e7b-8434-717e40c3e114.png
  - 프롬프트: Use case: infographic-diagram. Wide 16:9 Korean insurance information thumbnail. Navy blue vivid blue white with yellow accents. Large clear Korean title exactly '수면다원검사' and subtitle exactly '비용·실비 확인'. Adult reviewing generic hospital cost estimate at desk, calm clinic consultation scene with a softly blurred empty examination bedroom in background. Balanced title left scene right. Only these two text phrases, no extra labels, no prices, no generation badges, no guarantees, no readable personal medical data, no logos, no invasive equipment, no watermark.
- assets/images/sleep-study-consult.webp
  - 원본: C:/Users/Solemee/.codex/generated_images/01a10aab-8d8f-7252-90a9-c3f3197c11f6/exec-32fced17-051e-4b7f-9979-4ae7642a3f71.png
  - 프롬프트: Use case: photorealistic-natural. Wide 16:9 quiet modern Korean clinic consultation room. Adult patient speaking to clinician across desk before a sleep study, pointing at generic blank estimate with blue folder and yellow pen. Natural light, respectful practical mood. No actual medical procedure, no readable text, no diagnosis or amounts, no personal records, no logos, no watermark. Illustrates asking whether insurance covers scheduled test and what the total cost includes.
- assets/images/sleep-study-documents.webp
  - 최종 원본: C:/Users/Solemee/.codex/generated_images/01a10aab-8d8f-7252-90a9-c3f3197c11f6/exec-b9e9ee50-a155-496b-8b13-35b1a4150c50.png
  - 최초 프롬프트: Use case: photorealistic-natural. Wide 16:9 overhead home desk view of adult hands comparing generic hospital receipt, itemized invoice and result envelope with smartphone ready for insurer inquiry. Navy blue folder, white papers, yellow pen, warm natural light. No readable text, numbers, personal data, diagnosis, logos or real insurer UI, no watermark. Distinct composition from clinic consultation. Explains document preparation for sleep study insurance claim.
  - 편집 프롬프트: Edit this image while preserving overhead desk, two hands, papers, navy folder, yellow pen and natural lighting. Replace all receipt and invoice typography, numbers and table contents with clean abstract light-grey bars that are clearly not readable. Remove the dark medical waveform panel on the right sheet and replace with a blank abstract grey header and three simple pale grey bars. Make no readable words, monetary values, diagnosis or medical waveform. Keep phone generic abstract shapes, no chat instructions. No new text, logos or personal information.
  - 최초 출력에 유사 숫자·파형이 있어 수정. 최종 이미지에서 읽을 수 있는 숫자·문구와 의료 파형 제거 확인.

## 배포와 공개 검증

콘텐츠 배포와 공개 페이지 확인 후 이 항목을 갱신합니다.
