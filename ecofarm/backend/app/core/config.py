"""Application settings.

CORS origins are explicitly configurable because the PWA frontend is hosted
separately from this backend.
"""

from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="ECOFARM_", env_file=".env", extra="ignore")

    app_name: str = "EcoFarm Decision Engine"
    environment: str = "development"
    database_path: str = "data/decisions.db"
    allowed_origins: str = (
        "http://localhost:3000,http://127.0.0.1:3000,"
        "https://ecofarm.vercel.app"
    )
    allow_all_origins: bool = False

    @property
    def origins(self) -> list[str]:
        if self.allow_all_origins:
            return ["*"]
        return [o.strip() for o in self.allowed_origins.split(",") if o.strip()]


@lru_cache(maxsize=1)
def settings() -> Settings:
    return Settings()
