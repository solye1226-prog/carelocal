import { writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const origin = 'https://hospital.hbuby.com';
const source = ['손해보험협회 보험금 청구서류 안내', 'https://consumer.knia.or.kr/m/consumer/insurance-guide/0202.do'];
const articles = [
  {
    slug: 'disease-vs-type-surgery-benefit',
    title: '질병수술비와 종수술비 차이, 수술 후 두 담보를 확인하는 순서',
    description: '질병수술비와 종수술비는 수술을 확인하는 기준이 다릅니다. 담보명, 수술 정의, 분류표, 동일일 수술 규정과 필요한 서류를 차례로 살펴보세요.',
    keyword: '질병수술비 종수술비 차이',
    lead: '수술을 받고 증권을 펼쳤는데 질병수술비와 종수술비가 모두 적혀 있다면 두 담보를 따로 확인해야 합니다. 하나는 질병으로 인한 수술인지, 다른 하나는 가입 약관의 수술분류표에서 어디에 해당하는지를 살펴보는 담보일 수 있습니다. 담보 이름만으로 중복 지급 여부나 금액을 결론 내릴 수는 없습니다.',
    thumb: 'disease-vs-type-surgery-thumb.webp',
    images: ['disease-vs-type-surgery-policy.webp', 'disease-vs-type-surgery-review.webp'],
    imageAlts: ['질병수술비와 종수술비 약관을 나란히 비교하는 장면', '수술확인서와 보험 약관을 대조하는 장면'],
    rows: [
      ['질병수술비', '질병으로 약관상 수술을 받았는지', '질병명, 실제 수술행위, 수술 정의와 제외 규정'],
      ['종수술비', '수술분류표의 항목과 지급 종수에 해당하는지', '적용 약관 버전, 수술명·부위·방법'],
      ['실손의료비', '실제 본인이 부담한 의료비의 보장 대상인지', '영수증, 세부내역서, 급여·비급여, 공제 조건']
    ],
    sections: [
      ['담보명이 비슷해도 확인할 기준은 다릅니다', '질병수술비는 질병으로 수술을 받았을 때를 다루는 정액형 담보인 경우가 많습니다. 종수술비는 약관에 정한 수술을 종류별로 구분해 지급액을 달리 정하는 담보입니다. 다만 실제 보장 범위는 상품과 가입 시기에 따라 달라집니다.', '수술이 고가이거나 입원을 오래 했다는 사정은 종수술비의 종수를 정하는 기준이 아닙니다. 반대로 수술확인서에 수술이라고 적혀 있어도 약관이 정한 수술의 정의·제외 항목은 별도로 살펴야 합니다.'],
      ['같은 수술로 둘 다 청구할 수 있을까요?', '두 특약에 모두 가입했고 각각의 지급 요건에 해당한다면 두 담보를 함께 청구할 수 있는지 확인할 수 있습니다. 다만 하나의 담보에 해당한다는 사실만으로 다른 담보의 지급이 확정되지는 않습니다.', '먼저 보험증권에서 담보명을 정확하게 확인하고, 각 담보의 보험금 지급 사유와 면책·제외 항목을 따로 읽으세요. 실손의료비는 실제 의료비를 보는 보험이므로 정액형 수술비와 같은 방식으로 금액을 계산하지 않습니다.'],
      ['수술확인서에서 무엇을 확인하나요?', '수술명, 수술일, 수술 부위, 수술 방법과 진단명이 출발점입니다. 병원의 표현과 약관의 분류표 명칭이 다르거나 수술 방법이 애매하면 수술기록지 등 실제 시행한 행위를 보여 주는 자료가 필요할 수 있습니다.', '예를 들어 내시경으로 조직을 일부 떼어낸 경우와 병변을 절제한 경우는 의료 기록상의 행위가 다릅니다. 이 글만으로 특정 시술을 보험상 수술이라고 판단하지 말고, 의료기관 기록과 해당 계약의 약관을 대조하세요.'],
      ['동일일 수술·재수술 규정을 놓치지 마세요', '한날에 두 부위를 수술하거나 같은 질병으로 다시 수술한 경우 지급 횟수는 담보별 약관에 따릅니다. 수술을 두 번 했다는 사실이 곧 두 번의 보험금 지급을 뜻하지는 않습니다.', '수술명과 날짜를 시간 순서대로 적고, 이전 청구내역도 함께 보관하세요. 보험사가 보완서류를 요청하면 어느 담보의 어떤 요건을 확인하려는 것인지 묻는 것이 실무적으로 유용합니다.']
    ],
    questions: [
      ['질병수술비와 종수술비는 같은 보험금인가요?', '아닙니다. 별도 담보일 수 있으며 지급 사유와 약관 기준도 각각 확인해야 합니다.'],
      ['한 번의 수술로 두 담보를 청구할 수 있나요?', '각 담보에 가입했고 각 지급 요건에 해당하는지 확인해야 합니다. 청구 가능성과 실제 지급은 약관 및 심사에 따릅니다.'],
      ['수술비가 비싸면 높은 종수인가요?', '아닙니다. 수술분류표의 해당 항목과 실제 시행한 수술을 대조합니다.'],
      ['종수술비에 없으면 질병수술비도 안 되나요?', '단정할 수 없습니다. 두 담보의 수술 정의와 제외 조항을 따로 읽어야 합니다.'],
      ['실손보험도 함께 확인해야 하나요?', '실제 낸 의료비가 있다면 별도 계약의 실손의료비 보장 여부를 확인할 수 있습니다.']
    ],
    related: [['수술분류표 확인', '/surgery-benefit/surgery-classification.html'], ['수술비 청구서류', '/claims/surgery-claim-documents.html'], ['종수술비 청구', '/surgery-benefit/type-surgery-benefit-claim']],
    sources: [source, ['네이버페이 수술비 특약 안내', 'https://pay.naver.com/mymoney/insurance/contents/50']]
  },
  {
    slug: 'cataract-surgery-benefit',
    title: '백내장 수술비 몇 종일까? 인공수정체·수술명과 약관 확인 방법',
    description: '백내장 수술비 종수는 수술비용이나 렌즈 가격만으로 정할 수 없습니다. 수술확인서의 실제 수술명, 가입 약관의 분류표, 실손의료비를 따로 확인하세요.',
    keyword: '백내장 수술비 몇 종',
    lead: '백내장 수술을 앞두거나 이미 받은 뒤 “몇 종 수술비인가요?”라고 묻는 경우가 많습니다. 답은 인터넷의 공통 분류표가 아니라 내가 가입한 상품의 약관과 실제 시행한 수술기록에 있습니다. 특히 인공수정체 종류와 수술비 청구 기준을 혼동하지 않는 것이 중요합니다.',
    thumb: 'cataract-surgery-benefit-thumb.webp',
    images: ['cataract-surgery-benefit-consult.webp', 'cataract-surgery-benefit-documents.webp'],
    imageAlts: ['안과에서 백내장 수술과 인공수정체를 상담하는 장면', '백내장 수술확인서와 진료비 서류를 살펴보는 장면'],
    rows: [
      ['종수술비', '가입 당시 수술분류표에서 실제 시행한 수술 찾기', '수술명, 양안 수술일, 동일일 규정'],
      ['질병수술비', '약관상 수술 정의와 백내장 관련 제외 사항', '수술확인서와 진단명'],
      ['실손의료비', '본인 부담 의료비와 급여·비급여 항목', '인공수정체 비용, 세부내역서, 계약 조건']
    ],
    sections: [
      ['백내장 수술비 종수를 한 숫자로 말할 수 없는 이유', '백내장 수술은 혼탁해진 수정체를 제거하고 인공수정체를 삽입하는 과정으로 이뤄집니다. 수술 방법은 환자 상태에 따라 달라질 수 있습니다. 그러나 의료행위의 설명이 보험 약관의 분류를 자동으로 정해 주지는 않습니다.', '1~3종 또는 1~5종처럼 분류 방식부터 계약마다 다를 수 있습니다. 다른 사람이 받은 보험금 액수나 온라인 수술분류표만 보고 내 계약의 종수를 추정하지 마세요.'],
      ['인공수정체 종류와 보험금 항목은 구분하세요', '단초점, 연속초점·다초점, 난시교정용 등 렌즈 선택은 눈 상태와 생활상 필요에 따른 의료 상담의 영역입니다. 렌즈 가격이 높다고 종수술비 종수가 높아지는 것은 아닙니다.', '실손의료비는 실제 의료비의 급여·비급여 구성과 계약 조건을 별도로 봅니다. 렌즈 관련 비용, 검사비, 수술비가 진료비 세부산정내역서에 어떻게 기재됐는지 확인하세요.'],
      ['양쪽 눈 수술이라면 날짜와 수술 단위를 적어두세요', '한쪽씩 다른 날 수술했는지, 같은 날 수술했는지에 따라 청구할 때 살펴볼 규정이 달라질 수 있습니다. 수술확인서에 좌안·우안, 각각의 수술일과 시행 행위가 드러나는지 확인하세요.', '지급 횟수는 수술 횟수만이 아니라 약관의 동일일·동일질병·동일부위 규정에 따릅니다. 보험사에 문의할 때도 어느 담보의 지급 단위를 묻는지 분명히 하세요.'],
      ['청구 전 자료 준비 순서', '증권에서 질병수술비·종수술비·실손의료비의 가입 여부를 확인합니다. 병원에는 수술명·날짜·좌우 눈이 적힌 수술확인서와 진료비 영수증·세부내역서를 요청하세요.', '보험사가 수술 방법이나 의학적 필요성을 추가 확인하면 수술기록지, 진료기록 등을 요청할 수 있습니다. 민감한 진료 자료는 공개 채팅에 올리지 말고 보험사 공식 접수 경로를 이용하세요.']
    ],
    questions: [
      ['백내장 수술은 모두 같은 종수인가요?', '아닙니다. 가입 당시 상품의 수술분류표와 실제 수술행위를 확인해야 합니다.'],
      ['다초점 렌즈를 선택하면 종수술비가 달라지나요?', '렌즈 종류나 가격만으로 종수를 결정할 수 없습니다. 별도 의료비 보장은 실손 약관을 확인하세요.'],
      ['양쪽 눈 수술비를 두 번 받을 수 있나요?', '수술일과 부위뿐 아니라 해당 담보의 지급 단위·횟수 제한을 확인해야 합니다.'],
      ['수술확인서만 있으면 되나요?', '접수는 가능할 수 있으나 보험사가 진단서나 수술기록지 등을 추가 요청할 수 있습니다.'],
      ['백내장 실비도 같이 청구하나요?', '실손에 가입했다면 실제 부담한 의료비의 보장 여부를 별도로 확인할 수 있습니다.']
    ],
    related: [['수술분류표 확인', '/surgery-benefit/surgery-classification.html'], ['수술비 청구서류', '/claims/surgery-claim-documents.html'], ['질병수술비·종수술비 차이', '/surgery-benefit/disease-vs-type-surgery-benefit.html']],
    sources: [source, ['질병관리청 국가건강정보포털 백내장', 'https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=6689']]
  },
  {
    slug: 'gallbladder-surgery-benefit',
    title: '담낭절제술 종수술비, 복강경 수술명과 약관을 확인하는 방법',
    description: '담낭절제술을 받았다면 담석·담낭염 진단명뿐 아니라 수술확인서의 실제 수술명과 방법, 가입 당시 수술분류표를 대조하세요. 청구서류도 정리했습니다.',
    keyword: '담낭절제술 종수술비',
    lead: '담석이나 담낭염 때문에 담낭절제술을 받았을 때 종수술비가 몇 종인지 궁금할 수 있습니다. 진단명이 같아도 시행한 수술 방법과 보험계약의 분류표는 따로 확인해야 합니다. 복강경 수술이라는 말만으로 종수나 지급액을 확정할 수는 없습니다.',
    thumb: 'gallbladder-surgery-benefit-thumb.webp',
    images: ['gallbladder-surgery-benefit-consult.webp', 'gallbladder-surgery-benefit-documents.webp'],
    imageAlts: ['담낭 모형을 보며 수술 방법을 설명받는 장면', '담낭절제술 수술확인서와 약관을 대조하는 장면'],
    rows: [
      ['진단', '담석증·담낭염 등 최종 진단명', '진단명만으로 수술 종수 결정 불가'],
      ['수술', '담낭절제술의 실제 수술명과 방법', '복강경·개복, 동반 시술 여부 기록'],
      ['계약', '질병수술비·종수술비 가입 여부', '가입 당시 약관의 수술분류표와 제외 규정']
    ],
    sections: [
      ['담석 진단과 담낭절제술은 다른 정보입니다', '담석증은 담낭이나 담도에 결석이 생기는 질환입니다. 담석이 발견됐다고 모두 담낭절제술을 받는 것은 아니며, 증상이나 합병증 등에 따라 치료가 달라집니다.', '보험금 청구에서는 진단서의 질병명과 수술확인서의 시행 행위를 분리해 봐야 합니다. 단순 검사나 담도 관련 내시경 처치와 담낭 자체를 절제한 수술은 같은 표현으로 묶지 마세요.'],
      ['복강경·개복이라는 표현을 어떻게 보나요?', '수술확인서와 필요 시 수술기록지에서 실제 담낭을 절제했는지, 수술 접근 방식과 동반 시행 행위가 무엇인지 확인합니다. 병원에서 쓰는 한글·영문 수술명이 약관 용어와 다를 수 있습니다.', '어느 종에 해당하는지는 수술 방법의 이름만으로 단정할 수 없습니다. 가입 당시 수술분류표의 항목·주석·제외 조항까지 확인하고, 불명확하면 보험사에 해당 약관 조항을 근거로 설명해 달라고 요청하세요.'],
      ['동시에 다른 시술을 받았다면 기록을 나눠 보세요', '담낭 수술 과정에서 담도 검사나 다른 처치가 함께 이뤄졌다면 수술기록지에는 여러 행위가 보일 수 있습니다. 각각이 독립한 수술비 지급 사유인지는 해당 담보의 동시수술 규정에 따라 판단됩니다.', '퇴원요약지·수술확인서·진료비 세부내역서에서 행위와 날짜를 구분해 적어두면 보완서류 요청에 대응하기 쉽습니다.'],
      ['담낭절제술 청구서류와 접수 순서', '수술명·수술일이 적힌 수술확인서, 진단명 확인 자료, 보험금 청구서와 신분 확인 자료가 출발점입니다. 실손의료비를 함께 청구한다면 진료비 영수증과 세부내역서도 필요할 수 있습니다.', '보험사 공식 안내에서 해당 담보의 제출서류를 확인한 뒤 앱이나 홈페이지로 접수하고, 접수번호를 저장하세요. 입원 일수나 병원비가 종수술비의 종수를 정하는 기준은 아닙니다.']
    ],
    questions: [
      ['복강경 담낭절제술은 몇 종인가요?', '모든 계약에 적용되는 단일 종수는 없습니다. 가입 약관의 수술분류표와 실제 수술명을 대조해야 합니다.'],
      ['담석 진단만으로 수술비 청구가 되나요?', '수술비 담보는 약관상 수술 요건을 확인해야 하므로 진단 사실만으로 판단할 수 없습니다.'],
      ['담낭염과 담석증은 청구서류가 다른가요?', '최종 진단명과 보험사 요청에 따라 추가 자료가 달라질 수 있습니다. 수술 사실 자료는 공통으로 확인하세요.'],
      ['담도 내시경 처치도 함께 받았으면 두 번 지급되나요?', '동시수술·처치에 관한 약관을 확인해야 하며 자동으로 두 번 지급되는 것은 아닙니다.'],
      ['실비보험도 따로 접수할 수 있나요?', '가입한 실손계약의 보장 대상 의료비인지 확인하고 영수증·세부내역서를 준비하세요.']
    ],
    related: [['수술분류표 확인', '/surgery-benefit/surgery-classification.html'], ['종수술비 청구', '/surgery-benefit/type-surgery-benefit-claim'], ['수술비 청구서류', '/claims/surgery-claim-documents.html']],
    sources: [source, ['질병관리청 국가건강정보포털 담석증', 'https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=6735']]
  },
  {
    slug: 'hemorrhoid-surgery-benefit',
    title: '치핵 수술비 몇 종일까? 절제술과 비수술 처치 구분하기',
    description: '치핵 치료 후 수술비를 확인할 때 치핵절제술과 결찰·경화 등 처치를 구분해야 합니다. 실제 시행 행위와 가입 약관의 수술 정의·분류표를 확인하세요.',
    keyword: '치핵 수술비 몇 종',
    lead: '치질 치료를 받았다고 해서 모든 치료가 같은 수술비 청구 대상은 아닙니다. 흔히 치질이라고 부르는 질환 가운데 치핵을 어떻게 치료했는지부터 확인해야 합니다. 치핵절제술, 고무밴드 결찰술, 경화술을 모두 한 가지 수술명으로 묶으면 약관 대조가 어려워집니다.',
    thumb: 'hemorrhoid-surgery-benefit-thumb.webp',
    images: ['hemorrhoid-surgery-benefit-consult.webp', 'hemorrhoid-surgery-benefit-documents.webp'],
    imageAlts: ['치핵 치료 방법을 의료진과 상담하는 장면', '치핵 수술확인서와 보험 서류를 살펴보는 장면'],
    rows: [
      ['치핵절제술', '조직을 절제한 실제 수술행위 확인', '수술확인서·기록지의 정확한 명칭'],
      ['결찰·경화 등', '비수술적 처치인지 실제 시행 내용 확인', '병원 표현과 보험상 수술 정의를 구분'],
      ['보험 담보', '질병수술비·종수술비·실손 가입 여부', '각각의 약관과 제출서류가 다름']
    ],
    sections: [
      ['치핵 치료는 수술만 있는 것이 아닙니다', '질병관리청은 치핵 치료를 보존적 치료, 고무밴드 결찰·경화 등 보조요법, 치핵절제술 같은 수술적 방법으로 구분합니다. 증상과 치핵 상태에 따라 의료진이 치료법을 정합니다.', '보험에서는 치료를 받았다는 사실뿐 아니라 실제 시행한 행위가 가입 약관에서 정의하는 수술인지 확인해야 합니다. 외래에서 간단하게 받았거나 입원했다는 사실만으로 결론을 내릴 수 없습니다.'],
      ['치핵 수술비 종수는 어디서 확인하나요?', '보험증권의 종수술비 담보명과 가입 시기를 확인한 뒤 그 계약의 수술분류표를 찾습니다. 병원의 수술확인서에 적힌 정확한 수술명과 방법을 대조하세요.', '치핵절제술도 수술 방법이 한 가지가 아닙니다. 온라인에서 “치핵은 몇 종”이라는 사례를 보더라도 자신의 수술기록과 약관에 그대로 적용하지 마세요.'],
      ['치질과 치핵, 진단명을 혼동하지 마세요', '일상적으로 치질이라고 부르지만 치핵 외 다른 항문질환일 수 있습니다. 보험 접수에서는 진단서의 질병명과 시행한 치료명 모두 중요합니다.', '수술확인서에 병명만 있고 행위가 모호하다면 의료기관에 실제 시술·수술명을 확인하세요. 증상 설명만으로 약관상 분류를 결정하지 않습니다.'],
      ['청구할 때 준비할 자료', '보험사 안내에 맞춰 보험금 청구서, 진단명 확인 자료, 수술확인서를 준비합니다. 처치인지 절제술인지 애매하면 수술기록지 또는 진료기록을 추가 요청받을 수 있습니다.', '실손의료비는 실제 부담한 치료비를 별도로 확인하므로 진료비 영수증과 세부내역서도 보관하세요. 민감정보가 있는 의료 기록은 보험사 공식 접수 경로로 제출합니다.']
    ],
    questions: [
      ['치질 수술은 모두 같은 종수인가요?', '아닙니다. 정확한 진단명·치료명과 가입 약관의 분류표를 확인해야 합니다.'],
      ['고무밴드 결찰술은 수술비가 나오나요?', '병원에서 시행한 행위와 약관상 수술 정의를 대조해야 하며 여기서 지급을 단정할 수 없습니다.'],
      ['치핵절제술 수술확인서에는 무엇이 있어야 하나요?', '최종 진단명, 실제 수술명과 수술일·방법을 확인할 수 있어야 합니다. 보험사 양식도 확인하세요.'],
      ['입원하지 않았으면 수술비 청구가 안 되나요?', '입원 여부만으로 결론 내리지 않습니다. 해당 담보의 수술 및 지급 요건을 확인하세요.'],
      ['실손과 수술비를 함께 확인할 수 있나요?', '가입한 두 담보의 보장 조건을 각각 살펴볼 수 있으며 서류도 다를 수 있습니다.']
    ],
    related: [['수술분류표 확인', '/surgery-benefit/surgery-classification.html'], ['수술비 청구서류', '/claims/surgery-claim-documents.html'], ['질병수술비·종수술비 차이', '/surgery-benefit/disease-vs-type-surgery-benefit.html']],
    sources: [source, ['질병관리청 국가건강정보포털 치핵', 'https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=5818']]
  },
  {
    slug: 'thyroid-surgery-benefit',
    title: '갑상선암 수술비, 절제 범위와 진단비를 따로 확인하는 방법',
    description: '갑상선암 수술 후 수술비와 진단비를 혼동하기 쉽습니다. 수술확인서의 절제 범위·접근 방법과 가입한 수술비 특약, 진단비 약관을 따로 대조하세요.',
    keyword: '갑상선암 수술비',
    lead: '갑상선암 진단을 받고 수술했다면 진단비와 수술비를 한 항목으로 생각하기 쉽습니다. 하지만 확정 진단에 관한 담보와 실제 수술에 관한 담보는 확인하는 자료가 다릅니다. 갑상선 일부를 절제했는지 전부 절제했는지, 어떤 방법으로 수술했는지부터 기록을 살펴보세요.',
    thumb: 'thyroid-surgery-benefit-thumb.webp',
    images: ['thyroid-surgery-benefit-consult.webp', 'thyroid-surgery-benefit-documents.webp'],
    imageAlts: ['갑상선 초음파와 수술 방법을 상담하는 장면', '갑상선암 수술기록과 진단서 및 보험약관을 대조하는 장면'],
    rows: [
      ['진단비', '갑상선암 확정 진단과 약관상 암 분류', '진단서·병리결과지·진단일'],
      ['종수술비', '실제 절제술과 수술분류표의 항목', '수술명·절제 범위·방법·동반 수술'],
      ['질병수술비', '약관상 질병 수술 지급 요건', '수술 정의와 제외·횟수 규정'],
      ['실손의료비', '본인 부담 의료비의 계약상 보장', '영수증·세부내역서']
    ],
    sections: [
      ['갑상선암 진단비와 수술비는 질문이 다릅니다', '진단비는 계약에서 정한 암 진단확정 요건과 분류를 확인합니다. 수술비는 실제 시행한 수술이 해당 특약의 지급 사유인지 확인합니다. 진단비를 청구했더라도 수술비 특약 가입 여부는 별도로 확인할 필요가 있습니다.', '갑상선암을 일반암·유사암 등으로 구분하는 방식은 계약마다 다를 수 있습니다. 진단비 분류를 수술비의 종수와 동일한 기준으로 보지 마세요.'],
      ['부분절제·전절제·로봇수술을 구분하세요', '갑상선암 수술에는 갑상선의 일부 또는 전부를 절제하는 방식이 있으며, 환자 상태에 따라 접근 방법도 달라질 수 있습니다. 국가암정보센터도 내시경·로봇수술 등 여러 방법을 설명합니다.', '수술확인서에서 실제 절제 범위와 수술명, 날짜를 확인하고 필요하면 수술기록지를 받으세요. 로봇을 이용했다는 사실이나 비용이 높다는 사정만으로 종수술비 분류가 확정되지는 않습니다.'],
      ['림프절 수술을 함께 받았다면', '갑상선 수술과 함께 림프절 관련 행위가 기록됐다면 각각의 수술명과 시행일을 확인하세요. 수술기록지와 병리결과지에서 어떤 조직을 절제했는지 구분할 수 있습니다.', '동시수술의 지급 횟수나 별도 수술로 인정되는지는 해당 약관의 지급 단위에 따릅니다. 수술이 여러 개로 보인다는 이유만으로 보험금을 합산하지 마세요.'],
      ['청구서류를 항목별로 준비하는 법', '진단비를 확인하려면 확정 진단서와 병리결과지를, 수술비를 확인하려면 수술확인서와 필요 시 수술기록지를 중심으로 준비합니다. 실손의료비는 영수증과 세부내역서를 추가로 살펴보세요.', '보험사 공식 청구 안내에서 담보별 서류 목록과 제출 방법을 확인하고 접수번호를 보관하세요. 의료 기록은 민감정보이므로 공개 대화방에 올리지 않는 것이 좋습니다.']
    ],
    questions: [
      ['갑상선암 진단비를 받으면 수술비도 지급되나요?', '자동으로 결정되지 않습니다. 수술비 특약의 가입 여부와 해당 수술의 지급 요건을 따로 확인해야 합니다.'],
      ['부분절제와 전절제는 같은 종수인가요?', '가입 약관의 수술분류표와 실제 수술명을 대조해야 하므로 일괄 답할 수 없습니다.'],
      ['로봇수술이면 높은 종수인가요?', '로봇을 사용했다는 사실이나 수술비용만으로 종수를 정할 수 없습니다.'],
      ['림프절 절제도 별도 수술비가 되나요?', '동시수술·부수술 규정과 실제 기록을 확인해야 합니다.'],
      ['진단서만으로 수술비를 청구할 수 있나요?', '수술명과 날짜를 확인할 수술확인서 등을 요청받을 수 있습니다.']
    ],
    related: [['갑상선암 진단비 청구', '/diagnosis-benefit/thyroid-cancer-benefit-claim'], ['수술분류표 확인', '/surgery-benefit/surgery-classification.html'], ['로봇수술 가이드', '/guides/robotic-surgery.html']],
    sources: [source, ['국가암정보센터 갑상선암 치료', 'https://www.cancer.go.kr/lay1/program/S1T211C212/cancer/view.do?cancer_seq=3341&menu_seq=3357']]
  }
];

const escape = (value) => String(value).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const link = ([label, href]) => `<a href="${escape(href)}"${href.startsWith('http') ? ' target="_blank" rel="noopener"' : ''}>${escape(label)}</a>`;
const figure = (file, alt, eager = false) => `<figure class="guide-image-panel"><img src="/assets/images/${file}" width="1672" height="941" loading="${eager ? 'eager' : 'lazy'}" decoding="async" alt="${escape(alt)}"></figure>`;

for (const a of articles) {
  const path = `/surgery-benefit/${a.slug}.html`;
  const articleJson = JSON.stringify({ '@context': 'https://schema.org', '@type': 'Article', headline: a.title, description: a.description, image: `${origin}/assets/images/${a.thumb}`, author: { '@type': 'Organization', name: '케어로컬' }, publisher: { '@type': 'Organization', name: '케어로컬' }, datePublished: '2026-09-22', dateModified: '2026-09-22', inLanguage: 'ko-KR' });
  const sections = a.sections.map(([heading, first, second], index) => `<h2>${escape(heading)}</h2><p>${escape(first)}</p>${index === 0 ? figure(a.images[0], a.imageAlts[0]) : ''}<p>${escape(second)}</p>${index === 2 ? figure(a.images[1], a.imageAlts[1]) : ''}`).join('\n');
  const rows = a.rows.map(([item, check, note]) => `<tr><td>${escape(item)}</td><td>${escape(check)}</td><td>${escape(note)}</td></tr>`).join('');
  const faq = a.questions.map(([q, answer]) => `<details><summary>${escape(q)}</summary><p>${escape(answer)}</p></details>`).join('');
  const html = `<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>${escape(a.title)}</title><meta name="description" content="${escape(a.description)}"><meta property="og:title" content="${escape(a.title)}"><meta property="og:description" content="${escape(a.description)}"><meta property="og:image" content="${origin}/assets/images/${a.thumb}"><link rel="canonical" href="${origin}${path}"><link rel="stylesheet" href="/assets/site.css?v=20260922-surgery-v1"><script type="application/ld+json">${articleJson}</script><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2258793659580551" crossorigin="anonymous"></script></head>
<body><header class="site-header"><nav class="nav" aria-label="주요 메뉴"><a class="brand" href="/"><span class="brand-mark">CL</span><span><strong>케어로컬</strong><small>보험 정보 자료실</small></span></a><div class="nav-links"><a href="/claims/">보험금 청구</a><a href="/silbi/">실비보험</a><a href="/diagnosis-benefit/">진단비</a><a href="/surgery-benefit/">수술비</a><a href="/standards/">약관·기준</a></div></nav></header>
<main class="section article-body insurance-series-article"><div class="breadcrumb"><a href="/">홈</a> / <a href="/surgery-benefit/">수술비</a> / ${escape(a.keyword)}</div><p class="eyebrow">Surgery Benefit</p><h1>${escape(a.title)}</h1><p class="lead">${escape(a.lead)}</p><div class="insurance-company-cta"><a href="/insurance-companies/">보험사별 공식 홈페이지 확인하기</a></div>${figure(a.thumb, `${a.keyword} 확인 가이드 카드뉴스`, true)}<div class="notice">본 콘텐츠는 일반적인 의료 및 보험 정보 제공을 목적으로 작성되었습니다. 보험금 지급 여부는 가입 상품, 약관, 가입 시기와 보험사 심사 기준에 따라 달라질 수 있습니다. 정확한 보장 여부는 개별 계약과 약관 확인이 필요합니다.</div>
<h2>${escape(a.keyword)} 핵심 확인</h2><table><thead><tr><th>항목</th><th>확인할 내용</th><th>주의할 점</th></tr></thead><tbody>${rows}</tbody></table>
${sections}
<h2>청구 전에 확인할 서류</h2><table><thead><tr><th>자료</th><th>확인 목적</th><th>준비할 때</th></tr></thead><tbody><tr><td>보험증권·가입 당시 약관</td><td>담보명과 수술 정의·분류표 확인</td><td>현재 판매 상품과 혼동하지 않기</td></tr><tr><td>수술확인서</td><td>수술명·시행일·방법 확인</td><td>기재가 모호하면 병원에 문의</td></tr><tr><td>진단서·진료확인서</td><td>질병명과 진단 시점 확인</td><td>담보별 요구 여부 확인</td></tr><tr><td>수술기록지</td><td>실제 시행 행위가 불분명한 경우</td><td>보험사 요청 시 추가 제출 가능</td></tr><tr><td>영수증·세부내역서</td><td>실손의료비를 함께 확인하는 경우</td><td>급여·비급여 구분 확인</td></tr></tbody></table>
<h2>확인 순서</h2><ol><li>가입 보험의 정확한 담보명과 가입 시기를 확인합니다.</li><li>병원 자료에서 최종 진단명과 실제 수술명·방법·날짜를 적습니다.</li><li>해당 계약의 수술 정의, 분류표, 지급 횟수 및 제외 규정을 대조합니다.</li><li>보험사 공식 안내에서 필요한 서류를 확인해 접수하고 결과를 기록합니다.</li></ol>
<h2>자주 묻는 질문</h2><div class="faq">${faq}</div><h2>함께 보면 좋은 글</h2><div class="article-actions">${a.related.map(link).join('')}</div><h2>공식 확인처</h2><ul>${a.sources.map((x) => `<li>${link(x)}</li>`).join('')}</ul><div class="insurance-company-cta"><a href="/insurance-companies/">보험사별 공식 홈페이지 확인하기</a></div><section class="kakao-inquiry-cta" aria-labelledby="contact-title"><p class="cta-label">문의 안내 <span>보험</span></p><h2 id="contact-title">가입한 보험의 보장이 궁금하신가요?</h2><p>가입한 보험의 보장 내용이나 콘텐츠와 관련해 궁금한 점이 있다면 카카오톡으로 문의해 주세요. 주민등록번호·진단서·영수증 등 민감한 개인정보가 포함된 자료는 전송하지 않는 것을 권장합니다.</p><a class="kakao-button" href="https://open.kakao.com/o/sVyT7uph" target="_blank" rel="noopener">카카오톡으로 문의하기</a></section></main></body></html>`;
  writeFileSync(join(root, 'surgery-benefit', `${a.slug}.html`), html + '\n', 'utf8');
  console.log(`${path}: ${a.title}`);
}
