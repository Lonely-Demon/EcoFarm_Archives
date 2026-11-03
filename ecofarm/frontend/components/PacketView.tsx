"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { api, ApiError, localRecords, type CropOption, type DecisionPacket } from "@/lib/api";

const BAND_LABEL: Record<string, string> = {
  stronger_fit: "Stronger fit",
  possible_fit: "Possible fit",
  weaker_fit: "Weaker fit",
  reference_only: "Reference list",
};

const REFERENCE_ORDER = [
  "groundnut", "sorghum", "maize", "pearl_millet", "green_gram",
  "black_gram", "cowpea", "cotton", "paddy", "sugarcane", "tapioca",
];

const FACTOR_LABEL: Record<string, string> = {
  water_fit: "Water availability fit",
  season_fit: "Sowing-window fit",
  soil_fit: "Soil fit",
  objective_fit: "Your stated objectives",
  duration_fit: "Crop duration",
  local_relevance: "Presence in Namakkal cropping",
  weather_advisory: "Weather and advisory",
  market_price: "Observed market price",
  pest_disease: "Pest and disease risk",
};

const RESPONSE_LABEL: Record<string, string> = {
  accepted: "This is useful",
  rejected: "This does not fit my situation",
  changed_mind: "I changed my plan",
  need_more_information: "I need more information",
};

export default function PacketView({
  packet,
  fresh,
}: {
  packet: DecisionPacket;
  fresh: boolean;
}) {
  const router = useRouter();
  const id = packet.decision_id;
  const [error, setError] = useState<{ message: string; state: string } | null>(null);
  const [open, setOpen] = useState<string | null>(() => {
    const top = packet.options.find((o) => o.band === "stronger_fit");
    return top?.crop_id ?? packet.options[0]?.crop_id ?? null;
  });
  const [showExcluded, setShowExcluded] = useState(true);
  const [confirmedDelete, setConfirmedDelete] = useState(false);
  const [busy, setBusy] = useState(false);
  const [feedback, setFeedback] = useState<string | null>(null);
  const [showAll, setShowAll] = useState(false);

  async function remove() {
    if (!id) return;
    setBusy(true);
    try {
      await api.deleteDecision(id);
      localRecords.remove(id);
      router.push("/?deleted=1");
    } catch (e) {
      setError({ message: (e as ApiError).message, state: "delete_failed" });
      setBusy(false);
    }
  }

  async function respond(choice: string) {
    if (!id) return;
    try {
      await api.respondToDecision(id, choice);
      setFeedback("Recorded. Thank you — this does not change what EcoFarm shows you.");
    } catch {
      setFeedback("Could not record that right now. You can still delete the record.");
    }
  }

  const isReference = packet.output_state === "informational_only";

  // Position span of each band. Within a band the ordering is not meaningful, so a
  // member of a multi-crop band is labelled with the band's span, not its own rank.
  const bandSpan: Record<string, [number, number]> = {};
  packet.options.forEach((option, index) => {
    const span = bandSpan[option.band];
    if (!span) bandSpan[option.band] = [index + 1, index + 1];
    else bandSpan[option.band] = [span[0], index + 1];
  });
  const grouped = packet.options.reduce<Record<string, CropOption[]>>((acc, option) => {
    acc[option.band] = acc[option.band] || [];
    acc[option.band].push(option);
    return acc;
  }, {});

  return (
    <>
      {fresh && (
        <div className="notice info" style={{ marginTop: 18 }}>
          <span className="notice-icon" aria-hidden>
            ✓
          </span>
          <div>
            <strong>Decision recorded</strong>
            Saved for <strong>{packet.retention.days} days</strong> unless you delete it. The ID is{" "}
            <code className="tiny">{packet.decision_id.slice(0, 8)}</code>.
          </div>
        </div>
      )}

      <p className="eyebrow" style={{ marginTop: 20 }}>
        Decision packet · {String(packet.farmer_context.block)}
        {packet.farmer_context.village ? ` · ${packet.farmer_context.village}` : ""}
      </p>
      <h1 style={{ marginTop: 4 }}>{packet.headline}</h1>

      <div className={`notice ${packet.output_state === "ranked_options_with_gaps" ? "warn" : "stop"}`}>
        <span className="notice-icon" aria-hidden>
          ⚠
        </span>
        <div>
          <strong>
            {packet.output_state === "informational_only"
              ? "Reference only — not a comparison for your farm"
              : packet.output_state === "insufficient_context"
              ? "Not enough context to compare"
              : "This comparison is incomplete by design"}
          </strong>
          {packet.limitation_note}
        </div>
      </div>

      {/* Excluded factors — the most important panel on the page */}
      <div className="excluded">
        <div style={{ display: "flex", justifyContent: "space-between", gap: 10, alignItems: "center" }}>
          <h3>What was left out, and why</h3>
          <button className="btn ghost" onClick={() => setShowExcluded((v) => !v)}>
            {showExcluded ? "Hide" : "Show"}
          </button>
        </div>
        {showExcluded && (
          <div className="stack" style={{ marginTop: 3 }}>
            {packet.excluded_factors.map((factor) => (
              <div key={factor.factor}>
                <div style={{ fontSize: 14, fontWeight: 620 }}>
                  <span className="status-dot blocked" />
                  {FACTOR_LABEL[factor.factor] ?? factor.factor}
                </div>
                <div className="small" style={{ color: "#7a5a4a", marginTop: 2 }}>
                  {factor.explanation}
                </div>
                {factor.provenance.map((p) => (
                  <a
                    key={p.source_id}
                    href={p.url}
                    target="_blank"
                    rel="noreferrer noopener"
                    className="tiny"
                    style={{ display: "block", color: "#8a6a5a", marginTop: 4 }}
                  >
                    {p.source_name} · {p.publisher} · {p.status.replace(/_/g, " ")} ↗
                  </a>
                ))}
              </div>
            ))}
          </div>
        )}
      </div>

      {isReference && (
        <section style={{ marginTop: 20 }}>
          <div className="eyebrow" style={{ marginBottom: 2 }}>
            Crops grown in Namakkal · {packet.options.length} entries
          </div>
          <p className="tiny muted" style={{ marginBottom: 10 }}>
            Listed in catalogue order, not in order of fit. No score is shown because none
            would be valid without your water situation.
          </p>
          {[...packet.options]
            .sort((a, b) => REFERENCE_ORDER.indexOf(a.crop_id) - REFERENCE_ORDER.indexOf(b.crop_id))
            .map((option) => (
              <CropCard
                key={option.crop_id}
                option={option}
                open={open === option.crop_id}
                onToggle={() => setOpen(open === option.crop_id ? null : option.crop_id)}
                hideScore
              />
            ))}
        </section>
      )}

      {/* Options grouped by band, not numbered */}
      {!isReference && ["stronger_fit", "possible_fit", "weaker_fit"].map((band) => {
        const options = grouped[band];
        if (!options || options.length === 0) return null;
        const collapsed = band === "weaker_fit" && !showAll;

        return (
          <section key={band} style={{ marginTop: 20 }}>
            <div className="card-head" style={{ marginBottom: 8 }}>
              <div>
                <div className="eyebrow" style={{ marginBottom: 2 }}>
                  {BAND_LABEL[band]} · {options.length} option{options.length > 1 ? "s" : ""}
                </div>
                <p className="tiny muted" style={{ marginBottom: 0 }}>
                  {band === "stronger_fit" && "Best supported by the factors EcoFarm can use. Not a recommendation."}
                  {band === "possible_fit" && "Mid-range; a small change in weighting could move these."}
                  {band === "weaker_fit" && "Poor fit against your stated constraints, or a hard constraint applies."}
                </p>
              </div>
            </div>

            {collapsed ? (
              <button className="btn secondary block" onClick={() => setShowAll(true)}>
                Show {options.length} weaker-fit options
              </button>
            ) : (
              options.map((option) => (
                <CropCard
                  key={option.crop_id}
                  option={option}
                  bandSpan={bandSpan[option.band]}
                  open={open === option.crop_id}
                  onToggle={() => setOpen(open === option.crop_id ? null : option.crop_id)}
                />
              ))
            )}
          </section>
        );
      })}

      {/* Sensitivity */}
      {!isReference && (
      <div className="card" style={{ marginTop: 22 }}>
        <h2>How stable is this ordering?</h2>
        <p className="small muted">{packet.sensitivity_note}</p>
        <div className="stack">
          {packet.sensitivity.slice(0, 5).map((entry) => {
            const option = packet.options.find((o) => o.crop_id === entry.crop_id);
            return (
              <div
                key={entry.crop_id}
                style={{ display: "flex", justifyContent: "space-between", gap: 10, fontSize: 13.5 }}
              >
                <span style={{ fontWeight: 600 }}>{option?.name_en ?? entry.crop_id}</span>
                <span className={entry.label === "stable" ? "chip" : "chip rank-moderate"}>
                  ranks {entry.rank_range[0]}–{entry.rank_range[1]} · {entry.label}
                </span>
              </div>
            );
          })}
        </div>
      </div>
      )}

      {/* Method notes */}
      <div className="card">
        <h2>How this was calculated</h2>
        <ul className="small muted" style={{ paddingLeft: 18, margin: 0 }}>
          {packet.method_notes.map((note, i) => (
            <li key={i} style={{ marginBottom: 6 }}>
              {note}
            </li>
          ))}
        </ul>
        <div className="divider" />
        <div className="pill-row">
          <span className="chip">engine {packet.engine_version}</span>
          <span className="chip">catalogue {packet.catalogue_version}</span>
          <span className="chip">state {packet.output_state.replace(/_/g, " ")}</span>
        </div>
      </div>

      {/* Referrals */}
      <div className="card">
        <h2>Where to check independently</h2>
        <div className="stack">
          {packet.referrals.map((r, i) => (
            <div key={i} style={{ paddingBottom: 12, borderBottom: i < packet.referrals.length - 1 ? "1px dashed var(--line)" : "none" }}>
              <div style={{ fontWeight: 620, fontSize: 14 }}>{r.contact_name}</div>
              <div className="small" style={{ marginTop: 2 }}>
                {r.contact_detail}
              </div>
              <p className="small muted" style={{ margin: "6px 0" }}>
                {r.wording}
              </p>
              <p className="tiny" style={{ color: "var(--ink-faint)", margin: 0 }}>
                {r.neutral_notice} Directory checked {r.verified_on}
                {r.is_stale ? " — this entry is past its review date and must be re-verified." : "."}{" "}
                <a href={r.source_url} target="_blank" rel="noreferrer noopener">
                  Source ↗
                </a>
              </p>
            </div>
          ))}
        </div>
      </div>

      {/* Feedback + retention */}
      <div className="card sunk">
        <h2>Did this help?</h2>
        <p className="small muted">
          Your answer is used only to evaluate the pilot, and skipping it never affects
          your access.
        </p>
        <div className="btn-row">
          {packet.farmer_response_options.map((choice) => (
            <button key={choice} className="btn secondary" onClick={() => respond(choice)}>
              {RESPONSE_LABEL[choice] ?? choice}
            </button>
          ))}
        </div>
        {feedback && (
          <p className="small" style={{ marginTop: 10, color: "var(--sage-deep)", marginBottom: 0 }}>
            {feedback}
          </p>
        )}
      </div>

      <div className="card sunk">
        <h2>Change one answer and re-run</h2>
        <p className="small muted">
          Opens a new form filled with these answers. The original record stays as it
          was, so you can compare what changed.
        </p>
        <Link href={`/decide?from=${packet.decision_id}`} className="btn secondary">
          Adjust and re-run
        </Link>
      </div>

      <div className="card sunk">
        <h2>Delete this record</h2>
        <p className="small muted">
          {packet.retention.deletion} {packet.retention.note}
        </p>
        {!confirmedDelete ? (
          <button className="btn danger" onClick={() => setConfirmedDelete(true)}>
            Delete my decision record
          </button>
        ) : (
          <div className="btn-row">
            <button className="btn danger" onClick={remove} disabled={busy}>
              {busy ? "Deleting…" : "Yes, delete it now"}
            </button>
            <button className="btn secondary" onClick={() => setConfirmedDelete(false)}>
              Keep it
            </button>
          </div>
        )}
      </div>

      <p className="tiny muted" style={{ textAlign: "center", marginTop: 24 }}>
        EcoFarm is not an emergency service, a pesticide adviser, or a buyer. For urgent
        crop-loss or safety concerns, follow official warnings and local emergency
        instructions.
      </p>
    </>
  );
}

function CropCard({
  option,
  bandSpan,
  open,
  onToggle,
  hideScore = false,
}: {
  option: CropOption;
  bandSpan?: [number, number];
  open: boolean;
  onToggle: () => void;
  hideScore?: boolean;
}) {
  const unstable = option.rank_range && option.rank_range[1] - option.rank_range[0] >= 3;
  const sharedBand = bandSpan && bandSpan[1] > bandSpan[0];

  // In a shared band the individual position is not meaningful, so show the span.
  const positionLabel = !option.rank_range
    ? null
    : sharedBand
    ? `no order within positions ${bandSpan[0]}–${bandSpan[1]}`
    : `position ${option.rank_range[0]}`;

  return (
    <div className="crop-card" data-band={option.band}>
      <div className="crop-head" onClick={onToggle} role="button" tabIndex={0} onKeyDown={(e) => e.key === "Enter" && onToggle()}>
        <div style={{ flex: 1 }}>
          <h3>{option.name_en}</h3>
          <div className="crop-meta">
            <span className="chip">water level {option.water_need_level}/5</span>
            <span className="chip">
              {option.duration_days[0]}–{option.duration_days[1]} days
            </span>
            {option.local_name && <span className="chip">{option.local_name}</span>}
            {!hideScore && positionLabel && (
              <span className={unstable || sharedBand ? "chip rank-moderate" : "chip"}>
                {positionLabel}
              </span>
            )}
          </div>
          {option.cautions.length > 0 && (
            <div className="small" style={{ color: "var(--clay)", marginTop: 8, fontWeight: 600 }}>
              ⚠ {option.cautions[0]}
            </div>
          )}
        </div>
        {!hideScore && (
          <div className="score-dial" title="Weighted fit score, 0 to 1">
            {option.score.toFixed(2)}
          </div>
        )}
      </div>

      {open && (
        <div className="crop-body">
          <div className="eyebrow">Factors used</div>
          {option.factors.map((factor) => (
            <div key={factor.factor} className="factor">
              <div className="factor-top">
                <span>{FACTOR_LABEL[factor.factor] ?? factor.factor}</span>
                <span className="factor-status">
                  {factor.status.replace(/_/g, " ")}
                  {!hideScore && factor.contribution !== null ? ` · ${factor.contribution.toFixed(2)}` : ""}
                </span>
              </div>
              {!hideScore && factor.contribution !== null && (
                <div className="bar">
                  <span style={{ width: `${factor.contribution * 100}%` }} />
                </div>
              )}
              <div className="factor-explanation">{factor.explanation}</div>
              {factor.provenance.length > 0 && (
                <div className="provenance">
                  {factor.provenance.map((p) => (
                    <span key={p.source_id}>
                      Source:{" "}
                      <a href={p.url} target="_blank" rel="noreferrer noopener">
                        {p.source_name}
                      </a>{" "}
                      · {p.status.replace(/_/g, " ")}
                    </span>
                  ))}
                </div>
              )}
            </div>
          ))}

          <div className="eyebrow" style={{ marginTop: 16 }}>
            Not scored for this crop
          </div>
          {option.excluded_factors.map((factor) => (
            <div key={factor.factor} className="factor">
              <div className="factor-top">
                <span style={{ color: "var(--ink-soft)" }}>{FACTOR_LABEL[factor.factor] ?? factor.factor}</span>
                <span className="factor-status">excluded</span>
              </div>
              <div className="factor-explanation">{factor.explanation}</div>
            </div>
          ))}

          {option.key_risks.length > 0 && (
            <>
              <div className="eyebrow" style={{ marginTop: 16 }}>
                Known risks
              </div>
              <ul className="small muted" style={{ paddingLeft: 18, margin: 0 }}>
                {option.key_risks.map((risk, i) => (
                  <li key={i} style={{ marginBottom: 4 }}>
                    {risk}
                  </li>
                ))}
              </ul>
            </>
          )}

          {option.guidance && (
            <div className="provenance" style={{ marginTop: 16 }}>
              Reference to read next:{" "}
              <a href={option.guidance.url} target="_blank" rel="noreferrer noopener">
                {option.guidance.source_name}
              </a>{" "}
              ({option.guidance.status.replace(/_/g, " ")} — shown as a citation only, never
              transformed into a computed rule).
            </div>
          )}
        </div>
      )}
    </div>
  );
}
