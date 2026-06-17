# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

"Hitup" — a FastAPI application. The entire app currently lives in `main.py` (a single `FastAPI` instance named `app`) exposing a CRUD-style `/exercises` resource. The POST/PUT/DELETE handlers are stubs (`pass`) — no persistence layer, models, or business logic exist yet.

Dependencies are managed with [uv](https://docs.astral.sh/uv/) (`pyproject.toml` + `uv.lock`). The only dependency is `fastapi[standard]`, which pulls in `uvicorn` and the `fastapi` CLI.

## Commands

```bash
uv sync                       # install dependencies into .venv
uv run fastapi dev main.py    # run dev server (auto-reload) at http://127.0.0.1:8000
uv run fastapi run main.py    # run production server
uv add <package>              # add a dependency (updates pyproject.toml + uv.lock)
```

Interactive API docs are served at `/docs` (Swagger) and `/redoc` once the server is running.

No test, lint, or build tooling is configured yet.

## Notes

- CORS is wide open (`allow_origins=["*"]` with credentials) — intended for early development, not production.
- `/exercises` and `/exercises/list` are aliased to the same handler.
