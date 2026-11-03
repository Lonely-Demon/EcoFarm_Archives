"use client";

import { useEffect, useState } from "react";
import { api, type Meta } from "@/lib/api";

type Method = {
  engine_version: string;
  catalogue_version: string;
  factors: { id: string; label: string; kind: "scored" | "excluded" }[];
  steps: string[];
  sensitivity: { draws: number; seed: number; weight_perturbation: string };
};

export default function MethodPage() {
  const [meta, setMeta] = useState<Meta | null>(null);
  const [method, setMethod] = useState<Method | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    Promise.all([api.meta(), api.method()])
      .then(([m, how]) => {
        setMeta(m);
        setMethod(how as unknown as Method);
      })
      .catch((e) => setError(e.message));
  }, []);

  if (error) {
    return (
      <div className="notice stop" style={{ marginTop: 24 }}>
        <span className="notice-icon" aria-hidden>
          ⚠
        </span>
        <div>
          <strong>Method unavailable</strong>
          {error}
        </div>
      </div>
    );
  }

  if (!meta || !method) {
    return (
      <>
        <div className="skeleton" style={{ height: 32, width: "50%", margin: "28px 0 16px" }} />
        <div className="skeleton" style={{ height: 220 }} />
      </>
    );
  }

  const scored = method.factors.filter((f) => f.kind === "scored");
  const excluded = method.factors.filter((f) => f.kind === "excluded");

  return (
    <>
      <p className="eyebrow">Method</p>
      <h1>How a score is produced.</h1>
      <p className="lede">
        The comparison is a transparent weighted sum over the factors EcoFarm can
        support. There is no machine-learning model, because there is no validation
        dataset to train or check one against.
      </p>

      <div className="card" style={{ marginTop: 20 }}>
        <h2>Pipeline</h2>
        <ol className="small" style={{ paddingLeft: 20, margin: "10px 0 0" }}>
          {method.steps.map((step, i) => (
            <li key={i} style={{ marginBottom: 8 }}>
              {step}
            </li>
          ))}
        </ol>
      </div>

      <div className="card">
        <h2>Factors that can be scored</h2>
        <div className="stack" style={{ marginTop: 8 }}>
          {scored.map((f) => (
            <div key={f.id} style={{ display: "flex", justifyContent: "space-between", gap: 10 }}>
              <span style={{ fontSize: 14 }}>{f.label}</span>
              <span className="chip">{f.id}</span>
            </div>
          ))}
        </div>
      </div>

      <div className="excluded">
        <h3>Factors that are never scored in this pilot</h3>
        <div className="stack" style={{ marginTop: 8 }}>
          {excluded.map((f) => (
            <div key={f.id} style={{ fontSize: 14 }}>
              <span className="status-dot blocked" />
              {f.label}
            </div>
          ))}
        </div>
        <p className="small" style={{ margin: "10px 0 0", color: "#7a5a4a" }}>
          Weather, observed prices and pest risk are shown as missing on every result.
          They are not defaulted, estimated, or pulled from a neighbouring region.
        </p>
      </div>

      <div className="card">
        <h2>Why there is no single winner</h2>
        <p className="small muted">
          Crop suitability scores are compressed: many crops share the same soil and
          season, so they land within a few hundredths of each other. The engine therefore
          cuts bands only where options differ by a meaningful margin, and reports a rank
          range per crop.
        </p>
        <dl className="kv" style={{ marginTop: 10 }}>
          <dt>Perturbation draws</dt>
          <dd>{method.sensitivity.draws}</dd>
          <dt>Noise model</dt>
          <dd>{method.sensitivity.weight_perturbation}</dd>
          <dt>Fixed seed</dt>
          <dd>{method.sensitivity.seed} (so a packet always reproduces)</dd>
        </dl>
        <p className="small muted" style={{ marginTop: 10 }}>
          Overlapping rank ranges mean the ordering between those crops is not evidence of
          a real difference. The interface shows the range next to every crop.
        </p>
      </div>

      <div className="card">
        <h2>Pilot limits</h2>
        <ul className="small muted" style={{ paddingLeft: 18, margin: 0 }}>
          {meta.limitations.map((limit, i) => (
            <li key={i} style={{ marginBottom: 6 }}>
              {limit}
            </li>
          ))}
        </ul>
      </div>

      <div className="card sunk">
        <div className="eyebrow">Honest provenance of these thresholds</div>
        <p className="small muted" style={{ marginBottom: 0 }}>
          Catalogue <code>{method.catalogue_version}</code> is a working set of agronomic
          thresholds compiled for the pilot engine. It is not a TNAU recommendation and is
          not calibrated to a soil series. Agronomist review is pending, and the review
          status travels with every result. TNAU’s Crop Production Guide is linked as a
          manual reference only, because its machine-reuse rights are unconfirmed.
        </p>
      </div>
    </>
  );
}
