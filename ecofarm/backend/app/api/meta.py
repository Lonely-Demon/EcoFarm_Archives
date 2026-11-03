"""Metadata endpoints.

The frontend renders consent wording, limitations, the source register and the
weather gate from here so that governance text has exactly one home: the
backend, not the UI.
"""

from __future__ import annotations

from fastapi import APIRouter

from app.domain.models import ConsentNotice, MetaResponse, Objective, WaterAvailability
from app.engine import weather_gate
from app.engine.packet import FIELD_NOTICES, OBJECTIVE_LABELS
from app.engine.registry import ENGINE_VERSION, catalogue, directory, source_register
from app.engine.scoring import FACTOR_LABELS, SEASON_MONTHS

router = APIRouter(prefix="/api/v1", tags=["meta"])

WATER_DESCRIPTIONS = {
    WaterAvailability.reliable: "Irrigation is available when you need it.",
    WaterAvailability.seasonal: "Water is available for part of the season.",
    WaterAvailability.rainfed: "No irrigation; the crop depends on rainfall.",
    WaterAvailability.uncertain: "You are not sure water will be there when needed.",
    WaterAvailability.unknown: "You would rather not say yet.",
}

SEASON_LABELS = {
    "jun_jul": "June - July",
    "aug_sep": "August - September",
    "oct_nov": "October - November",
    "dec_jan": "December - January",
    "feb_mar": "February - March",
    "apr_may": "April - May",
}


@router.get("/meta", response_model=MetaResponse)
def meta() -> MetaResponse:
    cat = catalogue()
    d = directory()
    register = source_register()

    return MetaResponse(
        engine_version=ENGINE_VERSION,
        catalogue_version=cat.catalogue_version,
        directory_version=d.directory_version,
        register_version=register.register_version,
        district=d.district,
        blocks=d.blocks,
        crops=[
            {
                "id": c.id,
                "name_en": c.name_en,
                "local_names": c.local_names,
                "category": c.category,
                "duration_days": list(c.duration_days),
                "water_need_level": c.water_need_level,
                "rainfed_suitable": c.rainfed_suitable,
                "assured_irrigation_required": c.assured_irrigation_required,
                "prevalence_namakkal": c.prevalence_namakkal,
            }
            for c in cat.crops
        ],
        objectives=[
            {"id": o.value, "label": OBJECTIVE_LABELS[o]} for o in Objective
        ],
        water_options=[
            {"id": w.value, "label": w.value.replace("_", " ").title(), "description": WATER_DESCRIPTIONS[w]}
            for w in WaterAvailability
        ],
        seasons=[
            {"id": key, "label": SEASON_LABELS[key], "months": months}
            for key, months in ((s.value, SEASON_MONTHS[s]) for s in SEASON_MONTHS)
        ],
        source_register=register.sources,
        consent_notice=ConsentNotice(
            purpose=(
                "To produce one sowing or early-establishment decision comparison for "
                "your block, and to keep a record you can inspect or delete."
            ),
            scope=(
                "Your answers are used only for this decision. Soil values are optional "
                "and are excluded entirely if you do not give them."
            ),
            retention="90 days from creation, unless you delete the record sooner.",
            deletion=(
                "Deleting the record removes your answers. Non-personal source audit "
                "entries, which contain no farmer context, may be kept for integrity review."
            ),
            fields=FIELD_NOTICES,
        ),
        weather_gate=weather_gate.assess("namakkal"),
        limitations=[
            "No weather or advisory source is approved for Namakkal, so no weather factor is scored.",
            "Observed market prices are excluded from the pilot.",
            "Pest and disease risk, yield, cost of cultivation and income are not modelled.",
            "Crop thresholds are working defaults, not TNAU recommendations, and await agronomist review.",
            "Pilot scope is Namakkal district blocks only.",
            "There is no best-crop answer, and no price or profit prediction.",
        ],
    )


@router.get("/method")
def method() -> dict:
    return {
        "engine_version": ENGINE_VERSION,
        "catalogue_version": catalogue().catalogue_version,
        "factors": [
            {
                "id": key,
                "label": label,
                "kind": "scored"
                if key
                in {
                    "water_fit",
                    "season_fit",
                    "soil_fit",
                    "objective_fit",
                    "duration_fit",
                    "local_relevance",
                }
                else "excluded",
            }
            for key, label in FACTOR_LABELS.items()
        ],
        "steps": [
            "Validate scope: block must be a Namakkal block, consent must be granted.",
            "Drop any factor whose input is missing or whose source is not approved.",
            "Score the remaining factors and normalise by the weight actually used.",
            "Apply hard constraints, for example assured-irrigation crops under rainfed water.",
            "Place crops into bands rather than a numbered ranking.",
            "Re-run the comparison 240 times with perturbed weights to produce a rank range.",
            "Attach provenance and referrals, then store the record for 90 days.",
        ],
        "sensitivity": {
            "draws": 240,
            "seed": 20260813,
            "weight_perturbation": "lognormal, sigma 0.40, renormalised per draw",
        },
    }


@router.get("/sources")
def sources() -> dict:
    register = source_register()
    return {
        "register_version": register.register_version,
        "archive_decision_date": register.archive_decision_date.isoformat(),
        "sources": [s.model_dump(mode="json") for s in register.sources],
    }


@router.get("/health")
def health() -> dict:
    return {"status": "ok", "engine_version": ENGINE_VERSION}
