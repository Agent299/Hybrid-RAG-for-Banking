from fastapi import FastAPI

app = FastAPI(title="Banking Hybrid RAG API")


@app.get("/health/live")
def liveness() -> dict[str, str]:
    return {"status": "ok"}
