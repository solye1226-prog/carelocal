import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const origin = 'https://hospital.hbuby.com';
const sources = {
  kdca: ['질병관리청 국가건강정보포털 하지정맥류', 'https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=5687'],
  hira: ['건강보험심사평가원 비급여 행위 목록', 'https://www.hira.or.kr/ebooksc/2025/02/BZ202502271249574.pdf'],
  hiraGlue: ['건강보험심사평가원 복재정맥 폐색술 진료비 확인 사례', 'https://www.hira.or.kr/bbsDummy.do?brdBltNo=45495&brdScnBltNo=4&pgmid=HIRAA010002080200'],
  hiraMechanical: ['건강보험심사평가원 경피적 기계화학 정맥폐쇄술 평가', 'https://www.hira.or.kr/bbsDummy.do?brdBltNo=46045&brdScnBltNo=4&pgmid=HIRAA030051000009'],
  samsung: ['삼성화재 보험금 청구 구비서류', 'https://direct.samsungfire.co.kr/claim/healthreward/health_doc.html'],
};

const articles = [
  {
    slug: 'varicose-laser-silbi-claim', title: '하지정맥류 레이저 수술 실비 청구, 필요한 서류와 비용 확인 방법',
    description: '하지정맥류 레이저정맥폐쇄술을 받았다면 초음파 역류 소견, 수술확인서, 영수증·세부내역서와 가입한 실손 약관을 나눠 확인하세요. 비급여와 수술비 특약도 구분합니다.',
    keyword: '하지정맥류 레이저 수술 실비', thumb: 'varicose-laser-thumb.webp', images: ['varicose-laser-ultrasound.webp', 'varicose-laser-documents.webp'],
    alts: ['하지정맥류 레이저 수술 전 다리 정맥 초음파로 역류를 확인하는 장면', '하지정맥류 레이저 수술 실비 청구서류를 분류하는 장면'],
    lead: '하지정맥류 레이저 수술을 받았는데 병원에서 비급여라고 안내했다면 실비도 안 되는 걸까요? 건강보험 급여 여부와 개인 실손보험의 지급 여부는 같은 질문이 아닙니다. 실제 레이저정맥폐쇄술을 했는지, 치료가 필요한 정맥 역류가 확인됐는지, 의료비가 어떤 항목으로 청구됐는지를 먼저 살펴야 합니다.',
    rows: [['치료 사실', '수술확인서의 정확한 수술명·시행일·좌우 부위', '레이저라는 넓은 표현만으로 담보 판단하지 않기'], ['진단 근거', '정맥 초음파 결과와 증상·진료기록', '육안상 혈관 돌출만으로 역류 단정하지 않기'], ['실제 비용', '병원 영수증·진료비 세부내역서', '행위료·재료비·검사비 및 입원·통원 구분']],
    sections: [
      ['레이저정맥폐쇄술과 실손 보장은 별개로 확인합니다', '질병관리청은 하지정맥류 진단에 정맥 초음파로 혈류와 역류 여부를 살핀다고 안내합니다. 치료 방법은 증상과 정맥 상태에 따라 달라지며 레이저를 이용한 정맥 내 치료가 한 방법입니다. 따라서 단순히 혈관이 보였다는 사실이나 병원 광고 문구보다 실제 진단·시술 기록이 중요합니다.', '건강보험심사평가원의 비급여 행위 목록에는 레이저정맥폐쇄술이 올라 있습니다. 비급여라는 분류가 개인 실손보험금의 지급 또는 거절을 자동으로 결정하지는 않습니다. 가입 당시 약관의 보장·제외 조건, 실제 의료비와 치료 목적을 따로 확인해야 합니다.'],
      ['수술 전에 받을 설명과 확인할 비용', '의료진에게 어느 정맥에서 역류가 확인됐는지, 레이저 치료가 필요한 이유와 다른 치료 선택지가 무엇인지 설명받으세요. 치료 예정 부위가 한쪽인지 양쪽인지, 예정된 처치가 한 가지인지 함께 확인합니다. 진료 판단은 의료진의 영역이며 보험 보장 판단과 혼동하지 않는 것이 좋습니다.', '견적서에서는 레이저 시술료, 치료재료, 정맥 초음파, 마취·진정, 압박용품 등 항목이 따로 표시되는지 살펴보세요. 비용이 한 줄로 묶여 있다면 병원에 실제 청구될 항목을 문의합니다. 보험사에는 내 실손 계약의 가입 시기·통원 한도·비급여 관련 조항을 기준으로 질문하세요.'],
      ['청구서류는 세 묶음으로 준비하세요', '첫째, 진료비 계산서·영수증과 세부내역서는 실제 결제 비용을 보여 줍니다. 둘째, 수술확인서 등에는 진단명·정확한 치료명·시행일·좌우 부위가 드러나야 합니다. 셋째, 보험사가 치료 목적을 확인하려면 정맥 초음파 결과지나 관련 진료기록을 추가 요청할 수 있습니다.', '삼성화재 공식 구비서류 안내는 실손·수술 청구에 필요한 자료를 담보별로 구분하며 상황에 따라 추가 서류가 달라질 수 있다고 안내합니다. 보험사마다 제출 방식이 다르니 유료 진단서를 모두 미리 발급하기보다 본인 보험사 안내를 먼저 확인하세요.'],
      ['당일 시술이면 통원 한도를 함께 보세요', '레이저 치료 후 당일 귀가하는 경우도 있지만 그 사실만으로 모든 계약에서 동일한 통원 기준이 적용된다고 할 수 없습니다. 실제 진료 경과, 병원의 기록, 약관의 입원 정의를 함께 확인해야 합니다. 병원에 머문 시간이나 입퇴원확인서 한 장만으로 보험금이 확정되는 것도 아닙니다.', '지급액이 예상보다 적다면 보험금 계산서에서 어떤 항목에 통원 한도·공제금액이 적용됐는지 확인하세요. 레이저 시술료와 검사료, 치료재료 비용이 각각 어떻게 처리됐는지 질문하면 차이의 원인을 찾기 쉽습니다.'],
      ['정액 수술비 특약은 따로 청구 가능성을 살펴보세요', '질병수술비나 종수술비에 가입했다면 실손의료비와 별도의 지급 요건이 적용됩니다. 수술확인서의 정확한 시술명을 가입 당시 약관의 수술 정의와 분류표에 대조합니다. 병원 세부내역서의 행위코드가 보험 수술 종수를 뜻하는 것은 아닙니다.', '한쪽 다리와 양쪽 다리 치료의 지급 횟수도 약관의 동일일·동일 질병·수술 1회 조항에 따라 달라질 수 있습니다. 보험사에 문의할 때는 담보 이름과 치료 날짜, 부위를 함께 알려 주세요.'],
    ],
    questions: [['레이저정맥폐쇄술이 비급여면 실비 청구가 불가능한가요?', '비급여 여부만으로 결론 나지 않습니다. 가입 약관과 치료 사실, 비용 항목을 확인해야 합니다.'], ['초음파 결과지는 꼭 내야 하나요?', '보험사 심사와 요청에 따라 다릅니다. 역류 소견을 확인해야 한다는 안내를 받으면 필요한 결과지 범위를 문의하세요.'], ['수술확인서에는 무엇이 적혀야 하나요?', '진단명, 실제 시술명, 시행일, 좌우 부위가 확인되는지 살펴보세요.'], ['당일 귀가하면 입원 실비를 받을 수 없나요?', '귀가 날짜만으로 단정할 수 없습니다. 실제 관찰·치료 내용과 해당 약관의 입원 정의를 봅니다.'], ['실비와 질병수술비를 같이 확인할 수 있나요?', '각 담보에 가입했다면 별도로 검토할 수 있습니다. 지급 기준은 서로 다릅니다.']],
    related: [['하지정맥류 실비 종합 안내', '/silbi/varicose-vein-silbi-claim'], ['고주파 수술 실비·수술비', '/silbi/varicose-radiofrequency-insurance'], ['보험금이 적거나 거절됐다면', '/claims/varicose-insurance-low-payout-denied']], sourceKeys: ['kdca', 'hira', 'samsung'],
  },
  {
    slug: 'varicose-radiofrequency-insurance', title: '하지정맥류 고주파 수술, 실비와 수술비 특약은 어떻게 다를까?',
    description: '하지정맥류 고주파정맥내막폐쇄술 뒤 실손 의료비와 질병수술비·종수술비는 다른 기준으로 심사합니다. 정확한 시술명, 치료재료비, 수술확인서와 약관을 대조하세요.',
    keyword: '하지정맥류 고주파 수술 실비', thumb: 'varicose-radiofrequency-thumb.webp', images: ['varicose-radiofrequency-consult.webp', 'varicose-radiofrequency-policy.webp'],
    alts: ['하지정맥류 고주파 치료 방법을 다리 정맥 모형으로 설명하는 장면', '하지정맥류 고주파 수술비 특약과 실비 서류를 나누어 보는 장면'],
    lead: '고주파로 하지정맥류를 치료했다면 “실비가 되니 수술비도 나오겠지”라고 생각하기 쉽습니다. 그러나 실손은 실제 지출한 의료비를, 질병수술비·종수술비는 가입 약관이 정한 수술 요건을 봅니다. 같은 치료를 청구하더라도 필요한 자료와 지급 계산은 서로 다릅니다.',
    rows: [['실손의료비', '본인이 부담한 시술료·재료비·검사비', '보장 제외·공제·입원·통원 한도 확인'], ['질병수술비', '약관상 수술 정의와 실제 시행 행위', '실손 지급 결과와 자동 연동되지 않음'], ['종수술비', '가입 당시 수술분류표의 해당 항목', '의료기관 행위코드와 보험 종수 혼동 금지']],
    sections: [
      ['고주파 치료명부터 확인하세요', '질병관리청은 고주파를 이용한 정맥 내 치료를 하지정맥류의 치료 방법 중 하나로 설명합니다. 건강보험심사평가원의 비급여 공개 항목에는 고주파정맥내막폐쇄술과 관련 치료재료가 구분되어 있습니다. 병원에서 “고주파 수술”이라고 부르는 것과 진료비 세부내역서에 적힌 정확한 행위명은 확인해 볼 필요가 있습니다.', '초음파 검사에서 어느 정맥에 역류가 있었는지, 실제 치료한 부위가 어디인지 의료진에게 설명받으세요. 진단 기록과 시술 기록이 서로 다른 부위를 가리키거나 치료가 추가됐다면 그 이유를 병원에 먼저 묻는 것이 좋습니다.'],
      ['실비는 지출 항목별로 계산합니다', '실손 청구에는 진료비 계산서·영수증과 세부내역서가 기본적인 비용 자료입니다. 같은 날 결제했더라도 고주파 시술료, 치료재료, 초음파 검사비, 약제비가 서로 다른 항목으로 처리될 수 있습니다. 본인의 가입 시기와 약관에 따라 비급여 보장·공제·한도가 달라질 수 있습니다.', '비급여로 표시되었다는 이유만으로 전액 지급 또는 전액 제외라고 결론 내리지 마세요. 병원 예상 환급액도 보험사 확정 지급액은 아닙니다. 보험금 산출내역이 나오면 항목별 인정액과 제외액을 확인합니다.'],
      ['수술비 특약은 정액 보장의 문구를 봅니다', '질병수술비는 해당 질병을 치료하기 위해 실제 시행한 행위가 가입 약관에서 정한 수술에 해당하는지 확인합니다. 종수술비는 별도 수술분류표와 주석, 지급 횟수 제한을 대조합니다. 따라서 실손이 지급되었어도 정액 수술비가 반드시 지급되는 것은 아닙니다.', '진단서의 질병분류기호나 세부내역서의 행위코드만 보고 몇 종이라고 단정할 수 없습니다. 보험증권에 적힌 정확한 담보 이름과 계약 당시 약관을 준비해 보험사에 적용 항목을 문의하세요.'],
      ['양쪽 다리·여러 부위를 치료했다면', '좌우 다리를 같은 날 또는 다른 날 치료할 수 있습니다. 병원 시술확인서에서 날짜별·부위별로 실제 시행한 고주파 치료를 확인하세요. 치료 부위의 개수와 보험금 지급 횟수는 같은 개념이 아닙니다.', '약관에 동일일 수술, 같은 질병의 반복 수술, 수술 1회당 지급 등의 문구가 있는지 살펴보세요. 실손은 각 진료일의 실제 의료비 자료를 나누어 정리하면 중복 청구나 누락을 확인하기 쉽습니다.'],
      ['이 순서로 보험사에 문의하세요', '먼저 가입한 실손과 수술비 특약 이름을 적습니다. 다음으로 병원 기록의 진단명, 고주파 시술명, 부위, 날짜를 확인합니다. 비용 자료와 수술 사실 자료를 따로 준비한 뒤 각 담보에 필요한 추가 서류를 문의하세요.', '보험사가 종수술비를 지급하지 않거나 예상과 다른 종수를 적용했다면 어떤 약관의 어떤 분류표 항목을 근거로 했는지 서면 설명을 요청합니다. 인터넷에 공개된 타인 지급 사례는 가입 약관과 시술기록이 다를 수 있습니다.'],
    ],
    questions: [['고주파 치료 실비를 받으면 질병수술비도 나오나요?', '자동으로 정해지지 않습니다. 두 담보의 가입 여부와 지급 요건을 각각 확인해야 합니다.'], ['고주파정맥내막폐쇄술은 몇 종인가요?', '모든 계약에 통하는 종수는 없습니다. 실제 시술명과 가입 당시 수술분류표를 대조하세요.'], ['치료재료비도 실비에 포함되나요?', '세부내역서의 항목과 계약의 보장·제외 조항을 확인해야 합니다.'], ['양쪽 다리면 수술비 두 번인가요?', '부위 수만으로 결정되지 않습니다. 약관의 지급 단위와 수술 날짜를 확인하세요.'], ['병원에서 어떤 확인서를 발급받아야 하나요?', '진단명·시술명·시행일·부위가 확인되는 자료의 발급 가능 여부를 문의하세요.']],
    related: [['하지정맥류 실비 종합 안내', '/silbi/varicose-vein-silbi-claim'], ['레이저 수술 실비 청구', '/silbi/varicose-laser-silbi-claim'], ['질병수술비와 종수술비 차이', '/surgery-benefit/disease-vs-type-surgery-benefit']], sourceKeys: ['kdca', 'hira', 'samsung'],
  },
  {
    slug: 'varicose-venaseal-clarivein-silbi', title: '베나실·클라리베인 하지정맥류 실비, 시술비와 재료비 어떻게 볼까?',
    description: '하지정맥류 베나실과 클라리베인은 서로 다른 방식입니다. 실제 시술명, 비급여 행위료와 치료재료비, 초음파 역류 소견 및 개인 실손보험 약관을 확인하세요.',
    keyword: '베나실 클라리베인 실비', thumb: 'varicose-glue-mechanical-thumb.webp', images: ['varicose-glue-consult.webp', 'varicose-glue-cost.webp'],
    alts: ['하지정맥류 베나실 시술을 정맥 모형으로 설명하는 장면', '베나실과 클라리베인 비용 항목을 비교하는 장면'],
    lead: '베나실과 클라리베인 중 무엇이 실비가 더 잘 되는지 묻기 전에 두 이름이 같은 시술인지부터 구분해야 합니다. 베나실은 접착제를 사용하는 폐색술로, 클라리베인은 기계적 자극과 경화제를 이용하는 방식으로 알려져 있습니다. 보험 청구에서는 제품 이름보다 병원 기록의 정확한 행위명·재료비와 가입 약관이 중요합니다.',
    rows: [['베나실 관련 행위', '시아노아크릴레이트를 이용한 복재정맥 폐색술 여부', '제품 이름과 의료행위명 구분'], ['클라리베인 관련 행위', '경피적 기계화학 정맥폐쇄술 여부', '실제 사용한 방법·재료 확인'], ['실손 청구', '시술료·재료비·검사비가 적힌 영수증과 세부내역서', '비급여 분류와 개인 실손 지급은 별개']],
    sections: [
      ['두 시술의 의료행위 이름은 다릅니다', '건강보험심사평가원은 시아노아크릴레이트를 이용한 복재정맥 폐색술과 경피적 기계화학 정맥폐쇄술을 별개 행위로 다룹니다. 전자는 접착 방식이며 후자는 기계적 자극과 경화제를 이용하는 방식입니다. 병원에서 들은 제품명만으로 실제 청구된 행위가 무엇인지 확정하지 마세요.', '정맥의 어느 부위에 역류가 있었는지, 해당 방법을 선택한 이유와 치료 범위를 의료진에게 설명받으세요. 질병관리청은 하지정맥류 진단에서 초음파로 혈류와 역류 여부를 확인한다고 안내합니다.'],
      ['비급여 표시만으로 실비 결론을 내리지 마세요', '건강보험심사평가원의 비급여 행위 목록은 이들 시술의 건강보험 분류를 살펴보는 공식 자료입니다. 건강보험의 비급여와 개인 실손보험의 보장 가능성은 서로 다른 체계입니다. 실손은 가입 시기, 약관, 치료 목적, 실제 지출 항목과 심사 자료를 함께 확인합니다.', '특히 견적서의 총액과 실제 진료비 세부내역서의 항목이 같은지 보세요. 시술 행위료, 카테터 등 치료재료, 초음파 검사, 부가 처치 비용을 나눠 보아야 제외 금액이나 공제액을 이해하기 쉽습니다.'],
      ['시술 전 병원과 보험사에 각각 물어보세요', '병원에는 “정확한 시술명과 사용 재료, 치료할 정맥, 좌우 부위, 예상 비용 항목”을 문의합니다. 보험사에는 “내 실손 계약에서 해당 비급여 행위와 재료비를 어떤 조항으로 심사하며 필요한 서류가 무엇인지”를 확인하세요.', '사전 상담에서 가능하다는 답변을 들어도 최종 지급을 보장하는 것은 아닙니다. 수술 후 실제 진료기록이나 최종 청구 비용이 달라질 수 있으므로 답변 내용과 계약 약관을 함께 보관합니다.'],
      ['청구 때 확인할 서류와 기록', '진료비 계산서·영수증, 세부내역서, 진단명·시술명·시행일이 드러나는 수술확인서 등은 기본 확인 자료입니다. 보험사가 치료 필요성을 추가로 확인한다면 정맥 초음파 결과나 진료기록을 요청할 수 있습니다.', '삼성화재 공식 안내는 청구 유형과 심사 상황에 따라 구비서류가 달라질 수 있다고 설명합니다. 검사 결과지 전체가 처음부터 필요한지, 특정 페이지나 판독 결과만 필요한지는 본인 보험사에 문의한 후 발급하세요.'],
      ['정액 수술비와 양쪽 다리 지급 횟수', '베나실이나 클라리베인에 대한 실손 지급 여부와 질병수술비·종수술비는 별개입니다. 정액 담보는 해당 계약의 수술 정의, 분류표, 제외 조항을 확인합니다. 비급여 행위코드가 보험 약관의 종수나 지급액을 그대로 말해 주지는 않습니다.', '양쪽 다리를 치료했거나 두 방법을 함께 썼다면 날짜별·부위별 실제 행위를 분리해 기록하세요. 같은 날 여러 행위의 지급 횟수와 한도는 각 특약의 약관을 따로 확인해야 합니다.'],
    ],
    questions: [['베나실과 클라리베인은 같은 시술인가요?', '아닙니다. 접착 폐색술과 기계화학 정맥폐쇄술은 의료행위 방식이 다릅니다.'], ['베나실이 비급여면 실비를 못 받나요?', '비급여 분류만으로 개인 실손보험 지급을 결론 내릴 수 없습니다. 가입 약관과 치료 사실을 확인하세요.'], ['클라리베인 재료비도 청구할 수 있나요?', '세부내역서의 실제 항목과 약관을 대조해야 합니다. 청구 가능 여부와 지급액은 별도 심사됩니다.'], ['초음파 역류 소견이 필요한가요?', '치료 목적 확인에 중요할 수 있습니다. 보험사가 요청하는 결과지 범위를 확인하세요.'], ['두 방법을 함께 받으면 수술비 두 번인가요?', '행위 수만으로 단정할 수 없습니다. 날짜·부위·가입 특약의 지급 단위를 확인하세요.']],
    related: [['하지정맥류 실비 종합 안내', '/silbi/varicose-vein-silbi-claim'], ['고주파 수술 실비·수술비', '/silbi/varicose-radiofrequency-insurance'], ['보험금이 적거나 거절됐다면', '/claims/varicose-insurance-low-payout-denied']], sourceKeys: ['kdca', 'hira', 'hiraGlue', 'hiraMechanical', 'samsung'],
  },
  {
    slug: 'varicose-insurance-low-payout-denied', title: '하지정맥류 보험금이 적거나 거절됐다면? 사유별 확인 순서',
    description: '하지정맥류 수술 후 실비 보험금이 예상보다 적거나 거절됐다면 지급 산출내역과 적용 약관부터 확인하세요. 통원 한도, 공제, 비급여 비용, 진단·시술 기록별로 대응 자료를 정리합니다.',
    keyword: '하지정맥류 보험금 지급 거절', thumb: 'varicose-low-payout-thumb.webp', images: ['varicose-low-payout-records.webp', 'varicose-low-payout-review.webp'],
    alts: ['하지정맥류 보험금 지급 산출내역과 병원비 세부내역서를 비교하는 장면', '하지정맥류 보험금 지급 거절 사유를 의료기록과 약관으로 확인하는 장면'],
    lead: '하지정맥류 치료 뒤 예상보다 적은 실비가 들어왔거나 보험금이 거절됐다면 같은 서류를 다시 보내기 전에 이유를 나눠 봐야 합니다. 공제와 통원 한도 때문에 적게 나온 경우, 특정 비급여 비용이 제외된 경우, 치료 목적이나 실제 시술 기록이 부족한 경우는 확인할 자료가 서로 다릅니다.',
    rows: [['지급액이 적음', '보험금 산출내역의 제외액·공제액·한도', '영수증 총액과 인정 의료비를 구분'], ['치료 목적 다툼', '초음파 역류 소견·증상·진료기록', '기록에 없는 사실을 새로 주장하지 않기'], ['시술 종류·담보 다툼', '수술확인서의 실제 행위명·가입 약관', '실손과 정액 수술비의 기준 분리']],
    sections: [
      ['먼저 지급 산출내역과 적용 조항을 받으세요', '보험금이 예상보다 적을 때는 병원에 낸 총액과 보험사가 보장 대상으로 인정한 의료비를 비교합니다. 지급 계산서에서 제외된 항목, 자기부담금·공제, 통원 한도, 최종 지급액을 나란히 보세요. 같은 차액이라도 원인이 다르면 보완할 자료도 다릅니다.', '거절 통보를 받았다면 어떤 담보에서 어떤 약관 조항과 사실관계를 적용했는지 서면으로 안내해 달라고 요청하세요. “하지정맥류라서 안 된다” 같은 짧은 설명만으로는 반박할 사실을 특정하기 어렵습니다.'],
      ['통원 한도와 비급여 항목이 원인이라면', '레이저·고주파·접착 폐쇄술·기계화학 폐쇄술 등은 병원 세부내역에 시술료와 치료재료, 검사비가 나뉘어 표시될 수 있습니다. 보험사가 어떤 항목을 인정했고 어느 항목을 제외했는지 의료기관의 세부내역서와 한 줄씩 대조하세요.', '통원으로 심사돼 지급액이 적다면 입원·통원 분류의 근거와 해당 계약의 한도를 확인합니다. 입퇴원확인서만 제출한다고 입원 의료비가 자동 인정되는 것은 아니므로 실제 관찰·치료 기록과 약관의 입원 정의를 살펴야 합니다.'],
      ['치료 필요성 자료가 부족하다는 답변이라면', '질병관리청은 하지정맥류 진단에서 정맥 초음파로 혈류와 역류 여부를 확인할 수 있다고 안내합니다. 보험사가 역류 소견이나 치료 목적을 문제 삼았다면 어떤 자료가 부족하다는 것인지 구체적으로 문의하세요.', '병원에 보관된 검사 판독지, 진료기록, 시술 전후 기록을 확인하고 누락된 원본 자료가 있으면 정식 경로로 추가 제출합니다. 보험금에 맞추어 진단명이나 시행하지 않은 치료를 바꿔 달라고 요청해서는 안 됩니다.'],
      ['수술비 특약을 거절당한 경우', '실손의료비가 지급됐어도 질병수술비나 종수술비가 지급되지 않을 수 있습니다. 정액 수술비는 실제 행위가 가입 당시 약관의 수술 정의·분류표에 맞는지 살피기 때문입니다. 병원 행위코드와 보험 종수를 같은 코드로 오해하지 마세요.', '시술명이 모호하게 적혀 있다면 병원 기록의 정확한 뜻을 확인합니다. 보험사에는 적용한 수술분류표 항목, 제외 조항, 동일일·반복 수술 제한이 무엇인지 문의하세요.'],
      ['재검토 요청은 원인별 자료로 하세요', '판단에 빠진 검사 결과나 잘못 읽힌 비용 항목이 있다면 해당 자료와 함께 재검토를 요청할 수 있습니다. 추가 서류 요청에는 어떤 담보와 어떤 사실을 확인하려는 것인지 먼저 묻고, 제출 날짜·접수번호를 기록하세요.', '설명을 받아도 이견이 남는다면 보험사 민원 절차를 확인하고 관련 문서를 보관하세요. 재검토를 요청했다고 지급이 확정되는 것은 아니며, 계약 조건과 실제 의료기록에 따라 결과가 달라질 수 있습니다.'],
    ],
    questions: [['병원에서 실비 된다고 했는데 왜 적게 나왔나요?', '병원의 예상 안내와 보험사의 계약별 지급 계산은 다릅니다. 산출내역에서 제외액·공제·한도를 확인하세요.'], ['초음파 결과를 추가로 내면 지급되나요?', '자동으로 결정되지 않습니다. 어떤 역류·치료 목적 사실을 확인하려는 요청인지 먼저 확인하세요.'], ['입퇴원확인서가 있으면 통원 판단을 바꿀 수 있나요?', '확인서만으로는 부족할 수 있습니다. 실제 치료·관찰 기록과 약관의 입원 정의를 함께 봅니다.'], ['실비 거절이면 수술비 특약도 거절인가요?', '두 담보는 별도 요건입니다. 각 담보의 결정 사유를 따로 확인하세요.'], ['보험사에 무엇을 서면으로 요청해야 하나요?', '적용 약관 조항, 제외 의료비 항목, 지급 계산과 부족하다고 본 의료 사실을 요청하세요.']],
    related: [['하지정맥류 실비 종합 안내', '/silbi/varicose-vein-silbi-claim'], ['레이저 수술 실비 청구', '/silbi/varicose-laser-silbi-claim'], ['베나실·클라리베인 실비', '/silbi/varicose-venaseal-clarivein-silbi']], sourceKeys: ['kdca', 'hira', 'samsung'],
  },
];

const escape = (value) => String(value).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const link = ([label, href]) => `<a href="${escape(href)}"${href.startsWith('http') ? ' target="_blank" rel="noopener"' : ''}>${escape(label)}</a>`;
const figure = (file, alt, eager = false) => `<figure class="guide-image-panel"><img src="/assets/images/${file}" width="1672" height="941" loading="${eager ? 'eager' : 'lazy'}" decoding="async" alt="${escape(alt)}"></figure>`;

for (const article of articles) {
  const category = article.slug === 'varicose-insurance-low-payout-denied' ? 'claims' : 'silbi';
  const categoryLabel = category === 'claims' ? '보험금 청구' : '실비보험';
  const path = `/${category}/${article.slug}`;
  const articleJson = JSON.stringify({ '@context': 'https://schema.org', '@type': 'Article', headline: article.title, description: article.description, image: `${origin}/assets/images/${article.thumb}`, mainEntityOfPage: `${origin}${path}`, author: { '@type': 'Organization', name: '케어로컬' }, publisher: { '@type': 'Organization', name: '케어로컬' }, datePublished: '2026-09-27', dateModified: '2026-09-27', inLanguage: 'ko-KR' });
  const rows = article.rows.map(([item, check, note]) => `<tr><td>${escape(item)}</td><td>${escape(check)}</td><td>${escape(note)}</td></tr>`).join('');
  const sections = article.sections.map(([heading, first, second], index) => `<h2>${escape(heading)}</h2><p>${escape(first)}</p>${index === 0 ? figure(article.images[0], article.alts[0]) : ''}<p>${escape(second)}</p>${index === 2 ? figure(article.images[1], article.alts[1]) : ''}`).join('\n');
  const faq = article.questions.map(([question, answer]) => `<details><summary>${escape(question)}</summary><p>${escape(answer)}</p></details>`).join('');
  const html = `<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>${escape(article.title)}</title><meta name="description" content="${escape(article.description)}"><meta property="og:type" content="article"><meta property="og:title" content="${escape(article.title)}"><meta property="og:description" content="${escape(article.description)}"><meta property="og:image" content="${origin}/assets/images/${article.thumb}"><link rel="canonical" href="${origin}${path}"><link rel="stylesheet" href="/assets/site.css?v=20260927-varicose-v1"><script type="application/ld+json">${articleJson}</script><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2258793659580551" crossorigin="anonymous"></script></head><body>
<header class="site-header"><nav class="nav" aria-label="주요 메뉴"><a class="brand" href="/"><span class="brand-mark">CL</span><span><strong>케어로컬</strong><small>보험 정보 자료실</small></span></a><div class="nav-links"><a href="/claims/">보험금 청구</a><a href="/silbi/">실비보험</a><a href="/diagnosis-benefit/">진단비</a><a href="/surgery-benefit/">수술비</a><a href="/standards/">약관·기준</a></div></nav></header>
<main class="section article-body insurance-series-article"><div class="breadcrumb"><a href="/">홈</a> / <a href="/${category}/">${categoryLabel}</a> / ${escape(article.keyword)}</div><h1>${escape(article.title)}</h1><p class="lead">${escape(article.lead)}</p><div class="insurance-company-cta"><a href="/insurance-companies/">보험사별 공식 홈페이지 확인하기</a></div>${figure(article.thumb, `${article.keyword} 카드뉴스`, true)}<p class="notice">보험금 지급 여부와 필요서류는 가입 상품, 약관, 가입 시기, 실제 의료기록과 보험사 심사에 따라 달라집니다. 본문 이미지는 이해를 돕는 AI 생성 장면이며 실제 환자 서류가 아닙니다.</p>
<h2>${escape(article.keyword)} 핵심 확인</h2><table><thead><tr><th scope="col">구분</th><th scope="col">확인할 내용</th><th scope="col">주의할 점</th></tr></thead><tbody>${rows}</tbody></table>
${sections}
<h2>접수 전 확인 순서</h2><ol><li>보험증권에서 실손의료비와 수술비 특약의 정확한 이름·가입 시기를 확인합니다.</li><li>진료기록에서 실제 치료명, 초음파 검사 결과, 좌우 부위와 시행일을 구분합니다.</li><li>병원 영수증·세부내역서와 가입 당시 약관, 보험사 공식 구비서류 안내를 대조합니다.</li><li>공식 앱·홈페이지로 접수하고 접수번호와 보완 요청 사유를 보관합니다.</li></ol>
<h2>자주 묻는 질문</h2><div class="faq">${faq}</div><h2>함께 보면 좋은 글</h2><div class="article-actions">${article.related.map(link).join('')}</div><h2>공식 확인처</h2><ul>${article.sourceKeys.map((key) => `<li>${link(sources[key])}</li>`).join('')}</ul><div class="insurance-company-cta"><a href="/insurance-companies/">보험사별 공식 홈페이지 확인하기</a></div><section class="kakao-inquiry-cta" aria-labelledby="contact-title"><p class="cta-label">문의 안내 <span>보험</span></p><h2 id="contact-title">가입한 보험의 보장이 궁금하신가요?</h2><p>가입한 보험의 보장 내용이나 콘텐츠와 관련해 궁금한 점이 있다면 카카오톡으로 문의해 주세요. 주민등록번호·진단서·영수증 등 민감한 개인정보가 포함된 자료는 전송하지 않는 것을 권장합니다.</p><a class="kakao-button" href="https://open.kakao.com/o/sVyT7uph" target="_blank" rel="noopener">카카오톡으로 문의하기</a></section></main></body></html>`;
  writeFileSync(join(root, category, `${article.slug}.html`), `${html}\n`, 'utf8');
  console.log(`${path}: ${article.title}`);
}

const overviewPath = join(root, 'silbi', 'varicose-vein-silbi-claim.html');
const overview = readFileSync(overviewPath, 'utf8');
const overviewLinks = '<h2>치료 방법과 지급 결과별로 확인하기</h2><div class="article-actions"><a href="/silbi/varicose-laser-silbi-claim">레이저 수술 실비와 서류</a><a href="/silbi/varicose-radiofrequency-insurance">고주파 수술 실비·수술비</a><a href="/silbi/varicose-venaseal-clarivein-silbi">베나실·클라리베인 비용</a><a href="/claims/varicose-insurance-low-payout-denied">보험금이 적거나 거절됐다면</a></div>';
if (!overview.includes('치료 방법과 지급 결과별로 확인하기')) {
  writeFileSync(overviewPath, overview.replace('<h2>공식 확인처</h2>', `${overviewLinks}<h2>공식 확인처</h2>`).replace('"dateModified":"2026-09-26"', '"dateModified":"2026-09-27"'), 'utf8');
}
