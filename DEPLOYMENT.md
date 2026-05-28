# Cloudflare Pages Deployment

## Recommended settings

- Project name: `carelocal`
- Production branch: `main`
- Framework preset: `None`
- Build command: leave empty
- Build output directory: `/`
- Root directory: `/`

## Direct upload

Use GitHub connection instead of Direct Upload if you need `/api/hospitals`.
Cloudflare Pages Functions are deployed from the project repository.

1. Open Cloudflare Dashboard.
2. Go to Workers & Pages.
3. Select Pages, then Create a project.
4. Choose Upload assets.
5. Upload `carelocal-cloudflare-pages.zip` or drag the project folder contents.
6. Deploy.

## GitHub connection

1. Push this folder to a GitHub repository.
2. In Cloudflare Pages, choose Connect to Git.
3. Select the repository.
4. Use the recommended settings above.

## HIRA hospital API

The site includes a Cloudflare Pages Function at `/api/hospitals` that proxies the
`건강보험심사평가원_병원정보서비스` OpenAPI without exposing the API key in browser code.
The public hospital list uses a static JSON snapshot at `/data/hospitals.json`
for speed and reliability.

1. In data.go.kr, copy the service key for `건강보험심사평가원_병원정보서비스`.
2. In Cloudflare Dashboard, open Workers & Pages > `carelocal`.
3. Go to Settings > Variables and Secrets > Add.
4. Add a production variable:
   - Name: `HIRA_SERVICE_KEY`
   - Value: your data.go.kr service key
5. Save, then redeploy the latest Pages deployment.
6. Test:
   - `/api/hospitals?q=세브란스병원&numOfRows=5`
   - `/api/hospitals?sidoCd=110000&numOfRows=10`

For local testing with Wrangler, copy `.dev.vars.example` to `.dev.vars` and put
the real key there. Do not commit `.dev.vars`.

To refresh the static hospital snapshot locally:

```powershell
$env:HIRA_SERVICE_KEY="YOUR_DATA_GO_KR_KEY"
node scripts/fetch-hira-hospitals.mjs
Remove-Item Env:HIRA_SERVICE_KEY
```

Commit the generated `data/hospitals.json` after checking the output.

## After deployment

Replace `https://hospital.hbuby.com` in these files with the final domain:

- `sitemap.xml`
- `robots.txt`
- HTML canonical URLs

Replace the placeholder publisher ID in `ads.txt` after AdSense approval.
