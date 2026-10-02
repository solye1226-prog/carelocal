# Canonical alignment review

- Checked 164 sitemap entries and 166 HTML files. Verification HTML and the private dashboard are not sitemap content pages and were not given canonicals.
- 39 existing canonical links and matching sitemap entries used .html aliases. Every alias was requested with curl HEAD following redirects; all ended at the corresponding extensionless URL with HTTP 200.
- Align only those 39 canonical links and sitemap entries with the verified final destinations. Preserve titles, medical/insurance content, images, advertising scripts, publication dates and old redirects.
- Added scripts/check_canonical.py to check unique sitemap entries, clean URL routes, existing local targets and exact matching self-canonicals.
- The first Python HTTP probe returned 403; curl succeeded for all 39. This is not evidence that Googlebot is blocked or allowed; bot-specific crawling was not tested.
- Guidance: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- Canonical, sitemap and redirect consistency can clarify preferred URLs. This does not establish that the mismatch caused low ranking, guarantee Google canonical selection, or prove an indexing/revenue improvement.
- No indexing requests or account/ad settings changed. Local private analytics records were not included in the deployment.
