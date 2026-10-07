# 2026-10-07 글 10개 발행 및 검색 등록 기록

## 발행 순서

| 순서 | 글 | 발행 커밋 |
|---|---|---|
| 1 | [2026 독감 무료접종](https://hospital.hbuby.com/guides/flu-vaccination-2026) | `b6b614d` (접종 일정 정정 `8961afe`) |
| 2 | [독감 검사비 실비 청구](https://hospital.hbuby.com/silbi/flu-test-cost-claim) | `808988c` |
| 3 | [CT 검사비 실비 청구](https://hospital.hbuby.com/silbi/ct-scan-cost-claim) | `9ff3b4b` |
| 4 | [복부초음파 검사비](https://hospital.hbuby.com/silbi/abdominal-ultrasound-cost-claim) | `1887872` |
| 5 | [약값 실비 청구](https://hospital.hbuby.com/silbi/pharmacy-prescription-claim) | `0d6abe2` |
| 6 | [응급실 비용 실비 청구](https://hospital.hbuby.com/silbi/emergency-room-cost-claim) | `c790a58` |
| 7 | [스케일링 건강보험](https://hospital.hbuby.com/treatment-costs/scaling-health-insurance-2026) | `887e22d` |
| 8 | [임플란트 건강보험 적용](https://hospital.hbuby.com/treatment-costs/dental-implant-health-insurance) | `3c93c93` |
| 9 | [치아보험 면책·감액기간](https://hospital.hbuby.com/standards/dental-insurance-waiting-reduction) | `a8c0a0c` |
| 10 | [해외여행 중 병원비 청구서류](https://hospital.hbuby.com/claims/overseas-hospital-bill-documents) | `a73488e` |

## 검증

- 10개 공개 페이지 모두 HTTP 200, 각자에게 맞는 canonical URL, 이미지 3개 각각 HTTP 200.
- 공개 사이트맵은 199개 URL을 담고 있으며 이번 10개 URL이 모두 포함됨. 관련 카테고리 5개 사이트맵 수정일은 `8dc03eb`에서 2026-10-07로 갱신함.
- `pnpm run check` 통과: HTML 파일 201개의 내부 링크, sitemap/canonical URL 199개, 글 카탈로그 174개, 관련 테스트.
- 공개 화면의 첫 화면을 글마다 확인했고, 360px/390px 모바일 및 1280px 데스크톱에서 본문·제목이 뷰포트 안에 들어옴. Google 자동 광고 iframe은 별도 가로 넘침을 만들 수 있으므로 페이지 전체의 가로 스크롤이 완전히 없다고 단정하지 않음.

## 검색 등록

- **네이버 서치어드바이저:** 2026-10-07 11:16:08~11:18:41(KST) `웹 페이지 수집` 요청 내역에 위 10개 URL이 모두 표시됨. [요청 내역 화면](oct7-naver-ten-crawl-requests.png). 이미 등록된 사이트맵도 사이트 요약에서 확인함. 수집 요청 접수는 실제 수집·색인 완료와 다름.
- **Google Search Console:** 갱신된 [`sitemap.xml`](https://hospital.hbuby.com/sitemap.xml)을 다시 제출했고 `사이트맵이 제출됨` 확인. [제출 화면](oct7-gsc-sitemap-submitted.png). 제출 목록의 제출일은 2026-10-07, 마지막 읽은 날짜는 2026-10-06, 이전에 발견된 페이지 수는 179로 표시됨. 새 10개 글 반영 여부는 Google의 다음 읽기 이후 확인 필요.
- Google 개별 URL 검사는 `속성의 URL 검사 용량을 초과했습니다. 용량은 매일 갱신됩니다.` 메시지로 진행되지 않음. 개별 URL 색인 요청 완료로 기록하지 않음.

모바일 공개 화면 기록: `oct7-01-public-390.png`부터 `oct7-10-public-390.png`까지.
