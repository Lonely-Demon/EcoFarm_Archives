"""Assembles the decision packet.

The packet is the product. It carries the farmer's stated context, the factors
that were used, the factors that were dropped and why, banded options with
sensitivity ranges, and a referral path. There is no "best crop" field, by
design.
"""

from __future__ import annotations

import uuid
from datetime import date, datetime, timedelta, timezone

from app.domain.models import (
    DecisionPacket,
    DecisionRequest,
    FactorResult,
    InputFieldNotice,
    Objective,
    OutputState,
    ReferralEntry,
    SensitivityEntry,
    WaterAvailability,
)
from app.engine import weather_gate
from app.engine.registry import ENGINE_VERSION, catalogue, directory
from app.engine.scoring import build_options, FACTOR_LABELS

RETENTION_DAYS = 90

OBJECTIVE_LABELS = {
    Objective.water_conservation: "Use less water",
    Objective.lower_input_cost: "Keep input cost low",
    Objective.timing_flexibility: "Fit a tight calendar",
    Objective.household_food: "Household food",
    Objective.market_sale: "Sell produce",
    Objective.risk_reduction: "Reduce risk of failure",
    Objective.fodder: "Fodder for livestock",
}

FIELD_NOTICES = [
    InputFieldNotice(
        field="block_id",
        label="Block",
        purpose="Confirms this decision is inside the tested Namakkal scope.",
        required=True,
        consent_scope="Stored with this decision record only.",
        deletion="Removed when you delete this decision record.",
    ),
    InputFieldNotice(
        field="village",
        label="Village (optional)",
        purpose="Keeps the record readable for you. It is not treated as a plot location.",
        required=False,
        consent_scope="Stored with this decision record only.",
        deletion="Removed when you delete this decision record.",
    ),
    InputFieldNotice(
        field="intended_sowing_window",
        label="Sowing window",
        purpose="Checks whether the crop's listed sowing season matches your plan.",
        required=True,
        consent_scope="Stored with this decision record only.",
        deletion="Removed when you delete this decision record.",
    ),
    InputFieldNotice(
        field="water_availability",
        label="Water situation",
        purpose="Compares your stated water constraint against each crop's water demand.",
        required=True,
        consent_scope="Stored with this decision record only.",
        deletion="Removed when you delete this decision record.",
    ),
    InputFieldNotice(
        field="objective",
        label="What matters to you",
        purpose="Explains trade-offs against your own goals. Never used to promise income.",
        required=True,
        consent_scope="Stored with this decision record only.",
        deletion="Removed when you delete this decision record.",
    ),
    InputFieldNotice(
        field="soil_texture / soil_ph",
        label="Soil texture and pH (optional)",
        purpose="Narrows soil fit. If you leave this blank, soil is dropped as a factor.",
        required=False,
        consent_scope="Stored with this decision record only.",
        deletion="Removed when you delete this decision record.",
    ),
    InputFieldNotice(
        field="land_area_ha",
        label="Area in hectares (optional)",
        purpose="Context only. Never used to predict cost, income or yield.",
        required=False,
        consent_scope="Stored with this decision record only.",
        deletion="Removed when you delete this decision record.",
    ),
]


def _state_for(request: DecisionRequest, options) -> OutputState:
    if not options:
        return OutputState.insufficient_context
    if request.water_availability is WaterAvailability.unknown:
        return OutputState.informational_only
    return OutputState.ranked_options_with_gaps


def _headline(state: OutputState, count: int) -> str:
    if state is OutputState.informational_only:
        return (
            "Reference list of crops grown in Namakkal. This is not a comparison: "
            "you have not told EcoFarm your water situation, so the engine will not "
            "rank options for your farm."
        )
    if state is OutputState.insufficient_context:
        return (
            "No crop in the pilot catalogue matches the constraints you gave. "
            "EcoFarm cannot produce a comparison from this set of inputs."
        )
    return (
        f"{count} crop options scored on the factors EcoFarm can support today. "
        "Weather and market factors are missing and are shown as missing."
    )


def _referrals(request: DecisionRequest, weather: dict) -> list[ReferralEntry]:
    d = directory()
    today = date.today()
    stale = d.is_stale(today)
    block = d.block(request.block_id)
    entries: list[ReferralEntry] = []

    entries.append(
        ReferralEntry(
            trigger="critical_source_missing",
            wording=(
                "No current, location-matched weather or advisory information is "
                "available for this decision. Please check the latest official "
                "agriculture or weather service before acting."
            ),
            contact_name=block.name + " Agricultural Extension Centre" if block else d.district_office.name,
            contact_detail=(block.office + " — phone " + block.phone) if block else d.district_office.office,
            source_url=d.publisher_url,
            verified_on=d.verified_on,
            is_stale=stale,
            neutral_notice=d.neutral_notice,
        )
    )

    entries.append(
        ReferralEntry(
            trigger="outside_tested_scope",
            wording=(
                "EcoFarm's pilot covers sowing and early-establishment decisions for "
                "Namakkal blocks only. It does not provide pest diagnosis, pesticide "
                "advice, price forecasts or buyer guarantees. For those questions, "
                "consult a qualified local agriculture adviser and follow product labels."
            ),
            contact_name=d.kvk.name,
            contact_detail=d.kvk.office + " — phone " + d.kvk.phone,
            source_url=d.kvk.source_url,
            verified_on=d.kvk.verified_on,
            is_stale=stale,
            neutral_notice=d.neutral_notice,
        )
    )

    if request.water_availability is WaterAvailability.unknown:
        entries.append(
            ReferralEntry(
                trigger="missing_water_evidence",
                wording=(
                    "You have not stated your water situation, so EcoFarm is not "
                    "comparing options. A local adviser can help you establish your "
                    "water position before choosing a crop."
                ),
                contact_name=d.district_office.name,
                contact_detail=d.district_office.office + " — phone " + d.district_office.phone,
                source_url=d.publisher_url,
                verified_on=d.verified_on,
                is_stale=stale,
                neutral_notice=d.neutral_notice,
            )
        )

    return entries


def _farmer_context(request: DecisionRequest) -> dict:
    d = directory()
    block = d.block(request.block_id)
    return {
        "block": block.name if block else request.block_id,
        "block_id": request.block_id,
        "village": request.village or None,
        "crop_stage": request.crop_stage,
        "intended_sowing_window": request.intended_sowing_window,
        "water_availability": request.water_availability.value,
        "objectives": [OBJECTIVE_LABELS[o] for o in request.objective],
        "soil_texture": request.soil_texture.value if request.soil_texture else None,
        "soil_ph": request.soil_ph,
        "land_area_ha": request.land_area_ha,
        "labour_available": request.labour_available,
        "language": request.language,
    }


def build_packet(request: DecisionRequest, decision_id: str | None = None) -> DecisionPacket:
    decision_id = decision_id or str(uuid.uuid4())
    now = datetime.now(timezone.utc)

    options, sensitivity_entries, excluded, coverage, top_spread = build_options(request)
    state = _state_for(request, options)
    weather = weather_gate.assess(request.block_id)

    cat = catalogue()

    if request.soil_test_available and request.soil_test_date is None:
        method_notes_extra = [
            "You indicated a soil test exists but gave no test date. The soil record is "
            "treated as unverified: any soil values you entered are used only as you "
            "reported them, and no staleness check was possible."
        ]
    else:
        method_notes_extra = []

    method_notes = [
        f"Scores combine {len([f for f in FACTOR_LABELS if f in {x.factor for x in options[0].factors}])} "
        f"usable factors at {round(coverage * 100)}% of the intended factor weight."
        if options
        else "No usable factors were available to score.",
        "Weather and advisory information is excluded because no source has passed the pilot's "
        "Namakkal locality and rights tests. The engine does not estimate rainfall.",
        "Observed market prices are excluded: no commodity, market, variety, grade and unit "
        "semantic test has been completed.",
        "Pest and disease risk, yield, cost of cultivation and income are not modelled at all.",
        (
            "This packet is a reference list, not a comparison. No band and no ordering "
            "is presented because the water constraint you would need to compare against "
            "was not stated."
            if state is OutputState.informational_only
            else "Scores are cut into bands only where options differ by at least 0.06. "
            "Ordering within a band is not meaningful and is not presented as a ranking."
        ),
        "Each option carries a rank range from a 240-draw weight-perturbation test, so a small "
        "score difference cannot be read as a reliable ordering.",
        (
            f"The top three options differ by only {round(top_spread, 2)} points, which is below "
            "the separation threshold. They are presented as one group, not as first, second and third."
            if top_spread < 0.12
            else f"The leading option is {round(top_spread, 2)} points ahead of the third option."
        ),
        "Thresholds are working defaults under review; they are not TNAU recommendations and are "
        "not calibrated to your soil series or plot.",
        *method_notes_extra,
    ]


    return DecisionPacket(
        decision_id=decision_id,
        created_at=now,
        engine_version=ENGINE_VERSION,
        catalogue_version=cat.catalogue_version,
        output_state=state,
        headline=_headline(state, len(options)),
        limitation_note=(
            "This packet is decision support from a pilot. It is not a TNAU "
            "recommendation, not a guarantee, and not a substitute for a local "
            "agriculture adviser. It does not predict price, profit or yield."
        ),
        farmer_context=_farmer_context(request),
        factors_used=[f for f in options[0].factors] if options else [],
        excluded_factors=excluded,
        options=options,
        sensitivity=sensitivity_entries,
        sensitivity_note=(
            "Rank ranges come from re-running the comparison with randomly perturbed "
            "factor weights. Overlapping ranges mean the ordering is not evidence of a "
            "real difference between those crops."
        ),
        referrals=_referrals(request, weather),
        farmer_response_options=[
            "accepted",
            "rejected",
            "changed_mind",
            "need_more_information",
        ],
        retention={
            "days": str(RETENTION_DAYS),
            "expires_at": (now + timedelta(days=RETENTION_DAYS)).isoformat(),
            "deletion": "Use Delete this decision record in the packet, or the support route, to remove it earlier.",
            "note": "Non-personal source audit records may be kept separately for integrity review.",
        },
        method_notes=method_notes,
    )
