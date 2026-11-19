import asyncio

from httpx import ASGITransport, AsyncClient, Response

from app.main import app


async def request_liveness() -> Response:
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        return await client.get("/health/live")


def test_liveness_reports_ok() -> None:
    response = asyncio.run(request_liveness())

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
