"""The weather gate.

The archive's operational test memo (EF-DAT-007) concluded that no external
weather or advisory source passed P0 approval: the TNAU district bulletin does
not carry Namakkal, and IMD/Agmarknet access is unestablished or untested.

This module therefore does not fetch or estimate weather. It reports, with
attribution, that weather is unavailable for this decision and why. The crop
engine is then required to show that gap rather than compensate for it.
"""

from __future__ import annotations

from datetime import date

from app.domain.models import Provenance, SourceStatus
from app.engine.registry import directory, source_register


def assess(target_block: str, today: date | None = None) -> dict:
    today = today or date.today()
    register = source_register()
    district = directory().district

    candidates = []
    for source_id in ("tnau_agromet_district", "imd_api"):
        record = register.get(source_id)
        if record is None:
            continue

        locality_blocked = (
            record.status is SourceStatus.rejected_locality
            and district.name in record.locality_exclusions
        )

        candidates.append(
            {
                "source_id": record.id,
                "source_name": record.name,
                "publisher": record.publisher,
                "url": record.url,
                "status": record.status.value,
                "status_detail": record.status_detail,
                "blocked_for_namakkal": bool(locality_blocked),
                "target_block": target_block,
                "checked_on": today.isoformat(),
            }
        )

    return {
        "weather_available": False,
        "state": "not_available_for_your_area",
        "headline": "No current, location-matched weather advisory is available to EcoFarm.",
        "detail": (
            "EcoFarm is not using an older bulletin, a neighbouring district, a "
            "statewide average, a generic weather provider, or a climate normal as "
            "if it were current weather. Crop ranking below is therefore built "
            "without any weather factor."
        ),
        "candidates": candidates,
        "consequence_for_engine": (
            "Weather_advisory is reported as excluded_no_approved_source on every "
            "option. Rainfall-timing claims are not made in this packet."
        ),
    }


def provenance() -> Provenance:
    record = source_register().get("tnau_agromet_district")
    assert record is not None
    return Provenance(
        source_id=record.id,
        source_name=record.name,
        publisher=record.publisher,
        url=record.url,
        status=record.status,
        note=record.status_detail,
    )
