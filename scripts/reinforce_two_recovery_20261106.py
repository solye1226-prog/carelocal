from pathlib import Path
from bs4 import BeautifulSoup
import json
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/two-article-recovery-2026-11-06'
OUT.mkdir(exist_ok=True)
SPECS=[
 ('silbi/cartistem-silbi-claim.html','카티스템 실비 청구, 약제비·수술료 확인과 필요서류','카티스템 실비 청구 전 약제비·수술료·입원비를 나누어 확인하세요. 식약처 허가정보와 실손 약관의 차이, 필요한 청구서류와 보험사에 물어볼 항목을 정리합니다.'),
 ('claims/surgery-claim-documents.html','수술확인서 수술기록지 차이, 수술비 청구서류와 대체 가능 여부','수술확인서는 수술 사실을, 수술기록지는 실제 수술 방법·범위를 확인하는 자료입니다. 둘 다 필요한 경우와 대체 가능 여부, 진단서·영수증 등 청구서류를 비교합니다.')]

for rel,title,description in SPECS:
    p=ROOT/rel
    original=p.read_text(encoding='utf-8')
    (OUT/(p.stem+'-original.html')).write_text(original,encoding='utf-8')
    s=BeautifulSoup(original,'html.parser'); main=s.select_one('main'); s.title.string=title;main.h1.string=title
    for attrs in [{'name':'description'},{'property':'og:description'},{'name':'twitter:description'}]:
        t=s.find('meta',attrs=attrs)
        if t:t['content']=description
    for attrs in [{'property':'og:title'},{'name':'twitter:title'}]:
        t=s.find('meta',attrs=attrs)
        if t:t['content']=title
    for tag in s.select('script[type="application/ld+json"]'):
        try:data=json.loads(tag.string or tag.get_text())
        except json.JSONDecodeError:continue
        def update(obj):
            if isinstance(obj,dict):
                if obj.get('@type') in ('Article','BlogPosting'):
                    obj['headline']=title;obj['dateModified']='2026-11-06';obj['description']=description
                for v in obj.values():update(v)
            elif isinstance(obj,list):
                for v in obj:update(v)
        update(data);tag.string=json.dumps(data,ensure_ascii=False)
    lead=main.select_one('p.lead')
    if rel.startswith('silbi/'):
        lead.clear();lead.append(BeautifulSoup('<strong>카티스템 실비 청구는 약제비·수술료·입원비를 나눠 접수하고, 가입한 실손 약관에서 각 비용의 보장 여부를 확인하는 절차입니다.</strong> 비급여라고 모두 제외되는 것도, 식약처 허가를 받았다고 전액 지급되는 것도 아닙니다. 먼저 실제 지출 자료와 가입 담보를 대조하고, 보완이 필요할 때 치료 기록을 추가합니다.','html.parser'))
        second=lead.find_next_sibling('p')
        second.clear();second.append(BeautifulSoup('치료 전 예상 비용은 <a href="/treatment-costs/cartistem-stem-cell-knee-cost">카티스템 수술비용</a>에서, 수술비 특약은 <a href="/surgery-benefit/cartistem-concurrent-procedure-records">동시에 받은 수술의 기록 구분</a>에서 확인하세요. 이 글은 치료 후 실비 접수에 필요한 비용·서류를 다룹니다.','html.parser'))
        heading=main.find('h2',string='카티스템 실비 청구 전 핵심 체크')
        heading.string='카티스템 실비 적용: 허가사항·약관·실제 비용을 나눠 확인'
        table=heading.find_next_sibling('table')
        table.replace_with(BeautifulSoup('''<table><caption>카티스템 실비 청구 전 확인할 세 가지</caption><thead><tr><th scope="col">구분</th><th scope="col">확인할 자료</th><th scope="col">이것만으로 알 수 없는 것</th></tr></thead><tbody>
<tr><td><span class="cell-label" aria-hidden="true">구분</span>어떤 치료를 받았는지</td><td><span class="cell-label" aria-hidden="true">확인할 자료</span>진단명·수술명, 사용한 제품, 담당의 진료기록</td><td><span class="cell-label" aria-hidden="true">이것만으로 알 수 없는 것</span>제품의 허가사항만으로 개인 보험금이 확정되지는 않음</td></tr>
<tr><td><span class="cell-label" aria-hidden="true">구분</span>내 계약이 보장하는 비용인지</td><td><span class="cell-label" aria-hidden="true">확인할 자료</span>실손 가입 시기·입원/통원 담보·비급여 보장 및 제외 조항</td><td><span class="cell-label" aria-hidden="true">이것만으로 알 수 없는 것</span>다른 사람의 지급 사례로 내 공제액·한도를 정할 수 없음</td></tr>
<tr><td><span class="cell-label" aria-hidden="true">구분</span>실제로 얼마를 냈는지</td><td><span class="cell-label" aria-hidden="true">확인할 자료</span>최종 영수증·세부내역서의 약제비·수술료·입원비</td><td><span class="cell-label" aria-hidden="true">이것만으로 알 수 없는 것</span>치료 전 견적 전체를 실제 지출액이나 예상 보험금으로 볼 수 없음</td></tr>
</tbody></table><p><a href="https://nedrug.mfds.go.kr/pbp/CCBBB01/getItemDetail?itemSeq=202106062" target="_blank" rel="noopener">식약처 카티스템 품목정보</a>의 효능·효과는 퇴행성 또는 반복적 외상에 의한 골관절염 환자(ICRS grade IV)의 무릎 연골 결손 치료로 안내됩니다. 이는 약의 허가 범위이며, 실손보험의 지급 조항이 아닙니다. 진단서에 ‘관절염’이라고 적혀 있다는 이유만으로 허가 조건이나 보장 조건을 모두 충족했다고 판단하지 마세요.</p>''','html.parser'))
        main.find('h2',string='카티스템 실비 청구 항목: 재료대·수술료·입원비').string='카티스템 실비 청구서류: 약제비·수술료·입원비별 준비'
        # Use the accessible insurer source verified this turn for document examples.
        for a in s.select('a[href*="samsungfire.com"]'):
            a['href']='https://www.chubb.com/kr-kr/claims-service/claims-documents-forms.html'
            a.string='라이나손해보험(Chubb) 실손 청구서류 안내 · 입원·통원 항목 확인 · 새 창 ↗'
    else:
        lead.clear();lead.append(BeautifulSoup('<strong>수술확인서는 수술명·수술일 등 수술 사실을 확인하는 서류이고, 수술기록지는 실제 수술 방법·부위·범위를 기록한 진료기록입니다.</strong> 수술비 청구에 두 서류가 언제나 함께 필요한 것은 아닙니다. 먼저 보험사가 인정하는 기본 서류를 준비하고, 수술 방법의 추가 확인이나 병원 발급 방식 때문에 필요한 경우에 기록지를 더합니다.','html.parser'))
        comparison=main.find('h2',id='certificate-choice');comparison.string='수술확인서 수술기록지 차이와 대체 가능 여부'
        table=comparison.find_next_sibling('table');note=table.find_next_sibling('p')
        note.clear();note.append(BeautifulSoup('<a href="https://www.chubb.com/kr-kr/claims-service/claims-documents-forms.html" target="_blank" rel="noopener">라이나손해보험(Chubb) 공식 구비서류 안내</a>의 수술 항목은 진단명·수술명·수술일자가 포함된 진단서 또는 수술확인서를 선택 자료로 안내합니다. 해당 회사의 예시이며, 수술기록지 한 장이 모든 보험사의 기본 서류를 자동으로 대체한다는 뜻은 아닙니다. 병원에서 발급 가능한 자료와 보험사의 인정 여부를 각각 확인하세요.','html.parser'))
        first=main.find('h2',id='document-checklist')
        # Put the existing comparison first, without duplicating its table or prose.
        for node in [comparison,table,note]:first.insert_before(node.extract())
        first.string='수술비 청구서류에서 먼저 확인할 네 가지 정보'
        q=main.find('h2',id='operative-record-request');q.string='수술확인서 제출 후 수술기록지를 추가 요청받았다면'
        nav=main.select_one('nav.reading-nav')
        nav.find('a',href='#certificate-choice').string='확인서·기록지 차이'
        p2=q.find_next_sibling()
        # Existing specialised article remains the place for handling additional requests.
        for a in s.select('a[href="/claims/surgery-record-additional-request"]'):
            a.string='수술기록지 추가 요청 사유와 발급 범위 확인'
    p.write_text(str(s)+'\n',encoding='utf-8')

# Preserve URLs; only the two changed pages receive a real modification date.
tree=ET.parse(ROOT/'sitemap.xml');ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
ET.register_namespace('',ns['s'])
for row in tree.getroot():
    loc=row.find('s:loc',ns)
    if loc is not None and any(loc.text=='https://hospital.hbuby.com/'+r.removesuffix('.html') for r,_,_ in SPECS):
        last=row.find('s:lastmod',ns)
        if last is not None:last.text='2026-11-06'
tree.write(ROOT/'sitemap.xml',encoding='utf-8',xml_declaration=True)
print('Updated two existing articles; no new URLs.')
