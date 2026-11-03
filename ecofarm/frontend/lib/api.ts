/**
 * Typed API client.
 *
 * BASE is deliberately resolved at build time so a separately hosted backend
 * works as a pure static/runtime configuration change.
 */

export type Provenance = {
  source_id: string;
  source_name: string;
  publisher: string;
  url: string;
  status: string;
  note: string;
};

export type FactorResult = {
  factor: string;
  status: string;
  weight: number;
  contribution: number | null;
  explanation: string;
  provenance: Provenance[];
};

export type CropOption = {
  crop_id: string;
  name_en: string;
  local_name: string | null;
  category: string;
  score: number;
  band: "stronger_fit" | "possible_fit" | "weaker_fit" | "reference_only";
  factors: FactorResult[];
  excluded_factors: FactorResult[];
  cautions: string[];
  key_risks: string[];
  duration_days: [number, number];
  water_need_level: number;
  seasons: string[];
  guidance: Provenance | null;
  rank_range: [number, number] | null;
};

export type Referral = {
  trigger: string;
  wording: string;
  contact_name: string;
  contact_detail: string;
  source_url: string;
  verified_on: string;
  is_stale: boolean;
  neutral_notice: string;
};

export type DecisionPacket = {
  decision_id: string;
  created_at: string;
  engine_version: string;
  catalogue_version: string;
  output_state:
    | "ranked_options_with_gaps"
    | "informational_only"
    | "insufficient_context"
    | "outside_tested_scope";
  headline: string;
  limitation_note: string;
  farmer_context: Record<string, unknown>;
  factors_used: FactorResult[];
  excluded_factors: FactorResult[];
  options: CropOption[];
  sensitivity: {
    crop_id: string;
    rank: number;
    rank_range: [number, number];
    label: "stable" | "moderate" | "unstable";
    note: string;
  }[];
  sensitivity_note: string;
  referrals: Referral[];
  farmer_response_options: string[];
  retention: Record<string, string>;
  method_notes: string[];
};

export type Meta = {
  engine_version: string;
  catalogue_version: string;
  directory_version: string;
  register_version: string;
  district: {
    id: string;
    name: string;
    state: string;
    agro_climatic_zones: string[];
    normal_annual_rainfall_mm: number;
    soil_summary: string;
    rainfall_note: string;
    source_url: string;
  };
  blocks: { id: string; name: string; office: string; phone: string }[];
  crops: {
    id: string;
    name_en: string;
    local_names: Record<string, string>;
    category: string;
    duration_days: number[];
    water_need_level: number;
    rainfed_suitable: boolean;
    assured_irrigation_required: boolean;
    prevalence_namakkal: string;
  }[];
  objectives: { id: string; label: string }[];
  water_options: { id: string; label: string; description: string }[];
  seasons: { id: string; label: string; months: number[] }[];
  source_register: {
    id: string;
    name: string;
    publisher: string;
    url: string;
    kind: string;
    status: string;
    status_detail: string;
    farmer_facing_state: string;
  }[];
  consent_notice: {
    purpose: string;
    scope: string;
    retention: string;
    deletion: string;
    fields: {
      field: string;
      label: string;
      purpose: string;
      required: boolean;
      consent_scope: string;
      deletion: string;
    }[];
  };
  weather_gate: {
    weather_available: boolean;
    state: string;
    headline: string;
    detail: string;
    candidates: {
      source_id: string;
      source_name: string;
      publisher: string;
      url: string;
      status: string;
      status_detail: string;
      blocked_for_namakkal: boolean;
    }[];
  };
  limitations: string[];
};

export type DecisionInput = {
  consent_granted: boolean;
  language: "en" | "ta";
  block_id: string;
  village?: string | null;
  crop_stage: "pre_sowing" | "sowing" | "early_establishment";
  intended_sowing_window: string;
  water_availability: string;
  objective: string[];
  land_area_ha?: number | null;
  soil_texture?: string | null;
  soil_ph?: number | null;
  soil_test_available?: boolean;
  soil_test_date?: string | null;
  labour_available?: string;
  exclude_crops?: string[];
};

export const API_BASE =
  process.env.NEXT_PUBLIC_API_BASE_URL?.replace(/\/$/, "") || "/api/proxy";

export class ApiError extends Error {
  state: string;
  constructor(message: string, state = "unknown") {
    super(message);
    this.state = state;
  }
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  let response: Response;
  try {
    response = await fetch(`${API_BASE}${path}`, {
      ...init,
      headers: { "Content-Type": "application/json", ...(init?.headers || {}) },
      cache: "no-store",
    });
  } catch {
    throw new ApiError(
      "The EcoFarm decision service could not be reached. No substitute or cached recommendation is shown.",
      "source_temporarily_unavailable",
    );
  }

  if (!response.ok) {
    let state = "error";
    let message = `Request failed (${response.status}).`;
    try {
      const body = await response.json();
      if (body?.detail?.state) state = body.detail.state;
      if (body?.detail?.message) message = body.detail.message;
      else if (typeof body?.detail === "string") message = body.detail;
    } catch {
      /* keep defaults */
    }
    throw new ApiError(message, state);
  }

  return (await response.json()) as T;
}

export const api = {
  meta: () => request<Meta>("/meta"),
  method: () => request<Record<string, unknown>>("/method"),
  createDecision: (body: DecisionInput) =>
    request<DecisionPacket>("/decisions", { method: "POST", body: JSON.stringify(body) }),
  getDecision: (id: string) => request<DecisionPacket>(`/decisions/${id}`),
  deleteDecision: (id: string) =>
    request<{ decision_id: string; deleted: boolean; message: string }>(`/decisions/${id}`, {
      method: "DELETE",
    }),
  respondToDecision: (id: string, response_text: string) =>
    request<{ decision_id: string; deleted: boolean; message: string }>(
      `/decisions/${id}/response?response_text=${encodeURIComponent(response_text)}`,
      { method: "POST" },
    ),
};

/**
 * Decisions are also kept on the device so a farmer can reopen a packet after
 * the network drops. The server copy is still authoritative.
 */
export const localRecords = {
  key: "ecofarm.decisions.v1",
  list(): { id: string; created_at: string; block: string; headline: string }[] {
    if (typeof window === "undefined") return [];
    try {
      return JSON.parse(window.localStorage.getItem(this.key) || "[]");
    } catch {
      return [];
    }
  },
  add(record: { id: string; created_at: string; block: string; headline: string }) {
    if (typeof window === "undefined") return;
    const items = this.list().filter((r) => r.id !== record.id);
    window.localStorage.setItem(this.key, JSON.stringify([record, ...items].slice(0, 20)));
  },
  remove(id: string) {
    if (typeof window === "undefined") return;
    window.localStorage.setItem(
      this.key,
      JSON.stringify(this.list().filter((r) => r.id !== id)),
    );
  },
};
