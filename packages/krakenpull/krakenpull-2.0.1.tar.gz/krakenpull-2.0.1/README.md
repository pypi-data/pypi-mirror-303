# Kraken-pull

## A user friendly Kraken API client using pydantic 🐙

### Installation 💿

The easiest way to use krakenpull is to install via pip:

```shell
pip install krakenpull
```

### Usage 🪚

Initialize a kraken client:

```python
from krakenpull import Kraken

client = Kraken(key, private_key)
```

Common methods and features:

```python
# get account balance
balances = client.get_account_balance()
print(balances) # {Currency.XBT: 5.23}

# get closed orders
closed_orders = client.get_closed_orders()
print(closed_orders) # [ClosedTransactions(...), ...]

# get order book
from krakenpull import Currency
order_book = client.get_order_book(currency_pair=(Currency.XBT, Currency.USD))
print(order_book) # {"asks": ["69854.10000", "17.384", 1711832989], "bids": ["69854.00000", "0.015", 1711832988]} 
```

### Contributing 🧑‍💻

Issues, PRs and other contributions are always welcome.

Please note this repository uses black for formatting, ruff for linting and mypy for type checking.

Pre-commit hooks help to make committing easier by automating running black and ruff so if you want to 
make use of them, you can install them by using the following commands:

```shell
brew install pre-commit
pre-commit install
```
