"""EcoFarm Decision Engine API.

Run locally:  uvicorn app.main:app --reload --port 8000
"""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import decisions, meta
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Purge anything past the 90-day retention window on boot.
    try:
        decisions.store().purge_expired()
    except Exception:  # pragma: no cover - never block startup on cleanup
        pass
    yield


app = FastAPI(
    title="EcoFarm Decision Engine",
    version="0.1.0",
    description=(
        "Human-supervised crop decision support for the Namakkal pilot. "
        "Fail-closed by design: factors without an approved source are reported "
        "as excluded rather than estimated."
    ),
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings().origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["X-EcoFarm-Engine", "X-EcoFarm-Output-State"],
)

app.include_router(decisions.router)
app.include_router(meta.router)


@app.get("/")
def root() -> dict:
    return {
        "name": "EcoFarm Decision Engine",
        "version": "0.1.0",
        "docs": "/docs",
        "endpoints": [
            "GET  /api/v1/meta",
            "GET  /api/v1/method",
            "GET  /api/v1/sources",
            "POST /api/v1/decisions",
            "GET  /api/v1/decisions/{id}",
            "DELETE /api/v1/decisions/{id}",
            "GET  /api/v1/health",
        ],
        "posture": (
            "Pilot decision support for Namakkal district. Not a TNAU recommendation, "
            "not a price or profit forecast, not pest diagnosis."
        ),
    }
