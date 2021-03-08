import config

from twelvedata import TDClient

td = TDClient(apikey=config.api_key)

# Access Time Series
ts = td.time_series(
    symbol="MMM",
    interval="5min"
).as_json()


def dummy_function():
    print(config.api_key)


if __name__ == '__main__':
    dummy_function()
