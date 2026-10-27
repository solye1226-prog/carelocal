# 구글 트렌드 재정렬 소재 6~10 발행 보고

작업 기준: 2026-10-27. 대상: hospital.hbuby.com 정적 Cloudflare Pages.

## 발행 및 연결

| 순서 | 새 글 | 연결한 기존 글 | 발행 커밋 |
|---|---|---|---|
| 6 | [코로나19 무료접종 고위험군·증빙](https://hospital.hbuby.com/guides/covid-vaccine-2026-high-risk-documents) | 독감 무료접종 2026 | 5276f5b |
| 7 | [위고비·마운자로 임신 계획](https://hospital.hbuby.com/guides/glp1-pregnancy-planning-official-guide) | 입원 시 개인약 인계 | 41b510d |
| 8 | [13세 레진 급여 확대 발표](https://hospital.hbuby.com/silbi/age13-composite-resin-coverage-update) | 치과 급여 실비 청구 | 979f420 |
| 9 | [2027 자궁경부암 검진 기록지 개정](https://hospital.hbuby.com/checkups/cervical-screening-report-2027-change) | ASC-US 후속 검사 | b31825b |
| 10 | [검진 비대상자 바이오빅데이터 참여](https://hospital.hbuby.com/checkups/national-biobank-noncheckup-participation) | 2026 건강검진 대상 조회 | 8a39e69 |

각 편을 별도 커밋으로 push하고, 앞선 편의 공개 본문·canonical·이미지·부모 글 링크 반영을 확인한 후 다음 편을 push했습니다. 새 글마다 기존 글로 돌아가는 문맥 링크, 기존 글에는 새 세부 안내로 향하는 링크를 넣었습니다. 기존 글의 원래 main 본문은 새 aside를 제거한 뒤 대조해 보존을 확인했습니다.

## 공식 근거와 시행 단계

- 6: 질병관리청 예방접종도우미. 12세 이상 고위험군 시행과 12세 미만 별도 도입·일정을 구분. 증빙 예외를 누락하지 않음.
- 7: 식약처 의약품안전나라 제품별 국내 허가사항 원문. 임신 계획 전 중단 기간 위고비 최소 2개월·마운자로 최소 1개월을 구분하고 경구피임약 4주 주의와 별개임을 설명. 개인 처방·임신 안전성 보장은 하지 않음.
- 8: 보건복지부 공식 추진방안 PDF 인쇄 17쪽/PDF 19쪽을 텍스트 추출·렌더링 검토. 13세 확대 추진 및 2027 재정 소요는 확인했으나 정확한 적용 개시일은 해당 자료만으로 확정되지 않아 **발표 단계**로 작성. 인접 임플란트 정책의 시행일을 레진에 전용하지 않음.
- 9: 고시 2026-214호·원문 HWP. 2027-01-01 시행 예정. 기록지의 최종 판정 5구분·유형별 진단·권고를 분리. 검진 의심 소견을 확진으로 표현하지 않음.
- 10: 질병관리청 모집 확대 발표와 공식 일반참여자 화면. 건강검진 비대상자 확대 운영, 만 19세 이상 대한민국 국적의 일반참여자 조건 확인. 연구 참여는 검진·진료의 대체가 아님.

세부 URL·확인 범위: [source-audit.md](source-audit.md). 이전 442개 글의 실제 본문 중복 검색 결과: duplicate-body-review.json.

## 품질 확인

- 총 글 카탈로그: 447편. 사이트맵: 472 URL.
- 내부 링크, canonical, 사이트맵 중복, 카탈로그 검사 통과.
- Python canonical 5개·Node 분석 10개 테스트 통과.
- 실제 로컬/공개 화면에서 5편 × 360·390·1280px = 각 15회, 총 30회 검수. 올바른 화면 폭·가로 넘침 없음·H1 하나·본문 이미지 3개 로딩 확인.
- 5편 공개 main 본문이 로컬과 일치. WebP 15개 HTTP 200. 양방향 부모/자식 링크 5쌍 확인.
- 대표 이미지 5개·본문 이미지 10개 생성. 한글과 장면을 모아 시각 확인, 원본 PNG는 별도 보존. WebP quality87 변환.
- 검증 요약: validation-summary.txt / public-audit.json / browser-qa.json.

## 네이버 수집 요청

최종 결과: **7개 접수(새 글 5·기존 글 2), 기존 글 3개 대기**. 치과 급여 실비 기존 글 요청에서 `사이트별 일간 최대 요청 수를 초과하였습니다.` 응답을 확인하여 즉시 중단했습니다. 이후 ASC-US·건강검진 대상 글에는 요청하지 않았습니다. naver-results-all.json, naver-request-pending.txt, naver-quota.txt 및 naver-receipts.png에 근거를 저장했습니다. 각 접수는 요청 내역의 URL·등록 시각으로 확인했습니다. **요청 등록은 실제 수집·색인 완료가 아닙니다.**

사용자가 수정한 docs/POSTING_GUIDELINES.md 및 기존 비관련 작업 파일은 커밋 대상에서 제외했습니다. Google 색인 요청과 광고 설정은 이번 범위에 포함하지 않았습니다.
