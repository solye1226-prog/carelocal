from pathlib import Path
import json, subprocess
R=Path(__file__).resolve().parents[1]
O=R/'docs/related-next10-2026-11-02'
data=json.loads((O/'manifest.json').read_text(encoding='utf8'))
parents=sorted({p for d in data for p in d['parents']})
lines=['케어로컬 관련 세부키워드 10편 발행 보고','작업 기간: 2026-11-02 ~ 2026-11-03 KST','',
'기존 501편의 실제 본문을 대상으로 중복 검색 의도를 검토하고 독립적인 검사·자료 확인 의도로 10편을 선정했습니다. 검색량·CPC·경쟁도 수치를 새로 측정한 황금키워드 순위는 아닙니다.',
'1~4번 발행일은 11월 2일, 5~10번은 11월 3일입니다. 작업 폴더는 시작 날짜를 유지합니다.','']
for n,d in enumerate(data,1):
 lines += [f'{n}. {d["keyword"]}',f'https://hospital.hbuby.com{d["path"]}',f'제목: {d["title"]}',f'독립 의도: {d["intent"]}','']
lines += ['내부 연결',f'기존 글 {len(parents)}편에 관련 글 링크를 추가했습니다. 기존 본문은 보존하고 관련 링크 영역을 통합했습니다.','\n'.join('https://hospital.hbuby.com'+p for p in parents),'',
'검수','각 글을 별도 커밋으로 순차 발행했습니다. public-1.json~public-10.json은 개별 공개 본문·이미지 검증, public-final.json은 새 글 10편·기존 글 13편·카테고리 3개의 공개 비교 결과입니다.',
'1280·390·360px 화면에서 10편 모두 검수했습니다. 총 30개 화면 조합에 가로 넘침이 없고 표가 모바일 카드 형태로 표시됩니다. 결과와 스크린샷은 responsive 폴더에 있습니다.',
'pnpm run check 통과: HTML 1056개 링크, 사이트맵 536 URL, 글 목록 511편, Python 5개와 Node 10개 테스트.',
'공식 근거 확인 범위와 접근 제한은 source-verification.json에 기록했습니다. 보험 지급은 개별 약관·시행 목적·실제 비용에 따라 달라진다는 조건을 구분했습니다.',
'채용 통보서의 과거 포스터 링크는 404여서 제외했습니다. 현행 공단 서비스 메뉴와 2026년 공공기관 채용공고 PDF 7쪽을 확인했습니다. 해당 기관 사례를 전국 공통 제출 기준으로 일반화하지 않았습니다.','',
'이미지','built-in image generation 모드로 30장 생성 후 WebP로 배치했습니다. 원본 경로·정확한 프롬프트·최종 파일 경로는 image-manifest.json과 image-sources.json에 있습니다. 이미지 장면은 설명용 가상 장면입니다.','',
'수집·색인 구분','이번 요청 범위인 기획·발행·내부링크·공개 검수를 진행했습니다. 이번 10편에 네이버 수집 요청을 별도로 제출하지 않았으며 실제 네이버·구글 색인 여부는 확인하지 않았습니다. 이전 수집 대기 기록은 유지했습니다.','']
(O/'REPORT.txt').write_text('\n'.join(lines),encoding='utf8')
(O/'published-urls.txt').write_text('\n'.join('https://hospital.hbuby.com'+d['path'] for d in data)+'\n',encoding='utf8')
print('Report and URL list saved')
