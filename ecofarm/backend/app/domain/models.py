"""Domain models for the EcoFarm crop recommendation engine.

Every model here is deliberately explicit about provenance, because the
archive's governing rule is that an output must never look more certain than
the evidence behind it.
"""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Any, Literal

from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# Enumerations
# ---------------------------------------------------------------------------


class Objective(str, Enum):
    """Farmer-stated goals. Never inferred, never profit-maximising by default."""

    water_conservation = "water_conservation"
    lower_input_cost = "lower_input_cost"
    timing_flexibility = "timing_flexibility"
    household_food = "household_food"
    market_sale = "market_sale"
    risk_reduction = "risk_reduction"
    fodder = "fodder"


class WaterAvailability(str, Enum):
    reliable = "reliable"
    seasonal = "seasonal"
    rainfed = "rainfed"
    uncertain = "uncertain"
    unknown = "unknown"


class SoilTexture(str, Enum):
    red = "red"
    black = "black"
    sandy = "sandy"
    loam = "loam"
    clay = "clay"


class Season(str, Enum):
    """Broad sowing season labels used for filtering, not for weather claims."""

    jun_jul = "jun_jul"
    aug_sep = "aug_sep"
    oct_nov = "oct_nov"
    dec_jan = "dec_jan"
    feb_mar = "feb_mar"
    apr_may = "apr_may"


class SourceStatus(str, Enum):
    approved = "approved"
    manual_reference = "manual_reference"
    blocked_permission = "blocked_permission"
    rejected_locality = "rejected_locality"
    rejected_rights = "rejected_rights"
    not_tested = "not_tested"


class FactorStatus(str, Enum):
    """How much authority a single factor carries in the shown result."""

    used = "used"
    excluded_missing_input = "excluded_missing_input"
    excluded_no_approved_source = "excluded_no_approved_source"
    excluded_out_of_scope = "excluded_out_of_scope"
    excluded_permission_pending = "excluded_permission_pending"
    reference_only = "reference_only"
    synthetic_not_used = "synthetic_not_used"


class OutputState(str, Enum):
    """Fail-closed states. There is no 'best crop' state on purpose."""

    ranked_options_with_gaps = "ranked_options_with_gaps"
    informational_only = "informational_only"
    insufficient_context = "insufficient_context"
    outside_tested_scope = "outside_tested_scope"


class Sensitivity(str, Enum):
    stable = "stable"
    moderate = "moderate"
    unstable = "unstable"


# ---------------------------------------------------------------------------
# Reference data models (loaded from YAML)
# ---------------------------------------------------------------------------


class CropSeason(BaseModel):
    id: str
    name: str
    months: list[int]


class SoilProfile(BaseModel):
    textures: list[SoilTexture]
    ph_range: tuple[float, float]
    drainage: str
    ec_tolerance_ds_m: float


class Crop(BaseModel):
    id: str
    name_en: str
    local_names: dict[str, str] = Field(default_factory=dict)
    category: str
    water_need_level: int
    water_mm: tuple[int, int]
    rainfed_suitable: bool
    assured_irrigation_required: bool
    duration_days: tuple[int, int]
    seasons: list[CropSeason]
    soil: SoilProfile
    cost_level: int
    labour_level: int
    objective_scores: dict[Objective, float]
    objective_notes: dict[Objective, str] = Field(default_factory=dict)
    key_risks: list[str] = Field(default_factory=list)
    guidance_reference: str
    prevalence_namakkal: str

    @property
    def duration_mid(self) -> float:
        return sum(self.duration_days) / 2


class Catalogue(BaseModel):
    catalogue_version: str
    review_status: str
    limitation_note: str
    crops: list[Crop]

    def by_id(self, crop_id: str) -> Crop | None:
        return next((c for c in self.crops if c.id == crop_id), None)


class Block(BaseModel):
    id: str
    name: str
    office: str
    phone: str


class District(BaseModel):
    id: str
    name: str
    state: str
    agro_climatic_zones: list[str]
    normal_annual_rainfall_mm: float
    soil_summary: str
    rainfall_note: str
    source_url: str


class ReferralContact(BaseModel):
    id: str
    name: str
    office: str
    phone: str
    source_url: str
    verified_on: date


class BlockDirectory(BaseModel):
    directory_version: str
    publisher: str
    publisher_url: str
    verified_on: date
    recheck_after_days: int
    neutral_notice: str
    district: District
    blocks: list[Block]
    district_office: ReferralContact
    kvk: ReferralContact

    def block(self, block_id: str) -> Block | None:
        return next((b for b in self.blocks if b.id == block_id), None)

    def is_stale(self, today: date) -> bool:
        return (today - self.verified_on).days > self.recheck_after_days


class SourceRecord(BaseModel):
    id: str
    name: str
    publisher: str
    url: str
    kind: str
    status: SourceStatus
    status_detail: str
    farmer_facing_state: str
    note_reference: str
    locality_exclusions: list[str] = Field(default_factory=list)


class SourceRegister(BaseModel):
    register_version: str
    archive_decision_date: date
    sources: list[SourceRecord]

    def get(self, source_id: str) -> SourceRecord | None:
        return next((s for s in self.sources if s.id == source_id), None)


# ---------------------------------------------------------------------------
# Provenance
# ---------------------------------------------------------------------------


class Provenance(BaseModel):
    """The minimum attribution set every source-derived item must carry."""

    source_id: str
    source_name: str
    publisher: str
    url: str
    status: SourceStatus
    note: str


class FactorResult(BaseModel):
    """A single scoring factor, including why it was or was not used."""

    factor: str
    status: FactorStatus
    weight: float = 0.0
    contribution: float | None = None
    explanation: str
    provenance: list[Provenance] = Field(default_factory=list)


class CropOption(BaseModel):
    crop_id: str
    name_en: str
    local_name: str | None = None
    category: str
    score: float
    band: Literal["stronger_fit", "possible_fit", "weaker_fit", "reference_only"]
    factors: list[FactorResult]
    excluded_factors: list[FactorResult] = Field(default_factory=list)
    cautions: list[str] = Field(default_factory=list)
    key_risks: list[str] = Field(default_factory=list)
    duration_days: tuple[int, int]
    water_need_level: int
    seasons: list[str]
    guidance: Provenance | None = None
    rank_range: tuple[int, int] | None = None


class SensitivityEntry(BaseModel):
    crop_id: str
    rank: int
    rank_range: tuple[int, int]
    label: Sensitivity
    note: str


class ReferralEntry(BaseModel):
    trigger: str
    wording: str
    contact_name: str
    contact_detail: str
    source_url: str
    verified_on: date
    is_stale: bool
    neutral_notice: str


class InputFieldNotice(BaseModel):
    field: str
    label: str
    purpose: str
    required: bool
    consent_scope: str
    deletion: str


class DecisionPacket(BaseModel):
    decision_id: str
    created_at: datetime
    engine_version: str
    catalogue_version: str
    output_state: OutputState
    headline: str
    limitation_note: str
    farmer_context: dict[str, Any]
    factors_used: list[FactorResult]
    excluded_factors: list[FactorResult]
    options: list[CropOption]
    sensitivity: list[SensitivityEntry]
    sensitivity_note: str
    referrals: list[ReferralEntry]
    farmer_response_options: list[str]
    retention: dict[str, str]
    method_notes: list[str]


# ---------------------------------------------------------------------------
# API request / response
# ---------------------------------------------------------------------------


class DecisionRequest(BaseModel):
    consent_granted: bool = Field(
        ...,
        description="Purpose-specific consent for this decision record. Required.",
    )
    language: Literal["en", "ta"] = "en"
    block_id: str = Field(..., description="Namakkal district block id")
    village: str | None = Field(
        default=None,
        max_length=120,
        description="Free-text village or hamlet the farmer states. Not treated as a plot location.",
    )
    crop_stage: Literal["pre_sowing", "sowing", "early_establishment"] = "pre_sowing"
    intended_sowing_window: Literal[
        "jun_jul", "aug_sep", "oct_nov", "dec_jan", "feb_mar", "apr_may"
    ]
    water_availability: WaterAvailability
    objective: list[Objective] = Field(
        ..., min_length=1, description="At least one stated objective is required"
    )
    land_area_ha: float | None = Field(default=None, gt=0, le=50)
    soil_texture: SoilTexture | None = None
    soil_ph: float | None = Field(default=None, ge=3.0, le=10.0)
    soil_test_available: bool = False
    soil_test_date: date | None = None
    labour_available: Literal["plenty", "limited", "scarce", "unknown"] = "unknown"
    exclude_crops: list[str] = Field(default_factory=list)


class ConsentNotice(BaseModel):
    purpose: str
    scope: str
    retention: str
    deletion: str
    fields: list[InputFieldNotice]


class MetaResponse(BaseModel):
    engine_version: str
    catalogue_version: str
    directory_version: str
    register_version: str
    district: District
    blocks: list[Block]
    crops: list[dict]
    objectives: list[dict]
    water_options: list[dict]
    seasons: list[dict]
    source_register: list[SourceRecord]
    consent_notice: ConsentNotice
    weather_gate: dict
    limitations: list[str]


class DeleteResponse(BaseModel):
    decision_id: str
    deleted: bool
    message: str
