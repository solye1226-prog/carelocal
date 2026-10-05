# 실비 청구 사진 업로드 오류 글 작업 기록

작업일: 2026-10-05
URL: https://hospital.hbuby.com/silbi/claim-photo-upload-error
제목: 실비보험 청구 사진 업로드가 안 될 때, 첨부 오류와 접수 확인 방법
발행 승인: 사용자의 이번 채팅 요청 "새로운 글 발행하자."

## 범위와 중복 점검

카탈로그와 HTML을 검색하고 청구 절차·보완서류·지급 지연 글을 대조했습니다.
기존 글은 서류 준비 또는 접수 이후 상태를 설명하며, 이번 글은 사진 선택과
파일 첨부 단계 점검 및 최종 접수 확인에 집중합니다. 실손24 병원 검색 문제와도 다릅니다.
검색량·순위·수익 효과를 추정하지 않았습니다.

## 공식 출처와 적용 범위

아래 페이지를 실제 열어 본문을 확인했습니다.
- https://samsungfire.com/claim/P_P03_01_01_001.html
  모바일 촬영, PC 청구, 우편·방문 방식과 절차의 한 보험사 예시.
- https://www.kbinsure.co.kr/CG212030016.ec?mdmn=0202
  본인확인 후 접수 건 진행·결과 조회, 청구일자·사고일자 조회 조건.
- https://support.google.com/android/answer/9431959?hl=ko
  앱별 권한 확인, 사진·동영상·카메라 권한의 의미.
- https://support.google.com/android/answer/13356023?hl=ko
  사진 선택 도구로 선택한 미디어를 공유하는 방식.
- https://support.apple.com/ko-kr/guide/iphone/iph251e92810/ios
  개인정보 보호 및 보안에서 앱 정보 접근 권한 관리.

공통 파일 용량·개수·형식 제한을 확인하지 못했으므로 숫자를 만들지 않았습니다.
JPG·PNG·PDF·HEIC는 확인할 형식의 예시이며 지원 보장이 아닙니다.
재촬영·원본 보관·문의 항목은 편집상 실용 안내이며 보험사 의무 규정이 아닙니다.
기술 오류 해결과 보험금 지급 판단을 구분했습니다.

## 이미지

built-in image_gen 사용, 3장 생성 후 실제 이미지 검토, WebP 품질 84 압축.
모두 1672x941, 개인정보·실제 앱 로고·읽을 수 있는 진단명과 금액 없음.
assets/images/claim-photo-upload-thumb.webp (82,614 bytes)
assets/images/claim-photo-upload-photo.webp (65,196 bytes)
assets/images/claim-photo-upload-call.webp (100,908 bytes)

프롬프트 요약:
- 썸네일: 남색·파랑·흰색·노랑, '실비 청구 사진 / 업로드가 안 된다면?', 휴대전화와 설명용 서류.
- 본문1: 밝은 책상에서 서류 전체를 휴대전화로 촬영, 글자·개인정보는 읽을 수 없게.
- 본문2: 집에서 앱과 서류를 확인하며 문의 기록 준비, 실제 회사 앱을 모방하지 않음.
AI 설명용 이미지임을 본문에 표시했습니다.

## 로컬 검증

- npm은 PATH에 없어 동일 package.json check 스크립트를 번들 pnpm run check로 실행, 통과.
- HTML 168개 로컬 링크, 사이트맵 166개 canonical, Python 5개·Node 10개 테스트 통과.
- 카탈로그 141개, 새 항목 반영.
- 실제 브라우저 390x1000, 360x800, 1280x900 렌더링과 스크린샷 확인.
- 문서 가로 넘침 없음. 모바일 질문 버튼 높이 45.09px.
- 표는 헤더를 유지한 가로 스크롤, 모바일 안내 문구 및 키보드 포커스 제공.
- 질문 링크 대상 4개 존재, 오류 단계·파일 확인 링크 클릭 후 URL fragment 확인.
- 스크롤 뒤 이미지 3장 loaded=true, 자연 크기 1672x941 확인.
- /silbi/ 및 실비 청구서류 글에 유입 링크 추가.
- 기존 POSTING_GUIDELINES.md 변경과 다른 미추적 파일은 보존.

## 배포

배포와 공개 검증 결과는 확인 후 이 기록에 추가합니다.
색인 요청 및 AdSense 설정 변경은 이번 발행 범위에 포함하지 않습니다.
