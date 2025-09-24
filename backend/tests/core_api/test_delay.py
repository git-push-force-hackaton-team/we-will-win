import datetime

import pytest


@pytest.mark.asyncio
async def test_transformer_delay(client):
    input_body = {"input": "сгущенное молоко"}

    start_time = datetime.datetime.now()
    resp = client.post("/api/predict", json=input_body)
    end_time = datetime.datetime.now()

    latency = end_time - start_time

    assert resp.status_code == 200
    assert latency < datetime.timedelta(seconds=1)

    print("\nlatency =", latency.total_seconds())
