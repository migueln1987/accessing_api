import config

from twelvedata import TDClient

API_KEY = config.api_key
PREFIX = "https://api.twelvedata.com"
ENDPOINT = "/quote"
SYMBOL = "GME"
INTERVAL = "1minapi_key"
EXCHANGE = "NYSE"
TYPE = "Stock"
FORMAT = "JSON"

td = TDClient(apikey=API_KEY)


def dummy_function():
    print(API_KEY)


if __name__ == '__main__':
    dummy_function()
