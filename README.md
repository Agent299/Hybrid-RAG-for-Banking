# Banking Hybrid RAG

This repository contains the FastAPI starter for a read-only banking decision-support project. Use synthetic data in development and keep credentials in local environment files or an approved secret store.

## Set up a fresh clone

Open a terminal in the root of your local clone. Install Git and uv, then run:

```sh
cd services/api
uv python install 3.12
uv sync --locked --python 3.12
uv run --locked ruff check .
uv run --locked pytest
```

## Run the API locally

From `services/api`:

```sh
uv run --locked uvicorn app.main:app --reload
```

In a second terminal, run `curl -fsS http://127.0.0.1:8000/health/live`. The API returns `{"status":"ok"}`. Interactive API documentation is at `http://127.0.0.1:8000/docs`.

The starter requires no local database or credentials. When dependencies change, run `uv lock`, verify with `uv sync --locked`, and commit `pyproject.toml` and `uv.lock` together.

## Project planning

- [Execution plan](Hybrid_RAG_Execution_Plan.md)
- [Task completion tracker](Hybrid_RAG_Task_Completion_Tracker.md)

## Repository layout

- `services/api/` contains the FastAPI gateway and scaffolds for scoped tools, specialists, retrieval and telemetry.
- `apps/web/` contains workspace and component scaffolds. Its npm manifest and lockfile contain no frontend dependencies yet.
- `infra/`, `pipelines/` and `data/` hold local database initialization, refresh pipeline scaffolds and synthetic or approved evaluation fixtures.
- `.github/` contains API CI and deployment workflow scaffolds. Deployment adapters fail until configured. See the [runbooks](docs/runbooks.md) for delivery setup.
- `docs/` holds [API contracts](docs/api-contracts.md), the [security model](docs/security-model.md) and architecture decision records.
