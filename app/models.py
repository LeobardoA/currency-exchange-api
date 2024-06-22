from pydantic import BaseModel

class ExchangeRateRequest(BaseModel):
    base_currency: str
    quote_currency: str

class ExchangeRateResponse(BaseModel):
    rate: float
    fee: float
    available_amount: float

class ExchangeRequest(BaseModel):
    base_currency: str
    quote_currency: str
    amount: float

class ExchangeResponse(BaseModel):
    new_base_amount: float
    new_quote_amount: float
