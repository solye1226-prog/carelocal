# Insurance Company Directory Review - 2026-10-02

## Scope

- Improve the existing insurance-companies page rather than publish a new article.
- Add client-side company-name filtering, result count and an empty state.
- Keep the full directory available when JavaScript is disabled.
- Match partial names while ignoring whitespace and letter case; no search data is sent to a server.
- Retain company names, phone numbers, existing official homepage URLs and advertising settings.

## Navigation Corrections

- Add Samsung Fire's official disease/injury claim-document link.
- Label Heungkuk Fire's existing automobile compensation link explicitly.
- Explain that readers should choose the insurer named in their contract, not infer it from a disease or benefit type.
- Add internal surgical-claim documents and payment follow-up guides.

## Primary Sources Checked

- https://direct.samsungfire.com/m/claim/MP040202_001.html?tab=1
  - Disease/injury document guide including surgery documents.
- https://www.heungkukfire.co.kr/FRW/compensation/carCompInfo.do
  - Automobile claim guidance. Preserve the URL and clarify its scope.
- https://www.idbins.com/pc/bizxpress/ct/dc/FWCUSV1301.shtm
  - Existing disease-related claim document destination remains accessible.

## Verification Boundaries

- This is not a comprehensive audit of every insurer's name, phone number or external URL.
- Local link and catalog checks, JavaScript syntax and deployed search behavior must be verified.
- Search behavior should cover partial matches across both insurer groups, whitespace, letter case, no matches and clearing the input.
- No indexing request, paid campaign or change to AdSense settings is part of this work.
- Internal navigation changes do not prove improved search CTR or revenue.

## Completed Verification

- Local links: 166 HTML files, all resolved. Catalog: 139 articles, consistent.
- node --check assets/company-directory.js and git diff --check passed.
- Public directory returned HTTP 200 with the search input and new document link.
- Deployed browser: partial Samsung query returned Samsung Fire and Samsung Life (2); spaced Samsung Fire returned 1; mixed-case aXa returned 1.
- Nonexistent query returned 0 with the empty message and both group headings hidden.
- Clearing the input restored all 39 companies and both groups.
- Search input displayed at 390x844 and 1440x900. Mobile and desktop screenshots saved locally.
- Existing auto ads remain visible; no claim is made that search results are free from advertising interruptions.
