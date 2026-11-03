# EcoFarm PWA

Next.js frontend for the EcoFarm crop decision engine. Installable, works as an
app on Android and iOS, and renders every decision packet on the server so it
survives a weak connection.

## Run locally

```bash
npm install
cp .env.example .env.local
npm run dev
```

The dev server proxies `/api/proxy/*` to the FastAPI backend at
`API_PROXY_TARGET` (default `http://127.0.0.1:8000`).

## Deploy

Set these environment variables on the host (Vercel or anywhere that runs
Next.js):

| Variable | Purpose |
|---|---|
| `NEXT_PUBLIC_API_BASE_URL` | Public origin of the FastAPI backend, e.g. `https://ecofarm-api.onrender.com`. **Required in production.** |
| `API_SERVER_URL` | Same origin, used for server-side rendering of `/packet/[id]`. Falls back to `API_PROXY_TARGET`. |
| `API_PROXY_TARGET` | Local development only. |

Do not deploy without `NEXT_PUBLIC_API_BASE_URL`; otherwise the browser will try
to call the frontend's own origin and every request will fail.
