from pathlib import Path
from bs4 import BeautifulSoup
import json,re,subprocess,sys
from publish_trend5_20261027 import h,p,a,ul
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/youtube6-publication-2026-11-02'
HANIL='https://health.hanilmed.net/health/contents.do?menuNo=60300000'
CHANGES=[
('/claims/medical-expense-claim-documents','실비보험 청구서류, 영수증·세부내역서·처방전 준비 순서','실비보험 청구서류는 통원·입원·약제비로 나눠 준비합니다. 진료비 영수증과 세부내역서, 진단명 자료의 역할을 구분하고 보험사별 소액 청구·추가서류 조건을 확인하세요.',
h('보험사별 소액 청구 조건은 공통 목록과 나눠 읽으세요')+p('이 글의 기본 서류 역할과 특정 보험사의 생략 조건을 구분하세요. 같은 금액의 통원비라도 회사별 기준·계약·추가 확인사항이 다를 수 있습니다. “소액이면 영수증만 제출”이라는 규칙을 모든 청구에 적용하지 않습니다.')+p(a('/claims/epost-silbi-claim-documents','우체국 실비 청구서류')+'에서 우체국의 입원·통원·약제비 목록과 동일 질병 기준 처방전 생략 조건을 따로 확인할 수 있습니다. 다른 회사 계약은 그 회사의 현재 안내를 먼저 확인하세요.')),
('/surgery-benefit/cataract-surgery-benefit','백내장 수술비 몇종? 인공수정체삽입술과 약관 분류표 확인','백내장 수술비 몇종인지는 가입 특약의 수술분류표와 실제 시행명으로 확인합니다. 인공수정체 종류, 양안 수술일, 레이저 후발백내장 처치를 구분해 청구자료를 정리하세요.',
h('백내장 수술비 몇종 문의에 먼저 적을 세 가지')+p('보험사에 종수를 묻기 전 ① 보험증권의 정확한 특약명·가입 시기 ② 수술확인서의 실제 시행명·수술일 ③ 약관 수술분류표의 후보 항목을 나란히 적어 보세요. “백내장”이라는 진단명과 렌즈 가격만 적으면 적용한 항목을 확인하기 어렵습니다.')+p('양안 수술이라면 좌우·날짜를 기록하고 지급 횟수 조항을 따로 문의합니다. 이 과정은 병원 기록을 약관과 대조하기 위한 정리 방법이며 모든 계약에 공통인 종수나 지급 횟수를 제시하는 것은 아닙니다.')),
('/silbi/abdominal-ultrasound-cost-claim','상복부 초음파 실비·비용, 검진과 진료 목적 및 청구서류','상복부 초음파 실비는 검사 목적과 실제 급여·비급여 항목을 확인합니다. 하복부·전립선 초음파와의 구분, 비용 비교와 영수증·세부내역서 준비 순서를 정리합니다.',
h('상복부 초음파 실비와 다른 부위 초음파를 구분하세요')+p('상복부 초음파 실비를 검색했더라도 실제 영수증의 검사 부위를 먼저 확인하세요. 상복부 장기 검사와 전립선·정낭 초음파는 같은 검사 항목이 아닙니다. 한 부위의 급여 조건이나 공개가격을 다른 부위에 옮기지 않습니다.')+p(a('/silbi/prostate-ultrasound-cost-claim','전립선 초음파 비용·실비')+'는 전립선 검사 목적과 병원별 비용 항목을 따로 다룹니다. 검진 패키지 안에 여러 검사가 있다면 각 시행명과 별도 진료비를 구분해 확인하세요.')),
('/checkups/health-checkup-fasting-medication','건강검진 금식·복용약·전날 술, 검사 전 확인할 사항','건강검진 금식과 복용약, 전날 술을 마셨을 때 예약 병원에 알릴 내용을 정리합니다. 검사별 준비와 물·약 복용 계획을 구분하고 음주 후 검사 일정은 의료진에게 확인하세요.',
h('건강검진 전날 술을 마셨다면 병원에 먼저 알리세요')+p(a(HANIL,'한일병원 일반건강검진 주의사항')+'은 검진 2~3일 전부터 과음을 피하도록 안내합니다. 이는 해당 병원의 준비 안내이며 모든 검사에 공통인 금주 시간표를 뜻하지 않습니다. 본인이 예약한 기관의 안내를 우선 확인하세요.')+ul(['마신 날짜·시간과 종류·양을 가능한 범위에서 사실대로 전달','혈액검사·내시경·진정검사 등 예정 항목을 함께 설명','검사를 진행할지 일정 조정이 필요한지 병원에 확인','음식 금식 시간을 채웠다는 이유로 음주 사실을 생략하지 않기'])+p('물·음식을 먹었다고 모든 검사가 취소되는 것은 아니듯, 술을 마셨다고 본인이 임의로 진행 가능 여부를 판정하지 않습니다. 평소 복용약도 스스로 중단하지 말고 처방 의료진과 검진기관의 계획을 확인하세요.')+'<section class="official-guide-actions"><h2>음주 전후 준비 안내 확인</h2><a class="official-guide-button" href="'+HANIL+'" target="_blank" rel="noopener"><strong>한일병원 검진 전 주의사항</strong><span>과음·과로 등 해당 기관의 안내. 본인 예약 병원 기준은 별도 확인 · 새 창 ↗</span></a></section>')]

def run():
 changed=[]
 for n,(url,title,desc,body) in enumerate(CHANGES,7):
  f=ROOT/(url[1:]+'.html');raw=f.read_text(encoding='utf8');backup=OUT/'before-refresh'/f.relative_to(ROOT);backup.parent.mkdir(parents=True,exist_ok=True)
  if not backup.exists():backup.write_text(raw,encoding='utf8')
  s=BeautifulSoup(raw,'html.parser');s.title.string=title;s.h1.clear();s.h1.string=title
  lead=s.select_one('main .lead');lead.clear();lead.string=desc
  for typ,key,value in [('name','description',desc),('property','og:title',title),('property','og:description',desc),('name','twitter:title',title),('name','twitter:description',desc)]:
   el=s.find('meta',attrs={typ:key})
   if el:el['content']=value
  for sc in s.find_all('script',type='application/ld+json'):
   try:
    d=json.loads(sc.string)
    if d.get('@type')=='Article':d.update(headline=title,description=desc,dateModified='2026-11-02');sc.string=json.dumps(d,ensure_ascii=False)
   except (ValueError,TypeError):pass
  block=BeautifulSoup('<section id="youtube-refresh-'+str(n)+'">'+body+'</section>','html.parser')
  anchor=s.main.find('section',class_='official-guide-actions') or s.main.find('h2',string=re.compile('공식 확인처|참고할 수')) or s.main.find('section',class_='kakao-inquiry-cta')
  if anchor:anchor.insert_before(block)
  else:s.main.append(block)
  f.write_text(str(s).rstrip()+'\n',encoding='utf8');changed.append(str(f.relative_to(ROOT)))
 sm=ROOT/'sitemap.xml';raw=sm.read_text(encoding='utf8')
 for url,*_ in CHANGES:raw=re.sub(r'(<loc>https://hospital.hbuby.com'+re.escape(url)+r'</loc>\s*<lastmod>)[^<]+',r'\g<1>2026-11-02',raw)
 sm.write_text(raw,encoding='utf8');changed+=['sitemap.xml','assets/article-catalog.json']
 subprocess.run([sys.executable,str(ROOT/'scripts/build-article-catalog.py')],check=True)
 (OUT/'changed-refresh.json').write_text(json.dumps(changed,ensure_ascii=False,indent=2),encoding='utf8')
 (OUT/'refresh-manifest.json').write_text(json.dumps([{'url':'https://hospital.hbuby.com'+u,'title':t,'description':d} for u,t,d,_ in CHANGES],ensure_ascii=False,indent=2),encoding='utf8')
 print(json.dumps(changed,ensure_ascii=False))
if __name__=='__main__':run()
