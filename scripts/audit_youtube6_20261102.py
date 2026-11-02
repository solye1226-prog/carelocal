from pathlib import Path
import sys,json,re,hashlib,subprocess
import requests
from bs4 import BeautifulSoup
from youtube6_20261102_data import DATA
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/youtube6-publication-2026-11-02'
BASE='https://hospital.hbuby.com'
def text(s):
    for x in s.select('aside,.kakao-inquiry-cta'):x.decompose()
    return re.sub(r'\s+',' ',s.get_text(' ',strip=True)).strip()
def audit(n,public=False):
    d=DATA[n-1];path=ROOT/(d['path'][1:]+'.html')
    local=BeautifulSoup(path.read_text(encoding='utf8'),'html.parser')
    soup=BeautifulSoup(requests.get(BASE+d['path'],timeout=25).text,'html.parser') if public else local
    assert soup.h1 and soup.h1.get_text()==d['title'],'H1 mismatch'
    assert soup.find('link',rel='canonical')['href']==BASE+d['path'],'canonical mismatch'
    assert soup.title.get_text()==d['title']
    sc=json.loads(soup.find('script',type='application/ld+json').string)
    assert sc['headline']==d['title'] and sc['datePublished']=='2026-11-02'
    imgs=soup.main.select('figure img');assert len(imgs)==3
    assert len({x['src'] for x in imgs})==3 and len({x['alt'] for x in imgs})==3
    assert soup.main.find('table') and '가상 예시' in soup.main.get_text()
    for pp in d['parents']:assert soup.main.find('a',href=pp)
    assert len(soup.main.find_all('a',href='/insurance-companies/'))==2
    assert soup.main.find('a',href='https://open.kakao.com/o/sVyT7uph')
    if public:
        assert text(BeautifulSoup(str(soup.main),'html.parser'))==text(BeautifulSoup(str(local.main),'html.parser')),'public body stale'
        for im in imgs:
            r=requests.get(BASE+im['src'],timeout=25);r.raise_for_status()
            assert hashlib.sha256(r.content).digest()==hashlib.sha256((ROOT/im['src'][1:]).read_bytes()).digest(),'image mismatch'
    parent_results=[]
    for pp in d['parents']:
        target=ROOT/(pp[1:]+'.html')
        old=subprocess.run(['git','show','69472c0:'+pp[1:]+'.html'],capture_output=True,check=True).stdout.decode('utf8')
        before=BeautifulSoup(old,'html.parser');after=BeautifulSoup(target.read_text(encoding='utf8'),'html.parser')
        if pp=='/claims/medical-expense-claim-documents':
            after.title.string=before.title.get_text()
            after.main.find('h1').clear();after.main.find('h1').string=before.main.find('h1').get_text()
            after.main.select_one('.lead').clear();after.main.select_one('.lead').string=before.main.select_one('.lead').get_text()
            for x in after.select('#youtube-refresh-7'):x.decompose()
        assert before.title.get_text()==after.title.get_text()
        assert text(before.main)==text(BeautifulSoup(str(after.main),'html.parser')),'parent body changed'
        if public:
            r=requests.get(BASE+pp,timeout=25);r.raise_for_status()
            assert BeautifulSoup(r.text,'html.parser').main.find('a',href=d['path']),'public parent missing link'
        parent_results.append(pp)
    result={'n':n,'url':BASE+d['path'],'public':public,'status':'passed','images':3,'parents':parent_results}
    (OUT/f'{"public" if public else "local"}-{n}.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
    print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__':audit(int(sys.argv[1]),'--public' in sys.argv)
