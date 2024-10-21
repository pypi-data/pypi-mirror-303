import base64
import hashlib
import hmac
import urllib.parse

import requests
from requests import Response

from krakenpull.models import (
    CurrencyPair,
    ClosedTransaction,
    TickerInfo,
    JSON,
    TradingPairs,
    CurrencyType,
)
from krakenpull.utils import get_unique_tickers, get_currency_pair, parse_currency

BASE_URL = "https://api.kraken.com/0"


class Kraken:
    def __init__(self, key: str, private_key: str):
        self.private_url = f"{BASE_URL}/private"
        self.public_url = f"{BASE_URL}/public"
        self.private_endpoint = "/0/private"
        self.public_endpoint = "/0/public"
        self.api_key = key
        self.private_key = private_key
        self.pair_map = self._parse_trading_pairs()

    def get_order_book(self, currency_pair: CurrencyPair) -> JSON:
        url, _ = self._return_url_endpoint(endpoint="Depth")
        res = requests.post(f"{url}?pair={''.join(c.value for c in currency_pair)}")
        result = self._get_result(res, op="get order book")
        return list(result.values())[0]

    def get_account_balance(self) -> dict[CurrencyType, float]:
        url, endpoint = self._return_url_endpoint(endpoint="Balance", private=True)
        nonce = self._get_server_time_unix()
        headers = self._headers(endpoint, nonce)
        res = requests.post(
            url,
            headers=headers,
            data={"nonce": nonce},
        )
        result = self._get_result(res, op="get account balance")
        return {
            parse_currency(k): float(v) for k, v in result.items() if float(v) > 1e-5
        }

    def get_closed_orders(self, trades: bool = False) -> list[ClosedTransaction]:
        url, endpoint = self._return_url_endpoint(endpoint="ClosedOrders", private=True)
        nonce = self._get_server_time_unix()
        data = {
            "nonce": nonce,
            "trades": trades,
        }
        headers = self._headers(endpoint, nonce, data)
        res = requests.post(url, headers=headers, data=data)
        result = self._get_result(res, op="get closed orders")

        closed_positions = result["closed"]

        return [
            ClosedTransaction.model_validate(
                v
                | v["descr"]
                | {
                    "id": k,
                    "pair": self.pair_map[v["descr"]["pair"]],
                    "price": v["price"],
                    "open_datetime": v["opentm"],
                    "close_datetime": v["closetm"],
                }
            )
            for k, v in closed_positions.items()
            if v["status"] == "closed"
        ]

    def get_ticker_info(
        self, currency_pairs: list[CurrencyPair] | CurrencyPair | None = None
    ) -> list[TickerInfo]:
        url, _ = self._return_url_endpoint(endpoint="Ticker")

        if currency_pairs:
            pairs = get_unique_tickers(
                currency_pairs if isinstance(currency_pairs, list) else [currency_pairs]
            )

            stringed_pairs = ["".join(c.value for c in pair) for pair in pairs]
            try:
                res = requests.post(f"{url}?pair={','.join(stringed_pairs)}")
                result = self._get_result(res, op="get ticker info")
            except Exception:
                stringed_pairs = [
                    "".join(c.value for c in reversed(pair)) for pair in pairs
                ]
                res = requests.post(f"{url}?pair={','.join(stringed_pairs)}")
                result = self._get_result(res, op="get ticker info")
        else:
            res = requests.post(url)
            result = self._get_result(res, op="get ticker info")

        return [
            TickerInfo.model_validate(
                {
                    "pair": self.pair_map[pair_id],
                    "price": data["a"][0],
                    "low": data["l"][0],
                    "high": data["h"][0],
                },
            )
            for pair_id, data in result.items()
        ]

    def _parse_trading_pairs(self) -> dict[str, CurrencyPair]:
        url, _ = self._return_url_endpoint(endpoint="AssetPairs")
        res = requests.post(url)
        result: dict[str, TradingPairs] = self._get_result(res, op="get ticker info")

        base_pair_map = {
            pair: get_currency_pair(pair_info["wsname"])
            for pair, pair_info in result.items()
        }
        pairs = list(base_pair_map.values())
        return base_pair_map | {
            pair_info["altname"]: pairs[i]
            for i, pair_info in enumerate(result.values())
        }

    def _return_url_endpoint(
        self, endpoint: str, private: bool = False
    ) -> tuple[str, str]:
        if private:
            return (
                f"{self.private_url}/{endpoint}",
                f"{self.private_endpoint}/{endpoint}",
            )
        else:
            return f"{self.public_url}/{endpoint}", f"{self.public_endpoint}/{endpoint}"

    def _get_server_time_unix(self) -> int:
        res = requests.get(f"{BASE_URL}/public/Time")
        result = self._get_result(res, op="get server time")
        return result["unixtime"]

    def _get_result(self, res: Response, op: str | None = None) -> JSON:
        json_res = res.json()
        error = json_res.get("error") or None
        if res.status_code != 200 or error:
            raise Exception(
                "Kraken api call failed"
                + (f" ({op})" if op else "")
                + f": {error[0] if isinstance(error, list) else error}"
            )
        return json_res["result"]

    def _headers(self, urlpath: str, nonce: int, data: JSON | None = None) -> JSON:
        data = data if data else {}
        postdata = urllib.parse.urlencode({"nonce": nonce, **data})
        encoded = (str(nonce) + postdata).encode()
        message = urlpath.encode() + hashlib.sha256(encoded).digest()

        mac = hmac.new(base64.b64decode(self.private_key), message, hashlib.sha512)
        sigdigest = base64.b64encode(mac.digest())
        return {"API-Key": self.api_key, "API-Sign": sigdigest.decode()}
