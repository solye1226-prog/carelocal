# 건강검진 결과 후속 확인 10편 발행 기록

- 작성일: 2026-10-07
- 대상: 건강검진 결과 이상 소견과 후속 검사 검색 의도 10개
- 범위: 개별 문서 10개, 문서별 대표 이미지 1장과 본문 이미지 2장, 건강검진 허브·이상 소견 종합 글·사이트맵·기사 카탈로그 갱신

## 대상 URL

1. `/checkups/health-checkup-high-fasting-glucose`
2. `/checkups/health-checkup-high-blood-pressure`
3. `/checkups/health-checkup-cholesterol-abnormal`
4. `/checkups/health-checkup-high-liver-enzymes`
5. `/checkups/health-checkup-proteinuria`
6. `/checkups/health-checkup-hematuria`
7. `/checkups/fecal-occult-blood-positive`
8. `/checkups/mammography-abnormal-followup`
9. `/checkups/chest-xray-abnormal-followup`
10. `/checkups/health-checkup-result-reissue`

## 공식 출처와 적용 범위

- 국민건강보험공단 일반건강검진·암검진 안내: 국가검진 항목, 질환의심 확진검사, 분변잠혈검사 뒤 대장내시경 안내 등 공단 지원 범위 확인
- 국민건강보험공단 2026년 건강검진 사후관리 안내: 고혈압·당뇨병 확진검사 항목과 대상 확인
- 질병관리청 국가건강정보포털: 고혈당, 이상지질혈증 검사, 간기능검사, 단백뇨와 만성콩팥병 설명 확인
- 국가암정보센터: 대장암·유방암·폐암 검진 권고와 검사 구분 확인

본문에서는 선별검사 결과와 확정 진단을 구분했다. 공단 지원 검사와 의료진이 추가로 정하는 검사 비용도 구분했으며, 개인별 지원 여부와 실제 비용은 공단 조회 및 방문 기관 확인이 필요하다고 명시했다.

## 이미지

- OpenAI 내장 이미지 생성으로 제작
- 공통 방향: 한국 의료기관 상담 장면, 파란색·흰색 정보형 썸네일, 실제 환자나 검사결과지가 아닌 설명용 이미지
- 대표 이미지 문구: `공복혈당 높음`, `혈압 높음`, `콜레스테롤 이상`, `간수치 높음`, `단백뇨 재검`, `혈뇨 판정`, `분변잠혈 양성`, `유방촬영 이상`, `흉부촬영 이상`, `검진 결과표 재발급`
- 저장 위치: `assets/images/<slug>-thumb.webp`, `assets/images/<slug>-body1.webp`, `assets/images/<slug>-body2.webp`
- 규격: 1672×941 WebP

## 로컬 검증

- `pnpm run check`: 통과
- 로컬 링크: 214개 HTML 파일 검사 통과
- 사이트맵·canonical: 212개 URL 검사 통과
- Python canonical 테스트: 5개 통과
- 기사 카탈로그: 187개 항목 일치
- 분석 기능 Node 테스트: 10개 통과
- 대표 이미지 몽타주로 한글 문구와 잘림을 확인함

## 공개 확인

- 발행 커밋: `89951e0`
- 10개 공개 URL: 모두 HTTP 200
- 자기 canonical: 10개 모두 일치
- 본문 이미지: 문서별 3장, 모두 WebP HTTP 200
- 360×800: 10개 모두 문서 너비와 스크롤 너비 일치, 제목·질문 링크·대표 이미지 정상
- 390×1000: 10개 모두 문서 너비와 스크롤 너비 일치, 제목·질문 링크·대표 이미지 정상
- 1280×900: 10개 모두 가로 넘침 없음
- 브라우저 콘솔 오류: 없음
- 자동 앵커 광고가 화면 하단 일부를 덮는 상태가 재현됨. 광고 영역은 클릭하지 않았으며 본문 레이아웃 오류와 구분해 기록한다.
