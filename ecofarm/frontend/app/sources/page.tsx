"use client";

import { useEffect, useState } from "react";
import { api, type Meta } from "@/lib/api";

const STATUS_GROUPS: { key: string; title: string; blurb: string; tone: "blocked" | "reference" | "approved" }[] = [
  {
    key: "approved",
    title: "Approved for use",
    blurb: "Passed access, rights, freshness, locality, provenance, semantics and failure tests.",
    tone: "approved",
  },
  {
    key: "manual_reference",
    title: "Manual reference only",
    blurb: "Can be cited and read by a human. Never parsed into a computed rule.",
    tone: "reference",
  },
  {
    key: "blocked_permission",
    title: "Blocked — permission",
    blurb: "Credentials, endpoint documentation or owner permission are not established.",
    tone: "blocked",
  },
  {
    key: "rejected_locality",
    title: "Rejected — wrong locality",
    blurb: "The source does not cover the target geography for this pilot.",
    tone: "blocked",
  },
  {
    key: "rejected_rights",
    title: "Rejected — rights",
    blurb: "Reuse, storage or redistribution is not permitted.",
    tone: "blocked",
  },
  {
    key: "not_tested",
    title: "Not tested",
    blurb: "No decision-relevant test has been executed, so it is excluded.",
    tone: "blocked",
  },
];

export default function SourcesPage() {
  const [meta, setMeta] = useState<Meta | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    api
      .meta()
      .then(setMeta)
      .catch((e) => setError(e.message));
  }, []);

  if (error) {
    return (
      <div className="notice stop" style={{ marginTop: 24 }}>
        <span className="notice-icon" aria-hidden>
          ⚠
        </span>
        <div>
          <strong>Source register unavailable</strong>
          {error}
          <p className="small" style={{ margin: "8px 0 0" }}>
            EcoFarm will not display a cached source list as if it were current.
          </p>
        </div>
      </div>
    );
  }

  if (!meta) {
    return (
      <>
        <div className="skeleton" style={{ height: 32, width: "55%", margin: "28px 0 16px" }} />
        <div className="skeleton" style={{ height: 120, marginBottom: 12 }} />
        <div className="skeleton" style={{ height: 200 }} />
      </>
    );
  }

  return (
    <>
      <p className="eyebrow">Source register · {meta.register_version}</p>
      <h1>What EcoFarm is allowed to use.</h1>
      <p className="lede">
        A page returning a successful response is not approval. Each source has to pass
        access, rights, freshness, target-locality, provenance, semantic and
        failure-behaviour checks before it can affect a result. Nothing in this list
        currently supplies weather.
      </p>

      <div className="card" style={{ marginTop: 20 }}>
        <div className="eyebrow">Weather gate</div>
        <h2>{meta.weather_gate.headline}</h2>
        <p className="small muted">{meta.weather_gate.detail}</p>
        <div className="stack">
          {meta.weather_gate.candidates.map((c) => (
            <div key={c.source_id} className="card sunk" style={{ marginBottom: 0, padding: 14 }}>
              <div style={{ fontWeight: 620, fontSize: 14 }}>
                <span className="status-dot blocked" />
                {c.source_name}
              </div>
              <div className="tiny muted" style={{ marginTop: 2 }}>
                {c.publisher}
              </div>
              <p className="small" style={{ margin: "8px 0 6px" }}>
                {c.status_detail}
              </p>
              <a href={c.url} target="_blank" rel="noreferrer noopener" className="tiny">
                Check the source yourself ↗
              </a>
            </div>
          ))}
        </div>
      </div>

      {STATUS_GROUPS.map((group) => {
        const items = meta.source_register.filter((s) => s.status === group.key);
        if (items.length === 0) return null;
        return (
          <div key={group.key} className="card">
            <div className="eyebrow">
              {items.length} source{items.length > 1 ? "s" : ""}
            </div>
            <h2>{group.title}</h2>
            <p className="small muted">{group.blurb}</p>
            <div className="stack" style={{ marginTop: 8 }}>
              {items.map((s) => (
                <div key={s.id} style={{ paddingBottom: 12, borderBottom: "1px dashed var(--line)" }}>
                  <div style={{ fontWeight: 620, fontSize: 14 }}>
                    <span className={`status-dot ${group.tone === "approved" ? "approved" : group.tone === "reference" ? "reference" : "blocked"}`} />
                    {s.name}
                  </div>
                  <div className="tiny muted">{s.publisher}</div>
                  <p className="small" style={{ margin: "6px 0" }}>
                    {s.status_detail}
                  </p>
                  <div className="tiny" style={{ color: "var(--ink-faint)" }}>
                    Farmer-facing state: <code>{s.farmer_facing_state.replace(/_/g, " ")}</code>
                    {s.url.startsWith("http") && (
                      <>
                        {" · "}
                        <a href={s.url} target="_blank" rel="noreferrer noopener">
                          Open source ↗
                        </a>
                      </>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        );
      })}

      <div className="card sunk">
        <div className="eyebrow">District context</div>
        <h2>{meta.district.name}, {meta.district.state}</h2>
        <dl className="kv">
          <dt>Normal rainfall</dt>
          <dd>{meta.district.normal_annual_rainfall_mm} mm</dd>
          <dt>Agro-climatic zones</dt>
          <dd>{meta.district.agro_climatic_zones.join(", ")}</dd>
          <dt>Soils</dt>
          <dd>{meta.district.soil_summary}</dd>
        </dl>
        <p className="small muted" style={{ marginTop: 10 }}>
          {meta.district.rainfall_note} These are district-level figures. They are never
          applied to your plot as if they were your plot’s measurements.{" "}
          <a href={meta.district.source_url} target="_blank" rel="noreferrer noopener">
            District source ↗
          </a>
        </p>
      </div>
    </>
  );
}
