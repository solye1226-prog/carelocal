# Cloudflare Pages Deployment

## Recommended settings

- Project name: `carelocal`
- Production branch: `main`
- Framework preset: `None`
- Build command: leave empty
- Build output directory: `/`
- Root directory: `/`

## Direct upload

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

## After deployment

Replace `https://hospital.hbuby.com` in these files with the final domain:

- `sitemap.xml`
- `robots.txt`
- HTML canonical URLs

Replace the placeholder publisher ID in `ads.txt` after AdSense approval.
