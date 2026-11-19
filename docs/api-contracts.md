# API contracts

The starter exposes `GET /health/live`. It returns HTTP 200 with `{"status":"ok"}` when the API process responds. This endpoint has no dependency checks. FastAPI serves the current OpenAPI schema at `/openapi.json`.

The chat, sources and feedback modules are reserved for future route registration.
