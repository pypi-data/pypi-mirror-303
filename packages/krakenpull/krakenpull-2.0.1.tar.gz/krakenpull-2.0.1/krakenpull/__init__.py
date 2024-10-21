import typing

__version__ = "2.0.1"

VERSION = __version__


if typing.TYPE_CHECKING:
    # import of virtually everything is supported via `__getattr__` below,
    # but we need them here for type checking and IDE support
    from .models import (
        FiatCurrency,
        CryptoCurrency,
        Currency,
        CurrencyPair,
        TransactionType,
        OrderType,
        ClosedTransaction,
        TickerInfo,
        Asset,
    )
    from .client import (
        Kraken,
    )

__version__ = VERSION
__all__ = (
    # models
    "FiatCurrency",
    "CryptoCurrency",
    "Currency",
    "CurrencyPair",
    "TransactionType",
    "OrderType",
    "ClosedTransaction",
    "TickerInfo",
    "Asset",
    # client
    "Kraken",
)

# A mapping of {<member name>: (package, <module name>)} defining dynamic imports
_dynamic_imports: "dict[str, tuple[str, str]]" = {
    # models
    "FiatCurrency": (__package__, ".models"),
    "CryptoCurrency": (__package__, ".models"),
    "Currency": (__package__, ".models"),
    "CurrencyPair": (__package__, ".models"),
    "TransactionType": (__package__, ".models"),
    "OrderType": (__package__, ".models"),
    "ClosedTransaction": (__package__, ".models"),
    "TickerInfo": (__package__, ".models"),
    "Asset": (__package__, ".models"),
    # client
    "get_kraken_client": (__package__, ".client"),
    "Kraken": (__package__, ".client"),
}


def __getattr__(attr_name: str) -> object:
    dynamic_attr = _dynamic_imports[attr_name]

    package, module_name = dynamic_attr

    from importlib import import_module

    if module_name == "__module__":
        return import_module(f".{attr_name}", package=package)
    else:
        module = import_module(module_name, package=package)
        return getattr(module, attr_name)


def __dir__() -> "list[str]":
    return list(__all__)
