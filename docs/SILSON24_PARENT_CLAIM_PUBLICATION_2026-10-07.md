# 실손24 부모님 대리 청구 발행 기록

- 작성·확인일: 2026-10-07 (KST)
- 대상: `/silbi/silson24-parent-third-party-claim`
- 검색 의도: 부모님 실비 청구서를 자녀가 작성할 때 누가 최종 전송하는가. 기존 실손24 전송 실패·병원 미검색 글은 이 질문에 직접 답하지 않는다.
- 공식 출처: [실손24 서비스 소개](https://www.silson24.or.kr/claim/web/system/systemIntro)에서 나의부모/제3자 청구, 본인 직접 전송, 휴대전화 미소지 시 어려움, 제3자 보험금 수령 불가를 확인했다. [고객지원](https://www.silson24.or.kr/claim/web/custSupp)에서 문의 경로를 확인했다.
- 이미지: imagegen으로 대표 1장·서로 다른 본문 장면 2장을 제작해 각각 1672×941 WebP로 저장했다. 설명용 생성 장면임을 본문에 표시했다.
- 로컬 검사: `pnpm run check` 통과. Edge/Playwright로 360×800, 390×1000, 1280×900 렌더링을 확인했다. 360px·390px에서 본문 가로 넘침 없음. 지연 이미지 마지막 장은 스크롤 후 로딩 확인.
- 로컬 화면: `.deploy/parent-claim-360-first.png`, `.deploy/parent-claim-390-first.png`.
- 공개 배포·공개 모바일 검증: 진행 후 기록.
