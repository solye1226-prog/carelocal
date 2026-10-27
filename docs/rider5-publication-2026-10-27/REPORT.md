# 약관 세부 소재 5편 발행 및 네이버 수집 요청

확인일: 2026-10-27(KST). 대상: https://hospital.hbuby.com

## 완료 범위

- 기획한 5편을 1→5 순서로 각각 커밋·푸시했고, 앞 글의 공개 반영을 확인한 뒤 다음 글을 발행했다.
- 기존 대표 글 5편에 신규 글을 설명하는 문맥형 내부링크를 추가했다. 새 글에서도 해당 기존 글로 연결했다. 카테고리 페이지에도 새 글 링크를 넣었다.
- 이전 작업에서 보완한 5편과 새 글 5편, 추가 연결 글 3편을 합쳐 **중복 없는 13개 URL**을 네이버에 수집 요청했고, 각각 요청 내역의 등록 시각을 확인했다.
- 수집 요청 등록은 실제 수집·색인 완료와 다르다. 이번 작업에서 색인 완료를 확인한 것은 아니다.
- 현재 카탈로그 437편, 사이트맵 462개 URL. 글 수와 사이트맵 URL 수에는 카테고리 등 비포스팅 페이지 차이가 있다.

## 순차 발행 글

|순서|글|커밋|기존 연결 글|
|---|---|---|---|
|1|[116대 질병수술비 vs 종수술비](https://hospital.hbuby.com/surgery-benefit/116-disease-vs-tier-surgery-benefit)|e1d91fd|type-surgery-benefit-claim|
|2|[뇌·심장 주요치료비 vs 진단비](https://hospital.hbuby.com/diagnosis-benefit/brain-heart-major-treatment-vs-diagnosis)|4ac9374|cerebrovascular-benefit-claim-documents|
|3|[통합암·전이암 vs 재진단암](https://hospital.hbuby.com/diagnosis-benefit/integrated-cancer-metastasis-vs-rediagnosis)|9326ab0|cancer-diagnosis-benefit-documents|
|4|[남녀생식기암 항암방사선치료비](https://hospital.hbuby.com/diagnosis-benefit/reproductive-cancer-radiation-rider-check)|56db310|heavy-ion-therapy|
|5|[3대질병 통원일당과 병원급](https://hospital.hbuby.com/diagnosis-benefit/three-disease-outpatient-daily-hospital-tier)|427e7e4|actual-vs-fixed-benefit|

## 약관 검증

원문은 보험사의 공개 상품 PDF에서 직접 확보했다. 파일 해시·적용일·공식 URL은 `official-source-record.json`, 발췌 위치는 `manifest.json`에 남겼다. 전체 PDF는 로컬 증거로 보존하고 공개 저장소에는 올리지 않는다.

- [KB 5.10.10 플러스 건강보험 26.09 공식 약관](https://www.kbinsure.co.kr/pop/CR301010002.ec?pdcd=25434): 2026-10-01 적용. 특별약관 73-1~73-6 및 199의 지급사유·감액·연간 정의·치료 범위 확인.
- [KB 9회주는 암보험Plus 26.07 공식 약관](https://www.kbinsure.co.kr/pop/CR301010002.ec?pdcd=25290): 2026-08-01 적용. 특별약관 119 통합암, 25 재진단암, 63·64 생식기암 방사선, 암 및 뇌·심장 통원 특약 확인.
- [보건복지부 상급종합병원 지정](https://www.mohw.go.kr/menu.es?mid=a10702030300): 병원 이름을 보고 급을 추정하지 않고 통원일의 지정 상태를 확인하도록 안내.
- PDF의 인쇄 본문 쪽수와 뷰어 쪽수는 2쪽 차이. 글마다 정확한 특약 번호·쪽수·적용 판본 및 공식 원문 버튼을 제공했다.

중요한 구분을 본문에 반영했다. 116대 특약의 Ⅰ~Ⅵ는 종수술 등급이 아니다. 주요치료비는 진단일 기준 연간이며 최초 1년 미만 진단의 감액이 지급 대상기간 동안 적용되는 예시다. 통합암은 세부 그룹별 최초 1회와 소멸을 확인하며 전이만으로 반복 지급되지 않는다. 방사선치료의 분할 횟수와 최초 1회형 보험금 횟수는 다르다. 뇌·심장 통원의 연간 30일을 모든 암 통원에 일반화하지 않았다.

현재 공개 판본을 가입자의 과거 약관에 소급 적용하지 않도록 구별했다. 가상 예시는 실제 지급 사례로 표현하지 않았고, 개별 지급·치료 적합성을 보장하지 않았다.

## 공개·가독성 검증

- 실제 공개 HTML의 제목·본문 전체 텍스트가 로컬 최종 원고와 일치: 5/5.
- 정확한 canonical 및 기존 글의 신규 링크 공개 반영 확인: 5/5.
- 신규 이미지 15개 공개 응답: 15/15 정상. 한글 썸네일 5개와 본문 생성 장면 10개를 눈으로 확인했다.
- 로컬 360/390/1280px, 공개 390/1280px에서 가로 넘침 없이 확인. 모바일 표의 카드형 표시도 확인했다. `local-layout.json`, `public-layout.json`, 화면 캡처 참조.
- `public-verification.json`은 제목·본문·이미지·역링크의 실제 공개 검사 결과다.
- 링크 검사 통과, 462개 사이트맵 canonical 검사 통과, 카탈로그 일치, canonical 단위검사 5개 및 analytics 검사 10개 통과.

이미지 생성 모드는 built-in `image_gen`. 원본을 보존하고 WebP로 복사했으며 정확한 프롬프트·원본 경로·장면·최종 파일은 `image-generation-record.json`, `image-provenance.json`에 기록했다. 이미지가 환자 실사 기록이 아닌 설명용 생성물임을 본문에 표시했다.

## 네이버 접수 증거

`naver-receipts.json`과 `naver-01.txt`~`naver-13.txt`에 각 요청 후 실제 등록된 URL·시각을 저장했다. 새 글 5편, 이전 보완 글 5편, 그 외 연결 글 3편이다. 앞서 접수한 2편은 새 글의 연결 대상으로도 사용돼 중복 계산하지 않았다. `naver-final.png`는 요청 내역 화면이다.

접수 13개 / 이번 범위 미접수 0개. 수집·색인 결과는 이후 별도로 확인해야 한다. 광고 설정 및 Google 색인 요청은 이번 작업에서 변경하지 않았다.
