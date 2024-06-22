# tests/test_fees.py
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_get_total_fees():
    response = client.get("/total-fees")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, float)
    assert data >= 0
