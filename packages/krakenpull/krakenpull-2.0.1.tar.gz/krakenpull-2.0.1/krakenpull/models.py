import datetime as dt
import json
from enum import Enum
from typing import Any, TypedDict, Type

from pydantic import BaseModel

from krakenpull.data import FiatCurrency, CryptoCurrency

JSON = dict[str, Any]


def extend_enum(base_enum: Type[Enum], other_enum: Type[Enum]):
    return Enum(
        base_enum.__name__,
        {c: c for c in base_enum.__members__} | {c: c for c in other_enum.__members__},
    )


CurrencyType = FiatCurrency | CryptoCurrency


Currency = extend_enum(CryptoCurrency, FiatCurrency)


CurrencyPair = (
    tuple[CryptoCurrency, CryptoCurrency]
    | tuple[CryptoCurrency, FiatCurrency]
    | tuple[FiatCurrency, FiatCurrency]
)


class TransactionType(Enum):
    buy = "buy"
    sell = "sell"


class OrderType(Enum):
    limit = "limit"
    market = "market"
    stop_loss = "stop-loss"
    take_profit = "take-profit"


class TradingPairs(TypedDict):
    altname: str
    wsname: str
    base: str
    quote: str


class BaseTickerInfo(BaseModel):
    pair: CurrencyPair
    price: float

    @property
    def currency1(self) -> CurrencyType:
        return self.pair[0]

    @property
    def currency2(self) -> CurrencyType:
        return self.pair[1]

    @property
    def currency_pair_id(self) -> str:
        return "".join(c.value for c in list(self.pair))


class ClosedTransaction(BaseTickerInfo):
    id: str
    type: TransactionType
    ordertype: OrderType
    vol: float
    cost: float
    leverage: str
    fee: float
    order: str
    open_datetime: dt.datetime
    close_datetime: dt.datetime


class TickerInfo(BaseTickerInfo):
    low: float
    high: float


class Asset(BaseModel):
    currency: CurrencyType
    value: float
    amount: float

    def jsonable_dict(self) -> JSON:
        return json.loads(self.model_dump_json())
