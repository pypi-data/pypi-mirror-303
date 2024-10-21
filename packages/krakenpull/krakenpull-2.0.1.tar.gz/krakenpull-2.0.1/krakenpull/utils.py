import json
import os
from pathlib import Path
from typing import Any

from krakenpull import CurrencyPair, Currency
from krakenpull.data import FIAT_CURRENCIES, CryptoCurrency, FiatCurrency
from krakenpull.models import CurrencyType


def get_root_dir():
    return Path(os.getenv("ROOT_DIRECTORY", Path(__file__).parents[1]))


def load_json(path: Path) -> Any:
    with open(get_root_dir() / path, "r") as f:
        return json.load(f)


def get_unique_tickers(tickers: list[CurrencyPair]) -> list[CurrencyPair]:
    uniq_list = []
    for ticker in tickers:
        if ticker not in uniq_list:
            uniq_list.append(ticker)

    return uniq_list


def get_currency_pair(wsname: str) -> CurrencyPair:
    pair_split = wsname.split("/")
    currency1: Currency
    try:
        currency1 = CryptoCurrency(pair_split[0])
    except ValueError:
        currency1 = FiatCurrency(pair_split[0])

    currency2: Currency
    try:
        currency2 = CryptoCurrency(pair_split[1])
    except ValueError:
        currency2 = FiatCurrency(pair_split[1])

    if isinstance(currency1, FiatCurrency) and isinstance(currency2, CryptoCurrency):
        raise ValueError(f"Unrecognized currency pair {wsname}")

    return currency1, currency2


def parse_currency(currency: CurrencyType | str) -> Currency:
    if isinstance(currency, CryptoCurrency) or isinstance(currency, FiatCurrency):
        return currency

    if currency in FIAT_CURRENCIES:
        return FiatCurrency(currency)

    if "Z" in currency:
        return FiatCurrency(currency[1:])

    return (
        CryptoCurrency(currency)
        if not currency.startswith("X")
        else CryptoCurrency(currency[1:])
    )
