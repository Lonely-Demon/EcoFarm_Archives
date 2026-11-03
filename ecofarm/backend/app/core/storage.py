"""Local decision-record storage.

Deliberately minimal: SQLite via the standard library, one table, short
retention, hard delete. Farmer context is only ever stored inside the decision
record so that deleting the record deletes the personal data with it. Source
audit events are stored separately and carry no farmer context.
"""

from __future__ import annotations

import json
import sqlite3
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

RETENTION_DAYS = 90


class DecisionStore:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS decisions (
                    decision_id TEXT PRIMARY KEY,
                    created_at TEXT NOT NULL,
                    expires_at TEXT NOT NULL,
                    payload TEXT NOT NULL,
                    response TEXT
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS audit_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    occurred_at TEXT NOT NULL,
                    category TEXT NOT NULL,
                    state TEXT NOT NULL,
                    action TEXT NOT NULL,
                    decision_id TEXT
                )
                """
            )

    # -- decision records ---------------------------------------------------

    def save(self, packet, retention_days: int = RETENTION_DAYS) -> None:
        created = packet.created_at
        expires = created + timedelta(days=retention_days)
        with self._connect() as conn:
            conn.execute(
                "INSERT OR REPLACE INTO decisions (decision_id, created_at, expires_at, payload) "
                "VALUES (?, ?, ?, ?)",
                (
                    packet.decision_id,
                    created.isoformat(),
                    expires.isoformat(),
                    packet.model_dump_json(),
                ),
            )

    def get(self, decision_id: str) -> dict | None:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT payload, expires_at FROM decisions WHERE decision_id = ?",
                (decision_id,),
            ).fetchone()
        if row is None:
            return None
        if datetime.fromisoformat(row["expires_at"]) < datetime.now(timezone.utc):
            self.delete(decision_id)
            return None
        return json.loads(row["payload"])

    def delete(self, decision_id: str) -> bool:
        with self._connect() as conn:
            cursor = conn.execute("DELETE FROM decisions WHERE decision_id = ?", (decision_id,))
        return cursor.rowcount > 0

    def record_response(self, decision_id: str, response: str) -> bool:
        with self._connect() as conn:
            cursor = conn.execute(
                "UPDATE decisions SET response = ? WHERE decision_id = ?",
                (response, decision_id),
            )
        return cursor.rowcount > 0

    def purge_expired(self) -> int:
        now = datetime.now(timezone.utc).isoformat()
        with self._connect() as conn:
            cursor = conn.execute("DELETE FROM decisions WHERE expires_at < ?", (now,))
        return cursor.rowcount

    # -- non-personal audit ------------------------------------------------

    def log_event(self, category: str, state: str, action: str, decision_id: str | None = None) -> None:
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO audit_events (occurred_at, category, state, action, decision_id) "
                "VALUES (?, ?, ?, ?, ?)",
                (datetime.now(timezone.utc).isoformat(), category, state, action, decision_id),
            )

    def events(self, limit: int = 100) -> list[dict]:
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT occurred_at, category, state, action FROM audit_events "
                "ORDER BY id DESC LIMIT ?",
                (limit,),
            ).fetchall()
        return [dict(row) for row in rows]
