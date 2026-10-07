# 1인실 병실료 차액 발행 기록

- 작성·확인일: 2026-10-07 (KST)
- 대상: `/silbi/single-room-charge-difference`
- 검색 의도: 입원 전 1인실 비용·기준병실 차액을 확인하고, 퇴원 후 해당 차액을 본인 실손보험 약관에 대조하는 방법. 기존 입원비 청구서류·본인부담상한제 글과 질문을 분리했다.
- 공식 출처: [국민건강보험공단 병실료 안내](https://www.nhis.or.kr/static/images/banner/longdesc/20190701_pop01longdesc.html)에서 2·3인실 적용 자료의 시점을 확인했다. [본인부담상한제 안내](https://www.nhis.or.kr/static/html/wbma/c/wbmac0209.html)에서 상급병실료 차액의 산정 제외를 확인했다. [삼성화재 상품 안내](https://direct.samsungfire.com/mall/PP030404_001.html?ver=522)는 한 상품의 보장 예시로만 사용했다.
- 이미지: imagegen으로 대표 1장·서로 다른 본문 장면 2장을 제작해 1672×941 WebP로 저장했다. 설명용 생성 장면임을 본문에 표시했다.
- 로컬 검사: `pnpm run check` 통과. Edge/Playwright 360×800, 390×1000, 1280×900에서 제목·첫 화면, 본문 너비, 이미지 3개 로딩 확인.
- 발행 커밋: `6d1073c` (`main` push).
- 공개 배포 확인: 대상 페이지 HTTP 200, canonical 일치, 공개 이미지 3개 모두 HTTP 200, 공개 sitemap 포함.
- 공개 모바일: 360×800·390×1000에서 본문 가로 넘침 없음. 증빙 `.deploy/single-room-public-360.png`, `.deploy/single-room-public-390.png`.
- 개별 검색 색인 여부는 확인하지 않았다.
