import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/latest"

def convert_to_rub(transaction: dict) -> float:
    amount = float(transaction.get("amount", 0))
    currency = transaction.get("currency", "RUB")

    if currency == "RUB":
        return amount

    if not API_KEY:
        return 0.0

    response = requests.get(
        API_URL,
        params={"base": currency, "symbols": "RUB"},
        headers={"apikey": API_KEY}
    )

    if response.status_code != 200:
        return 0.0

    data = response.json()
    try:
        rate = data["rates"]["RUB"]
        return round(amount * rate, 2)
    except (KeyError, TypeError):
        return 0.0