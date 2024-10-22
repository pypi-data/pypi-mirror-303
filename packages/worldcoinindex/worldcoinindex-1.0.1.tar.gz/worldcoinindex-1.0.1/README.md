## worldcoinindex

[![Downloads](https://static.pepy.tech/badge/worldcoinindex)](https://pepy.tech/project/worldcoinindex)
[![PyPI](https://badge.fury.io/py/worldcoinindex.svg)](https://pypi.org/project/worldcoinindex/)

A Python wrapper for the [WorldCoinIndex API](https://www.worldcoinindex.com/apiservice).

# Features

- Fetch ticker information
- Retrieve market data
- Handle errors gracefully
- Lightweight with no external dependencies

# Installation

You can install the package via pip:

```bash
pip install worldcoinindex
```
# Usage

```
from worldcoinindex import CryptocoinEngine

# Initialize the client with your API key
api_key = "YOUR_API_KEY"
client = CryptocoinEngine(api_key=api_key)

# Get tickers
tickers = client.get_tickers(labels=["ethbtc", "ltcbtc"], fiat="btc")
print(tickers)

# Get markets (v2)
markets = client.get_markets(fiat="btc")
print(markets_v2)
```

