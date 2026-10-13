# 핵심 검색 유입 주제 후속 10편 발행

## 완료 범위

기획서 순서대로 10편을 한 편씩 작성·검사·커밋·배포했다. 매번 공개 head·main 일치를 확인한 뒤 다음 글로 진행했다. 이후 기존 대표 글 8편에 관련 설명 직후 후속 링크 10개를 추가했다. 새 글에서도 각 대표 글로 돌아갈 수 있다. 연결 배포 커밋은 `596af4e`다.

검색어 자료는 실제 도착 URL 자료가 아니므로 연결한 기존 글의 클릭 수를 확정하지 않는다. 검색량·CPC·경쟁도가 측정된 황금키워드라고 주장하지 않는다. Google Ads·AdSense 설정은 변경하지 않았다.

## 발행 순서와 URL

1. [담도 스텐트 제거·교체 수술비](https://hospital.hbuby.com/surgery-benefit/biliary-stent-removal-replacement-benefit)
2. [담낭용종 수술 보험청구](https://hospital.hbuby.com/claims/gallbladder-polyp-surgery-insurance-documents)
3. [담낭 수술 중 개복 전환](https://hospital.hbuby.com/surgery-benefit/gallbladder-laparoscopy-open-conversion-benefit)
4. [ERCP 반복 시술 수술비](https://hospital.hbuby.com/surgery-benefit/repeated-ercp-surgery-benefit)
5. [후발백내장 레이저 치료 수술비](https://hospital.hbuby.com/surgery-benefit/secondary-cataract-laser-benefit)
6. [백내장 수술 전 검사비 실비](https://hospital.hbuby.com/silbi/cataract-preoperative-test-claim)
7. [카티스템과 함께 시행한 수술기록](https://hospital.hbuby.com/surgery-benefit/cartistem-concurrent-procedure-records)
8. [카티스템 실비 치료 필요성 추가자료](https://hospital.hbuby.com/silbi/cartistem-medical-necessity-supplement)
9. [같은 수술의 계약별 종수 비교](https://hospital.hbuby.com/surgery-benefit/same-surgery-different-policy-tiers)
10. [영문 수술기록지 보험청구](https://hospital.hbuby.com/claims/english-operative-record-insurance-check)

## 근거와 편집

- 서울아산병원 ERCP 안내에서 검사와 결석 제거·확장·스텐트 삽입의 구분을 확인했다. 제거·반복 지급 횟수는 병원 설명으로 단정하지 않았다.
- 서울대학교병원 담낭절제술 안내에서 담낭용종과 개복 전환 설명을, 백내장 수술 안내에서 후낭혼탁과 후속 레이저 치료를 확인했다.
- 카티스템은 식약처 품목정보 `itemSeq=202106062`의 효능효과·투여방법과 제조사 상세 페이지를 대조했다. 투여 과정의 구멍 형성과 별도 미세천공술을 자동으로 동일시하거나 동시 지급을 약속하지 않는다.
- 삼성화재 담보별 서류 안내는 한 회사의 제출서류 예시로만 사용했다. 서울대학교병원 기록 발급 안내도 해당 병원의 절차로 한정했다.
- 계약별 종수 글은 두 계약을 대조하는 방법이며 특정 회사 간 확정 종수 비교표가 아니다. 영문 기록은 약어 자동 번역이나 모든 청구의 공증 번역을 권하지 않는다.
- 각 글에 실제 기록에서 찾을 항목, 쟁점 비교표, 보험사에 물어볼 문장, 다음 행동, 공식 상세 버튼을 제공했다. 공식 버튼은 총 28개이며 출처의 설명 범위를 함께 표시했다.
- imagegen 기본 도구로 주제별 썸네일 10개를 생성·검토하고 `assets/images/<각 slug>-thumb.webp`에 저장했다. 프롬프트는 주제별 짧은 한글 제목, 남색·파랑·노랑 색상, 서류를 확인하는 설명 장면, 실제 개인정보·지급액·의료 처치 장면 제외를 지정했다. 본문 이미지는 관련 기존 설명 이미지 2개를 활용해 글마다 3장 배치했다.

## 검증

- 최종 `pnpm run check`: HTML 304개 링크, 사이트맵·canonical 302개, Python 5개·Node 10개 테스트, 카탈로그 277편 모두 통과.
- 로컬 새 글 10편 × 360·390·1280px: 30/30 통과. 이미지 로드·가로 넘침·공식 버튼 크기·화면 안 배치 확인.
- 공개 새 글 10편 × 3개 폭: 30/30 통과. 기존 대표 글 8편 × 3개 폭: 24/24 통과 및 후속 링크 확인.
- 새 글 10편과 대표 글 8편 공개 HTTP 200, head·main 일치 18/18. noindex 응답 헤더 없음.
- 모바일 대표 화면과 썸네일 10개를 육안 검토했다. 렌더링 검사는 광고 네트워크 요청을 제외한 편집 콘텐츠 기준이며 광고 포함 전체 페이지 경험이나 실사용자 Core Web Vitals를 입증하지 않는다.
- 색인 요청·검색 색인 완료·검색 순위·클릭 증가·수익 발생은 이번 발행 검증에 포함하지 않는다.

## 증거 파일

- `CLUSTER_10_PUBLICATION_2026-10-13.json`: 순서·URL·각 발행 커밋·공개 본문 검증.
- `CLUSTER_10_SOURCES_2026-10-13.json`: 공식 출처 7개와 적용 범위.
- `CLUSTER_10_LOCAL_1_2026-10-13.json`부터 `CLUSTER_10_LOCAL_10_2026-10-13.json`: 글별 로컬 렌더 검사.
- `CLUSTER_10_PUBLIC_2026-10-13.json`: 새 글 공개 렌더 검사.
- `CLUSTER_10_PARENT_RENDER_2026-10-13.json`: 대표 글 공개 연결·가로 넘침 검사.
- `CLUSTER_10_PUBLIC_FINAL_2026-10-13.json`: 18개 공개 URL 최종 대조.
- `cluster10-public-1-390.png`부터 `cluster10-public-10-390.png`: 새 글 공개 모바일 화면.
- `cluster10-public-existing-ercp-links-390.png`: 기존 ERCP 글의 문맥상 링크 화면.
