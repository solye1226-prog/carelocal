from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests,json,hashlib
from pypdf import PdfReader
from bs4 import BeautifulSoup as B
OUT=Path(__file__).resolve().parents[1]/'docs/youtube6-publication-2026-11-02/sources'
OUT.mkdir(parents=True,exist_ok=True)
SOURCES={
'law-penalty-current':'https://www.law.go.kr/LSW/flDownload.do?gubun=&flSeq=167382913&bylClsCd=110201',
'dementia-policy-202601':'https://www.samsungfire.com/publication/pdf/ZPB369040_0_20260101_file1.pdf',
'cochlear-hira':'https://www.hira.or.kr/bbsDummy.do?brdBltNo=47809&brdScnBltNo=4&pgmid=HIRAA010006011100',
'epost-documents':'https://www.epostlife.go.kr/PYIMRD0002.do',
'epost-method':'https://www.epostlife.go.kr/PYIMIM0001.do',
'driving-healthcheck':'https://www.safedriving.or.kr/diGuide/selectDiGuide01.do',
'prostate-price-brmh':'https://www.brmh.org/medi_info/non_medifee.do?CSUBCD_NM1=&page=49&site=001&user_code=009015000',
}
def fetch(item):
 key,url=item
 try:
  r=requests.get(url,timeout=45);r.raise_for_status()
  result={'key':key,'url':url,'status':r.status_code,'sha256':hashlib.sha256(r.content).hexdigest()}
  if r.content.startswith(b'%PDF'):
   path=OUT/(key+'.pdf');path.write_bytes(r.content);pdf=PdfReader(path)
   texts=[p.extract_text() or '' for p in pdf.pages]
   (OUT/(key+'.txt')).write_text('\n\n'.join(f'PDF PAGE {i+1}\n'+t for i,t in enumerate(texts)),encoding='utf8')
   result.update(pages=len(texts),matches=[{'page':i+1,'excerpts':[t[max(0,t.find(w)-120):t.find(w)+900] for w in ['제133조','건강진단을 하지','치매상태의 정의','CDR 검사결과지'] if w in t]} for i,t in enumerate(texts) if any(w in t for w in ['제133조','건강진단을 하지','치매상태의 정의','CDR 검사결과지'])])
  else:
   r.encoding=r.apparent_encoding;s=B(r.text,'html.parser')
   for x in s.select('script,style,header,footer'):x.decompose()
   txt=s.get_text(' ',strip=True);(OUT/(key+'.txt')).write_text(txt,encoding='utf8')
   result.update(chars=len(txt),title=s.title.get_text() if s.title else '')
  return result
 except Exception as e:return {'key':key,'url':url,'error':str(e)}
if __name__=='__main__':
 with ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(fetch,SOURCES.items()))
 (OUT/'fetch-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
 print(json.dumps([{k:v for k,v in x.items() if k!='matches'} for x in results],ensure_ascii=False,indent=2))
