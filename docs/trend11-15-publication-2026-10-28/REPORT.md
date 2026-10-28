# 재정렬 소재 11~15 순차 발행 보고 — 2026-10-28

## 완료

| 순서 | 발행 글 | 연결한 기존 글 | 커밋 |
|---|---|---|---|
| 11 | [호스피스 병원 찾기](https://hospital.hbuby.com/guides/hospice-provider-type-cost-check) | 퇴원 전 가정간호 | 1c7a0fc |
| 12 | [희귀질환 산정특례 재등록 서류](https://hospital.hbuby.com/treatment-costs/rare-disease-reregistration-evidence) | 암 산정특례 등록 | 0fd60f2 |
| 13 | [빌로이 건강보험 급여 확인](https://hospital.hbuby.com/treatment-costs/vyloy-health-insurance-eligibility) | 위암 | c4fc9bf |
| 14 | [파드셉·키트루다 병용 급여](https://hospital.hbuby.com/treatment-costs/padcev-keytruda-combination-coverage) | 방광암 | c48f2f1 |
| 15 | [자스케이드 허가·공급·비용 확인](https://hospital.hbuby.com/treatment-costs/jascayd-nerandomilast-cost-check) | 약국 처방약 실비 | 4a864a9 |

각 글을 한 편씩 별도 커밋으로 push하고 앞선 글의 공개 main 본문·canonical·이미지·부모 글 링크 반영을 확인한 뒤 다음 글을 push했습니다. 기존 글에는 맥락을 설명하는 새 aside를 추가하고 새 글도 부모 글로 연결했습니다. 기존 main 본문은 새 aside만 제거한 상태에서 원본과 같음을 확인했습니다.

## 공식 근거와 시행 상태

- 호스피스: 중앙호스피스센터 현재 기관 검색과 유형 안내, 국가암정보센터 이용 절차 확인. 기존 제도이며 새 서비스 개시로 표현하지 않음. 과거 연도 비용 예시를 현재 견적으로 사용하지 않음.
- 재등록: 공단 공고 의료비지원실-2026-제10호, 9월15일 시행 현행 기준표 XLSX 원문 확인. 질환별 신규·재등록 칸을 대조하고 검사 간소화와 재등록 신청 생략을 구분.
- 빌로이 및 병용요법: 심평원 공고2026-210호 10월1일 시행. 공고의 공식 HWP 원문에서 검사·암종·차수·병용요법·과거 치료 조건 확인. 개인 적용·효과·보험금 보장으로 단정하지 않음.
- 자스케이드: 식약처 10월15일 국내 품목허가와 효능효과 확인. 제품별 급여 개시일·공급 일정·개인 약값을 확정할 근거는 확보하지 못해 확인 질문과 공식 조회 경로로 범위를 제한. 비급여라고도 단정하지 않음.

출처 URL과 검증 범위는 source-audit.md, 원문·추출·공식 UI 자료는 같은 폴더에 보존했습니다. 신규 기획의 중복 검색은 447편의 실제 HTML main 본문·제목에서 수행했습니다. duplicate-body-review.json 참조.

## 검수

- 카탈로그452편, 사이트맵477URL.
- 내부링크741 HTML 파일 검사 통과, canonical·사이트맵 중복·카탈로그 검사 통과.
- Python5개·Node10개 테스트 통과.
- 로컬/공개 각5편 ×360·390·1280px, 총30회 실제 화면 검수. 화면 폭이 요청 값과 일치, 페이지 가로 넘침 없음, H1하나, 이미지3개 정상 로딩.
- 공개 본문5편 로컬과 일치, WebP15개 HTTP200, 부모/자식 양방향 링크5쌍 확인.
- 이미지15개(대표5·본문10)는 생성 후 한글·장면을 시각 검토, 원본 보존 후 WebP 변환.
- 검증 기록: public-audit.json / browser-qa.json / validation-summary.txt / publication-proof.png.

## 네이버 수집 요청 — 10개 접수 완료

관리 계정 로그인 후 2026-10-28 12:27:33~12:29:42(KST)에 새 글5편과 내부링크 보완 기존 글5편의 수집 요청을 순서대로 제출했습니다. 각 URL의 등록 내역과 등록 시각을 확인한 뒤 다음 주소로 진행했습니다. **접수10개·대기0개·오류0개**입니다.

최종 기록: naver-results.json, naver-01~10-accepted.txt, naver-final-receipts.txt/png. naver-request-pending.txt는 비웠습니다. 이전 로그인 필요 증거는 당시 상태의 기록으로 보존합니다. **요청 접수는 실제 수집·색인 완료를 뜻하지 않습니다.**

이전 작업의 미제출3개는 이번10개와 별도 목록이며 임의로 추가 제출하지 않았습니다.

사용자 수정 docs/POSTING_GUIDELINES.md와 다른 기존 작업 파일은 변경·스테이징하지 않았습니다. 광고 설정과 Google 색인 요청을 실행하지 않았습니다.
