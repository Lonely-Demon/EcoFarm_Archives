"""Crop suitability scoring.

Design rules taken from the archive and enforced here:

1. No factor is scored from a source that has not passed P0 approval. Weather,
   market price and pest/disease therefore appear as *excluded* factors on every
   option rather than as quiet defaults.
2. Missing farmer input lowers weight coverage; it never gets replaced by a
   district average or a guess.
3. Scores are shown as bands. Ranks are accompanied by a sensitivity range so a
   difference of 0.02 cannot be read as a real ordering.
4. Nothing here produces the words "best", "recommended for profit", or a
   yield or income number.
"""

from __future__ import annotations

import random
from dataclasses import dataclass

from app.domain.models import (
    Crop,
    CropOption,
    DecisionRequest,
    FactorResult,
    FactorStatus,
    Objective,
    Season,
    SensitivityEntry,
    Sensitivity,
    SoilTexture,
    WaterAvailability,
)
from app.engine.registry import (
    catalogue,
    provenance_for,
)

# ---------------------------------------------------------------------------
# Weights
# ---------------------------------------------------------------------------

BASE_WEIGHTS: dict[str, float] = {
    "water_fit": 0.28,
    "season_fit": 0.20,
    "soil_fit": 0.18,
    "objective_fit": 0.22,
    "duration_fit": 0.07,
    "local_relevance": 0.05,
}

FACTOR_LABELS: dict[str, str] = {
    "water_fit": "Water availability fit",
    "season_fit": "Sowing-window fit",
    "soil_fit": "Soil fit",
    "objective_fit": "Your stated objectives",
    "duration_fit": "Crop duration",
    "local_relevance": "Presence in Namakkal cropping",
    "weather_advisory": "Weather and advisory",
    "market_price": "Observed market price",
    "pest_disease": "Pest and disease risk",
}

SEASON_MONTHS: dict[Season, list[int]] = {
    Season.jun_jul: [6, 7],
    Season.aug_sep: [8, 9],
    Season.oct_nov: [10, 11],
    Season.dec_jan: [12, 1],
    Season.feb_mar: [2, 3],
    Season.apr_may: [4, 5],
}

WATER_CAPACITY: dict[WaterAvailability, int | None] = {
    WaterAvailability.reliable: 5,
    WaterAvailability.seasonal: 3,
    WaterAvailability.rainfed: 1,
    WaterAvailability.uncertain: 2,
    WaterAvailability.unknown: None,
}

PREVALENCE_SCORE = {"major": 1.0, "notable": 0.6}


def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


# ---------------------------------------------------------------------------
# Individual factors
# ---------------------------------------------------------------------------


def score_water(crop: Crop, request: DecisionRequest) -> FactorResult:
    capacity = WATER_CAPACITY[request.water_availability]
    if capacity is None:
        return FactorResult(
            factor="water_fit",
            status=FactorStatus.excluded_missing_input,
            explanation=(
                "You did not state your water situation, so water fit is left out "
                "rather than assumed. Rainfall is not substituted for this."
            ),
        )

    need = crop.water_need_level
    gap = max(0, need - capacity)
    score = _clamp(1.0 - 0.22 * gap)
    notes: list[str] = []

    if gap == 0:
        notes.append(
            f"Crop water demand level {need} is within your stated "
            f"'{request.water_availability.value}' availability."
        )
    else:
        notes.append(
            f"Crop water demand level {need} exceeds your stated "
            f"'{request.water_availability.value}' availability by {gap} level(s)."
        )

    if crop.assured_irrigation_required and capacity < 3:
        score = min(score, 0.15)
        notes.append(
            "This crop requires assured irrigation, which your stated water "
            "situation does not provide."
        )

    if crop.rainfed_suitable and capacity == 1:
        score = _clamp(score + 0.10)
        notes.append("This crop is listed as suitable for rainfed cultivation.")

    return FactorResult(
        factor="water_fit",
        status=FactorStatus.used,
        weight=BASE_WEIGHTS["water_fit"],
        contribution=round(score, 3),
        explanation=" ".join(notes),
        provenance=[
            p for p in [provenance_for("farmer_input"), provenance_for("ecofarm_working_thresholds")] if p
        ],
    )


def score_season(crop: Crop, request: DecisionRequest) -> FactorResult:
    target = SEASON_MONTHS[Season(request.intended_sowing_window)]
    crop_months = {month for season in crop.seasons for month in season.months}

    if set(target) & crop_months:
        score, note = 1.0, "The crop is sown in your intended window."
    elif any(abs(t - m) == 1 for t in target for m in crop_months):
        score, note = 0.6, "Your window is adjacent to a listed sowing window for this crop."
    else:
        score, note = 0.2, "Your window falls outside the listed sowing windows for this crop."

    return FactorResult(
        factor="season_fit",
        status=FactorStatus.used,
        weight=BASE_WEIGHTS["season_fit"],
        contribution=round(score, 3),
        explanation=note,
        provenance=[p for p in [provenance_for("ecofarm_working_thresholds")] if p],
    )


def score_soil(crop: Crop, request: DecisionRequest) -> FactorResult:
    if request.soil_texture is None and request.soil_ph is None:
        return FactorResult(
            factor="soil_fit",
            status=FactorStatus.excluded_missing_input,
            explanation=(
                "No soil texture or pH was given. EcoFarm does not substitute a "
                "district-average soil value for your plot."
            ),
        )

    parts: list[float] = []
    notes: list[str] = []

    if request.soil_texture is not None:
        if request.soil_texture in crop.soil.textures:
            parts.append(1.0)
            notes.append(f"{request.soil_texture.value} soil is in this crop's suited textures.")
        else:
            parts.append(0.35)
            notes.append(
                f"{request.soil_texture.value} soil is not in this crop's suited "
                f"textures ({', '.join(t.value for t in crop.soil.textures)})."
            )

    if request.soil_ph is not None:
        low, high = crop.soil.ph_range
        if low <= request.soil_ph <= high:
            parts.append(1.0)
            notes.append(f"pH {request.soil_ph} is inside this crop's range {low}-{high}.")
        else:
            distance = low - request.soil_ph if request.soil_ph < low else request.soil_ph - high
            if distance <= 0.5:
                parts.append(0.7)
            elif distance <= 1.0:
                parts.append(0.4)
            else:
                parts.append(0.15)
            notes.append(f"pH {request.soil_ph} is outside this crop's range {low}-{high}.")

    score = sum(parts) / len(parts)

    if request.soil_test_available and request.soil_test_date is None:
        notes.append("You indicated a soil test exists but gave no test date, so its age is unverified.")

    return FactorResult(
        factor="soil_fit",
        status=FactorStatus.used,
        weight=BASE_WEIGHTS["soil_fit"],
        contribution=round(score, 3),
        explanation=" ".join(notes),
        provenance=[p for p in [provenance_for("farmer_input"), provenance_for("ecofarm_working_thresholds")] if p],
    )


def score_objective(crop: Crop, request: DecisionRequest) -> FactorResult:
    values = [crop.objective_scores[obj] for obj in request.objective]
    score = sum(values) / len(values)

    notes = [f"Scored against {len(request.objective)} stated objective(s)."]
    for obj in request.objective:
        if obj in crop.objective_notes:
            notes.append(crop.objective_notes[obj])

    notes.append("This is a stated-preference fit. It is not an income or profit expectation.")

    return FactorResult(
        factor="objective_fit",
        status=FactorStatus.used,
        weight=BASE_WEIGHTS["objective_fit"],
        contribution=round(score, 3),
        explanation=" ".join(notes),
        provenance=[p for p in [provenance_for("farmer_input"), provenance_for("ecofarm_working_thresholds")] if p],
    )


def score_duration(crop: Crop, request: DecisionRequest) -> FactorResult:
    mid = crop.duration_mid

    if Objective.timing_flexibility in request.objective:
        score = _clamp(1.0 - (mid - 90) / 400, 0.15, 1.0)
        note = (
            f"About {int(mid)} days to harvest; shorter duration scores higher "
            "because you said timing flexibility matters."
        )
    else:
        score = 1.0 if mid <= 160 else 0.45
        note = f"About {int(mid)} days to harvest."

    if request.crop_stage in {"sowing", "early_establishment"} and mid > 200:
        score = min(score, 0.3)
        note += " Long duration is a weak fit when you are already at or after sowing."

    return FactorResult(
        factor="duration_fit",
        status=FactorStatus.used,
        weight=BASE_WEIGHTS["duration_fit"],
        contribution=round(score, 3),
        explanation=note,
        provenance=[p for p in [provenance_for("ecofarm_working_thresholds")] if p],
    )


def score_local_relevance(crop: Crop) -> FactorResult:
    score = PREVALENCE_SCORE.get(crop.prevalence_namakkal, 0.3)
    note = {
        "major": "Listed by the district agriculture department as a major Namakkal crop.",
        "notable": "Grown in the district but not listed among its major crops.",
    }.get(crop.prevalence_namakkal, "Local prevalence not established.")

    return FactorResult(
        factor="local_relevance",
        status=FactorStatus.used,
        weight=BASE_WEIGHTS["local_relevance"],
        contribution=round(score, 3),
        explanation=note,
        provenance=[p for p in [provenance_for("namakkal_agri_directory")] if p],
    )


# ---------------------------------------------------------------------------
# Excluded factors (always reported, never silently dropped)
# ---------------------------------------------------------------------------


def excluded_factors_for(request: DecisionRequest) -> list[FactorResult]:
    weather_prov = provenance_for("tnau_agromet_district")
    imd_prov = provenance_for("imd_api")
    market_prov = provenance_for("agmarknet_market")
    guide_prov = provenance_for("tnau_crop_production_guide")

    return [
        FactorResult(
            factor="weather_advisory",
            status=FactorStatus.excluded_no_approved_source,
            explanation=(
                "No weather or advisory source has passed the pilot's approval "
                "tests for Namakkal. Rainfall timing, dry-spell risk and sowing "
                "rain this week are therefore not scored."
            ),
            provenance=[p for p in [weather_prov, imd_prov] if p],
        ),
        FactorResult(
            factor="market_price",
            status=FactorStatus.excluded_out_of_scope,
            explanation=(
                "Observed mandi prices are outside the tested scope: no crop, "
                "market, variety, grade or unit semantic test has been completed. "
                "No price, price trend or buyer assurance is shown."
            ),
            provenance=[p for p in [market_prov] if p],
        ),
        FactorResult(
            factor="pest_disease",
            status=FactorStatus.excluded_out_of_scope,
            explanation=(
                "Pest and disease pressure is not scored. EcoFarm does not "
                "diagnose plant problems or prescribe treatment."
            ),
            provenance=[p for p in [guide_prov] if p],
        ),
    ]


# ---------------------------------------------------------------------------
# Weighted combination
# ---------------------------------------------------------------------------


@dataclass
class ScoredCrop:
    crop: Crop
    raw_score: float
    used_factors: list[FactorResult]
    excluded: list[FactorResult]
    weight_coverage: float
    cautions: list[str]


def _combine(factors: list[FactorResult], weights: dict[str, float]) -> tuple[float, float]:
    """Return (weighted score normalised to used weight, coverage of total weight)."""
    used = [f for f in factors if f.status is FactorStatus.used and f.contribution is not None]
    used_weight = sum(weights[f.factor] for f in used)
    if used_weight <= 0:
        return 0.0, 0.0
    score = sum(weights[f.factor] * f.contribution for f in used) / used_weight
    return score, used_weight / sum(weights.values())


def score_crop(crop: Crop, request: DecisionRequest, weights: dict[str, float] | None = None) -> ScoredCrop:
    weights = weights or BASE_WEIGHTS
    used = [
        score_water(crop, request),
        score_season(crop, request),
        score_soil(crop, request),
        score_objective(crop, request),
        score_duration(crop, request),
        score_local_relevance(crop),
    ]
    raw, coverage = _combine(used, weights)

    cautions: list[str] = []
    capacity = WATER_CAPACITY[request.water_availability]
    if crop.assured_irrigation_required and (capacity is not None and capacity < 3):
        cautions.append(
            "Hard constraint: this crop needs assured irrigation and your stated "
            "water situation does not provide it."
        )
        raw = min(raw, 0.25)
    if request.water_availability in {WaterAvailability.unknown}:
        cautions.append(
            "Water situation unknown, so several options may be overstated for your farm."
        )

    return ScoredCrop(
        crop=crop,
        raw_score=raw,
        used_factors=used,
        excluded=excluded_factors_for(request),
        weight_coverage=coverage,
        cautions=cautions,
    )


# ---------------------------------------------------------------------------
# Bands and sensitivity
# ---------------------------------------------------------------------------


MIN_SEPARATION = 0.06
"""Scores must differ by at least this much to count as a separate band.

Crop suitability scores are compressed by construction: most viable crops for a
Namakkal block score between 0.4 and 1.0 because they share the same soil and
season. An absolute threshold would therefore put almost everything in one band
and let a 0.01 difference look like a ranking. Bands are cut on gaps instead.
"""


def assign_bands(scores: list[tuple[str, float]]) -> tuple[dict[str, str], float]:
    """Assign bands by gap detection over descending scores.

    Returns the band per crop id and the score spread between the top option and
    the third option, which the UI uses to state whether the ordering is
    meaningful at all.
    """
    ordered = sorted(scores, key=lambda item: item[1], reverse=True)
    if not ordered:
        return {}, 0.0

    bands: dict[str, str] = {}
    band_index = 0
    anchor = ordered[0][1]

    for _, (crop_id, score) in enumerate(ordered):
        if anchor - score >= MIN_SEPARATION:
            band_index = min(band_index + 1, 2)
            anchor = score
        bands[crop_id] = ("stronger_fit", "possible_fit", "weaker_fit")[band_index]

    third = ordered[min(2, len(ordered) - 1)][1]
    spread = ordered[0][1] - third
    return bands, round(spread, 3)


def _perturbed_weights(rng: random.Random) -> dict[str, float]:
    raw = {f: BASE_WEIGHTS[f] * rng.lognormvariate(0, 0.40) for f in BASE_WEIGHTS}
    total = sum(raw.values())
    return {f: w / total for f, w in raw.items()}


def sensitivity(
    crops: list[Crop],
    request: DecisionRequest,
    draws: int = 240,
    seed: int = 20260813,
) -> tuple[list[SensitivityEntry], dict[str, tuple[int, int]]]:
    """Rank each crop under perturbed factor weights.

    Returns per-crop entries plus a rank-range map used to annotate options. The
    seed is fixed so a given decision always reproduces the same ranges.
    """
    rng = random.Random(seed)
    ranks: dict[str, list[int]] = {c.id: [] for c in crops}

    for _ in range(draws):
        weights = _perturbed_weights(rng)
        scored = sorted(
            ((score_crop(c, request, weights).raw_score, c.id) for c in crops),
            key=lambda item: item[0],
            reverse=True,
        )
        for position, (_, crop_id) in enumerate(scored, start=1):
            ranks[crop_id].append(position)

    base_order = sorted(
        ((score_crop(c, request).raw_score, c.id) for c in crops),
        key=lambda item: item[0],
        reverse=True,
    )

    entries: list[SensitivityEntry] = []
    ranges: dict[str, tuple[int, int]] = {}

    for base_rank, (_, crop_id) in enumerate(base_order, start=1):
        observed = sorted(ranks[crop_id])
        low = observed[int(len(observed) * 0.10)]
        high = observed[int(len(observed) * 0.90) - 1]
        low, high = min(low, base_rank), max(high, base_rank)
        width = high - low

        if width <= 1:
            label = Sensitivity.stable
            note = "Holds this position across weight variations."
        elif width <= 4:
            label = Sensitivity.moderate
            note = f"Could sit anywhere from position {low} to {high} depending on factor weighting."
        else:
            label = Sensitivity.unstable
            note = (
                f"Position is not reliable: it ranges from {low} to {high}. "
                "Treat this as one option among many, not a ranking."
            )

        ranges[crop_id] = (low, high)
        entries.append(
            SensitivityEntry(
                crop_id=crop_id,
                rank=base_rank,
                rank_range=(low, high),
                label=label,
                note=note,
            )
        )

    return entries, ranges


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------


def build_options(
    request: DecisionRequest,
) -> tuple[list[CropOption], list[SensitivityEntry], list[FactorResult], float, float]:
    cat = catalogue()
    pool = [
        c
        for c in cat.crops
        if c.id not in set(request.exclude_crops)
    ]

    scored = [score_crop(c, request) for c in pool]
    scored.sort(key=lambda s: s.raw_score, reverse=True)

    reference_mode = request.water_availability is WaterAvailability.unknown
    if reference_mode:
        # No comparison may be presented when a required constraint is missing.
        bands = {s.crop.id: "reference_only" for s in scored}
        top_spread = 0.0
    else:
        bands, top_spread = assign_bands([(s.crop.id, s.raw_score) for s in scored])

    sens_entries, ranges = sensitivity(pool, request)
    sens_by_id = {e.crop_id: e for e in sens_entries}

    options: list[CropOption] = []
    for item in scored:
        entry = sens_by_id[item.crop.id]
        guidance = provenance_for(item.crop.guidance_reference)
        options.append(
            CropOption(
                crop_id=item.crop.id,
                name_en=item.crop.name_en,
                local_name=item.crop.local_names.get(request.language),
                category=item.crop.category,
                score=round(item.raw_score, 2),
                band=bands.get(item.crop.id, "weaker_fit"),
                factors=item.used_factors,
                excluded_factors=item.excluded,
                cautions=item.cautions,
                key_risks=item.crop.key_risks,
                duration_days=item.crop.duration_days,
                water_need_level=item.crop.water_need_level,
                seasons=[s.name for s in item.crop.seasons],
                guidance=guidance,
                rank_range=None if reference_mode else entry.rank_range,
            )
        )

    coverage = scored[0].weight_coverage if scored else 0.0
    return options, sens_entries, excluded_factors_for(request), coverage, top_spread
