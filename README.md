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
