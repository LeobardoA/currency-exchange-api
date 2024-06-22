from fastapi import APIRouter, HTTPException
from .models import ExchangeRateRequest, ExchangeRateResponse, ExchangeRequest, ExchangeResponse
from .services import get_exchange_rate, exchange_currency, get_total_fees

router = APIRouter()

@router.post("/exchange-rate", response_model=ExchangeRateResponse)
def query_exchange_rate(request: ExchangeRateRequest):
    rate, fee, available_amount = get_exchange_rate(request.base_currency, request.quote_currency)
    if rate is None:
        raise HTTPException(status_code=404, detail="Currency not found")
    return ExchangeRateResponse(rate=rate, fee=fee, available_amount=available_amount)

@router.post("/exchange", response_model=ExchangeResponse)
def perform_exchange(request: ExchangeRequest):
    new_base_amount, new_quote_amount, total_fees = exchange_currency(request.base_currency, request.quote_currency, request.amount)
    if new_base_amount is None:
        raise HTTPException(status_code=400, detail="Insufficient funds or currency not found")
    return ExchangeResponse(new_base_amount=new_base_amount, new_quote_amount=new_quote_amount)

@router.get("/total-fees", response_model=float)
def get_total_fees_route():
    total_fees = get_total_fees()
    return total_fees
