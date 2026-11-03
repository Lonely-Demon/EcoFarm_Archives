"""Engine and API tests.

These tests encode the archive's non-negotiables rather than the UI's taste.
If one fails, the product has started claiming more than the evidence allows.
"""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from app.core.config import settings
from app.engine.registry import source_register
from app.engine.scoring import MIN_SEPARATION
from app.main import app
from app.domain.models import SourceStatus


@pytest.fixture()
def client(tmp_path, monkeypatch):
    from app.api import decisions

    monkeypatch.setattr(settings(), "database_path", str(tmp_path / "test.db"), raising=False)
    decisions._store = None
    with TestClient(app) as c:
        yield c
    decisions._store = None


BASE = {
    "consent_granted": True,
    "language": "en",
    "block_id": "paramathi_velur",
    "crop_stage": "pre_sowing",
    "intended_sowing_window": "jun_jul",
    "water_availability": "rainfed",
    "objective": ["water_conservation", "risk_reduction"],
    "soil_texture": "red",
    "soil_ph": 7.2,
}


def create(client, **overrides):
    response = client.post("/api/v1/decisions", json={**BASE, **overrides})
    return response


# ---------------------------------------------------------------------------
# Governance gates
# ---------------------------------------------------------------------------


def test_consent_is_required(client):
    response = create(client, consent_granted=False)
    assert response.status_code == 403
    assert response.json()["detail"]["state"] == "consent_required"


def test_out_of_scope_block_fails_closed(client):
    response = create(client, block_id="coimbatore")
    assert response.status_code == 422
    detail = response.json()["detail"]
    assert detail["state"] == "outside_tested_scope"
    assert "paramathi_velur" in detail["allowed_blocks"]


def test_no_weather_source_is_approved():
    """The engine may not quietly start trusting a weather feed."""
    approved = [
        s.id
        for s in source_register().sources
        if s.status is SourceStatus.approved and s.kind in {"weather", "weather_advisory"}
    ]
    assert approved == []


def test_weather_is_reported_as_excluded_on_every_option(client):
    packet = create(client).json()
    assert packet["output_state"] == "ranked_options_with_gaps"
    excluded_ids = {f["factor"] for f in packet["excluded_factors"]}
    assert {"weather_advisory", "market_price", "pest_disease"} <= excluded_ids

    for option in packet["options"]:
        used = {f["factor"] for f in option["factors"]}
        dropped = {f["factor"] for f in option["excluded_factors"]}
        assert "weather_advisory" not in used
        assert "weather_advisory" in dropped
        weather = next(f for f in option["excluded_factors"] if f["factor"] == "weather_advisory")
        assert weather["status"] == "excluded_no_approved_source"


# ---------------------------------------------------------------------------
# Missing input behaviour
# ---------------------------------------------------------------------------


def test_unknown_water_never_produces_a_comparison(client):
    packet = create(client, water_availability="unknown").json()
    assert packet["output_state"] == "informational_only"
    assert "not a comparison" in packet["headline"].lower()
    triggers = {r["trigger"] for r in packet["referrals"]}
    assert "missing_water_evidence" in triggers


def test_informational_packet_is_banded_as_reference_not_ranked(client):
    """A reference list must not carry fit bands or rank ranges."""
    packet = create(client, water_availability="unknown").json()
    assert {o["band"] for o in packet["options"]} == {"reference_only"}
    assert all(o["rank_range"] is None for o in packet["options"])
    assert not any("band" in note and "not a comparison" not in note for note in packet["method_notes"])
    assert any("reference list, not a comparison" in note for note in packet["method_notes"])


def test_missing_soil_is_excluded_not_averaged(client):
    packet = create(client, soil_texture=None, soil_ph=None).json()
    option = packet["options"][0]
    soil = next(f for f in option["factors"] + option["excluded_factors"] if f["factor"] == "soil_fit")
    assert soil["status"] == "excluded_missing_input"
    assert soil["contribution"] is None
    assert "district-average" in soil["explanation"] or "does not substitute" in soil["explanation"]


def test_assured_irrigation_crop_is_cautioned_under_rainfed():
    from app.domain.models import DecisionRequest
    from app.engine.scoring import score_crop
    from app.engine.registry import catalogue

    request = DecisionRequest(**BASE)
    paddy = catalogue().by_id("paddy")
    scored = score_crop(paddy, request)
    assert scored.raw_score <= 0.25
    assert any("assured irrigation" in c for c in scored.cautions)


# ---------------------------------------------------------------------------
# Honesty of the presentation
# ---------------------------------------------------------------------------


def test_bands_never_contain_a_pair_closer_than_separation(client):
    packet = create(client).json()
    band_order = ["stronger_fit", "possible_fit", "weaker_fit"]
    for option in packet["options"]:
        original_index = band_order.index(option["band"])
        # every option sitting in a later band must be at least the separation below
        for other in packet["options"]:
            if band_order.index(other["band"]) > original_index:
                assert option["score"] - other["score"] >= MIN_SEPARATION - 1e-9


def test_rank_ranges_bracket_the_reported_rank(client):
    packet = create(client).json()
    by_id = {o["crop_id"]: o for o in packet["options"]}
    for entry in packet["sensitivity"]:
        low, high = by_id[entry["crop_id"]]["rank_range"]
        assert low <= entry["rank"] <= high
        assert low <= high


def test_packet_never_promises_price_profit_yield_or_diagnosis(client):
    packet = create(client)
    text = packet.text.lower()
    for banned in ("guaranteed", "guarantee profit", "best crop", "recommended crop", "₹", "per quintal", "yield kg"):
        assert banned not in text

    payload = packet.json()
    assert not any("yield" in note.lower() and "not modelled" not in note.lower() for note in payload["method_notes"])


def test_every_used_factor_carries_provenance(client):
    packet = create(client).json()
    for option in packet["options"]:
        for factor in option["factors"]:
            assert factor["provenance"], f"{option['crop_id']} / {factor['factor']} has no provenance"
            for entry in factor["provenance"]:
                assert entry["source_id"] and entry["url"] and entry["status"]


def test_retention_is_ninety_days(client):
    packet = create(client).json()
    assert packet["retention"]["days"] == "90"


def test_referrals_use_neutral_no_partnership_wording(client):
    packet = create(client).json()
    assert packet["referrals"]
    for referral in packet["referrals"]:
        assert "does not claim" in referral["neutral_notice"] or "not claiming" in referral["neutral_notice"]
        assert "partner" not in referral["contact_name"].lower()


# ---------------------------------------------------------------------------
# Retention and deletion
# ---------------------------------------------------------------------------


def test_delete_removes_record_and_is_idempotent(client):
    decision_id = create(client).json()["decision_id"]

    assert client.get(f"/api/v1/decisions/{decision_id}").status_code == 200
    assert client.delete(f"/api/v1/decisions/{decision_id}").json()["deleted"] is True
    assert client.get(f"/api/v1/decisions/{decision_id}").status_code == 404
    assert client.delete(f"/api/v1/decisions/{decision_id}").json()["deleted"] is False


def test_recorded_response_requires_valid_choice(client):
    decision_id = create(client).json()["decision_id"]
    ok = client.post(f"/api/v1/decisions/{decision_id}/response", params={"response_text": "rejected"})
    assert ok.status_code == 200
    bad = client.post(f"/api/v1/decisions/{decision_id}/response", params={"response_text": "maybe"})
    assert bad.status_code == 422


# ---------------------------------------------------------------------------
# Metadata contract used by the frontend
# ---------------------------------------------------------------------------


def test_meta_exposes_governance_text(client):
    meta = client.get("/api/v1/meta").json()
    assert len(meta["blocks"]) == 15
    assert meta["weather_gate"]["weather_available"] is False
    assert meta["consent_notice"]["retention"].startswith("90 days")
    assert any("not TNAU" in lim for lim in meta["limitations"])
    assert meta["district"]["name"] == "Namakkal"


def test_method_endpoint_marks_excluded_factors(client):
    method = client.get("/api/v1/method").json()
    kinds = {f["id"]: f["kind"] for f in method["factors"]}
    assert kinds["weather_advisory"] == "excluded"
    assert kinds["water_fit"] == "scored"
