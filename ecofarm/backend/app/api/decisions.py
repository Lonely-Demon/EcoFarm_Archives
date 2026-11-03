"""Crop decision endpoints."""

from __future__ import annotations

from datetime import date

from fastapi import APIRouter, HTTPException, Response, status

from app.core.config import settings
from app.core.storage import DecisionStore
from app.domain.models import DecisionPacket, DecisionRequest, DeleteResponse
from app.engine.packet import build_packet
from app.engine.registry import directory

router = APIRouter(prefix="/api/v1", tags=["decisions"])

_store: DecisionStore | None = None


def store() -> DecisionStore:
    global _store
    if _store is None:
        _store = DecisionStore(settings().database_path)
    return _store


@router.post("/decisions", response_model=DecisionPacket)
def create_decision(request: DecisionRequest, response: Response) -> DecisionPacket:
    if not request.consent_granted:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={
                "state": "consent_required",
                "message": (
                    "This decision record cannot be created without your explicit "
                    "consent for the stated purpose."
                ),
            },
        )

    d = directory()
    if d.block(request.block_id) is None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={
                "state": "outside_tested_scope",
                "message": (
                    "That block is outside the tested pilot scope. EcoFarm will not "
                    "generalise Namakkal evidence to another district."
                ),
                "allowed_blocks": [b.id for b in d.blocks],
            },
        )

    packet = build_packet(request)
    store().save(packet)
    store().log_event(
        category="decision",
        state=packet.output_state.value,
        action="packet_created",
        decision_id=packet.decision_id,
    )
    response.headers["X-EcoFarm-Engine"] = packet.engine_version
    response.headers["X-EcoFarm-Output-State"] = packet.output_state.value
    return packet


@router.get("/decisions/{decision_id}", response_model=DecisionPacket)
def get_decision(decision_id: str) -> DecisionPacket:
    payload = store().get(decision_id)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "state": "not_found_or_expired",
                "message": (
                    "This decision record is not available. It may have passed the "
                    "90-day retention period, or been deleted."
                ),
            },
        )
    return DecisionPacket.model_validate(payload)


@router.delete("/decisions/{decision_id}", response_model=DeleteResponse)
def delete_decision(decision_id: str) -> DeleteResponse:
    deleted = store().delete(decision_id)
    store().log_event(
        category="deletion",
        state="deleted" if deleted else "not_found",
        action="farmer_requested_deletion",
        decision_id=None,
    )
    return DeleteResponse(
        decision_id=decision_id,
        deleted=deleted,
        message=(
            "The decision record and the farmer details in it were removed. "
            "Non-personal source audit entries, which contain no farmer context, "
            "may be retained for integrity review."
        ),
    )


@router.post("/decisions/{decision_id}/response", response_model=DeleteResponse)
def record_farmer_response(decision_id: str, response_text: str) -> DeleteResponse:
    allowed = {"accepted", "rejected", "changed_mind", "need_more_information"}
    if response_text not in allowed:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={"state": "invalid_response", "allowed": sorted(allowed)},
        )
    updated = store().record_response(decision_id, response_text)
    return DeleteResponse(
        decision_id=decision_id,
        deleted=False,
        message="Your response was recorded for pilot evaluation only." if updated else "Record not found.",
    )
