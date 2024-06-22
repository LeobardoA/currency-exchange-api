# services.py
import random

currencies = ['EUR', 'USD', 'JPY', 'GBP', 'CHF', 'AUD', 'CAD', 'NZD']

exchange_rates = {currency: {c: random.uniform(0.5, 1.5) for c in currencies if c != currency} for currency in currencies}
fees = {currency: random.uniform(0.01, 0.05) for currency in currencies}
amounts = {currency: 1000.0 for currency in currencies}
total_fees_collected = 0.0

def get_exchange_rate(base_currency: str, quote_currency: str):
    if base_currency in exchange_rates and quote_currency in exchange_rates[base_currency]:
        return exchange_rates[base_currency][quote_currency], fees[base_currency], amounts[quote_currency]
    return None, None, None

def exchange_currency(base_currency: str, quote_currency: str, amount: float):
    global total_fees_collected
    rate, fee, available_amount = get_exchange_rate(base_currency, quote_currency)
    if rate is None or amount > amounts[base_currency]:
        return None, None, None

    fee_amount = amount * fee
    total_fees_collected += fee_amount
    new_base_amount = amounts[base_currency] - amount - fee_amount
    new_quote_amount = amounts[quote_currency] + (amount * rate)

    amounts[base_currency] = new_base_amount
    amounts[quote_currency] = new_quote_amount

    return new_base_amount, new_quote_amount, total_fees_collected

def get_total_fees():
    global total_fees_collected
    return total_fees_collected
