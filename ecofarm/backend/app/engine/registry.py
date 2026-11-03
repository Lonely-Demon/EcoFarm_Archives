"""Reference-data registry.

Loads the governed YAML catalogues once and exposes them read-only. The engine
never invents reference data at request time: if a file is missing the service
refuses to start rather than serving partial agronomy.
"""

from __future__ import annotations

import functools
from pathlib import Path

import yaml

from app.domain.models import (
    BlockDirectory,
    Catalogue,
    Crop,
    SourceRegister,
)

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

ENGINE_VERSION = "ecofarm-rec-engine-0.1.0"


def _load_yaml(name: str) -> dict:
    path = DATA_DIR / name
    if not path.exists():  # pragma: no cover - deployment guard
        raise RuntimeError(f"Required data file missing: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


@functools.lru_cache(maxsize=1)
def catalogue() -> Catalogue:
    return Catalogue.model_validate(_load_yaml("crops.yaml"))


@functools.lru_cache(maxsize=1)
def directory() -> BlockDirectory:
    return BlockDirectory.model_validate(_load_yaml("blocks.yaml"))


@functools.lru_cache(maxsize=1)
def source_register() -> SourceRegister:
    return SourceRegister.model_validate(_load_yaml("sources.yaml"))


def crop_or_none(crop_id: str) -> Crop | None:
    return catalogue().by_id(crop_id)


def provenance_for(source_id: str):
    """Build a Provenance object from the source register, or None if unknown."""
    from app.domain.models import Provenance

    record = source_register().get(source_id)
    if record is None:
        return None
    return Provenance(
        source_id=record.id,
        source_name=record.name,
        publisher=record.publisher,
        url=record.url,
        status=record.status,
        note=record.status_detail,
    )
