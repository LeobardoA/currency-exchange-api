# tests/test_exchange_rate.py
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_query_exchange_rate():
    response = client.post("/exchange-rate", json={"base_currency": "USD", "quote_currency": "EUR"})
    assert response.status_code == 200
    data = response.json()
    assert "rate" in data
    assert "fee" in data
    assert "available_amount" in data
