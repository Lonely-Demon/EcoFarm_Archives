"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { api, localRecords, type Meta } from "@/lib/api";

export default function Home() {
  const [meta, setMeta] = useState<Meta | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [records, setRecords] = useState<ReturnType<typeof localRecords.list>>([]);

  useEffect(() => {
    setRecords(localRecords.list());
    api
      .meta()
      .then(setMeta)
      .catch((e) => setError(e.message));
  }, []);

  return (
    <>
      <p className="eyebrow">Namakkal pilot</p>
      <h1>Crop decisions that show their working.</h1>
      <p className="lede">
        EcoFarm compares crops using the evidence it is actually allowed to use. When a
        factor is missing — weather, market prices, pest risk — it says so instead of
        filling the gap with a guess.
      </p>

      {error && (
        <div className="notice stop" style={{ marginTop: 18 }}>
          <span className="notice-icon" aria-hidden>
            ⚠
          </span>
          <div>
            <strong>Service unavailable</strong>
            {error}
          </div>
        </div>
      )}

      <div style={{ marginTop: 20 }}>
        <Link href="/decide" className="btn block" style={{ padding: "16px 20px", fontSize: 16 }}>
          Start a decision
        </Link>
      </div>

      {meta && (
        <div className="card" style={{ marginTop: 18 }}>
          <div className="eyebrow">Today’s honest state</div>
          <h2 style={{ marginBottom: 10 }}>{meta.weather_gate.headline}</h2>
          <p className="small muted" style={{ marginBottom: 14 }}>
            {meta.weather_gate.detail}
          </p>
          <div className="pill-row">
            {meta.weather_gate.candidates.map((c) => (
              <span key={c.source_id} className="chip">
                <span className="status-dot blocked" />
                {c.source_name} · {c.status.replace(/_/g, " ")}
              </span>
            ))}
          </div>
        </div>
      )}

      {!meta && !error && (
        <div className="card" style={{ marginTop: 18 }}>
          <div className="skeleton" style={{ height: 16, width: "45%", marginBottom: 10 }} />
          <div className="skeleton" style={{ height: 13, width: "90%", marginBottom: 6 }} />
          <div className="skeleton" style={{ height: 13, width: "70%" }} />
        </div>
      )}

      <div className="grid-2" style={{ marginTop: 18 }}>
        <div className="card sunk">
          <div className="eyebrow">What it does</div>
          <p className="small" style={{ marginBottom: 0 }}>
            Ranks Namakkal crop options against your water situation, sowing window,
            soil and stated goals — and flags where the ordering is too close to call.
          </p>
        </div>
        <div className="card sunk">
          <div className="eyebrow">What it refuses to do</div>
          <p className="small" style={{ marginBottom: 0 }}>
            No price or profit prediction, no buyer assurance, no pest diagnosis, no
            weather claim, no automated irrigation.
          </p>
        </div>
      </div>

      <div className="card">
        <div className="card-head">
          <div>
            <h2>Your recent decisions</h2>
            <p className="small muted" style={{ marginBottom: 0 }}>
              Kept on this device for quick reopening. The server copy expires after 90 days.
            </p>
          </div>
        </div>

        {records.length === 0 ? (
          <p className="small muted" style={{ marginBottom: 0 }}>
            No decisions yet. Your first one takes about a minute.
          </p>
        ) : (
          <div className="stack">
            {records.map((r) => (
              <Link
                key={r.id}
                href={`/packet/${r.id}`}
                className="option"
                style={{ textDecoration: "none", color: "inherit" }}
              >
                <div style={{ flex: 1 }}>
                  <div style={{ fontWeight: 600, fontSize: 14 }}>{r.block}</div>
                  <div className="small muted">{r.headline}</div>
                  <div className="tiny muted" style={{ marginTop: 2 }}>
                    {new Date(r.created_at).toLocaleString()}
                  </div>
                </div>
                <span aria-hidden style={{ color: "var(--ink-faint)" }}>
                  ›
                </span>
              </Link>
            ))}
          </div>
        )}
      </div>

      {meta && (
        <div className="card sunk">
          <div className="eyebrow">Where the thresholds come from</div>
          <p className="small muted">
            Catalogue <code>{meta.catalogue_version}</code>, engine{" "}
            <code>{meta.engine_version}</code>, directory <code>{meta.directory_version}</code>.
          </p>
          <Link href="/method" className="small">
            Read the method and its limits →
          </Link>
        </div>
      )}
    </>
  );
}
