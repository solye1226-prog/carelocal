# 건강검진 후속 확인 2차 10편 발행 기록

- 작성일: 2026-10-07
- 대상: 신장기능, 빈혈, 지방간, 담낭용종, 골감소증, 장상피화생, ASC-US, PSA, TSH, 신장낭종
- 범위: 개별 문서 10개, 문서별 이미지 3장, 건강검진 허브·이상 소견 종합 글·사이트맵·기사 카탈로그 갱신

## 대상 URL

1. `/checkups/health-checkup-low-egfr`
2. `/checkups/health-checkup-low-hemoglobin`
3. `/checkups/fatty-liver-ultrasound-followup`
4. `/checkups/gallbladder-polyp-ultrasound-followup`
5. `/checkups/osteopenia-bone-density-followup`
6. `/checkups/gastric-intestinal-metaplasia-followup`
7. `/checkups/cervical-screening-ascus-followup`
8. `/checkups/high-psa-followup`
9. `/checkups/thyroid-tsh-abnormal-followup`
10. `/checkups/kidney-cyst-ultrasound-followup`

## 출처와 작성 범위

- 국민건강보험공단: 일반건강검진 및 암검진의 국가검진 범위 확인
- 질병관리청 국가건강정보포털: 만성콩팥병, 빈혈, 총혈구검사, 대사이상지방간질환, 복부초음파검사, 담낭용종, 골다공증, 위염, 종양표지자검사, 갑상선기능저하증·항진증 확인
- 국가암정보센터: 자궁경부암 검진과 ASC-US 후속 평가 확인
- 서울대학교병원: 낭종의 일반적인 정의와 단순 낭종 관리 범위 확인

본문에서는 선별·검진 결과와 확정 진단을 구분했다. 국가검진 기본 항목과 민간 종합검진·추가 진료 검사를 구분하고, 실제 검사 비용은 진료 목적과 급여 기준에 따라 달라진다고 명시했다.

## 이미지

- OpenAI 내장 이미지 생성으로 제작
- 대표 이미지 10장, 상담 장면 10장, 검사 준비 장면 10장
- 준비 장면에서 생성된 가짜 글자를 발견해 10장 모두 글자 없는 아이콘·빈 체크리스트로 다시 편집함
- 저장 위치: `assets/images/<slug>-thumb.webp`, `assets/images/<slug>-body1.webp`, `assets/images/<slug>-body2.webp`
- 규격: 1672×941 WebP

## 로컬 검증

- `pnpm run check`: 통과
- 로컬 링크: 224개 HTML 파일 검사 통과
- 사이트맵·canonical: 222개 URL 검사 통과
- Python canonical 테스트: 5개 통과
- 기사 카탈로그: 197개 항목 일치
- 분석 기능 Node 테스트: 10개 통과
- 대표·상담·준비 이미지 몽타주를 확인하고 주제 매칭과 한글 제목을 검수함

## 공개 확인

배포 후 각 URL의 HTTP 응답, canonical, 이미지 응답과 360×800·390×1000·1280×900 실제 렌더링을 확인한다.
