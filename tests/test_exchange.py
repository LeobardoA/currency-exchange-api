# tests/test_exchange.py
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_perform_exchange():
    response = client.post("/exchange", json={"base_currency": "USD", "quote_currency": "EUR", "amount": 100})
    assert response.status_code == 200
    data = response.json()
    assert "new_base_amount" in data
    assert "new_quote_amount" in data
