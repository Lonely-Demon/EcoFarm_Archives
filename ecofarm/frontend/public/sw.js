/* EcoFarm service worker.
 *
 * Deliberately conservative: it caches the app shell so the interface opens
 * offline, and it NEVER caches decision packets or API responses. Showing a
 * stale recommendation is exactly the failure mode the pilot forbids, so API
 * requests fail closed in the UI instead.
 */

const CACHE = "ecofarm-shell-v1";
const SHELL = ["/", "/decide", "/sources", "/method", "/offline", "/manifest.webmanifest"];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE).then((cache) => cache.addAll(SHELL)).then(() => self.skipWaiting()),
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches
      .keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim()),
  );
});

self.addEventListener("fetch", (event) => {
  const url = new URL(event.request.url);

  // Never serve a cached decision, source register or metadata response.
  if (url.pathname.startsWith("/api/") || event.request.method !== "GET") {
    return;
  }

  if (event.request.mode === "navigate") {
    event.respondWith(
      fetch(event.request)
        .then((response) => {
          const copy = response.clone();
          caches.open(CACHE).then((cache) => cache.put(event.request, copy));
          return response;
        })
        .catch(() => caches.match(event.request).then((hit) => hit || caches.match("/offline"))),
    );
    return;
  }

  event.respondWith(
    caches.match(event.request).then(
      (hit) =>
        hit ||
        fetch(event.request)
          .then((response) => {
            if (response.ok && url.origin === self.location.origin) {
              const copy = response.clone();
              caches.open(CACHE).then((cache) => cache.put(event.request, copy));
            }
            return response;
          })
          .catch(() => hit),
    ),
  );
});
