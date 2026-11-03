/**
 * Server-side API access.
 *
 * This runs inside Next.js on the server, so it talks to the backend directly
 * rather than through the browser proxy. That lets a decision packet render as
 * real HTML: it works on a weak connection, it survives JavaScript being off,
 * and it never degrades into a client that silently shows nothing.
 *
 * A failure here is surfaced to the page, which fails closed.
 */

import type { DecisionPacket } from "./api";

export type { DecisionPacket };

/** Server-only base URL. Falls back to the local backend during development. */
export const SERVER_API_BASE = (
  process.env.API_SERVER_URL ??
  process.env.API_PROXY_TARGET ??
  "http://127.0.0.1:8000"
).replace(/\/$/, "");

export class ServerApiError extends Error {
  state: string;
  constructor(message: string, state = "unknown") {
    super(message);
    this.state = state;
  }
}

async function get<T>(path: string): Promise<T> {
  let response: Response;
  try {
    response = await fetch(`${SERVER_API_BASE}/api/v1${path}`, {
      cache: "no-store",
      headers: { Accept: "application/json" },
    });
  } catch {
    throw new ServerApiError(
      "The EcoFarm decision service could not be reached. No substitute or cached recommendation is shown.",
      "source_temporarily_unavailable",
    );
  }

  if (!response.ok) {
    let state = "error";
    let message = `The decision service responded with ${response.status}.`;
    try {
      const body = await response.json();
      if (body?.detail?.state) state = body.detail.state;
      if (body?.detail?.message) message = body.detail.message;
    } catch {
      /* keep defaults */
    }
    throw new ServerApiError(message, state);
  }

  return (await response.json()) as T;
}

export function fetchPacketServer(id: string): Promise<DecisionPacket> {
  return get<DecisionPacket>(`/decisions/${encodeURIComponent(id)}`);
}
