import config

from twelvedata import TDClient

td = TDClient(apikey=config.api_key)


def dummy_function():
    print(config.api_key)


if __name__ == '__main__':
    dummy_function()
