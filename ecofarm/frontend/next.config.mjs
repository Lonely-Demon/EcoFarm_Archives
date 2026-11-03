/** @type {import('next').NextConfig} */

// The backend is hosted separately. In production set NEXT_PUBLIC_API_BASE_URL to
// the deployed FastAPI origin. When unset, requests go to /api/proxy/* and Next
// forwards them to API_PROXY_TARGET, which keeps a single-origin preview working.
const proxyTarget = process.env.API_PROXY_TARGET || "http://127.0.0.1:8000";

const nextConfig = {
  reactStrictMode: true,
  async rewrites() {
    return [
      {
        source: "/api/proxy/:path*",
        destination: `${proxyTarget}/api/v1/:path*`,
      },
    ];
  },
  async headers() {
    return [
      {
        source: "/(.*)",
        headers: [
          { key: "X-Content-Type-Options", value: "nosniff" },
          { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
        ],
      },
      {
        source: "/sw.js",
        headers: [
          { key: "Cache-Control", value: "no-cache, no-store, must-revalidate" },
          { key: "Service-Worker-Allowed", value: "/" },
        ],
      },
    ];
  },
};

export default nextConfig;
