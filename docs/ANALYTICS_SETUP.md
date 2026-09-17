# On-site article analytics

The owner dashboard is `/dashboard/`. It does not redirect to Cloudflare.

## Production secrets

Configure these as encrypted production secrets for the **carelocal-git** Pages project:

- `CF_ANALYTICS_TOKEN`: Cloudflare Account Analytics / Read, restricted to the owner's account. Never commit this value or place it in client JavaScript.
- `ANALYTICS_ADMIN_PASSWORD`: a unique, randomly generated owner access key of at least 32 characters. Do not reuse the Cloudflare password.

The API fails closed without both secrets. Authentication is required for every metrics request. Responses use `private, no-store`. The client keeps the owner key in memory only, clears the input, and provides a lock button. The public dashboard shell and article catalog contain no traffic numbers.

Token creation needs owner approval. Do not add DNS or Pages edit permissions to the analytics token. Do not expose an account-wide token to the client. A separate Cloudflare Access policy can be added later for identity-based access.

## Article index

Run `npm run build:catalog` after adding or retitling articles. The generator reads public canonical URLs and page titles using HTMLParser. It excludes section indexes and noindex pages. `npm run check` detects a stale catalog.

The table combines canonical, `.html`, and trailing-slash paths. It lists all indexed articles, with search, sorting, and 15 items per page. A zero is shown only after a successful complete API result. Truncated results show unknown counts instead of invented zeros.

## Metrics

- Today, 7 days and 30 days include today, using Korea calendar-day boundaries.
- Views and visits are distinct metrics. Visits are not unique users.
- Article detail requests filter the same hostname and canonical aliases.
- Referrers are referring hostnames, not guaranteed acquisition attribution. Missing referrers mean direct or unknown, and same-site navigation is labelled separately.
- Search Console is not connected. No keyword clicks or search impressions are fabricated.
- Statistics before beacon installation cannot be recovered. Sampling, tracking prevention and processing delays affect counts.

## Verification before declaring the connection complete

1. Run `npm run check`.
2. Verify GraphQL field access and time-range limits with the approved token. Mock tests do not prove live schema access.
3. Add production secrets, deploy, and test unauthorized requests return 401 without metrics.
4. Authenticate on `/dashboard/`, compare live numbers with the Cloudflare hostname-filtered Web Analytics report, and test an article detail request.
5. Confirm mobile layout, period changes, search, pagination, lock and error states.

Current status: analytics token saved in the production project. Live API tested for today, 7/30 days and an article path. Owner access secret and production authenticated verification are still pending.

Queries use windows of at most seven days and combine disjoint results; a single 30-day request returned zero on this low-traffic site despite recent events. Counts remain subject to Cloudflare sampling. Dashboard paths are excluded. Local preview credentials are temporary and are not production credentials.
