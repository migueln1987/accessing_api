import config
import requests
import json

from twelvedata import TDClient

API_KEY = config.api_key
PREFIX = "https://api.twelvedata.com"
QUOTE_ENDPOINT = "/quote"
PRICE_ENDPOINT = "/price"
SYMBOL = "GME"
INTERVAL = "1min"
EXCHANGE = "NYSE"
TYPE = "Stock"
FORMAT = "JSON"

td = TDClient(apikey=API_KEY)


def get_gme_price():
    response = requests.get(f"{PREFIX}{PRICE_ENDPOINT}?symbol="
                            f"{SYMBOL}&apikey={API_KEY}")
    obj = json.loads(response.text)
    return obj['price']


def get_price(symbol):
    response = requests.get(f"{PREFIX}{PRICE_ENDPOINT}?symbol="
                            f"{symbol}&apikey={API_KEY}")
    obj = json.loads(response.text)
    return obj['price']


if __name__ == '__main__':
    print(f"GameStop's price is: {get_gme_price()}")
    print(f"Apple's price is: {get_price('AAPL')}")
