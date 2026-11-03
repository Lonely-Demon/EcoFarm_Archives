"use client";

import { Suspense, useEffect, useMemo, useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { api, ApiError, localRecords, type DecisionPacket, type Meta } from "@/lib/api";

const SOIL_TEXTURES = ["red", "black", "sandy", "loam", "clay"];

const CROP_STAGES = [
  { id: "pre_sowing", label: "Not sown yet", desc: "Still choosing what to plant." },
  { id: "sowing", label: "Sowing now", desc: "Seed already going in." },
  { id: "early_establishment", label: "Just emerged", desc: "Crop is a few weeks old." },
];

const LABOUR = [
  { id: "plenty", label: "Plenty" },
  { id: "limited", label: "Limited" },
  { id: "scarce", label: "Scarce" },
  { id: "unknown", label: "Not sure" },
];

export default function DecidePage() {
  return (
    <Suspense
      fallback={
        <>
          <div className="skeleton" style={{ height: 30, width: "60%", margin: "28px 0 16px" }} />
          <div className="skeleton" style={{ height: 180, marginBottom: 14 }} />
          <div className="skeleton" style={{ height: 180 }} />
        </>
      }
    >
      <DecideForm />
    </Suspense>
  );
}

function DecideForm() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const prefill = searchParams?.get("from") ?? null;
  const [meta, setMeta] = useState<Meta | null>(null);
  const [loadError, setLoadError] = useState<string | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const [submitError, setSubmitError] = useState<string | null>(null);

  const [blockId, setBlockId] = useState("");
  const [village, setVillage] = useState("");
  const [cropStage, setCropStage] = useState("pre_sowing");
  const [sowingWindow, setSowingWindow] = useState("");
  const [water, setWater] = useState("");
  const [objectives, setObjectives] = useState<string[]>([]);
  const [soilTexture, setSoilTexture] = useState("");
  const [soilPh, setSoilPh] = useState("");
  const [landArea, setLandArea] = useState("");
  const [labour, setLabour] = useState("unknown");
  const [hasSoilTest, setHasSoilTest] = useState(false);
  const [consent, setConsent] = useState(false);
  const [notice, setNotice] = useState<string | null>(null);
  const [pendingObjectiveLabels, setPendingObjectiveLabels] = useState<string[]>([]);

  useEffect(() => {
    api
      .meta()
      .then(setMeta)
      .catch((e) => setLoadError(e.message));
  }, []);

  // Adjust-and-re-run: copy a previous decision's answers back into the form.
  useEffect(() => {
    if (!prefill) return;
    api
      .getDecision(prefill)
      .then((packet) => {
        const ctx = packet.farmer_context as Record<string, unknown>;
        setBlockId((ctx.block_id as string) || "");
        setVillage((ctx.village as string) || "");
        setCropStage((ctx.crop_stage as string) || "pre_sowing");
        setSowingWindow((ctx.intended_sowing_window as string) || "");
        setWater((ctx.water_availability as string) || "");
        setSoilTexture((ctx.soil_texture as string) || "");
        setSoilPh(ctx.soil_ph != null ? String(ctx.soil_ph) : "");
        setLandArea(ctx.land_area_ha != null ? String(ctx.land_area_ha) : "");
        const labels = (ctx.objectives as string[]) || [];
        // map display labels back to ids once meta is loaded
        setPendingObjectiveLabels(labels);
        setNotice("Answers copied from your previous decision. Change anything and re-run.");
      })
      .catch(() => {
        setNotice("Could not copy the previous answers. You can fill the form fresh.");
      });
  }, [prefill]);

  // resolve objective labels -> ids after meta arrives
  useEffect(() => {
    if (!meta || pendingObjectiveLabels.length === 0) return;
    const ids = meta.objectives
      .filter((o) => pendingObjectiveLabels.includes(o.label))
      .map((o) => o.id);
    setObjectives(ids);
    setPendingObjectiveLabels([]);
  }, [meta, pendingObjectiveLabels]);

  const toggleObjective = (id: string) => {
    setObjectives((prev) => (prev.includes(id) ? prev.filter((o) => o !== id) : [...prev, id]));
  };

  const missing = useMemo(() => {
    const items: string[] = [];
    if (!blockId) items.push("block");
    if (!sowingWindow) items.push("sowing window");
    if (!water) items.push("water situation");
    if (objectives.length === 0) items.push("at least one goal");
    if (!consent) items.push("consent");
    return items;
  }, [blockId, sowingWindow, water, objectives, consent]);

  async function submit() {
    setSubmitting(true);
    setSubmitError(null);
    try {
      const packet: DecisionPacket = await api.createDecision({
        consent_granted: consent,
        language: "en",
        block_id: blockId,
        village: village || null,
        crop_stage: cropStage as "pre_sowing" | "sowing" | "early_establishment",
        intended_sowing_window: sowingWindow,
        water_availability: water,
        objective: objectives,
        soil_texture: soilTexture || null,
        soil_ph: soilPh ? Number(soilPh) : null,
        land_area_ha: landArea ? Number(landArea) : null,
        soil_test_available: hasSoilTest,
        labour_available: labour,
      });

      localRecords.add({
        id: packet.decision_id,
        created_at: packet.created_at,
        block: String(packet.farmer_context.block ?? blockId),
        headline: packet.headline,
      });

      router.push(`/packet/${packet.decision_id}?fresh=1`);
    } catch (e) {
      const err = e as ApiError;
      setSubmitError(err.message);
      setSubmitting(false);
    }
  }

  if (loadError) {
    return (
      <div className="notice stop" style={{ marginTop: 24 }}>
        <span className="notice-icon" aria-hidden>
          ⚠
        </span>
        <div>
          <strong>Cannot load the decision form</strong>
          {loadError}
        </div>
      </div>
    );
  }

  if (!meta) {
    return (
      <>
        <div className="skeleton" style={{ height: 30, width: "60%", margin: "28px 0 16px" }} />
        <div className="skeleton" style={{ height: 180, marginBottom: 14 }} />
        <div className="skeleton" style={{ height: 180 }} />
      </>
    );
  }

  return (
    <>
      <p className="eyebrow">New decision</p>
      <h1>What are you deciding?</h1>
      <p className="lede" style={{ marginBottom: 22 }}>
        Six answers are required. Everything else is optional, and leaving it blank
        removes that factor from the comparison rather than guessing it.
      </p>

      {notice && (
        <div className="notice info" style={{ marginBottom: 16 }}>
          <span className="notice-icon" aria-hidden>
            ↺
          </span>
          <div>{notice}</div>
        </div>
      )}

      <div className="notice info" style={{ marginBottom: 22 }}>
        <span className="notice-icon" aria-hidden>
          ◐
        </span>
        <div>
          <strong>Weather and price are not part of this comparison</strong>
          No weather source has passed the pilot’s Namakkal tests, and market prices are
          outside tested scope. Your result will show both as missing.
        </div>
      </div>

      <div className="field">
        <label className="label" htmlFor="block">
          Block
        </label>
        <div className="hint">Pilot scope is Namakkal district only.</div>
        <select id="block" value={blockId} onChange={(e) => setBlockId(e.target.value)}>
          <option value="">Select your block</option>
          {meta.blocks.map((b) => (
            <option key={b.id} value={b.id}>
              {b.name}
            </option>
          ))}
        </select>
      </div>

      <div className="field">
        <label className="label" htmlFor="village">
          Village or hamlet <span className="muted small">(optional)</span>
        </label>
        <div className="hint">Used only to keep your record readable. It is not treated as a plot location.</div>
        <input
          id="village"
          type="text"
          value={village}
          onChange={(e) => setVillage(e.target.value)}
          placeholder="e.g. Kabilarmalai"
          autoComplete="off"
        />
      </div>

      <div className="field">
        <span className="label">Crop stage</span>
        <div className="hint">There is no default stage; it changes which information is relevant.</div>
        <div className="options">
          {CROP_STAGES.map((stage) => (
            <label key={stage.id} className="option" data-selected={cropStage === stage.id}>
              <input
                type="radio"
                name="stage"
                checked={cropStage === stage.id}
                onChange={() => setCropStage(stage.id)}
              />
              <span>
                <span style={{ fontWeight: 600 }}>{stage.label}</span>
                <div className="option-desc">{stage.desc}</div>
              </span>
            </label>
          ))}
        </div>
      </div>

      <div className="field">
        <label className="label" htmlFor="window">
          When do you plan to sow?
        </label>
        <div className="hint">Used to check the crop’s listed sowing season. It is not a weather forecast.</div>
        <select id="window" value={sowingWindow} onChange={(e) => setSowingWindow(e.target.value)}>
          <option value="">Select a window</option>
          {meta.seasons.map((s) => (
            <option key={s.id} value={s.id}>
              {s.label}
            </option>
          ))}
        </select>
      </div>

      <div className="field">
        <span className="label">Water situation</span>
        <div className="hint">
          Required. If you choose “not sure”, EcoFarm shows a reference list instead of a
          comparison, because the comparison depends on this answer.
        </div>
        <div className="options">
          {meta.water_options.map((w) => (
            <label key={w.id} className="option" data-selected={water === w.id}>
              <input type="radio" name="water" checked={water === w.id} onChange={() => setWater(w.id)} />
              <span>
                <span style={{ fontWeight: 600 }}>{w.label}</span>
                <div className="option-desc">{w.description}</div>
              </span>
            </label>
          ))}
        </div>
      </div>

      <div className="field">
        <span className="label">What matters to you?</span>
        <div className="hint">
          Pick one or more. These explain trade-offs only; they are never turned into an
          income promise.
        </div>
        <div className="options">
          {meta.objectives.map((o) => (
            <label key={o.id} className="option" data-selected={objectives.includes(o.id)}>
              <input type="checkbox" checked={objectives.includes(o.id)} onChange={() => toggleObjective(o.id)} />
              <span style={{ fontWeight: 600 }}>{o.label}</span>
            </label>
          ))}
        </div>
      </div>

      <div className="field">
        <span className="label">Soil — optional</span>
        <div className="hint">
          Leave both blank if you are unsure. EcoFarm will drop soil from the comparison
          rather than substitute a district average.
        </div>
        <div className="grid-2">
          <div>
            <label className="label small" htmlFor="texture">
              Texture
            </label>
            <select id="texture" value={soilTexture} onChange={(e) => setSoilTexture(e.target.value)}>
              <option value="">Not given</option>
              {SOIL_TEXTURES.map((t) => (
                <option key={t} value={t}>
                  {t[0].toUpperCase() + t.slice(1)} soil
                </option>
              ))}
            </select>
          </div>
          <div>
            <label className="label small" htmlFor="ph">
              pH (from a test)
            </label>
            <input
              id="ph"
              type="number"
              inputMode="decimal"
              step="0.1"
              min="3"
              max="10"
              value={soilPh}
              onChange={(e) => setSoilPh(e.target.value)}
              placeholder="e.g. 7.2"
            />
          </div>
        </div>
        <label className="option" style={{ marginTop: 10 }} data-selected={hasSoilTest}>
          <input type="checkbox" checked={hasSoilTest} onChange={(e) => setHasSoilTest(e.target.checked)} />
          <span>
            <span style={{ fontWeight: 600 }}>I have a soil test report</span>
            <div className="option-desc">
              If you enter values without a date, EcoFarm records the soil record as
              unverified. It will not read the report itself.
            </div>
          </span>
        </label>
      </div>

      <div className="field">
        <span className="label">Labour — optional</span>
        <div className="options">
          {LABOUR.map((l) => (
            <label key={l.id} className="option" data-selected={labour === l.id}>
              <input type="radio" name="labour" checked={labour === l.id} onChange={() => setLabour(l.id)} />
              <span style={{ fontWeight: 600 }}>{l.label}</span>
            </label>
          ))}
        </div>
      </div>

      <div className="field">
        <label className="label" htmlFor="area">
          Area in hectares <span className="muted small">(optional)</span>
        </label>
        <div className="hint">Context only. Never used to predict cost, income or yield.</div>
        <input
          id="area"
          type="number"
          inputMode="decimal"
          min="0.1"
          max="50"
          step="0.1"
          value={landArea}
          onChange={(e) => setLandArea(e.target.value)}
          placeholder="e.g. 1.5"
        />
      </div>

      <div className="card sunk" style={{ marginTop: 26 }}>
        <div className="eyebrow">Consent</div>
        <p className="small" style={{ marginBottom: 10 }}>
          <strong>Purpose.</strong> {meta.consent_notice.purpose}
        </p>
        <p className="small" style={{ marginBottom: 10 }}>
          <strong>Scope.</strong> {meta.consent_notice.scope}
        </p>
        <p className="small" style={{ marginBottom: 10 }}>
          <strong>Retention.</strong> {meta.consent_notice.retention}
        </p>
        <p className="small" style={{ marginBottom: 14 }}>
          <strong>Deletion.</strong> {meta.consent_notice.deletion}
        </p>

        <details style={{ marginBottom: 14 }}>
          <summary className="small" style={{ fontWeight: 600 }}>
            What each field is used for
          </summary>
          <div className="stack" style={{ marginTop: 10 }}>
            {meta.consent_notice.fields.map((f) => (
              <div key={f.field} className="small" style={{ paddingBottom: 8, borderBottom: "1px dashed var(--line)" }}>
                <strong>
                  {f.label} {f.required ? "" : "(optional)"}
                </strong>
                <div className="muted">{f.purpose}</div>
              </div>
            ))}
          </div>
        </details>

        <label className="option" data-selected={consent}>
          <input type="checkbox" checked={consent} onChange={(e) => setConsent(e.target.checked)} />
          <span style={{ fontWeight: 600 }}>
            I agree to EcoFarm using these answers for this one decision, as described above.
          </span>
        </label>
      </div>

      {submitError && (
        <div className="notice stop" style={{ marginTop: 16 }}>
          <span className="notice-icon" aria-hidden>
            ⚠
          </span>
          <div>
            <strong>No result was produced</strong>
            {submitError}
          </div>
        </div>
      )}

      <div style={{ marginTop: 18 }}>
        <button className="btn block" onClick={submit} disabled={missing.length > 0 || submitting}>
          {submitting ? (
            <>
              <span className="spinner" /> Comparing options…
            </>
          ) : (
            "Show my options"
          )}
        </button>
        {missing.length > 0 && (
          <p className="tiny muted" style={{ textAlign: "center", marginTop: 8 }}>
            Still needed: {missing.join(", ")}
          </p>
        )}
      </div>
    </>
  );
}
