# Four-step surgery content review

Reviewed: 2026-10-02. Six existing pages; no new posts.

## Sequential changes

1. Classification overview and third-tier guide: distinguish overview navigation from the contract-specific third-tier amount/count worksheet. Clarify that 1-3 and 1-5 systems cannot be interchanged. Replace the third-tier secondary reference with a dated FSS consumer notice; clarify the KNIA source scope.
2. Cataract: separate tier, actual-expense lens coverage, and bilateral payment count. Correct the FAQ to check document contents and common submission requirements instead of suggesting a surgery certificate alone permits submission.
3. Gallbladder and hemorrhoids: codes are clues, not benefit tiers or payment counts. Correct hemorrhoid diagnosis versus disease-code wording and distinguish medical auxiliary-treatment categories from the contract's surgery definition.
4. Generic surgery documents: separate common submission requirements, medical information, actual-expense cost records and additional-review records. Diagnosis-benefit tests are not mandatory for every surgery claim. Replace the old Samsung source URL with the verified official page.

## Sources and limits

- Samsung Fire official guide: common, surgery, diagnosis-benefit and actual-expense sections checked. A single insurer's example, not universal requirements.
  https://direct.samsungfire.com/m/claim/MP040202_001.html?tab=1
- FSS December 2023 consumer notice, KIRI-hosted PDF, page 4: lens surgery versus YAG procedure classification in one contract. No universal tier assigned.
  https://kiri.or.kr/PDF/weeklytrend/20231226/trend20231226_2.pdf
- KDCA hemorrhoid guide: diagnosis and auxiliary versus surgical therapy checked. Medical categories do not determine insurance eligibility.
  https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=5818
- Existing HIRA code examples were not expanded. The web tool could not retrieve the full PDF again; no new code-to-tier mappings or code inclusion rules were introduced.
  https://www.hira.or.kr/ebooksc/2026/01/BZ202601272870642.pdf
- Existing historical ABL policy example was not changed. See SURGERY_EVIDENCE_REVIEW_2026-10-01.md for its scope and earlier evidence.

## Verification

- 166 HTML files: local links resolve; catalog check: 139 articles.
- Existing analytics/CSV tests: 10 passed.
- Targeted invariants: titles, canonical URLs, publication dates, ad scripts preserved; one H1 per page; embedded JSON parses.
- Public deployment df93e39: all six extensionless URLs returned HTTP 200 and their individual new text markers.
- Browser checks at 390px: all six pages fit the page viewport; long tables retain their existing inner horizontal scrolling. Desktop checklist and mobile article/table screenshots inspected. Existing late-loading ads can shift anchor positions or cover content; ad configuration remained unchanged as requested.
- No indexing submissions, advertising configuration, tracking installation or claims of improved revenue/rankings.
- Individual contracts still require insurer review; this is not medical/legal expert certification.
