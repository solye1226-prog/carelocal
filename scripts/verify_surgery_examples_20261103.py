from pathlib import Path
from bs4 import BeautifulSoup
import requests,json,sys
R=Path(__file__).resolve().parents[1];O=R/'docs/surgery-table-examples-2026-11-03';U='https://hospital.hbuby.com/surgery-benefit/surgery-classification'
local=BeautifulSoup((R/'surgery-benefit/surgery-classification.html').read_text(encoding='utf8'),'html.parser')
public='--public' in sys.argv
if public:
 r=requests.get(U,timeout=40);r.raise_for_status();s=BeautifulSoup(r.text,'html.parser');assert ' '.join(s.main.stripped_strings)==' '.join(local.main.stripped_strings),'Public body not yet current'
 assert [x.get_text() for x in s.head.find_all('style')]==[x.get_text() for x in local.head.find_all('style')]
else:s=local
assert s.select_one('link[rel=canonical]')['href']==U
assert len(s.select('.first-tier-table tbody tr'))==10 and len(s.select('.source-table tbody tr'))==8
assert len(s.select('h1'))==1 and len(s.main.find_all('img'))==3
assert '보험사·상품·특약·가입 시기' in s.main.get_text()
assert '다른 보험에서 같은 종수라는 뜻은 아닙니다' in s.find(id='first-tier-examples').get_text()
assert not any('쪽' in tr.get_text() or '항 ·' in tr.get_text() for tr in s.select('.source-table tr,.first-tier-table tr'))
assert s.find(id='policy-source-details') and not s.find(id='policy-source-details').has_attr('open')
assert not [a['href'] for a in s.main.find_all('a',href=True) if a['href'].startswith('#') and not s.find(id=a['href'][1:])]
result={'status':'passed','public':public,'representative_examples':8,'first_tier_examples':10,'disclaimer':'by insurer product rider and issue version','provenance':'retained in collapsed source details','indexing':'not requested or checked'}
(O/('public-verification.json' if public else 'local-verification.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(result))
