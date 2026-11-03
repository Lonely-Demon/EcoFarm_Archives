# EcoFarm — crop decision engine + PWA

A working implementation of the part of EcoFarm that the archive says is
buildable *today*: a human-supervised crop decision comparison for Namakkal
district blocks, with every source, gap and limitation visible in the result.

The broader EcoFarm vision in the archive (sensor hardware, irrigation
actuation, marketplace, community, price intelligence) is deliberately **not**
built here. The archive's own P0 memo blocks those surfaces, and building them
would put a confident-looking product in front of a farmer on evidence that does
not exist.

```
ecofarm/
├── backend/    FastAPI + deterministic scoring engine + governance data
└── frontend/   Next.js 15 PWA (installable, server-rendered packets)
```

## What it does

1. Farmer picks a Namakkal block, sowing window, crop stage, water situation and
   one or more goals.
2. The engine scores 11 crops against six factors it can defend.
3. Three factors are **always** withheld — weather, market price, pest risk — and
   the result explains each one with its source and rejection reason.
4. Options are grouped into bands, never numbered, and each carries a rank range
   from a 240-draw weight-perturbation test.
5. Every factor names its source, publisher, URL and status.
6. The record expires after 90 days and can be deleted immediately.
7. Where the engine cannot answer, it shows a neutral public referral.

## What it refuses to do

| Refusal | Enforced in |
|---|---|
| Predict price, profit or yield | no such field exists in the schema |
| Name a "best crop" | bands + rank ranges only |
| Estimate weather | `engine/weather_gate.py` returns unavailable |
| Substitute district-average soil for a plot | `score_soil` excludes instead |
| Score an unapproved source | `source_register` + tests |
| Diagnose pests or dose pesticides | no such endpoint |
| Claim institutional partnership | neutral wording enforced in referrals |

## Quick start

```bash
# backend
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload --port 8000     # http://127.0.0.1:8000/docs

# frontend (separate terminal)
cd frontend
npm install
cp .env.example .env.local
npm run dev                                    # http://127.0.0.1:3000
```

```bash
cd backend && pytest        # 18 tests
```

## Architecture

```
Next.js PWA ──browser──▶ FastAPI /api/v1/decisions ──▶ scoring engine
     │                          │
     └─server render──────────▶ │──▶ crops.yaml      (thresholds, 11 crops)
                                │──▶ blocks.yaml     (15 Namakkal blocks + directory)
                                └──▶ sources.yaml    (source status register)
                                     decisions.db    (90-day records, SQLite)
```

The frontend holds **no** governance text and **no** agronomy. Consent wording,
limitations, source status and the weather gate all come from `/api/v1/meta`, so
there is one place to correct them.

Decision packets render on the server (`app/packet/[id]/page.tsx` → `lib/server-api.ts`),
so they work without JavaScript and no cached comparison is ever shown in place
of a missing one.

## Deploying the backend to a remote server

The must-haves in production:

```bash
ECOFARM_ALLOWED_ORIGINS=https://your-pwa.example.org
ECOFARM_DATABASE_PATH=/data/decisions.db     # mount a volume
```

```bash
docker build -t ecofarm-api backend
docker run -p 8000:8000 -v ecofarm-data:/data \
  -e ECOFARM_ALLOWED_ORIGINS=https://your-pwa.example.org ecofarm-api
```

`backend/render.yaml` is a working Render blueprint. Any Docker host works; the
only stateful dependency is the SQLite file, which can be swapped for Postgres
in `app/core/storage.py` without touching the engine.

## Deploying the PWA

Set `NEXT_PUBLIC_API_BASE_URL` **and** `API_SERVER_URL` to the backend origin,
then deploy on Vercel (or any Next.js host). See `frontend/README.md`.

## The engine, in one paragraph

Each factor returns a 0–1 score with a written explanation and its provenance.
Scores are combined as a weighted sum over the weights that were actually
usable, so a missing factor lowers confidence instead of being replaced by a
default. Hard constraints cap a crop (for example, paddy under rainfed water).
Bands are cut only where options differ by at least 0.06, because otherwise
eleven viable crops for one block all cluster within a few hundredths. Finally
the whole comparison is re-run 240 times with lognormally perturbed weights; the
resulting rank range is printed next to every crop so a 0.01 gap cannot be read
as a real ordering.

## Where each rule comes from

| Code | Archive decision |
|---|---|
| `sources.yaml` statuses | `EF-DAT-005`, `EF-DAT-007` operational test results |
| Weather withheld, TNAU locality failure | `EF-DAT-007` §3 |
| Provenance on every output item | `EF-DAT-006` source-attribution row |
| Consent, retention, deletion | `EF-DAT-003` consent map + retention default |
| Neutral referrals | `EF-DAT-009` |
| Missing input fails closed | `EF-DAT-006` field-level build gates |
| Namakkal blocks and directory | `EF-DAT-015` |
| Crops and district context | `EF-DAT-015`, `EF-REG-007` |
| No price / profit / diagnosis | `EF-DAT-005` §4 prohibitions |

See `docs/archive-traceability.md` for the full mapping, including the places
where this build is *weaker* than the archive asks for.

## Known gaps before field use

These are real and should not be papered over:

1. **Thresholds are unreviewed.** `crops.yaml` carries
   `review_status: unreviewed_pending_agronomist`. A qualified agronomist must
   review every water/pH/duration value against TNAU guidance per crop and
   season before a single farmer sees a result.
2. **No Tamil interface yet.** `ta` exists in the data model and API, but the UI
   is English. The archive requires a Tamil input/comprehension test and forbids
   silently inferring language.
3. **No human reviewer console.** P0 requires a reviewer who can suppress an
   output, record why, and refer. Currently suppression is automatic via the
   fail-closed states, but there is no reviewer sign-off step.
4. **Referral directory ages.** `blocks.yaml` is verified to 2026-08-13 with a
   180-day recheck. Past that date the API flags `is_stale`; nothing enforces a
   re-verification workflow.
5. **No evaluation export.** Farmer responses are stored, but there is no
   evidence dashboard like `EF-FLD-017` describes.
6. **SQLite.** Fine for one pilot node; needs Postgres before multiple regions.
