import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const origin = 'https://hospital.hbuby.com';
const sources = {
  kdca: ['질병관리청 국가건강정보포털 백내장', 'https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=6689'],
  samsung: ['삼성화재 보험금 청구 구비서류', 'https://direct.samsungfire.co.kr/claim/healthreward/health_doc.html'],
  court: ['대법원 다초점 인공수정체 비용 관련 판결 안내', 'https://scourt.go.kr/supreme/news/NewsViewAction2.work?gubun=4&searchOption=&searchWord=&seqnum=10236'],
};

const articles = [
  {
    slug: 'cataract-surgery-claim-documents', title: '백내장 수술 보험금 청구서류, 실비와 수술비는 무엇을 준비할까?',
    description: '백내장 수술 후 실비보험과 수술비 특약에 필요한 서류를 구분합니다. 진료비 영수증, 세부내역서, 수술확인서, 인공수정체 자료를 어떤 순서로 확인할지 정리했습니다.',
    keyword: '백내장 수술 보험금 청구서류', lead: '백내장 수술 후 병원에서 어떤 서류를 받아야 할까요? 실손의료비는 실제 결제한 비용과 항목을, 수술비 특약은 진단명·수술명·수술일과 약관상 수술 여부를 살핍니다. 한 번에 모든 유료 증명서를 발급하기보다 가입 담보부터 확인하면 필요한 자료를 더 정확히 준비할 수 있습니다.',
    thumb: 'cataract-docs-thumb.webp', images: ['cataract-docs-hospital.webp', 'cataract-docs-home.webp'],
    alts: ['백내장 수술 후 병원 창구에서 보험금 청구서류를 받는 장면', '백내장 수술 진료비 영수증과 수술확인서를 정리하는 장면'],
    rows: [['실손의료비', '진료비 계산서·영수증, 진료비 세부내역서', '수술·검사·인공수정체 비용 항목을 구분'], ['수술비 특약', '진단명·수술명·수술일이 확인되는 수술확인서 등', '가입 당시 수술 정의·분류표와 대조'], ['입원 관련 담보', '입퇴원확인서와 실제 진료·관찰 기록', '확인서만으로 입원 보장이 결정되지는 않음']],
    sections: [
      ['실비와 정액 수술비는 서류 목적이 다릅니다', '실손의료비는 병원에 실제로 지급한 의료비 중 가입한 약관의 보장 대상 금액을 확인하는 담보입니다. 병원에서 발급한 진료비 계산서·영수증과 세부내역서가 비용 확인의 출발점입니다. 카드 승인 문자만으로는 수술료와 렌즈 재료비를 나누기 어렵습니다.', '수술비 특약은 지출액과 별개로 약관에서 정한 수술에 해당하는지를 봅니다. 백내장 진단명과 실제 수술명, 날짜가 드러나는 수술확인서나 보험사가 인정하는 대체 서류를 준비하세요. 둘 다 가입했더라도 심사는 각각 진행됩니다.'],
      ['병원 창구에서 먼저 받아둘 서류', '진료비 계산서·영수증, 진료비 세부내역서, 수술확인서 발급 가능 여부를 문의하세요. 삼성화재 공식 안내는 수술 청구 시 진단명·수술명·수술일이 확인되는 자료를, 실손 청구 시 병원비 자료를 담보별로 안내합니다. 이는 한 보험사의 예시이므로 실제 제출 목록은 가입 보험사에서 다시 확인해야 합니다.', '다초점 인공수정체를 사용했다면 세부내역서에서 렌즈 재료비와 수술·검사비가 어떻게 기재됐는지 살펴보세요. 검사 결과나 진료기록 등 추가 자료가 필요한지는 접수 후 보험사 요청 사유를 확인하고 발급해도 됩니다.'],
      ['입원·통원 표시는 별도로 확인하세요', '백내장 수술은 환자 상태와 수술 경과에 따라 당일 귀가하는 경우가 있습니다. 질병관리청의 백내장 안내도 합병증이 없다면 당일 퇴원이 가능하다고 설명합니다. 병원에서 입퇴원확인서를 받았다는 사실만으로 보험 약관상 입원 의료비가 된다고 단정할 수는 없습니다.', '입원일당이나 실손 입원 한도가 쟁점이라면 실제 진료기록, 관찰·처치 내용, 귀가 시각과 가입 약관을 함께 확인하세요. 보험사가 통원으로 심사했다면 적용한 약관 조항과 근거를 문서로 요청하는 편이 좋습니다.'],
      ['양쪽 눈을 수술했다면 날짜별로 분리하세요', '양안을 다른 날짜에 수술했다면 각 날짜의 영수증·세부내역서·수술확인서를 한 묶음씩 정리하세요. 같은 날 두 눈을 수술했다면 한 장의 확인서에 양안 수술 내용이 어떻게 기록됐는지 확인해야 합니다. 자료를 날짜별·눈별로 구분하면 보완 요청 시 대응이 쉽습니다.', '수술비의 지급 횟수는 눈의 개수만으로 결정되지 않습니다. 계약의 수술 1회 정의, 동일일 수술 조항, 담보별 제한을 따로 대조해야 합니다.'],
      ['접수 전 빠르게 점검할 것', '보험증권에서 실손, 질병수술비, 종수술비, 입원비 등 실제 가입 담보를 확인합니다. 진료비 서류와 수술 사실 증명 자료를 준비한 뒤 보험사 공식 앱·홈페이지에서 접수 가능 여부를 확인하세요. 원본이나 추가 기록을 요구하는 경우가 있으니 발급 비용이 큰 서류는 먼저 문의하는 것이 좋습니다.', '접수 후에는 접수번호, 제출 파일, 보완서류 요청 내용과 지급 계산서를 저장하세요. 예상보다 적게 지급됐다면 렌즈 재료비, 비급여 항목, 자기부담금, 통원·입원 분류 중 어디에서 차이가 생겼는지 확인합니다.'],
    ],
    questions: [['백내장 수술확인서만 내면 실비 청구가 되나요?', '비용 심사를 위해 병원 영수증과 세부내역서 등 추가 자료가 필요할 수 있습니다.'], ['진단서와 수술확인서를 모두 발급받아야 하나요?', '항상 둘 다 필요한 것은 아닙니다. 가입 보험사의 담보별 안내에서 대체 가능 서류를 확인하세요.'], ['다초점 렌즈 영수증도 제출하나요?', '렌즈 비용이 포함된 세부내역서를 준비하면 비용 항목을 구분하는 데 도움이 됩니다. 보장 여부는 계약 약관에 따라 별도 판단됩니다.'], ['입퇴원확인서가 있으면 입원비가 나오나요?', '확인서만으로 확정되지 않습니다. 실제 치료 경과와 입원 필요성, 가입 약관을 함께 봅니다.'], ['양쪽 눈 수술 서류를 하나로 접수할 수 있나요?', '보험사 접수 방식에 따라 다릅니다. 날짜별 영수증과 수술 내용을 분리해 준비하세요.']],
    related: [['백내장 수술비 종합 안내', '/surgery-benefit/cataract-surgery-benefit.html'], ['다초점 렌즈 실비 비용', '/claims/cataract-multifocal-lens-silbi'], ['백내장 당일 수술 입원·통원', '/claims/cataract-day-surgery-inpatient-outpatient']], sourceKeys: ['kdca', 'samsung'],
  },
  {
    slug: 'cataract-multifocal-lens-silbi', title: '백내장 다초점 인공수정체 비용, 실비보험은 어디까지 확인할까?',
    description: '백내장 다초점 인공수정체 실비 청구에서 렌즈 재료비와 수술·검사비를 구분하세요. 가입 시기별 약관, 세부내역서, 보험금 지급 계산서를 확인하는 방법을 정리했습니다.',
    keyword: '백내장 다초점 인공수정체 실비', lead: '백내장 수술에서 다초점 인공수정체를 선택했다면 높은 렌즈 비용 전체가 실비로 처리되는지 궁금할 수 있습니다. 핵심은 렌즈 재료비와 수술·검사비를 같은 비용으로 묶지 않는 것입니다. 보장 여부는 의료기관의 비용 표기뿐 아니라 가입 시기와 실손 약관의 제외 조항에 따라 달라집니다.',
    thumb: 'cataract-multifocal-thumb.webp', images: ['cataract-multifocal-consult.webp', 'cataract-multifocal-cost.webp'],
    alts: ['백내장 수술 전 다초점 인공수정체 선택을 상담하는 장면', '백내장 다초점 렌즈 비용과 수술비 세부내역을 구분하는 장면'],
    rows: [['인공수정체 재료비', '단초점·다초점 등 실제 사용한 렌즈와 청구액', '계약 약관의 렌즈 비용 보장·제외 조항'], ['수술·검사비', '수술료, 검사료, 진찰료의 세부 항목', '렌즈 재료비와 별도로 확인'], ['지급 결과', '제외 금액, 자기부담금, 입원·통원 구분', '보험금 산출내역서로 이유 확인']],
    sections: [
      ['렌즈 종류와 보험 보장은 다른 질문입니다', '질병관리청은 백내장 수술에서 혼탁한 수정체를 제거하고 인공수정체를 삽입하며 렌즈의 종류가 다양하다고 설명합니다. 다초점 렌즈를 썼다는 사실은 의료적 선택과 비용 항목을 보여 줄 뿐, 그 비용이 내 실손 계약에서 보장된다는 뜻은 아닙니다.', '수술 전에는 의료진에게 예상되는 시력 결과와 비용을, 보험사에는 본인 계약의 렌즈 관련 약관을 각각 문의하세요. 보험사 답변을 들을 때는 판매 중인 새 상품이 아니라 내 보험증권의 가입 시기와 약관 버전을 기준으로 해 달라고 요청합니다.'],
      ['영수증 총액보다 세부내역서가 중요합니다', '병원 진료비 계산서·영수증에는 최종 결제액이 보이지만, 어떤 항목이 수술료이고 어떤 항목이 렌즈 재료비인지 명확하지 않을 수 있습니다. 세부내역서에서 인공수정체 비용, 검사, 처치, 수술 항목을 표시해 보세요.', '대법원은 다초점 인공수정체 비용과 실손보험 청구를 둘러싼 사건을 다룬 바 있습니다. 다만 판결 한 건을 모든 계약의 일괄 결론으로 적용할 수 없습니다. 실제 심사에서는 해당 계약의 약관과 의료비 항목, 청구 내용이 중요합니다.'],
      ['가입 시기와 약관 문구를 찾아보세요', '실손보험은 가입 시기에 따라 보장 구조와 자기부담금, 비급여 처리 방식이 다릅니다. 계약서에서 인공수정체, 시력교정 목적 치료, 안경·렌즈 관련 제외 조항을 확인하세요. 다초점 비용이 제외되더라도 다른 수술·검사 항목까지 같은 결론이라고 단정하지 마세요.', '약관 표현이 어렵다면 보험사에 “다초점 인공수정체 재료비와 백내장 수술·검사비를 항목별로 어떻게 심사하나요?”라고 물어보세요. 구두 설명만 듣기보다 적용 조항이나 지급 산출내역을 받아두면 이후 비교가 쉽습니다.'],
      ['보험금이 예상보다 적게 나왔다면', '지급 계산서에서 병원 청구액, 보장 제외액, 공제액, 최종 지급액을 순서대로 확인합니다. 렌즈 재료비가 제외됐는지, 검사 항목이 제외됐는지, 통원 한도가 적용됐는지에 따라 대응할 자료가 달라집니다.', '진료비 항목이나 렌즈 종류가 잘못 기재됐다고 생각되면 먼저 의료기관에 기록을 확인하세요. 보험사 판단에 의문이 있다면 어떤 약관과 어떤 의료비 항목을 근거로 했는지 설명을 요청한 뒤 필요 서류를 보완합니다.'],
      ['수술비 특약은 별도로 살펴보세요', '다초점 렌즈 재료비의 실손 보장 여부와 질병수술비·종수술비 특약의 지급 여부는 다른 판단입니다. 정액 수술비는 실제 수술명과 수술일, 약관상 수술 정의를 중심으로 확인합니다.', '수술확인서에는 백내장 수술명이, 세부내역서에는 비용 항목이 드러납니다. 두 문서를 함께 준비하되 하나의 담보 결과를 다른 담보의 결론으로 삼지 마세요.'],
    ],
    questions: [['다초점 인공수정체 비용은 실비에서 모두 제외되나요?', '계약마다 다를 수 있어 일괄적으로 말할 수 없습니다. 가입 당시 약관의 렌즈 관련 조항과 비용 항목을 확인하세요.'], ['다초점 렌즈가 제외되면 수술비도 못 받나요?', '그렇지 않을 수 있습니다. 정액 수술비 특약은 별도 지급 요건을 확인합니다.'], ['병원에서 실비 가능하다고 했으면 확정인가요?', '아닙니다. 병원 안내와 보험사의 계약 심사는 다르므로 보험사에 내 약관 기준으로 확인해야 합니다.'], ['어떤 서류에서 렌즈 값을 확인하나요?', '진료비 세부내역서에서 인공수정체 재료비와 관련 항목을 확인하세요.'], ['지급액이 낮으면 무엇부터 보나요?', '보험금 산출내역서에서 제외 항목과 공제액, 통원·입원 분류를 먼저 확인하세요.']],
    related: [['백내장 수술 청구서류', '/claims/cataract-surgery-claim-documents'], ['백내장 당일 수술 입원·통원', '/claims/cataract-day-surgery-inpatient-outpatient'], ['백내장 수술비 종합 안내', '/surgery-benefit/cataract-surgery-benefit.html']], sourceKeys: ['kdca', 'samsung', 'court'],
  },
  {
    slug: 'cataract-day-surgery-inpatient-outpatient', title: '백내장 당일 수술은 입원일까 통원일까? 실비 청구 전 확인할 기준',
    description: '백내장 당일 수술 뒤 입퇴원확인서가 있어도 보험상 입원이 자동 인정되지는 않습니다. 실제 관찰·치료 기록과 가입 약관, 실비 통원 한도를 확인하는 순서를 정리했습니다.',
    keyword: '백내장 당일 수술 입원 통원', lead: '백내장 수술을 받고 몇 시간 뒤 귀가했다면 실손보험에서 입원으로 처리될까요, 통원으로 처리될까요? 병원에서 입퇴원확인서를 발급받았는지나 머문 시간만으로 답할 수 없습니다. 실제 치료와 관찰이 왜 필요했는지, 가입한 약관이 입원을 어떻게 정하는지까지 확인해야 합니다.',
    thumb: 'cataract-day-surgery-thumb.webp', images: ['cataract-day-recovery.webp', 'cataract-day-home.webp'],
    alts: ['백내장 당일 수술 후 병원에서 회복 상태를 확인하는 장면', '백내장 수술 뒤 귀가 시간과 진료기록을 검토하는 장면'],
    rows: [['의료기관 기록', '실제 입원·관찰·처치 내용과 귀가 시각', '병상 사용·확인서 발급만으로 단정하지 않기'], ['실손 약관', '입원·통원 정의, 각 한도와 공제 방식', '가입 시기와 상품별 차이'], ['보험사 판단', '적용 조항, 진료기록 검토 결과', '통원 심사 시 근거를 서면으로 확인']],
    sections: [
      ['당일 퇴원 가능한 수술이라는 점부터 이해하세요', '질병관리청은 백내장 수술 뒤 합병증이 없으면 당일 퇴원이 가능하다고 안내합니다. 이는 당일 수술이 늘 통원이라는 뜻도, 병원에 몇 시간 머물렀다면 늘 입원이라는 뜻도 아닙니다. 개인별 건강 상태와 수술 경과는 다를 수 있습니다.', '보험에서는 의료기관의 명칭뿐 아니라 실제 치료 경과와 계약의 입원 정의를 봅니다. 따라서 “6시간 있었으니 입원” 또는 “당일 귀가했으니 통원”처럼 단순화하면 예상 지급액과 차이가 날 수 있습니다.'],
      ['입퇴원확인서가 증명하는 것과 못하는 것', '입퇴원확인서는 병원이 기록한 입원·퇴원 사실과 기간을 보여 주는 자료입니다. 그러나 보험사가 약관상 입원 의료비로 볼지 여부는 별도 심사할 수 있습니다. 단순 대기나 회복 시간과 의료적으로 필요한 입원 관찰·치료를 같은 것으로 보지 않는 이유입니다.', '입원 필요성이 쟁점이라면 수술기록, 간호기록, 처치·투약 기록, 의사의 관찰 지시 등 실제 기록을 확인하세요. 기록 내용이 사실과 다르다면 의료기관에 먼저 문의합니다.'],
      ['실손 통원으로 분류되면 달라지는 것', '실손보험은 가입 상품에 따라 입원과 통원의 보장 한도와 공제 구조가 다를 수 있습니다. 통원으로 분류되면 같은 병원비라도 적용 한도나 자기부담금 때문에 지급액이 달라질 수 있습니다.', '다초점 인공수정체 비용처럼 렌즈 자체의 보장 여부는 입원·통원 분류와 또 다른 문제입니다. 병원비 전체가 적게 나왔다면 먼저 어떤 비용이 제외됐고 어떤 비용에 통원 한도가 적용됐는지 나누어 확인하세요.'],
      ['보험사가 통원으로 심사했다면 이렇게 물으세요', '지급 계산서와 함께 적용한 입원 정의·한도 조항, 실제 진료기록 중 어떤 사실을 근거로 통원으로 판단했는지 요청하세요. 단순히 “입원확인서가 있는데 왜 통원인가요?”라고 묻는 것보다 판단 근거를 특정하는 편이 다음 단계에 도움이 됩니다.', '관찰·치료 기록이 누락되었다면 병원에서 원본 진료기록을 확인한 뒤 보험사에 재검토 가능 여부를 문의합니다. 재검토가 곧 지급을 뜻하는 것은 아니며 계약과 의료 사실에 따라 결론이 달라집니다.'],
      ['입원일당과 수술비도 각각 봐야 합니다', '입원일당 담보는 해당 계약에서 정한 입원 요건을 따로 충족해야 합니다. 실손에서 입원으로 보지 않았더라도 다른 담보의 판단이 무조건 같거나 다르다고 말할 수 없습니다.', '질병수술비와 종수술비는 실제 수술 행위와 약관상 지급 기준을 확인합니다. 당일 수술이라는 이유만으로 정액 수술비가 자동 제외된다고 단정하지 마세요.'],
    ],
    questions: [['백내장 수술 후 6시간 이상 머물면 입원인가요?', '시간만으로 자동 인정되지 않습니다. 실제 관찰·치료 필요성과 가입 약관을 함께 확인합니다.'], ['입퇴원확인서가 있으면 실비 입원 한도가 적용되나요?', '확인서만으로 확정되지 않습니다. 보험사의 약관상 입원 판단 근거를 확인하세요.'], ['당일 귀가하면 수술비 특약도 못 받나요?', '당일 귀가 여부와 정액 수술비 지급 요건은 별개입니다. 실제 수술명과 약관을 대조하세요.'], ['통원으로 심사돼 지급액이 적으면 어떻게 하나요?', '지급 산출내역에서 통원 한도·공제와 제외 비용을 구분하고 적용 조항을 요청하세요.'], ['다초점 렌즈 비용은 입원이면 보장되나요?', '입원 분류만으로 렌즈 보장은 결정되지 않습니다. 렌즈 관련 제외 조항을 별도로 확인해야 합니다.']],
    related: [['백내장 다초점 렌즈 실비', '/claims/cataract-multifocal-lens-silbi'], ['백내장 수술 청구서류', '/claims/cataract-surgery-claim-documents'], ['백내장 수술비 종합 안내', '/surgery-benefit/cataract-surgery-benefit.html']], sourceKeys: ['kdca', 'samsung'],
  },
  {
    slug: 'cataract-both-eyes-surgery-benefit', title: '양쪽 눈 백내장 수술비, 두 번 받을까? 수술일과 약관 지급 단위',
    description: '양쪽 눈 백내장 수술 뒤 질병수술비와 종수술비 지급 횟수를 눈의 개수만으로 판단하지 마세요. 같은 날·다른 날 수술 기록과 약관의 수술 1회 기준을 확인합니다.',
    keyword: '양쪽 눈 백내장 수술비 횟수', lead: '양쪽 눈의 백내장을 수술했다면 수술비도 두 번 나오는지 궁금할 수 있습니다. 답은 눈의 개수 하나로 정해지지 않습니다. 같은 날 두 눈을 수술했는지, 날짜를 나누었는지, 가입한 질병수술비·종수술비 특약이 수술 1회를 어떻게 계산하는지 봐야 합니다.',
    thumb: 'cataract-both-eyes-thumb.webp', images: ['cataract-both-eyes-consult.webp', 'cataract-both-eyes-records.webp'],
    alts: ['양쪽 눈 백내장 수술 날짜를 의료진에게 확인하는 장면', '왼쪽 눈과 오른쪽 눈 백내장 수술 기록을 날짜별로 정리하는 장면'],
    rows: [['같은 날 양안 수술', '확인서의 양쪽 눈 수술명·수술일', '동일일·동일 질병 지급 제한 확인'], ['다른 날짜 수술', '눈별 수술일·기록·이전 청구내역', '별개 날짜여도 자동으로 2회 확정 아님'], ['담보 종류', '질병수술비·종수술비·실손 가입 여부', '담보마다 지급 단위와 계산 방식 다름']],
    sections: [
      ['먼저 수술 날짜와 눈별 기록을 확인하세요', '백내장 수술을 왼쪽 눈과 오른쪽 눈에 각각 시행했다는 사실은 의료기록에서 확인합니다. 수술확인서에 양안 수술이 함께 적혀 있는지, 날짜별로 별도 확인서가 발급됐는지 살펴보세요. 병원비를 두 번 결제했다고 보험상 수술비가 두 번 지급되는 것은 아닙니다.', '같은 날 수술과 다른 날 수술은 검토할 약관 문구가 다를 수 있습니다. 기록을 눈별·날짜별로 정리하면 보험사에 지급 단위를 구체적으로 질문할 수 있습니다.'],
      ['질병수술비와 종수술비를 구분하세요', '질병수술비는 약관상 수술 정의와 지급 제한을, 종수술비는 수술분류표의 해당 항목 및 지급 기준을 봅니다. 같은 백내장 수술이어도 두 담보의 가입 여부와 약관 문구가 달라 각각 확인해야 합니다.', '수술비 특약에 동일일 수술, 동일 질병, 같은 종류의 반복 수술에 대한 제한이 있는지 찾으세요. 인터넷의 다른 회사 사례나 현재 판매 상품의 지급 방식을 오래된 계약에 그대로 적용하지 않는 것이 중요합니다.'],
      ['날짜가 다르면 자동으로 두 번일까요?', '두 눈을 다른 날짜에 수술했더라도 계약이 수술 횟수를 어떻게 정하는지 확인해야 합니다. 반대로 같은 질병명이라는 이유만으로 한 번만 지급한다고 단정할 수도 없습니다. 실제 수술일과 부위, 약관의 반복 수술 제한을 함께 봅니다.', '보험사가 한 번만 지급했다면 어느 담보의 어떤 조항을 적용했는지, 두 번째 수술 기록 중 무엇을 같은 수술로 보았는지 서면 설명을 요청하세요. 지급 계산서와 날짜별 수술확인서를 나란히 놓고 확인하면 좋습니다.'],
      ['실손의료비는 눈별 의료비를 따로 정리하세요', '실손의료비는 실제 부담한 비용 중 약관상 보장 대상 금액을 검토합니다. 눈별 수술 날짜와 영수증, 세부내역서를 따로 보관해야 비용 중복이나 누락을 확인하기 쉽습니다.', '다초점 렌즈 비용과 통원·입원 분류는 수술비 횟수와 별개의 문제입니다. 수술비가 1회 지급됐다고 실손 의료비도 1회만 청구할 수 있다고 곧바로 결론 내리지 마세요.'],
      ['보험사에 이렇게 질문해 보세요', '“왼쪽 눈은 언제, 오른쪽 눈은 언제 백내장 수술을 받았습니다. 제가 가입한 질병수술비와 종수술비 각각에서 수술 1회는 어떻게 계산하나요?”라고 물어보세요. 수술명, 날짜, 가입 담보명을 함께 제시하면 답변의 범위를 좁힐 수 있습니다.', '접수 시에는 날짜별 수술확인서, 진단 자료, 병원비 영수증과 세부내역서를 준비합니다. 추가 기록이 필요하다는 답변을 받으면 어떤 사실을 확인하려는 서류인지 문의한 뒤 발급하세요.'],
    ],
    questions: [['양쪽 눈 백내장 수술이면 수술비 두 번인가요?', '자동으로 두 번이라고 할 수 없습니다. 수술일과 가입 특약의 지급 단위를 확인해야 합니다.'], ['같은 날 양쪽 눈을 수술하면 한 번인가요?', '계약의 동일일 수술 규정에 따라 달라집니다. 실제 수술 기록과 약관을 대조하세요.'], ['다른 날 수술하면 무조건 두 번인가요?', '그렇지 않습니다. 반복 수술·동일 질병 제한 등 해당 계약의 조항을 확인해야 합니다.'], ['질병수술비와 종수술비 둘 다 받을 수 있나요?', '두 담보에 가입했다면 각각 청구 요건을 확인할 수 있지만 어느 한쪽 지급이 다른 쪽을 보장하지는 않습니다.'], ['실비는 두 눈 각각 청구할 수 있나요?', '각 수술에서 실제 부담한 의료비를 날짜별로 제출하고 약관상 보장 범위를 확인하세요.']],
    related: [['백내장 수술 청구서류', '/claims/cataract-surgery-claim-documents'], ['백내장 당일 수술 입원·통원', '/claims/cataract-day-surgery-inpatient-outpatient'], ['수술분류표 확인 방법', '/surgery-benefit/surgery-classification.html']], sourceKeys: ['kdca', 'samsung'],
  },
];

const escape = (value) => String(value).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const link = ([label, href]) => `<a href="${escape(href)}"${href.startsWith('http') ? ' target="_blank" rel="noopener"' : ''}>${escape(label)}</a>`;
const figure = (file, alt, eager = false) => `<figure class="guide-image-panel"><img src="/assets/images/${file}" width="1672" height="941" loading="${eager ? 'eager' : 'lazy'}" decoding="async" alt="${escape(alt)}"></figure>`;

for (const article of articles) {
  const path = `/claims/${article.slug}`;
  const articleJson = JSON.stringify({ '@context': 'https://schema.org', '@type': 'Article', headline: article.title, description: article.description, image: `${origin}/assets/images/${article.thumb}`, mainEntityOfPage: `${origin}${path}`, author: { '@type': 'Organization', name: '케어로컬' }, publisher: { '@type': 'Organization', name: '케어로컬' }, datePublished: '2026-09-27', dateModified: '2026-09-27', inLanguage: 'ko-KR' });
  const rows = article.rows.map(([item, check, note]) => `<tr><td>${escape(item)}</td><td>${escape(check)}</td><td>${escape(note)}</td></tr>`).join('');
  const sections = article.sections.map(([heading, first, second], index) => `<h2>${escape(heading)}</h2><p>${escape(first)}</p>${index === 0 ? figure(article.images[0], article.alts[0]) : ''}<p>${escape(second)}</p>${index === 2 ? figure(article.images[1], article.alts[1]) : ''}`).join('\n');
  const faq = article.questions.map(([question, answer]) => `<details><summary>${escape(question)}</summary><p>${escape(answer)}</p></details>`).join('');
  const html = `<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>${escape(article.title)}</title><meta name="description" content="${escape(article.description)}"><meta property="og:type" content="article"><meta property="og:title" content="${escape(article.title)}"><meta property="og:description" content="${escape(article.description)}"><meta property="og:image" content="${origin}/assets/images/${article.thumb}"><link rel="canonical" href="${origin}${path}"><link rel="stylesheet" href="/assets/site.css?v=20260927-cataract-v1"><script type="application/ld+json">${articleJson}</script><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2258793659580551" crossorigin="anonymous"></script></head><body>
<header class="site-header"><nav class="nav" aria-label="주요 메뉴"><a class="brand" href="/"><span class="brand-mark">CL</span><span><strong>케어로컬</strong><small>보험 정보 자료실</small></span></a><div class="nav-links"><a href="/claims/">보험금 청구</a><a href="/silbi/">실비보험</a><a href="/diagnosis-benefit/">진단비</a><a href="/surgery-benefit/">수술비</a><a href="/standards/">약관·기준</a></div></nav></header>
<main class="section article-body insurance-series-article"><div class="breadcrumb"><a href="/">홈</a> / <a href="/claims/">보험금 청구</a> / ${escape(article.keyword)}</div><h1>${escape(article.title)}</h1><p class="lead">${escape(article.lead)}</p><div class="insurance-company-cta"><a href="/insurance-companies/">보험사별 공식 홈페이지 확인하기</a></div>${figure(article.thumb, `${article.keyword} 카드뉴스`, true)}<p class="notice">보험금 지급 여부와 필요서류는 가입 상품, 약관, 가입 시기, 실제 의료기록과 보험사 심사에 따라 달라집니다. 본문 이미지는 이해를 돕는 AI 생성 장면이며 실제 환자 서류가 아닙니다.</p>
<h2>${escape(article.keyword)} 핵심 확인</h2><table><thead><tr><th scope="col">구분</th><th scope="col">확인할 내용</th><th scope="col">주의할 점</th></tr></thead><tbody>${rows}</tbody></table>
${sections}
<h2>청구 전 확인 순서</h2><ol><li>보험증권에서 해당 담보의 정확한 이름과 가입 시기를 확인합니다.</li><li>수술확인서와 진료비 서류에서 실제 수술·비용 항목·날짜를 구분합니다.</li><li>가입 당시 약관과 보험사 공식 구비서류 안내를 확인합니다.</li><li>공식 앱·홈페이지로 접수하고 접수번호와 보완 요청 사유를 보관합니다.</li></ol>
<h2>자주 묻는 질문</h2><div class="faq">${faq}</div><h2>함께 보면 좋은 글</h2><div class="article-actions">${article.related.map(link).join('')}</div><h2>공식 확인처</h2><ul>${article.sourceKeys.map((key) => `<li>${link(sources[key])}</li>`).join('')}</ul><div class="insurance-company-cta"><a href="/insurance-companies/">보험사별 공식 홈페이지 확인하기</a></div><section class="kakao-inquiry-cta" aria-labelledby="contact-title"><p class="cta-label">문의 안내 <span>보험</span></p><h2 id="contact-title">가입한 보험의 보장이 궁금하신가요?</h2><p>가입한 보험의 보장 내용이나 콘텐츠와 관련해 궁금한 점이 있다면 카카오톡으로 문의해 주세요. 주민등록번호·진단서·영수증 등 민감한 개인정보가 포함된 자료는 전송하지 않는 것을 권장합니다.</p><a class="kakao-button" href="https://open.kakao.com/o/sVyT7uph" target="_blank" rel="noopener">카카오톡으로 문의하기</a></section></main></body></html>`;
  writeFileSync(join(root, 'claims', `${article.slug}.html`), `${html}\n`, 'utf8');
  console.log(`${path}: ${article.title}`);
}

const overviewPath = join(root, 'surgery-benefit', 'cataract-surgery-benefit.html');
const overview = readFileSync(overviewPath, 'utf8');
const overviewLinks = '<h2>백내장 수술 질문별로 확인하기</h2><div class="article-actions"><a href="/claims/cataract-surgery-claim-documents">백내장 수술 청구서류</a><a href="/claims/cataract-multifocal-lens-silbi">다초점 인공수정체 실비</a><a href="/claims/cataract-day-surgery-inpatient-outpatient">당일 수술 입원·통원</a><a href="/claims/cataract-both-eyes-surgery-benefit">양쪽 눈 수술비 횟수</a></div>';
if (!overview.includes('백내장 수술 질문별로 확인하기')) {
  writeFileSync(overviewPath, overview.replace('<h2>공식 확인처</h2>', `${overviewLinks}<h2>공식 확인처</h2>`).replace('"dateModified":"2026-09-22"', '"dateModified":"2026-09-27"'), 'utf8');
}
