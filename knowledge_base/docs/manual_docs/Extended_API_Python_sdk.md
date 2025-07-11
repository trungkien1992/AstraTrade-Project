Directory structure:
└── x10xchange-python_sdk/
    ├── README.md
    ├── LICENSE
    ├── Makefile
    ├── pyproject.toml
    ├── tox.ini
    ├── .flake8
    ├── examples/
    │   ├── __init__.py
    │   ├── logger.yml
    │   ├── onboarding_example.py
    │   ├── placed_order_example_advanced.py
    │   ├── placed_order_example_simple.py
    │   ├── simple_client_example.py
    │   ├── stream_example.py
    │   ├── utils.py
    │   ├── withdrawal_example.py
    │   └── x10_throughput_latency_test.py
    ├── tests/
    │   ├── conftest.py
    │   ├── fixtures/
    │   │   ├── accounts.py
    │   │   ├── assets.py
    │   │   ├── candles.py
    │   │   ├── markets.py
    │   │   └── orderbook.py
    │   ├── perpetual/
    │   │   ├── test_l2_key_derivation.py
    │   │   ├── test_onboarding_payload.py
    │   │   ├── test_order_object.py
    │   │   ├── test_orderbook_price_impact.py
    │   │   ├── test_stream_client.py
    │   │   ├── test_trading_client.py
    │   │   ├── test_transfer_object.py
    │   │   └── test_withdrawal_object.py
    │   └── utils/
    │       ├── test_date.py
    │       ├── test_http.py
    │       └── test_model.py
    ├── x10/
    │   ├── __init__.py
    │   ├── config.py
    │   ├── errors.py
    │   ├── perpetual/
    │   │   ├── __init__.py
    │   │   ├── accounts.py
    │   │   ├── amounts.py
    │   │   ├── assets.py
    │   │   ├── balances.py
    │   │   ├── candles.py
    │   │   ├── configuration.py
    │   │   ├── contract.py
    │   │   ├── fees.py
    │   │   ├── funding_rates.py
    │   │   ├── markets.py
    │   │   ├── order_object.py
    │   │   ├── orderbook.py
    │   │   ├── orderbooks.py
    │   │   ├── orders.py
    │   │   ├── positions.py
    │   │   ├── trades.py
    │   │   ├── transfer_object.py
    │   │   ├── transfers.py
    │   │   ├── withdrawal_object.py
    │   │   ├── withdrawals.py
    │   │   ├── abi/
    │   │   │   ├── erc20.json
    │   │   │   └── stark-perpetual.json
    │   │   ├── simple_client/
    │   │   │   └── simple_trading_client.py
    │   │   ├── stream_client/
    │   │   │   ├── __init__.py
    │   │   │   ├── perpetual_stream_connection.py
    │   │   │   └── stream_client.py
    │   │   ├── trading_client/
    │   │   │   ├── __init__.py
    │   │   │   ├── account_module.py
    │   │   │   ├── base_module.py
    │   │   │   ├── info_module.py
    │   │   │   ├── markets_information_module.py
    │   │   │   ├── order_management_module.py
    │   │   │   └── trading_client.py
    │   │   └── user_client/
    │   │       ├── __init__.py
    │   │       ├── l1_signing.py
    │   │       ├── onboarding.py
    │   │       └── user_client.py
    │   └── utils/
    │       ├── __init__.py
    │       ├── date.py
    │       ├── http.py
    │       ├── log.py
    │       ├── model.py
    │       ├── starkex.py
    │       └── string.py
    ├── .devcontainer/
    │   └── devcontainer.json
    └── .github/
        ├── CODEOWNERS
        ├── pull_request_template.md
        └── workflows/
            ├── build-release.yml
            └── code-checks.yml


Files Content:

================================================
FILE: README.md
================================================
[Binary file]


================================================
FILE: LICENSE
================================================
MIT License

Copyright (c) 2024, X10

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



================================================
FILE: Makefile
================================================
format:
	isort --profile black ./examples ./tests ./x10
	black --target-version py310 --line-length 120 ./examples ./tests ./x10

lint:
	safety check \
		-i 51457 \
		-i 64227 \
		-i 64396 \
		-i 64459 \
		-i 64642 \
		-i 65693 \
		-i 66742 \
		-i 67599 \
		-i 67895 \
		-i 70612 \
		-i 70630 \
		-i 71064 \
		-i 71545 \
		-i 71591 \
		-i 71608 \
		-i 73456 \
		-i 74251 \
		-i 76752
	black --check --diff --target-version py310 --line-length 120 ./examples ./tests ./x10
	flake8 ./examples ./tests ./x10
	mypy

test:
	tox

bump:
	poetry version patch



================================================
FILE: pyproject.toml
================================================
[build-system]
requires = ["poetry-core>=1.7.0"]
build-backend = "poetry.core.masonry.api"


[tool.poetry]
name = "x10-python-trading"
version = "0.4.5"
description = "Python client for X10 API"
authors = ["X10 <tech@ex10.org>"]
repository = "https://github.com/x10xchange/python_sdk"
documentation = "https://api.docs.extended.exchange/"
readme = "README.md"
classifiers = [
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
packages = [
    { include = "vendor" },
    { include = "x10" },
]

[tool.poetry.dependencies]
aiohttp = "==3.10.11"
ecdsa = "==0.18.0"
eth-account = "==0.11.2"
eth_typing="==4.4.0"
fast-stark-crypto = "==0.1.0"
fastecdsa = "==2.3.2"
mpmath = "==1.3.0"
numpy = "==1.26.2"
pydantic = "==2.5.3"
python = "^3.10"
pyyaml = "==6.0.1"
sortedcontainers = "==2.4.0"
sympy = "==1.12"
web3 = "==6.20.1"
websockets = "==12.0"

[tool.poetry.group.dev.dependencies]
black = "==23.12.0"
flake8 = "==6.1.0"
flake8-bugbear = "==24.12.12"
freezegun = "==1.4.0"
isort = "==5.13.2"
mypy = "==1.8.0"
mypy-extensions = "==1.0.0"
PyHamcrest = "2.1.0"
pytest = "==7.4.3"
pytest-aiohttp = "==1.0.5"
pytest-asyncio = "==0.23.3"
pytest-cov = "==4.1.0"
pytest-forked = "==1.6.0"
pytest-mock = "==3.12.0"
python-dotenv = "==1.0.1"
safety = "==2.4.0b2"
tox = "==4.11.4"
types-pyyaml = "==6.0.12.12"
typing-extensions = "==4.9.0"


[tool.mypy]
packages = ["examples", "tests", "x10"]
plugins = ["pydantic.mypy"]

[[tool.mypy.overrides]]
module = "vendor.starkware.*"
ignore_errors = true

[tool.pydantic-mypy]
init_forbid_extra = true
init_typed = true
warn_required_dynamic_aliases = true



================================================
FILE: tox.ini
================================================
[tox]
isolated_build = true

[testenv]
skip_install = true
allowlist_externals = poetry
commands_pre =
    poetry install
commands =
    poetry run pytest --cov=x10 --cov-fail-under=70 --forked tests/ --import-mode importlib



================================================
FILE: .flake8
================================================
[flake8]
max-line-length = 120



================================================
FILE: examples/__init__.py
================================================
[Empty file]


================================================
FILE: examples/logger.yml
================================================
version: 1

formatters:
  standard:
    format: "%(asctime)s %(process)s %(thread)s %(levelname)s %(name)s %(message)s"

handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    formatter: standard
    stream: ext://sys.stdout

root:
  level: INFO
  handlers: [console]
  propagate: yes

loggers:
  x10:
    level: DEBUG



================================================
FILE: examples/onboarding_example.py
================================================
import asyncio
from decimal import Decimal

from eth_account import Account
from eth_account.signers.local import LocalAccount

from x10.perpetual.accounts import StarkPerpetualAccount
from x10.perpetual.assets import AssetOperationType
from x10.perpetual.configuration import TESTNET_CONFIG
from x10.perpetual.contract import call_erc20_approve, call_stark_perpetual_deposit
from x10.perpetual.trading_client.trading_client import PerpetualTradingClient
from x10.perpetual.user_client.user_client import UserClient


# flake8: noqa
async def on_board_example():
    environment_config = TESTNET_CONFIG
    eth_account: LocalAccount = Account.from_key("<your private key>")
    user_client = UserClient(endpoint_config=environment_config, l1_private_key=eth_account.key.hex)
    onboarded_user = await user_client.onboard()
    sub_account_1 = await user_client.onboard_subaccount(1, "sub account 1")

    default_api_key = await user_client.create_account_api_key(onboarded_user.account, "trading api key")
    account_1_api_key = await user_client.create_account_api_key(sub_account_1.account, "sub account 1 api key")

    default_account_trading_client = PerpetualTradingClient(
        environment_config,
        StarkPerpetualAccount(
            vault=onboarded_user.account.l2_vault,
            private_key=onboarded_user.l2_key_pair.private_hex,
            public_key=onboarded_user.l2_key_pair.public_hex,
            api_key=default_api_key,
        ),
    )

    sub_account_1_trading_client = PerpetualTradingClient(
        environment_config,
        StarkPerpetualAccount(
            vault=sub_account_1.account.l2_vault,
            private_key=sub_account_1.l2_key_pair.private_hex,
            public_key=sub_account_1.l2_key_pair.public_hex,
            api_key=account_1_api_key,
        ),
    )

    call_erc20_approve(
        human_readable_amount=Decimal("1000"), get_eth_private_key=eth_account.key.hex, config=environment_config
    )

    await default_account_trading_client.account.deposit(
        human_readable_amount=Decimal("1000"),
        get_eth_private_key=eth_account.key.hex,
    )

    default_account_trading_client.account.transfer(
        to_vault=int(sub_account_1.account.l2_vault),
        to_l2_key=sub_account_1.l2_key_pair.public_hex,
        amount=Decimal("10"),
    )

    created_withdrawal_id = await default_account_trading_client.account.slow_withdrawal(
        amount=Decimal("10"),
        eth_address=eth_account.address,
    )

    withdrawals = await default_account_trading_client.account.asset_operations(
        operations_type=[AssetOperationType.SLOW_WITHDRAWAL],
    )

    #### wait until withdrawal is in status READY_FOR_CLAIM

    available_withdrawal_balance = await user_client.available_l1_withdrawal_balance()

    withdrawal_tx_hash = await user_client.perform_l1_withdrawal()

    print()


asyncio.run(on_board_example())



================================================
FILE: examples/placed_order_example_advanced.py
================================================
import asyncio
import logging
import logging.config
import logging.handlers
from asyncio import run
from collections.abc import Awaitable
from decimal import Decimal
from typing import Dict, Optional, Tuple

from x10.config import ADA_USD_MARKET
from x10.perpetual.accounts import StarkPerpetualAccount
from x10.perpetual.configuration import TESTNET_CONFIG
from x10.perpetual.markets import MarketModel
from x10.perpetual.order_object import create_order_object
from x10.perpetual.orders import OrderSide, PlacedOrderModel
from x10.perpetual.stream_client.perpetual_stream_connection import (
    PerpetualStreamConnection,
)
from x10.perpetual.stream_client.stream_client import PerpetualStreamClient
from x10.perpetual.trading_client import PerpetualTradingClient
from x10.utils.http import WrappedApiResponse
from x10.utils.model import EmptyModel

NUM_ORDERS_PER_PRICE_LEVEL = 100
NUM_PRICE_LEVELS = 80

API_KEY = "<API_KEY>"
PRIVATE_KEY = "<PRIVATE_KEY>"
PUBLIC_KEY = "<PUBLIC_KEY"
VAULT_ID = 12345677890

order_condtions: Dict[str, asyncio.Condition] = {}
socket_connect_condition = asyncio.Condition()
socket_connected = False
order_loop_finished = False
stream: Optional[PerpetualStreamConnection] = None


stark_account = StarkPerpetualAccount(vault=VAULT_ID, private_key=PRIVATE_KEY, public_key=PUBLIC_KEY, api_key=API_KEY)


async def build_markets_cache(trading_client: PerpetualTradingClient):
    markets = await trading_client.markets_info.get_markets()
    assert markets.data is not None
    return {m.name: m for m in markets.data}


async def order_stream():
    stream_client = PerpetualStreamClient(api_url=TESTNET_CONFIG.stream_url)
    global stream
    stream = await stream_client.subscribe_to_account_updates(API_KEY)

    global socket_connected
    socket_connected = True

    async with socket_connect_condition:
        socket_connect_condition.notify_all()

    async for event in stream:
        if order_loop_finished:
            break
        if not (event.data and event.data.orders):
            continue
        else:
            pass
        for order in event.data.orders:
            print(f"processing order {order.external_id}")
            condition = order_condtions.get(order.external_id)
            if not condition:
                continue
            if condition:
                async with condition:
                    condition.notify_all()
                    del order_condtions[order.external_id]


async def order_loop(
    i: int,
    trading_client: PerpetualTradingClient,
    markets_cache: dict[str, MarketModel],
):
    if not socket_connected:
        async with socket_connect_condition:
            await socket_connect_condition.wait()

    for _ in range(NUM_ORDERS_PER_PRICE_LEVEL):
        (external_id, order_response) = await place_order(i, trading_client, markets_cache)
        print(f"placed order {external_id}")
        condition = order_condtions.get(external_id)
        if condition:
            async with condition:
                await condition.wait()
        if order_response and order_response.data:
            print(f"cancelling order {external_id}")
            await trading_client.orders.cancel_order(order_id=order_response.data.id)
            print(f"cancelled order {external_id}")


async def place_order(
    i: int,
    trading_client: PerpetualTradingClient,
    markets_cache: dict[str, MarketModel],
) -> Tuple[str, WrappedApiResponse[PlacedOrderModel]]:
    should_buy = i % 2 == 0
    price = Decimal("0.660") - Decimal("0.00" + str(i)) if should_buy else Decimal("0.6601") + Decimal("0.00" + str(i))
    order_side = OrderSide.BUY if should_buy else OrderSide.SELL
    market = markets_cache[ADA_USD_MARKET]
    new_order = create_order_object(stark_account, market, Decimal("100"), price, order_side)
    order_condtions[new_order.id] = asyncio.Condition()
    return new_order.id, await trading_client.orders.place_order(order=new_order)


async def clean_it():
    logger = logging.getLogger("placed_order_example")
    trading_client = PerpetualTradingClient(TESTNET_CONFIG, stark_account)
    positions = await trading_client.account.get_positions()
    logger.info("Positions: %s", positions.to_pretty_json())
    balance = await trading_client.account.get_balance()
    logger.info("Balance: %s", balance.to_pretty_json())
    open_orders = await trading_client.account.get_open_orders(market_names=[ADA_USD_MARKET])

    def __cancel_order(order_id: int) -> Awaitable[WrappedApiResponse[EmptyModel]]:
        return trading_client.orders.cancel_order(order_id=order_id)

    cancel_futures = list(map(__cancel_order, [order.id for order in open_orders.data]))
    await asyncio.gather(*cancel_futures)


async def setup_and_run():
    await clean_it()
    print("Press enter to start load test")
    input()

    trading_client = PerpetualTradingClient(TESTNET_CONFIG, stark_account)
    markets_cache = await build_markets_cache(trading_client)
    stream_future = asyncio.create_task(order_stream())

    def __create_order_loop(i: int):
        return asyncio.create_task(
            order_loop(
                i,
                trading_client=trading_client,
                markets_cache=markets_cache,
            )
        )

    order_loop_futures = map(__create_order_loop, range(NUM_PRICE_LEVELS))
    await asyncio.gather(*order_loop_futures)
    print("Load Test Complete")
    global order_loop_finished
    order_loop_finished = True
    if stream:
        await stream.close()
    await stream_future
    await clean_it()


if __name__ == "__main__":
    run(main=setup_and_run())



================================================
FILE: examples/placed_order_example_simple.py
================================================
import asyncio
import logging
import logging.config
import logging.handlers
import os
from asyncio import run
from decimal import Decimal

from dotenv import load_dotenv

from x10.perpetual.accounts import StarkPerpetualAccount
from x10.perpetual.configuration import TESTNET_CONFIG
from x10.perpetual.orderbook import OrderBook
from x10.perpetual.orders import OrderSide
from x10.perpetual.simple_client.simple_trading_client import BlockingTradingClient
from x10.perpetual.trading_client import PerpetualTradingClient

NUM_PRICE_LEVELS = 1

load_dotenv()

API_KEY = os.getenv("X10_API_KEY")
PUBLIC_KEY = os.getenv("X10_PUBLIC_KEY")
PRIVATE_KEY = os.getenv("X10_PRIVATE_KEY")
VAULT_ID = int(os.environ["X10_VAULT_ID"])


async def clean_it(trading_client: PerpetualTradingClient):
    logger = logging.getLogger("placed_order_example")
    positions = await trading_client.account.get_positions()
    logger.info("Positions: %s", positions.to_pretty_json())
    balance = await trading_client.account.get_balance()
    logger.info("Balance: %s", balance.to_pretty_json())
    open_orders = await trading_client.account.get_open_orders()
    await trading_client.orders.mass_cancel(order_ids=[order.id for order in open_orders.data])


async def setup_and_run():
    stark_account = StarkPerpetualAccount(
        vault=VAULT_ID,
        private_key=PRIVATE_KEY,
        public_key=PUBLIC_KEY,
        api_key=API_KEY,
    )
    trading_client = PerpetualTradingClient(
        endpoint_config=TESTNET_CONFIG,
        stark_account=stark_account,
    )
    positions = await trading_client.account.get_positions()
    for position in positions.data:
        print(
            f"market: {position.market} \
            side: {position.side} \
            size: {position.size} \
            mark_price: ${position.mark_price} \
            leverage: {position.leverage}"
        )
        print(f"consumed im: ${round((position.size * position.mark_price) / position.leverage, 2)}")

    await clean_it(trading_client)

    blocking_client = BlockingTradingClient(
        endpoint_config=TESTNET_CONFIG,
        account=stark_account,
    )

    orderbook = await OrderBook.create(
        endpoint_config=TESTNET_CONFIG,
        market_name="BTC-USD",
    )

    await orderbook.start_orderbook()

    def order_loop(idx: int, side: OrderSide) -> asyncio.Task:
        offset = (Decimal("-1") if side == OrderSide.BUY else Decimal("1")) * Decimal(idx + 1)

        async def inner():
            while True:
                baseline_price = orderbook.best_bid() if side == OrderSide.BUY else orderbook.best_ask()
                if baseline_price:
                    order_price = round(
                        baseline_price.price + offset * baseline_price.price * Decimal("0.002"),
                        1,
                    )
                    placed_order = await blocking_client.create_and_place_order(
                        market_name="BTC-USD",
                        amount_of_synthetic=Decimal("0.01"),
                        price=order_price,
                        side=side,
                        post_only=True,
                    )
                    print(f"baseline: {baseline_price.price}, order: {order_price}, id: {placed_order.id}")
                    await blocking_client.cancel_order(order_id=placed_order.id)
                    await asyncio.sleep(0)
                else:
                    await asyncio.sleep(1)

        return asyncio.get_running_loop().create_task(inner())

    sell_tasks = list(map(lambda idx: order_loop(idx, OrderSide.SELL), range(NUM_PRICE_LEVELS)))
    buy_tasks = list(map(lambda idx: order_loop(idx, OrderSide.BUY), range(NUM_PRICE_LEVELS)))

    for task in sell_tasks:
        print(await task)
    for task in buy_tasks:
        print(await task)


if __name__ == "__main__":
    run(main=setup_and_run())



================================================
FILE: examples/simple_client_example.py
================================================
import asyncio
from decimal import Decimal

from x10.perpetual.accounts import StarkPerpetualAccount
from x10.perpetual.configuration import TESTNET_CONFIG
from x10.perpetual.orders import OrderSide
from x10.perpetual.simple_client.simple_trading_client import BlockingTradingClient


async def setup_and_run():
    api_key = "<api>"
    public_key = "<public>"
    private_key = "<private>"
    vault = 100001

    stark_account = StarkPerpetualAccount(
        vault=vault,
        private_key=private_key,
        public_key=public_key,
        api_key=api_key,
    )

    client = BlockingTradingClient(endpoint_config=TESTNET_CONFIG, account=stark_account)

    placed_order = await client.create_and_place_order(
        amount_of_synthetic=Decimal("1"),
        price=Decimal("62133.6"),
        market_name="BTC-USD",
        side=OrderSide.BUY,
        post_only=False,
    )

    print(placed_order)

    await client.cancel_order(placed_order.id)


if __name__ == "__main__":
    asyncio.run(main=setup_and_run())



================================================
FILE: examples/stream_example.py
================================================
import asyncio
import logging
import signal

from examples.utils import init_logging
from x10.perpetual.configuration import TESTNET_CONFIG
from x10.perpetual.stream_client import PerpetualStreamClient

API_KEY = "<API_KEY>"


async def iterator_example():
    logger = logging.getLogger("stream_example[iterator_example]")
    stream_client = PerpetualStreamClient(api_url=TESTNET_CONFIG.stream_url)
    stream = await stream_client.subscribe_to_account_updates(API_KEY)

    async for event in stream:
        logger.info(event)


async def manual_example():
    logger = logging.getLogger("stream_example[manual_example]")
    stream_client = PerpetualStreamClient(api_url=TESTNET_CONFIG.stream_url)
    stream = await stream_client.subscribe_to_account_updates(API_KEY)

    event1 = await stream.recv()
    event2 = await stream.recv()

    logger.info("Event #1: %s", event1)
    logger.info("Event #2: %s", event2)

    # etc

    await stream.close()


async def context_manager_example():
    logger = logging.getLogger("stream_example[context_manager_example]")
    stream_client = PerpetualStreamClient(api_url=TESTNET_CONFIG.stream_url)

    async with stream_client.subscribe_to_orderbooks("BTC-USD") as stream:
        msg1 = await stream.recv()
        msg2 = await stream.recv()

        logger.info("Message #1: %s", msg1)
        logger.info("Message #2: %s", msg2)

        # etc


async def merge_streams_example():
    logger = logging.getLogger("stream_example[merge_streams_example]")
    stop_event = asyncio.Event()

    def sigint_handler(sig, frame):
        logger.info("Interrupted by the user, stopping...")
        stop_event.set()

    signal.signal(signal.SIGINT, sigint_handler)

    stream_client = PerpetualStreamClient(api_url=TESTNET_CONFIG.stream_url)
    queue = asyncio.Queue()

    async def run_producer_stream1():
        async with stream_client.subscribe_to_orderbooks("BTC-USD") as stream1:
            while not stop_event.is_set():
                msg = await asyncio.wait_for(stream1.recv(), timeout=5)
                await queue.put(("stream1", msg))

                if stream1.msgs_count == 5:
                    logger.info("Stream #1 produced 5 messages, stopping...")
                    break

    async def run_producer_stream2():
        async with stream_client.subscribe_to_account_updates(API_KEY) as stream2:
            while not stop_event.is_set():
                msg = await asyncio.wait_for(stream2.recv(), timeout=5)
                await queue.put(("stream2", msg))

                if stream2.msgs_count == 3:
                    logger.info("Stream #2 produced 3 messages, stopping...")
                    break

    async def run_consumer():
        while not stop_event.is_set():
            try:
                msg = await asyncio.wait_for(queue.get(), timeout=5)
                logger.info("Message: %s", msg)
                queue.task_done()
            except asyncio.TimeoutError:
                logger.info("No messages received in the last 5 seconds, stopping...")
                break

    await asyncio.gather(run_producer_stream1(), run_producer_stream2(), run_consumer())


async def main():
    await iterator_example()


if __name__ == "__main__":
    init_logging()
    asyncio.run(main=main())



================================================
FILE: examples/utils.py
================================================
import logging
import logging.config
import logging.handlers
from pathlib import Path

import yaml


def init_logging():
    config_as_str = Path(__file__).parent.joinpath("./logger.yml").read_text()

    config = yaml.safe_load(config_as_str)
    logging.config.dictConfig(config)



================================================
FILE: examples/withdrawal_example.py
================================================
from asyncio import run
from decimal import Decimal

from x10.perpetual.accounts import StarkPerpetualAccount
from x10.perpetual.configuration import MAINNET_CONFIG
from x10.perpetual.trading_client import PerpetualTradingClient


async def setup_and_run():
    stark_account = StarkPerpetualAccount(
        vault=1337,
        private_key="<>",
        public_key="<>",
        api_key="<>",
    )
    trading_client = PerpetualTradingClient(
        endpoint_config=MAINNET_CONFIG,
        stark_account=stark_account,
    )

    await trading_client.account.slow_withdrawal(
        amount=Decimal("20"), eth_address="0x9361F2761cc1349ceA6606D4Bc6f048c1E4881d1"
    )

    print("Withdrawal complete")
    print("press enter to continue")
    input()


if __name__ == "__main__":
    run(main=setup_and_run())



================================================
FILE: examples/x10_throughput_latency_test.py
================================================
import asyncio
import dataclasses
import logging
import logging.config
import logging.handlers
import os
from asyncio import run
from decimal import Decimal
from multiprocessing import Process, Queue
from typing import List, Optional

from dotenv import load_dotenv

from x10.perpetual.accounts import StarkPerpetualAccount
from x10.perpetual.configuration import TESTNET_CONFIG
from x10.perpetual.orderbook import OrderBook
from x10.perpetual.orders import OrderSide
from x10.perpetual.simple_client.simple_trading_client import BlockingTradingClient
from x10.perpetual.trading_client import PerpetualTradingClient

NUM_PRICE_LEVELS = 1

PLACE = "PLACE"
CANCEL = "CANCEL"
NANOS_IN_SECOND = 1000 * 1000 * 1000


@dataclasses.dataclass(frozen=True)
class TimedOperation:
    name: str
    start_nanos: int
    end_nanos: int
    operation_ms: float


@dataclasses.dataclass(frozen=True)
class TimeSeriesChunk:
    start_ns: int
    end_ns: int
    mean_operation_latency_ms: float
    std_dev_operation_latency_ms: float
    throughput: float


async def clean_it(trading_client: PerpetualTradingClient, market_name: str | None = None):
    logger = logging.getLogger("placed_order_example")
    positions = await trading_client.account.get_positions()
    logger.info("Positions: %s", positions.to_pretty_json())
    balance = await trading_client.account.get_balance()
    logger.info("Balance: %s", balance.to_pretty_json())
    open_orders = await trading_client.account.get_open_orders(market_names=[market_name] if market_name else None)
    await trading_client.orders.mass_cancel(order_ids=[order.id for order in open_orders.data])


async def setup_and_run(base: str = "BTC", queue: Optional[Queue] = None):
    market_name = f"{base}-USD"
    print("Running for market: ", market_name)
    load_dotenv(f"./env/{base}.env")
    API_KEY = os.environ["X10_API_KEY"]
    PUBLIC_KEY = os.environ["X10_PUBLIC_KEY"]
    PRIVATE_KEY = os.environ["X10_PRIVATE_KEY"]
    VAULT_ID = int(os.environ["X10_VAULT_ID"])

    stark_account = StarkPerpetualAccount(
        vault=VAULT_ID,
        private_key=PRIVATE_KEY,
        public_key=PUBLIC_KEY,
        api_key=API_KEY,
    )
    trading_client = PerpetualTradingClient(
        endpoint_config=TESTNET_CONFIG,
        stark_account=stark_account,
    )

    positions = await trading_client.account.get_positions()
    for position in positions.data:
        print(
            f"market: {position.market} \
            side: {position.side} \
            size: {position.size} \
            mark_price: ${position.mark_price} \
            leverage: {position.leverage}"
        )
        print(f"consumed im: ${round((position.size * position.mark_price) / position.leverage, 2)}")

    await clean_it(trading_client)

    blocking_client = BlockingTradingClient(
        endpoint_config=TESTNET_CONFIG,
        account=stark_account,
    )

    markets = await blocking_client.get_markets()
    market = markets[market_name]

    orderbook = await OrderBook.create(
        endpoint_config=TESTNET_CONFIG,
        market_name=market_name,
    )

    await orderbook.start_orderbook()

    def order_loop(idx: int, side: OrderSide, outbound_queue: Optional[Queue] = None) -> asyncio.Task:
        side_adjustment = Decimal("-1") if side == OrderSide.BUY else Decimal("1")
        base_offset = side_adjustment * Decimal("0.02")

        async def inner():
            while True:
                baseline_price = orderbook.best_bid() if side == OrderSide.BUY else orderbook.best_ask()
                if baseline_price:
                    order_price = round(
                        (baseline_price.price + baseline_price.price * base_offset)
                        + side_adjustment * market.trading_config.min_price_change * idx,
                        market.trading_config.price_precision,
                    )
                    timed_place = await blocking_client.create_and_place_order(
                        market_name=market_name,
                        amount_of_synthetic=market.trading_config.min_order_size,
                        price=order_price,
                        side=side,
                        post_only=True,
                    )
                    queue.put(
                        TimedOperation(
                            PLACE,
                            timed_place.start_nanos,
                            timed_place.end_nanos,
                            timed_place.operation_ms,
                        )
                    )
                    timed_cancel = await blocking_client.cancel_order(order_id=timed_place.id)
                    queue.put(
                        TimedOperation(
                            CANCEL,
                            timed_cancel.start_nanos,
                            timed_cancel.end_nanos,
                            timed_cancel.operation_ms,
                        )
                    )
                else:
                    print("No baseline price for market", market_name)
                    await asyncio.sleep(1)

        return asyncio.get_running_loop().create_task(inner())

    sell_tasks = list(
        map(
            lambda idx: order_loop(idx, OrderSide.SELL, outbound_queue=queue),
            range(NUM_PRICE_LEVELS),
        )
    )
    buy_tasks = list(
        map(
            lambda idx: order_loop(idx, OrderSide.BUY, outbound_queue=queue),
            range(NUM_PRICE_LEVELS),
        )
    )

    for task in sell_tasks:
        print(await task)
    for task in buy_tasks:
        print(await task)


def entry_point(base: str, queue: Queue):
    run(main=setup_and_run(base=base, queue=queue))


if __name__ == "__main__":
    markets = ["BTC", "ETH"]
    cancels: List[TimedOperation] = []
    cancels_chunks: List[TimeSeriesChunk] = []
    places: List[TimedOperation] = []
    place_chunks: List[TimeSeriesChunk] = []

    q: "Queue[TimedOperation]" = Queue()
    subprocesses = map(lambda market: Process(target=entry_point, args=[market, q]), markets)

    for p in subprocesses:
        p.start()

    import csv
    import threading

    cancel_file = open("cancel.csv", "w")
    place_file = open("place.csv", "w")
    cancels_csv = csv.DictWriter(cancel_file, fieldnames=list(TimeSeriesChunk.__annotations__.keys()))
    places_csv = csv.DictWriter(place_file, fieldnames=list(TimeSeriesChunk.__annotations__.keys()))

    poison_pill = None

    def handle_operation(
        new_operation: TimedOperation, list: List[TimedOperation], chunks: List[TimeSeriesChunk]
    ) -> TimeSeriesChunk | None:
        list.append(new_operation)
        newest = new_operation.end_nanos
        oldest = list[0].start_nanos
        if newest - oldest > NANOS_IN_SECOND:
            latencies = [operation.operation_ms for operation in list]
            mean_latency = round(sum(latencies) / len(latencies), 1)
            latency_std_dev = round((sum((x - mean_latency) ** 2 for x in latencies) / len(latencies)) ** 0.5, 1)
            throughput_per_second = round(len(list) / ((newest - oldest) / NANOS_IN_SECOND), 1)
            chunk = TimeSeriesChunk(
                start_ns=oldest,
                end_ns=newest,
                mean_operation_latency_ms=mean_latency,
                std_dev_operation_latency_ms=latency_std_dev,
                throughput=throughput_per_second,
            )
            chunks.append(chunk)
            list.clear()
            return chunk
        return None

    def read_queue():
        cancels_csv.writeheader()
        places_csv.writeheader()
        while True:
            element: TimedOperation = q.get()
            if element == poison_pill:
                break
            if element.name == PLACE:
                chunk = handle_operation(element, places, place_chunks)
                if chunk:
                    places_csv.writerow(dataclasses.asdict(chunk))
                    place_file.flush()
            elif element.name == CANCEL:
                chunk = handle_operation(element, cancels, cancels_chunks)
                if chunk:
                    cancels_csv.writerow(dataclasses.asdict(chunk))
                    cancel_file.flush()
        cancel_file.close()
        place_file.close()
        print("Exiting queue reader")

    queue_reader = threading.Thread(target=read_queue)
    queue_reader.start()

    import signal
    import sys

    def signal_handler(sig, frame):
        print("You pressed Ctrl+C!")
        q.put(None)
        for p in subprocesses:
            p.kill()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    print("Press Ctrl+C to exit")
    signal.pause()



================================================
FILE: tests/conftest.py
================================================
import pytest


@pytest.fixture
def create_accounts():
    from tests.fixtures.accounts import create_accounts as _create_accounts

    return _create_accounts


@pytest.fixture
def create_trading_account():
    from tests.fixtures.accounts import (
        create_trading_account as _create_trading_account,
    )

    return _create_trading_account


@pytest.fixture
def btc_usd_market_json_data():
    from tests.fixtures.markets import get_btc_usd_market_json_data

    return get_btc_usd_market_json_data()


@pytest.fixture
def create_btc_usd_market(btc_usd_market_json_data):
    from tests.fixtures.markets import create_btc_usd_market as _create_btc_usd_market

    return lambda: _create_btc_usd_market(btc_usd_market_json_data)


@pytest.fixture
def create_orderbook_message():
    from tests.fixtures.orderbook import (
        create_orderbook_message as _create_orderbook_message,
    )

    return _create_orderbook_message


@pytest.fixture
def create_account_update_trade_message():
    from tests.fixtures.accounts import (
        create_account_update_trade_message as _create_account_update_trade_message,
    )

    return _create_account_update_trade_message


@pytest.fixture
def create_account_update_unknown_message():
    from tests.fixtures.accounts import (
        create_account_update_unknown_message as _create_account_update_unknown_message,
    )

    return _create_account_update_unknown_message


@pytest.fixture
def create_asset_operations():
    from tests.fixtures.assets import (
        create_asset_operations as _create_asset_operations,
    )

    return _create_asset_operations



================================================
FILE: tests/fixtures/accounts.py
================================================
from decimal import Decimal

from x10.perpetual.accounts import AccountModel


def create_accounts():
    return [
        AccountModel(
            status="ACTIVE",
            l2_key="0x6970ac7180192cb58070d639064408610d0fbfd3b16c6b2c6219b9d91aa456f",
            l2_vault="10001",
            account_index=0,
            id=1001,
            description="Account 1",
            api_keys=[],
        ),
        AccountModel(
            status="ACTIVE",
            l2_key="0x3895139a98a6168dc8b0db251bcd0e6dcf97fd1e96f7a87d9bd3f341753a844",
            l2_vault="10002",
            account_index=1,
            id=1002,
            description="Account 2",
            api_keys=[],
        ),
    ]


def create_trading_account():
    from x10.perpetual.accounts import StarkPerpetualAccount

    return StarkPerpetualAccount(
        vault=10002,
        private_key="0x7a7ff6fd3cab02ccdcd4a572563f5976f8976899b03a39773795a3c486d4986",
        public_key="0x61c5e7e8339b7d56f197f54ea91b776776690e3232313de0f2ecbd0ef76f466",
        api_key="dummy_api_key",
    )


def create_account_update_trade_message():
    from x10.perpetual.accounts import AccountStreamDataModel
    from x10.perpetual.trades import AccountTradeModel
    from x10.utils.http import WrappedStreamResponse

    return WrappedStreamResponse[AccountStreamDataModel](
        type="TRADE",
        data=AccountStreamDataModel(
            trades=[
                AccountTradeModel(
                    id=1811328331296018432,
                    account_id=3004,
                    market="BTC-USD",
                    order_id=1811328331287359488,
                    side="BUY",
                    price=Decimal("58249.8000000000000000"),
                    qty=Decimal("0.0010000000000000"),
                    value=Decimal("58.2498000000000000"),
                    fee=Decimal("0.0291240000000000"),
                    is_taker=True,
                    trade_type="TRADE",
                    created_time=1720689301691,
                )
            ]
        ),
        ts=1704798222748,
        seq=570,
    )


def create_account_update_unknown_message():
    from x10.perpetual.accounts import AccountStreamDataModel
    from x10.utils.http import WrappedStreamResponse

    return WrappedStreamResponse[AccountStreamDataModel](
        type="UNEXPECTED",
        data=None,
        ts=1704798222748,
        seq=570,
    )



================================================
FILE: tests/fixtures/assets.py
================================================
from decimal import Decimal

from x10.perpetual.assets import AssetOperationModel


def create_asset_operations():
    return [
        AssetOperationModel(
            id="1816814506626514944",
            type="TRANSFER",
            status="COMPLETED",
            amount=Decimal("-100.0000000000000000"),
            fee=Decimal("0"),
            asset=1,
            time=1721997307818,
            account_id=3004,
            counterparty_account_id=7349,
        ),
        AssetOperationModel(
            id="1813548171448147968",
            type="CLAIM",
            status="COMPLETED",
            amount=Decimal("100000.0000000000000000"),
            fee=Decimal("0"),
            asset=1,
            time=1721218552833,
            account_id=3004,
        ),
    ]



================================================
FILE: tests/fixtures/candles.py
================================================
from typing import List

from x10.perpetual.candles import CandleModel
from x10.utils.http import WrappedStreamResponse


def create_candle_stream_message():
    return WrappedStreamResponse[List[CandleModel]](
        data=[
            CandleModel(
                open="3458.64", low="3399.07", high="3476.89", close="3414.85", volume="3.938", timestamp=1721106000000
            )
        ],
        ts=1721283121979,
        seq=1,
    )



================================================
FILE: tests/fixtures/markets.py
================================================
from typing import List


def get_btc_usd_market_json_data():
    return """
    {
        "status": "OK",
        "data": [
            {
                "name": "BTC-USD",
                "category": "L1",
                "assetName": "BTC",
                "assetPrecision": 5,
                "collateralAssetName": "USD",
                "collateralAssetPrecision": 6,
                "active": true,
                "marketStats": {
                    "dailyVolume": "2410800.768021",
                    "dailyVolumeBase": "37.94502",
                    "dailyPriceChange": "969.9",
                    "dailyPriceChangePercentage": "0.02",
                    "dailyLow": "62614.8",
                    "dailyHigh": "64421.1",
                    "lastPrice": "64280.0",
                    "askPrice": "64268.2",
                    "bidPrice": "64235.9",
                    "markPrice": "64267.380482593245",
                    "indexPrice": "64286.409493065992",
                    "fundingRate": "-0.000034",
                    "nextFundingRate": 1715072400000,
                    "openInterest": "150629.886375",
                    "openInterestBase": "2.34380",
                    "deleverageLevels": {
                        "shortPositions": [
                            {
                                "level": 1,
                                "rankingLowerBound": "-5919.3176"
                            },
                            {
                                "level": 2,
                                "rankingLowerBound": "-1.8517"
                            }
                        ],
                        "longPositions": [
                            {
                                "level": 1,
                                "rankingLowerBound": "0.0000"
                            },
                            {
                                "level": 2,
                                "rankingLowerBound": "0.0000"
                            }
                        ]
                    }
                },
                "tradingConfig": {
                    "minOrderSize": "0.0001",
                    "minOrderSizeChange": "0.00001",
                    "minPriceChange": "0.1",
                    "maxMarketOrderValue": "1000000",
                    "maxLimitOrderValue": "5000000",
                    "maxPositionValue": "10000000",
                    "maxLeverage": "50.00",
                    "maxNumOrders": "200",
                    "limitPriceCap": "0.05",
                    "limitPriceFloor": "0.05",
                    "riskFactorConfig": [
                        {
                            "upperBound": "400000",
                            "riskFactor": "0.02"
                        },
                        {
                            "upperBound": "800000",
                            "riskFactor": "0.04"
                        },
                        {
                            "upperBound": "1200000",
                            "riskFactor": "0.06"
                        },
                        {
                            "upperBound": "1600000",
                            "riskFactor": "0.08"
                        },
                        {
                            "upperBound": "2000000",
                            "riskFactor": "0.1"
                        },
                        {
                            "upperBound": "2400000",
                            "riskFactor": "0.12"
                        },
                        {
                            "upperBound": "2800000",
                            "riskFactor": "0.14"
                        },
                        {
                            "upperBound": "3200000",
                            "riskFactor": "0.16"
                        },
                        {
                            "upperBound": "3600000",
                            "riskFactor": "0.18"
                        },
                        {
                            "upperBound": "4000000",
                            "riskFactor": "0.2"
                        },
                        {
                            "upperBound": "4400000",
                            "riskFactor": "0.22"
                        },
                        {
                            "upperBound": "4800000",
                            "riskFactor": "0.24"
                        },
                        {
                            "upperBound": "5200000",
                            "riskFactor": "0.26"
                        },
                        {
                            "upperBound": "5600000",
                            "riskFactor": "0.28"
                        },
                        {
                            "upperBound": "6000000",
                            "riskFactor": "0.3"
                        },
                        {
                            "upperBound": "6400000",
                            "riskFactor": "0.32"
                        },
                        {
                            "upperBound": "6800000",
                            "riskFactor": "0.34"
                        },
                        {
                            "upperBound": "7200000",
                            "riskFactor": "0.36"
                        },
                        {
                            "upperBound": "7600000",
                            "riskFactor": "0.38"
                        },
                        {
                            "upperBound": "8000000",
                            "riskFactor": "0.4"
                        },
                        {
                            "upperBound": "8400000",
                            "riskFactor": "0.42"
                        },
                        {
                            "upperBound": "8800000",
                            "riskFactor": "0.44"
                        },
                        {
                            "upperBound": "9200000",
                            "riskFactor": "0.46"
                        },
                        {
                            "upperBound": "9600000",
                            "riskFactor": "0.48"
                        },
                        {
                            "upperBound": "10000000",
                            "riskFactor": "0.5"
                        },
                        {
                            "upperBound": "1000000000",
                            "riskFactor": "1"
                        }
                    ]
                },
                "l2Config": {
                    "type": "STARKX",
                    "collateralId": "0x31857064564ed0ff978e687456963cba09c2c6985d8f9300a1de4962fafa054",
                    "syntheticId": "0x4254432d3600000000000000000000",
                    "syntheticResolution": 1000000,
                    "collateralResolution": 1000000
                }
            }
        ]
    }
    """


def create_btc_usd_market(json_data: str):
    from x10.perpetual.markets import MarketModel
    from x10.utils.http import WrappedApiResponse

    result = WrappedApiResponse[List[MarketModel]].model_validate_json(json_data)

    assert result.data

    return result.data[0]



================================================
FILE: tests/fixtures/orderbook.py
================================================
from decimal import Decimal


def create_orderbook_message():
    from x10.perpetual.orderbooks import OrderbookQuantityModel, OrderbookUpdateModel
    from x10.utils.http import WrappedStreamResponse

    return WrappedStreamResponse[OrderbookUpdateModel](
        type="SNAPSHOT",
        data=OrderbookUpdateModel(
            market="BTC-USD",
            bid=[
                OrderbookQuantityModel(qty=Decimal("0.008"), price=Decimal("43547.00")),
                OrderbookQuantityModel(qty=Decimal("0.007000"), price=Decimal("43548.00")),
            ],
            ask=[OrderbookQuantityModel(qty=Decimal("0.008"), price=Decimal("43546.00"))],
        ),
        ts=1704798222748,
        seq=570,
    )



================================================
FILE: tests/perpetual/test_l2_key_derivation.py
================================================
from eth_account import Account


def test_known_l2_accounts():
    from x10.perpetual.user_client.onboarding import get_l2_keys_from_l1_account

    known_private_key = "50c8e358cc974aaaa6e460641e53f78bdc550fd372984aa78ef8fd27c751e6f4"
    known_l2_private_key = "0x7dbb2c8651cc40e1d0d60b45eb52039f317a8aa82798bda52eee272136c0c44"
    known_l2_public_key = "0x78298687996aff29a0bbcb994e1305db082d084f85ec38bb78c41e6787740ec"

    derived_keys = get_l2_keys_from_l1_account(Account.from_key(known_private_key), 0, signing_domain="x10.exchange")
    assert derived_keys.private_hex == known_l2_private_key
    assert derived_keys.public_hex == known_l2_public_key



================================================
FILE: tests/perpetual/test_onboarding_payload.py
================================================
import datetime

from eth_account import Account

from x10.perpetual.user_client.onboarding import get_l2_keys_from_l1_account


def test_onboarding_object_generation():
    # all known values from authentication service tests
    from x10.perpetual.user_client.onboarding import get_onboarding_payload

    known_private_key = "50c8e358cc974aaaa6e460641e53f78bdc550fd372984aa78ef8fd27c751e6f4"
    known_l2_public_key = "0x78298687996aff29a0bbcb994e1305db082d084f85ec38bb78c41e6787740ec"

    l1_account = Account.from_key(known_private_key)
    key_pair = get_l2_keys_from_l1_account(l1_account=l1_account, account_index=0, signing_domain="x10.exchange")

    payload = get_onboarding_payload(
        account=l1_account,
        time=datetime.datetime(
            year=2024,
            month=7,
            day=30,
            hour=16,
            minute=1,
            second=2,
            tzinfo=datetime.timezone.utc,
        ),
        key_pair=key_pair,
        signing_domain="x10.exchange",
    ).to_json()

    assert (
        payload["l1Signature"]
        == "0x4b093c2a0206dfa8bc2d09832947a4a567d80a4bfcec14c9874ac2aefcdcf60526c4973007696f26395e75af2383a89fbabe76c5a7a787b5a765f92a4067c58b1c"  # noqa: E501
    )

    assert payload["l2Key"] == known_l2_public_key
    assert payload["l2Signature"]["r"] == "0x70881694c59c7212b1a47fbbc07df4d32678f0326f778861ec3a2a5dbc09157"
    assert payload["l2Signature"]["s"] == "0x558805193faa5d780719cba5f699ae1c888eec1fee23da4215fdd94a744d2cb"
    assert payload["accountCreation"]["time"] == "2024-07-30T16:01:02Z"
    assert payload["accountCreation"]["action"] == "REGISTER"
    assert payload["accountCreation"]["tosAccepted"] is True



================================================
FILE: tests/perpetual/test_order_object.py
================================================
from datetime import timedelta
from decimal import Decimal

import pytest
from freezegun import freeze_time
from hamcrest import assert_that, equal_to, has_entries
from pytest_mock import MockerFixture

from x10.perpetual.orders import OrderSide, SelfTradeProtectionLevel
from x10.utils.date import utc_now

FROZEN_NONCE = 1473459052


@pytest.mark.asyncio
async def test_create_sell_order_with_default_expiration(
    mocker: MockerFixture, create_trading_account, create_btc_usd_market
):
    mocker.patch("x10.utils.starkex.generate_nonce", return_value=FROZEN_NONCE)

    freezer = freeze_time("2024-01-05 01:08:56.860694")
    frozen_time = freezer.start()

    from x10.perpetual.order_object import create_order_object

    frozen_time.move_to("2024-01-05 01:08:57")

    trading_account = create_trading_account()
    btc_usd_market = create_btc_usd_market()
    order_obj = create_order_object(
        account=trading_account,
        market=btc_usd_market,
        amount_of_synthetic=Decimal("0.00100000"),
        price=Decimal("43445.11680000"),
        side=OrderSide.SELL,
    )

    freezer.stop()

    assert_that(
        order_obj.to_api_request_json(),
        equal_to(
            {
                "id": "2096045681239655445582070517240411138302380632690430411530650608228763263945",
                "market": "BTC-USD",
                "type": "LIMIT",
                "side": "SELL",
                "qty": "0.00100000",
                "price": "43445.11680000",
                "reduceOnly": False,
                "postOnly": False,
                "timeInForce": "GTT",
                "expiryEpochMillis": 1704445737000,
                "fee": "0.0005",
                "nonce": "1473459052",
                "selfTradeProtectionLevel": "ACCOUNT",
                "cancelId": None,
                "settlement": {
                    "signature": {
                        "r": "0x39ff8493e8e26c9a588a7046e1380b6e1201287a179e10831b7040d3efc26d",
                        "s": "0x5c9acd1879bf8d43e4ccd14648186d2a9edf387fe1b61e491fe0a539de3272b",
                    },
                    "starkKey": "0x61c5e7e8339b7d56f197f54ea91b776776690e3232313de0f2ecbd0ef76f466",
                    "collateralPosition": "10002",
                },
                "trigger": None,
                "tpSlType": None,
                "takeProfit": None,
                "stopLoss": None,
                "debuggingAmounts": {"collateralAmount": "43445116", "feeAmount": "21723", "syntheticAmount": "1000"},
            }
        ),
    )


@freeze_time("2024-01-05 01:08:56.860694")
@pytest.mark.asyncio
async def test_create_sell_order(mocker: MockerFixture, create_trading_account, create_btc_usd_market):
    mocker.patch("x10.utils.starkex.generate_nonce", return_value=FROZEN_NONCE)

    from x10.perpetual.order_object import create_order_object

    trading_account = create_trading_account()
    btc_usd_market = create_btc_usd_market()
    order_obj = create_order_object(
        account=trading_account,
        market=btc_usd_market,
        amount_of_synthetic=Decimal("0.00100000"),
        price=Decimal("43445.11680000"),
        side=OrderSide.SELL,
        expire_time=utc_now() + timedelta(days=14),
    )

    assert_that(
        order_obj.to_api_request_json(),
        equal_to(
            {
                "id": "2656406151911156282898770907232061209407892373872976831396563134482995247110",
                "market": "BTC-USD",
                "type": "LIMIT",
                "side": "SELL",
                "qty": "0.00100000",
                "price": "43445.11680000",
                "reduceOnly": False,
                "postOnly": False,
                "timeInForce": "GTT",
                "expiryEpochMillis": 1705626536860,
                "fee": "0.0005",
                "nonce": "1473459052",
                "selfTradeProtectionLevel": "ACCOUNT",
                "cancelId": None,
                "settlement": {
                    "signature": {
                        "r": "0x5766fe0420270feadb55cd6d89cedba0bb8cbd3847fca73d27fe78b0c499b48",
                        "s": "0xc8456b2db2060d25990471f22cae59bed86d51e508812455458f0464cc5867",
                    },
                    "starkKey": "0x61c5e7e8339b7d56f197f54ea91b776776690e3232313de0f2ecbd0ef76f466",
                    "collateralPosition": "10002",
                },
                "trigger": None,
                "tpSlType": None,
                "takeProfit": None,
                "stopLoss": None,
                "debuggingAmounts": {"collateralAmount": "43445116", "feeAmount": "21723", "syntheticAmount": "1000"},
            }
        ),
    )


@freeze_time("2024-01-05 01:08:56.860694")
@pytest.mark.asyncio
async def test_create_buy_order(mocker: MockerFixture, create_trading_account, create_btc_usd_market):
    mocker.patch("x10.utils.starkex.generate_nonce", return_value=FROZEN_NONCE)

    from x10.perpetual.order_object import create_order_object

    trading_account = create_trading_account()
    btc_usd_market = create_btc_usd_market()
    order_obj = create_order_object(
        account=trading_account,
        market=btc_usd_market,
        amount_of_synthetic=Decimal("0.00100000"),
        price=Decimal("43445.11680000"),
        side=OrderSide.BUY,
        expire_time=utc_now() + timedelta(days=14),
        self_trade_protection_level=SelfTradeProtectionLevel.CLIENT,
    )

    assert_that(
        order_obj.to_api_request_json(),
        equal_to(
            {
                "id": "1166889461421716582054747865777410838520755143669870072976787470981175645302",
                "market": "BTC-USD",
                "type": "LIMIT",
                "side": "BUY",
                "qty": "0.00100000",
                "price": "43445.11680000",
                "reduceOnly": False,
                "postOnly": False,
                "timeInForce": "GTT",
                "expiryEpochMillis": 1705626536860,
                "fee": "0.0005",
                "nonce": "1473459052",
                "selfTradeProtectionLevel": "CLIENT",
                "cancelId": None,
                "settlement": {
                    "signature": {
                        "r": "0x52a42b6cb980b552c08d5d01b86852b64f7468f5ed7430133f0e2ea1b53df0",
                        "s": "0x67287f8aca9f96bc0fa58e5f0f6875e52f869fc392d912145ff9cb16b73a666",
                    },
                    "starkKey": "0x61c5e7e8339b7d56f197f54ea91b776776690e3232313de0f2ecbd0ef76f466",
                    "collateralPosition": "10002",
                },
                "trigger": None,
                "tpSlType": None,
                "takeProfit": None,
                "stopLoss": None,
                "debuggingAmounts": {"collateralAmount": "43445117", "feeAmount": "21723", "syntheticAmount": "1000"},
            }
        ),
    )


@freeze_time("2024-01-05 01:08:56.860694")
@pytest.mark.asyncio
async def test_cancel_previous_order(mocker: MockerFixture, create_trading_account, create_btc_usd_market):
    mocker.patch("x10.utils.starkex.generate_nonce", return_value=FROZEN_NONCE)

    from x10.perpetual.order_object import create_order_object

    trading_account = create_trading_account()
    btc_usd_market = create_btc_usd_market()
    order_obj = create_order_object(
        account=trading_account,
        market=btc_usd_market,
        amount_of_synthetic=Decimal("0.00100000"),
        price=Decimal("43445.11680000"),
        side=OrderSide.BUY,
        expire_time=utc_now() + timedelta(days=14),
        previous_order_id="previous_custom_id",
    )

    assert_that(
        order_obj.to_api_request_json(),
        has_entries(
            {
                "cancelId": equal_to("previous_custom_id"),
            }
        ),
    )


@freeze_time("2024-01-05 01:08:56.860694")
@pytest.mark.asyncio
async def test_external_order_id(mocker: MockerFixture, create_trading_account, create_btc_usd_market):
    mocker.patch("x10.utils.starkex.generate_nonce", return_value=FROZEN_NONCE)

    from x10.perpetual.order_object import create_order_object

    trading_account = create_trading_account()
    btc_usd_market = create_btc_usd_market()
    order_obj = create_order_object(
        account=trading_account,
        market=btc_usd_market,
        amount_of_synthetic=Decimal("0.00100000"),
        price=Decimal("43445.11680000"),
        side=OrderSide.BUY,
        expire_time=utc_now() + timedelta(days=14),
        order_external_id="custom_id",
    )

    assert_that(
        order_obj.to_api_request_json(),
        has_entries(
            {
                "id": equal_to("custom_id"),
            }
        ),
    )



================================================
FILE: tests/perpetual/test_orderbook_price_impact.py
================================================
import decimal
from unittest import TestCase

from x10.perpetual.configuration import TESTNET_CONFIG
from x10.perpetual.orderbook import OrderBook
from x10.perpetual.orderbooks import OrderbookUpdateModel


class TestOrderBook(TestCase):
    def setUp(self):
        self.endpoint_config = TESTNET_CONFIG
        self.market_name = "dummy-market"
        self.orderbook = OrderBook(
            self.endpoint_config,
            self.market_name,
            best_ask_change_callback=None,
            best_bid_change_callback=None,
        )
        self.populate_dummy_data()

    def populate_dummy_data(self):
        dummy_data = OrderbookUpdateModel(
            market=self.market_name,
            bid=[
                {"price": decimal.Decimal("100"), "qty": decimal.Decimal("1")},
                {"price": decimal.Decimal("99"), "qty": decimal.Decimal("2")},
                {"price": decimal.Decimal("98"), "qty": decimal.Decimal("1")},
            ],
            ask=[
                {"price": decimal.Decimal("101"), "qty": decimal.Decimal("1")},
                {"price": decimal.Decimal("102"), "qty": decimal.Decimal("2")},
                {"price": decimal.Decimal("103"), "qty": decimal.Decimal("1")},
            ],
        )
        self.orderbook.update_orderbook(dummy_data)

    def test_calculate_impact_partial_buy(self):
        notional = decimal.Decimal("105")
        expected_amount = decimal.Decimal("1") + decimal.Decimal("4") / decimal.Decimal("102")
        expected_average_price = notional / expected_amount
        result = self.orderbook.calculate_price_impact_notional(notional, "BUY")
        self.assertEqual(result.amount, expected_amount)
        self.assertEqual(result.price, expected_average_price)

    def test_calculate_impact_partial_sell(self):
        notional = decimal.Decimal("110")
        expected_amount = decimal.Decimal(1) + decimal.Decimal("10") / decimal.Decimal("99")
        expected_average_price = notional / expected_amount
        result = self.orderbook.calculate_price_impact_notional(notional, "SELL")
        self.assertEqual(result.amount, expected_amount)
        self.assertEqual(result.price, expected_average_price)

    def test_calculate_price_impact_total_match_sell(self):
        notional = decimal.Decimal("199")
        expected_amount = decimal.Decimal("2")
        expected_average_price = notional / expected_amount
        result = self.orderbook.calculate_price_impact_notional(notional, "SELL")
        self.assertEqual(result.amount, expected_amount)
        self.assertEqual(result.price, expected_average_price)

    def test_calculate_price_impact_total_match_buy(self):
        notional = decimal.Decimal("101") + decimal.Decimal("2") * decimal.Decimal("102") + decimal.Decimal("103")
        expected_amount = decimal.Decimal("4")
        expected_average_price = notional / expected_amount
        result = self.orderbook.calculate_price_impact_notional(notional, "BUY")
        self.assertEqual(result.amount, expected_amount)
        self.assertEqual(result.price, expected_average_price)

    def test_calculate_price_impact_insufficient_liquidity_bid(self):
        notional = decimal.Decimal("1000")
        result = self.orderbook.calculate_price_impact_notional(notional, "SELL")
        self.assertIsNone(result)

    def test_calculate_price_impact_insufficient_liquidity_ask(self):
        notional = decimal.Decimal("1000")
        result = self.orderbook.calculate_price_impact_notional(notional, "BUY")
        self.assertIsNone(result)

    def test_calculate_price_impact_invalid_notional(self):
        notional = decimal.Decimal("-10")
        result = self.orderbook.calculate_price_impact_notional(notional, "SELL")
        self.assertIsNone(result)

    def test_calculate_price_impact_invalid_side(self):
        notional = decimal.Decimal("100")
        result = self.orderbook.calculate_price_impact_notional(notional, "invalid")
        self.assertIsNone(result)

    def test_calculate_qty_impact_partial_buy(self):
        """
        Buy a partial quantity that spans multiple ask levels.
        For example: buying 2 units:
          - 1 unit at price 101
          - 1 unit at price 102
        total cost = 101 + 102 = 203
        average price = 203 / 2 = 101.5
        """
        qty = decimal.Decimal("2")
        result = self.orderbook.calculate_price_impact_qty(qty, "BUY")

        self.assertIsNotNone(result, "Result should not be None for partial fill.")
        self.assertEqual(result.amount, qty, "Filled amount should match requested qty.")

        expected_average_price = decimal.Decimal("101.5")
        self.assertEqual(result.price, expected_average_price)

    def test_calculate_qty_impact_partial_sell(self):
        """
        Sell a partial quantity that spans multiple bid levels.
        For example: selling 2 units:
          - 1 unit at price 100
          - 1 unit at price 99
        total received = 100 + 99 = 199
        average price = 199 / 2 = 99.5
        """
        qty = decimal.Decimal("2")
        result = self.orderbook.calculate_price_impact_qty(qty, "SELL")

        self.assertIsNotNone(result, "Result should not be None for partial fill.")
        self.assertEqual(result.amount, qty, "Filled amount should match requested qty.")

        expected_average_price = decimal.Decimal("99.5")
        self.assertEqual(result.price, expected_average_price)

    def test_calculate_qty_impact_total_match_buy(self):
        """
        Buy all available ask liquidity: total ask qty = 1 + 2 + 1 = 4
        Fill:
          - 1 @101 => cost 101
          - 2 @102 => cost 204
          - 1 @103 => cost 103
        total = 101 + 204 + 103 = 408
        average = 408 / 4 = 102
        """
        qty = decimal.Decimal("4")
        result = self.orderbook.calculate_price_impact_qty(qty, "BUY")

        self.assertIsNotNone(result, "Result should not be None when liquidity matches exactly.")
        self.assertEqual(result.amount, qty, "Filled amount should match requested qty.")

        expected_average_price = decimal.Decimal("102")
        self.assertEqual(result.price, expected_average_price)

    def test_calculate_qty_impact_total_match_sell(self):
        """
        Sell all available bid liquidity: total bid qty = 1 + 2 + 1 = 4
        Fill:
          - 1 @100 => 100
          - 2 @99 => 198
          - 1 @98 => 98
        total = 100 + 198 + 98 = 396
        average = 396 / 4 = 99
        """
        qty = decimal.Decimal("4")
        result = self.orderbook.calculate_price_impact_qty(qty, "SELL")

        self.assertIsNotNone(result, "Result should not be None when liquidity matches exactly.")
        self.assertEqual(result.amount, qty)

        expected_average_price = decimal.Decimal("99")
        self.assertEqual(result.price, expected_average_price)

    def test_calculate_qty_impact_insufficient_liquidity_buy(self):
        """
        Request a qty larger than available on the ask side (4 total).
        Asking for 5 => insufficient => should return None.
        """
        qty = decimal.Decimal("5")
        result = self.orderbook.calculate_price_impact_qty(qty, "BUY")
        self.assertIsNone(result, "Result should be None when there's insufficient ask liquidity.")

    def test_calculate_qty_impact_insufficient_liquidity_sell(self):
        """
        Request a qty larger than available on the bid side (4 total).
        Asking for 5 => insufficient => should return None.
        """
        qty = decimal.Decimal("5")
        result = self.orderbook.calculate_price_impact_qty(qty, "SELL")
        self.assertIsNone(result, "Result should be None when there's insufficient bid liquidity.")

    def test_calculate_qty_impact_invalid_qty(self):
        """
        Negative or zero qty should return None.
        """
        qty = decimal.Decimal("-1")
        result = self.orderbook.calculate_price_impact_qty(qty, "BUY")
        self.assertIsNone(result, "Result should be None for invalid qty (negative).")

        qty_zero = decimal.Decimal("0")
        result_zero = self.orderbook.calculate_price_impact_qty(qty_zero, "SELL")
        self.assertIsNone(result_zero, "Result should be None for invalid qty (zero).")

    def test_calculate_qty_impact_invalid_side(self):
        """
        Any side not 'BUY' or 'SELL' should yield None.
        """
        qty = decimal.Decimal("1")
        result = self.orderbook.calculate_price_impact_qty(qty, "INVALID_SIDE")
        self.assertIsNone(result, "Result should be None for invalid side.")



================================================
FILE: tests/perpetual/test_stream_client.py
================================================
import pytest
import websockets
from hamcrest import assert_that, equal_to
from websockets import WebSocketServer


def get_url_from_server(server: WebSocketServer):
    host, port = server.sockets[0].getsockname()  # type: ignore[index]
    return f"ws://{host}:{port}"


def serve_message(message):
    async def _serve_message(websocket):
        await websocket.send(message)

    return _serve_message


@pytest.mark.asyncio
async def test_orderbook_stream(create_orderbook_message):
    from x10.perpetual.stream_client import PerpetualStreamClient

    message_model = create_orderbook_message()

    async with websockets.serve(serve_message(message_model.model_dump_json()), "127.0.0.1", 0) as server:
        stream_client = PerpetualStreamClient(api_url=get_url_from_server(server))
        stream = await stream_client.subscribe_to_orderbooks()
        msg = await stream.recv()
        await stream.close()

        assert_that(
            msg.to_api_request_json(),
            equal_to(
                {
                    "type": "SNAPSHOT",
                    "data": {
                        "m": message_model.data.market,
                        "b": [{"q": "0.008", "p": "43547.00"}, {"q": "0.007000", "p": "43548.00"}],
                        "a": [{"q": "0.008", "p": "43546.00"}],
                    },
                    "error": None,
                    "ts": 1704798222748,
                    "seq": 570,
                }
            ),
        )


@pytest.mark.asyncio
async def test_account_update_trade_stream(create_account_update_trade_message):
    from x10.perpetual.stream_client import PerpetualStreamClient

    api_key = "dummy_api_key"
    message_model = create_account_update_trade_message()

    async with websockets.serve(serve_message(message_model.model_dump_json()), "127.0.0.1", 0) as server:
        stream_client = PerpetualStreamClient(api_url=get_url_from_server(server))
        stream = await stream_client.subscribe_to_account_updates(api_key)
        msg = await stream.recv()
        await stream.close()

        assert_that(
            msg.to_api_request_json(),
            equal_to(
                {
                    "type": "TRADE",
                    "data": {
                        "orders": None,
                        "positions": None,
                        "trades": [
                            {
                                "id": 1811328331296018432,
                                "accountId": 3004,
                                "market": "BTC-USD",
                                "orderId": 1811328331287359488,
                                "side": "BUY",
                                "price": "58249.8000000000000000",
                                "qty": "0.0010000000000000",
                                "value": "58.2498000000000000",
                                "fee": "0.0291240000000000",
                                "isTaker": True,
                                "tradeType": "TRADE",
                                "createdTime": 1720689301691,
                            }
                        ],
                        "balance": None,
                    },
                    "error": None,
                    "ts": 1704798222748,
                    "seq": 570,
                }
            ),
        )


@pytest.mark.asyncio
async def test_account_update_stream_with_unexpected_type(create_account_update_unknown_message):
    from x10.perpetual.stream_client import PerpetualStreamClient

    api_key = "dummy_api_key"
    message_model = create_account_update_unknown_message()

    async with websockets.serve(serve_message(message_model.model_dump_json()), "127.0.0.1", 0) as server:
        stream_client = PerpetualStreamClient(api_url=get_url_from_server(server))
        stream = await stream_client.subscribe_to_account_updates(api_key)
        msg = await stream.recv()
        await stream.close()

        assert_that(
            msg.to_api_request_json(),
            equal_to(
                {
                    "type": "UNKNOWN",
                    "data": None,
                    "error": None,
                    "ts": 1704798222748,
                    "seq": 570,
                }
            ),
        )


@pytest.mark.asyncio
async def test_candle_stream():
    from tests.fixtures.candles import create_candle_stream_message
    from x10.perpetual.stream_client import PerpetualStreamClient

    message_model = create_candle_stream_message()

    async with websockets.serve(serve_message(message_model.model_dump_json()), "127.0.0.1", 0) as server:
        stream_client = PerpetualStreamClient(api_url=get_url_from_server(server))
        stream = await stream_client.subscribe_to_candles("ETH-USD", "trades", "PT1M")
        msg = await stream.recv()
        await stream.close()

        assert_that(
            msg.to_api_request_json(),
            equal_to(
                {
                    "type": None,
                    "data": [
                        {
                            "o": "3458.64",
                            "l": "3399.07",
                            "h": "3476.89",
                            "c": "3414.85",
                            "v": "3.938",
                            "T": 1721106000000,
                        }
                    ],
                    "error": None,
                    "ts": 1721283121979,
                    "seq": 1,
                }
            ),
        )



================================================
FILE: tests/perpetual/test_trading_client.py
================================================
import dataclasses
from typing import List

import pytest
from aiohttp import web
from hamcrest import assert_that, equal_to, has_length

from x10.perpetual.assets import AssetOperationModel
from x10.perpetual.configuration import TESTNET_CONFIG
from x10.perpetual.markets import MarketModel
from x10.utils.http import WrappedApiResponse


def serve_data(data):
    async def _serve_data(_request):
        return web.Response(text=data)

    return _serve_data


@pytest.mark.asyncio
async def test_get_markets(aiohttp_server, create_btc_usd_market):
    from x10.perpetual.trading_client import PerpetualTradingClient

    expected_market = create_btc_usd_market()
    expected_markets = WrappedApiResponse[List[MarketModel]].model_validate(
        {"status": "OK", "data": [expected_market.model_dump()]}
    )

    app = web.Application()
    app.router.add_get("/info/markets", serve_data(expected_markets.model_dump_json()))

    server = await aiohttp_server(app)
    url = f"http://{server.host}:{server.port}"

    endpoint_config = dataclasses.replace(TESTNET_CONFIG, api_base_url=url)
    trading_client = PerpetualTradingClient(endpoint_config=endpoint_config)
    markets = await trading_client.markets_info.get_markets()

    assert_that(markets.status, equal_to("OK"))
    assert_that(markets.data, has_length(1))
    assert_that(
        markets.data[0].to_api_request_json(),
        equal_to(
            {
                "name": "BTC-USD",
                "assetName": "BTC",
                "assetPrecision": 5,
                "collateralAssetName": "USD",
                "collateralAssetPrecision": 6,
                "active": True,
                "marketStats": {
                    "dailyVolume": "2410800.768021",
                    "dailyVolumeBase": "37.94502",
                    "dailyPriceChange": "969.9",
                    "dailyLow": "62614.8",
                    "dailyHigh": "64421.1",
                    "lastPrice": "64280.0",
                    "askPrice": "64268.2",
                    "bidPrice": "64235.9",
                    "markPrice": "64267.380482593245",
                    "indexPrice": "64286.409493065992",
                    "fundingRate": "-0.000034",
                    "nextFundingRate": 1715072400000,
                    "openInterest": "150629.886375",
                    "openInterestBase": "2.34380",
                },
                "tradingConfig": {
                    "minOrderSize": "0.0001",
                    "minOrderSizeChange": "0.00001",
                    "minPriceChange": "0.1",
                    "maxMarketOrderValue": "1000000",
                    "maxLimitOrderValue": "5000000",
                    "maxPositionValue": "10000000",
                    "maxLeverage": "50.00",
                    "maxNumOrders": 200,
                    "limitPriceCap": "0.05",
                    "limitPriceFloor": "0.05",
                    "riskFactorConfig": [
                        {"upperBound": "400000", "riskFactor": "0.02"},
                        {"upperBound": "800000", "riskFactor": "0.04"},
                        {"upperBound": "1200000", "riskFactor": "0.06"},
                        {"upperBound": "1600000", "riskFactor": "0.08"},
                        {"upperBound": "2000000", "riskFactor": "0.1"},
                        {"upperBound": "2400000", "riskFactor": "0.12"},
                        {"upperBound": "2800000", "riskFactor": "0.14"},
                        {"upperBound": "3200000", "riskFactor": "0.16"},
                        {"upperBound": "3600000", "riskFactor": "0.18"},
                        {"upperBound": "4000000", "riskFactor": "0.2"},
                        {"upperBound": "4400000", "riskFactor": "0.22"},
                        {"upperBound": "4800000", "riskFactor": "0.24"},
                        {"upperBound": "5200000", "riskFactor": "0.26"},
                        {"upperBound": "5600000", "riskFactor": "0.28"},
                        {"upperBound": "6000000", "riskFactor": "0.3"},
                        {"upperBound": "6400000", "riskFactor": "0.32"},
                        {"upperBound": "6800000", "riskFactor": "0.34"},
                        {"upperBound": "7200000", "riskFactor": "0.36"},
                        {"upperBound": "7600000", "riskFactor": "0.38"},
                        {"upperBound": "8000000", "riskFactor": "0.4"},
                        {"upperBound": "8400000", "riskFactor": "0.42"},
                        {"upperBound": "8800000", "riskFactor": "0.44"},
                        {"upperBound": "9200000", "riskFactor": "0.46"},
                        {"upperBound": "9600000", "riskFactor": "0.48"},
                        {"upperBound": "10000000", "riskFactor": "0.5"},
                        {"upperBound": "1000000000", "riskFactor": "1"},
                    ],
                },
                "l2Config": {
                    "type": "STARKX",
                    "collateralId": "0x31857064564ed0ff978e687456963cba09c2c6985d8f9300a1de4962fafa054",
                    "collateralResolution": 1000000,
                    "syntheticId": "0x4254432d3600000000000000000000",
                    "syntheticResolution": 1000000,
                },
            }
        ),
    )


@pytest.mark.asyncio
async def test_get_asset_operations(aiohttp_server, create_asset_operations, create_trading_account):
    from x10.perpetual.trading_client import PerpetualTradingClient

    expected_operations = create_asset_operations()
    expected_response = WrappedApiResponse[List[AssetOperationModel]].model_validate(
        {"status": "OK", "data": [op.model_dump() for op in expected_operations]}
    )

    app = web.Application()
    app.router.add_get("/user/assetOperations", serve_data(expected_response.model_dump_json()))

    server = await aiohttp_server(app)
    url = f"http://{server.host}:{server.port}"

    stark_account = create_trading_account()
    endpoint_config = endpoint_config = dataclasses.replace(TESTNET_CONFIG, api_base_url=url)
    trading_client = PerpetualTradingClient(endpoint_config=endpoint_config, stark_account=stark_account)
    operations = await trading_client.account.asset_operations()

    assert_that(operations.status, equal_to("OK"))
    assert_that(operations.data, has_length(2))
    assert_that(
        [op.to_api_request_json() for op in operations.data],
        equal_to(
            [
                {
                    "id": "1816814506626514944",
                    "type": "TRANSFER",
                    "status": "COMPLETED",
                    "amount": "-100.0000000000000000",
                    "fee": "0",
                    "asset": 1,
                    "time": 1721997307818,
                    "accountId": 3004,
                    "counterpartyAccountId": 7349,
                    "transactionHash": None,
                },
                {
                    "id": "1813548171448147968",
                    "type": "CLAIM",
                    "status": "COMPLETED",
                    "amount": "100000.0000000000000000",
                    "fee": "0",
                    "asset": 1,
                    "time": 1721218552833,
                    "accountId": 3004,
                    "counterpartyAccountId": None,
                    "transactionHash": None,
                },
            ]
        ),
    )



================================================
FILE: tests/perpetual/test_transfer_object.py
================================================
from decimal import Decimal

import pytest
from freezegun import freeze_time
from hamcrest import assert_that, equal_to
from pytest_mock import MockerFixture

from x10.perpetual.configuration import TESTNET_CONFIG

FROZEN_NONCE = 1473459052


@freeze_time("2024-01-05 01:08:56.860694")
@pytest.mark.asyncio
async def test_create_transfer(mocker: MockerFixture, create_trading_account, create_accounts, create_btc_usd_market):
    mocker.patch("x10.utils.starkex.generate_nonce", return_value=FROZEN_NONCE)

    from x10.perpetual.transfer_object import create_transfer_object

    trading_account = create_trading_account()
    accounts = create_accounts()

    transfer_obj = create_transfer_object(
        from_vault=int(accounts[0].l2_vault),
        from_l2_key=accounts[0].l2_key,
        to_vault=int(accounts[1].l2_vault),
        to_l2_key=accounts[1].l2_key,
        amount=Decimal("1.1"),
        stark_account=trading_account,
        config=TESTNET_CONFIG,
    )

    assert_that(
        transfer_obj.to_api_request_json(),
        equal_to(
            {
                "fromVault": 10001,
                "toVault": 10002,
                "amount": "1.1",
                "transferredAsset": "0x31857064564ed0ff978e687456963cba09c2c6985d8f9300a1de4962fafa054",
                "settlement": {
                    "amount": 1100000,
                    "assetId": "0x31857064564ed0ff978e687456963cba09c2c6985d8f9300a1de4962fafa054",
                    "expirationTimestamp": 473954,
                    "nonce": 1473459052,
                    "receiverPositionId": 10002,
                    "receiverPublicKey": "0x3895139a98a6168dc8b0db251bcd0e6dcf97fd1e96f7a87d9bd3f341753a844",
                    "senderPositionId": 10001,
                    "senderPublicKey": "0x6970ac7180192cb58070d639064408610d0fbfd3b16c6b2c6219b9d91aa456f",
                    "signature": {
                        "r": "0x6840d40d8a7e190caa9bf823e9d8ee08462148b30cfdaff306302d686b22fa9",
                        "s": "0x4bd52731c5549f4e0781e8ffa7c5aea9be0aa01ca502a50ca7fc7cc46ccdb2f",
                    },
                },
            }
        ),
    )



================================================
FILE: tests/perpetual/test_withdrawal_object.py
================================================
from decimal import Decimal

import pytest
from freezegun import freeze_time
from hamcrest import assert_that, equal_to
from pytest_mock import MockerFixture

from x10.perpetual.configuration import TESTNET_CONFIG

FROZEN_NONCE = 1473459052


@freeze_time("2024-01-05 01:08:56.860694")
@pytest.mark.asyncio
async def test_create_withdrawal(mocker: MockerFixture, create_trading_account, create_accounts, create_btc_usd_market):
    mocker.patch("x10.utils.starkex.generate_nonce", return_value=FROZEN_NONCE)

    from x10.perpetual.withdrawal_object import create_withdrawal_object

    trading_account = create_trading_account()
    withdrawal_obj = create_withdrawal_object(
        amount=Decimal("1.1"),
        eth_address="0x6c5a62e584D0289def8Fe3c9C8194a07246a2C52",
        description="withdraw my gains",
        config=TESTNET_CONFIG,
        stark_account=trading_account,
    )

    assert_that(
        withdrawal_obj.to_api_request_json(),
        equal_to(
            {
                "amount": "1.1",
                "settlement": {
                    "amount": 1100000,
                    "collateralAssetId": "0x31857064564ed0ff978e687456963cba09c2c6985d8f9300a1de4962fafa054",
                    "ethAddress": "0x6c5a62e584d0289def8fe3c9c8194a07246a2c52",
                    "expirationTimestamp": 474146,
                    "nonce": 1473459052,
                    "positionId": 10002,
                    "publicKey": "0x61c5e7e8339b7d56f197f54ea91b776776690e3232313de0f2ecbd0ef76f466",
                    "signature": {
                        "r": "0x3f3aa8b0c2f2a8953aef42dd79d7c1003a98df241b7a989bb0ed122ae9e99dd",
                        "s": "0x789b22f03b13df2e95d5bffd472f1c8abb325291a142e55b7bd61a6cc998b46",
                    },
                },
                "description": "withdraw my gains",
            }
        ),
    )



================================================
FILE: tests/utils/test_date.py
================================================
from datetime import datetime

from hamcrest import assert_that, equal_to, raises

from x10.utils.date import to_epoch_millis


def test_convert_datetime_to_epoch_millis():
    dt = datetime.fromisoformat("2024-01-08 11:35:20.447+00:00")

    assert_that(to_epoch_millis(dt), equal_to(1704713720447))


def test_throw_on_non_utc_timezone():
    dt1 = datetime.fromisoformat("2024-01-08 11:35:20.447")
    dt2 = datetime.fromisoformat("2024-01-08 11:35:20.447+02:00")

    assert_that(lambda: to_epoch_millis(dt1), raises(AssertionError, "`value` must be in UTC"))
    assert_that(lambda: to_epoch_millis(dt2), raises(AssertionError, "`value` must be in UTC"))



================================================
FILE: tests/utils/test_http.py
================================================
from enum import Enum

from hamcrest import assert_that, equal_to, raises

from x10.utils.http import get_url


class _QueryParamEnum(Enum):
    KEY_1 = "VALUE_1"
    KEY_2 = "VALUE_2"


def test_generate_valid_url_from_template():
    assert_that(
        get_url(
            "/info/candles",
            query={
                "param1": "value1",
                "param2": ["value2_1", "value2_2"],
                "param3": None,
                "param4": 0,
                "param5": False,
                "param6": _QueryParamEnum.KEY_1,
                "param7": [_QueryParamEnum.KEY_1, _QueryParamEnum.KEY_2],
            },
        ),
        equal_to(
            "/info/candles?param1=value1&param2=value2_1&param2=value2_2&param4=0&param5=False&param6=VALUE_1&param7=VALUE_1&param7=VALUE_2"  # noqa: E501
        ),
    )
    assert_that(get_url("/info/candles/<market>", market="BTC-USD"), equal_to("/info/candles/BTC-USD"))
    assert_that(
        get_url("/info/candles/<market>/<candle_type>", market="BTC-USD", candle_type="trades"),
        equal_to("/info/candles/BTC-USD/trades"),
    )
    assert_that(lambda: get_url("/info/candles/<market>"), raises(KeyError))
    assert_that(get_url("/info/candles/<market?>"), equal_to("/info/candles"))
    assert_that(get_url("/info/candles/<market?>", market="BTC-USD"), equal_to("/info/candles/BTC-USD"))
    assert_that(get_url("/info/candles/<market?>", market=None), equal_to("/info/candles"))



================================================
FILE: tests/utils/test_model.py
================================================
import re
from typing import Optional

from hamcrest import assert_that, equal_to, raises
from pydantic import ValidationError

from x10.utils.model import X10BaseModel


class _TestModel(X10BaseModel):
    market: str
    order_type: Optional[str] = "LIMIT"
    created_time: int
    expiry_time: Optional[int] = None


def test_model_should_parse_json_with_missing_optional_fields():
    model = _TestModel.model_validate_json('{"market": "BTC-USD", "createdTime": 0}')

    assert_that(model, equal_to(_TestModel(market="BTC-USD", created_time=0)))
    assert_that(model.order_type, equal_to("LIMIT"))
    assert_that(model.expiry_time, equal_to(None))


def test_model_should_parse_json():
    model = _TestModel.model_validate_json('{"market": "BTC-USD", "createdTime": 0, "expiryTime": 1}')

    assert_that(model, equal_to(_TestModel(market="BTC-USD", created_time=0, expiry_time=1)))


def test_model_should_throw_error_when_field_is_modified():
    test_model = _TestModel(market="BTC-USD", created_time=0)

    def try_to_modify_field():
        test_model.market = "ETH-USD"

    assert_that(try_to_modify_field, raises(ValidationError, pattern=re.compile("Instance is frozen")))



================================================
FILE: x10/__init__.py
================================================
[Empty file]


================================================
FILE: x10/config.py
================================================
import importlib.metadata

TRADING_API_URL_DEV = "http://api.testnet.extended.exchange/api/v1"
STREAM_API_URL_DEV = "wss://api.testnet.extended.exchange/stream.extended.exchange/v1"

BTC_USD_MARKET = "BTC-USD"
SOL_USD_MARKET = "SOL-USD"
ADA_USD_MARKET = "ADA-USD"
ETH_USD_MARKET = "ETH-USD"

DEFAULT_REQUEST_TIMEOUT_SECONDS = 500
SDK_VERSION = importlib.metadata.version("x10-python-trading")
USER_AGENT = f"X10PythonTradingClient/{SDK_VERSION}"



================================================
FILE: x10/errors.py
================================================
class X10Error(Exception):
    pass



================================================
FILE: x10/perpetual/__init__.py
================================================
[Empty file]


================================================
FILE: x10/perpetual/accounts.py
================================================
from decimal import Decimal
from typing import Dict, List, Optional, Tuple

from pydantic import AliasChoices, Field

from x10.perpetual.balances import BalanceModel
from x10.perpetual.fees import TradingFeeModel
from x10.perpetual.orders import OpenOrderModel
from x10.perpetual.positions import PositionModel
from x10.perpetual.trades import AccountTradeModel
from x10.utils.model import X10BaseModel
from x10.utils.starkex import sign
from x10.utils.string import is_hex_string


class StarkPerpetualAccount:
    __vault: int
    __private_key: int
    __public_key: int
    __trading_fee: Dict[str, TradingFeeModel]

    def __init__(self, vault: int | str, private_key: str, public_key: str, api_key: str):
        assert is_hex_string(private_key)
        assert is_hex_string(public_key)

        if isinstance(vault, str):
            vault = int(vault)
        elif isinstance(vault, int):
            self.__vault = vault
        else:
            raise ValueError("Invalid vault type")

        self.__vault = vault
        self.__private_key = int(private_key, base=16)
        self.__public_key = int(public_key, base=16)
        self.__api_key = api_key
        self.__trading_fee = {}

    @property
    def vault(self):
        return self.__vault

    @property
    def public_key(self):
        return self.__public_key

    @property
    def api_key(self):
        return self.__api_key

    @property
    def trading_fee(self):
        return self.__trading_fee

    def sign(self, msg_hash: int) -> Tuple[int, int]:
        return sign(private_key=self.__private_key, msg_hash=msg_hash)


class AccountStreamDataModel(X10BaseModel):
    orders: Optional[List[OpenOrderModel]] = None
    positions: Optional[List[PositionModel]] = None
    trades: Optional[List[AccountTradeModel]] = None
    balance: Optional[BalanceModel] = None


class AccountLeverage(X10BaseModel):
    market: str
    leverage: Decimal


class AccountModel(X10BaseModel):
    id: int = Field(validation_alias=AliasChoices("accountId", "id"), serialization_alias="id")
    description: str
    account_index: int
    status: str
    l2_key: str
    l2_vault: int
    api_keys: Optional[List[str]] = None


class ApiKeyResponseModel(X10BaseModel):
    key: str


class ApiKeyRequestModel(X10BaseModel):
    description: str



================================================
FILE: x10/perpetual/amounts.py
================================================
import decimal
from dataclasses import dataclass
from decimal import Decimal

from x10.perpetual.assets import Asset

ROUNDING_SELL_CONTEXT = decimal.Context(rounding=decimal.ROUND_DOWN)
ROUNDING_BUY_CONTEXT = decimal.Context(rounding=decimal.ROUND_UP)
ROUNDING_FEE_CONTEXT = decimal.Context(rounding=decimal.ROUND_UP)


@dataclass
class HumanReadableAmount:
    value: Decimal
    asset: Asset

    def to_l1_amount(self) -> "L1Amount":
        converted_value = self.asset.convert_internal_quantity_to_l1_quantity(self.value)
        return L1Amount(converted_value, self.asset)

    def to_stark_amount(self, rounding_context: decimal.Context) -> "StarkAmount":
        converted_value = self.asset.convert_human_readable_to_stark_quantity(self.value, rounding_context)
        return StarkAmount(converted_value, self.asset)


@dataclass
class L1Amount:
    value: int
    asset: Asset

    def to_internal_amount(self) -> HumanReadableAmount:
        converted_value = self.asset.convert_l1_quantity_to_internal_quantity(self.value)
        return HumanReadableAmount(converted_value, self.asset)


@dataclass
class StarkAmount:
    value: int
    asset: Asset

    def to_internal_amount(self) -> HumanReadableAmount:
        converted_value = self.asset.convert_stark_to_internal_quantity(self.value)
        return HumanReadableAmount(converted_value, self.asset)


@dataclass
class StarkOrderAmounts:
    collateral_amount_internal: HumanReadableAmount
    synthetic_amount_internal: HumanReadableAmount
    fee_amount_internal: HumanReadableAmount
    fee_rate: Decimal
    rounding_context: decimal.Context



================================================
FILE: x10/perpetual/assets.py
================================================
from dataclasses import dataclass
from decimal import Context, Decimal
from enum import Enum
from typing import Optional

from x10.utils.model import HexValue, X10BaseModel


@dataclass
class Asset:
    id: int
    name: str
    precision: int
    active: bool
    is_collateral: bool
    settlement_external_id: str
    settlement_resolution: int
    l1_external_id: str
    l1_resolution: int

    def convert_human_readable_to_stark_quantity(self, internal: Decimal, rounding_context: Context) -> int:
        return int(
            rounding_context.multiply(internal, Decimal(self.settlement_resolution)).to_integral(
                context=rounding_context
            )
        )

    def convert_stark_to_internal_quantity(self, stark: int) -> Decimal:
        return Decimal(stark) / Decimal(self.settlement_resolution)

    def convert_l1_quantity_to_internal_quantity(self, l1: int) -> Decimal:
        return Decimal(l1) / Decimal(self.l1_resolution)

    def convert_internal_quantity_to_l1_quantity(self, internal: Decimal) -> int:
        if not self.is_collateral:
            raise ValueError("Only collateral assets have an L1 representation")
        return int(internal * Decimal(self.l1_resolution))


class AssetOperationType(str, Enum):
    CLAIM = "CLAIM"
    DEPOSIT = "DEPOSIT"
    FAST_WITHDRAWAL = "FAST_WITHDRAWAL"
    SLOW_WITHDRAWAL = "SLOW_WITHDRAWAL"
    TRANSFER = "TRANSFER"


class AssetOperationStatus(Enum):
    # Technical status
    UNKNOWN = "UNKNOWN"

    CREATED = "CREATED"
    IN_PROGRESS = "IN_PROGRESS"
    REJECTED = "REJECTED"
    READY_FOR_CLAIM = "READY_FOR_CLAIM"
    COMPLETED = "COMPLETED"


class AssetOperationModel(X10BaseModel):
    id: str
    type: AssetOperationType
    status: AssetOperationStatus
    amount: Decimal
    fee: Decimal
    asset: int
    time: int
    account_id: int

    # When operation type is `TRANSFER`
    counterparty_account_id: Optional[int] = None
    transaction_hash: Optional[HexValue] = None



================================================
FILE: x10/perpetual/balances.py
================================================
from decimal import Decimal

from x10.utils.model import X10BaseModel


class BalanceModel(X10BaseModel):
    collateral_name: str
    balance: Decimal
    equity: Decimal
    available_for_trade: Decimal
    available_for_withdrawal: Decimal
    unrealised_pnl: Decimal
    initial_margin: Decimal
    margin_ratio: Decimal
    updated_time: int



================================================
FILE: x10/perpetual/candles.py
================================================
from decimal import Decimal
from typing import Literal, Optional

from pydantic import AliasChoices, Field

from x10.utils.model import X10BaseModel

CandleType = Literal["trades", "mark-prices", "index-prices"]
CandleInterval = Literal["PT1M", "PT5M", "PT15M", "PT30M", "PT1H", "PT2H", "PT4H", "P1D"]


class CandleModel(X10BaseModel):
    open: Decimal = Field(validation_alias=AliasChoices("open", "o"), serialization_alias="o")
    low: Decimal = Field(validation_alias=AliasChoices("low", "l"), serialization_alias="l")
    high: Decimal = Field(validation_alias=AliasChoices("high", "h"), serialization_alias="h")
    close: Decimal = Field(validation_alias=AliasChoices("close", "c"), serialization_alias="c")
    volume: Optional[Decimal] = Field(
        validation_alias=AliasChoices("volume", "v"), serialization_alias="v", default=None
    )
    timestamp: int = Field(validation_alias=AliasChoices("timestamp", "T"), serialization_alias="T")



================================================
FILE: x10/perpetual/configuration.py
================================================
from dataclasses import dataclass


@dataclass
class EndpointConfig:
    chain_rpc_url: str
    api_base_url: str
    stream_url: str
    onboarding_url: str
    signing_domain: str
    collateral_asset_contract: str
    asset_operations_contract: str
    collateral_asset_on_chain_id: str
    collateral_decimals: int


TESTNET_CONFIG = EndpointConfig(
    chain_rpc_url="https://rpc.sepolia.org",
    api_base_url="https://api.testnet.extended.exchange/api/v1",
    stream_url="wss://api.testnet.extended.exchange/stream.extended.exchange/v1",
    onboarding_url="https://api.testnet.extended.exchange",
    signing_domain="testnet.extended.exchange",
    collateral_asset_contract="0x0C9165046063B7bCD05C6924Bbe05ed535c140a1",
    asset_operations_contract="0xe42bb60Fab4EA4905832AEbDf0f001c784dA271b",
    collateral_asset_on_chain_id="0x31857064564ed0ff978e687456963cba09c2c6985d8f9300a1de4962fafa054",
    collateral_decimals=6,
)

MAINNET_CONFIG = EndpointConfig(
    chain_rpc_url="https://cloudflare-eth.com",
    api_base_url="https://api.extended.exchange/api/v1",
    stream_url="wss://api.extended.exchange/stream.extended.exchange/v1",
    onboarding_url="https://api.extended.exchange",
    signing_domain="extended.exchange",
    collateral_asset_contract="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    asset_operations_contract="0x1cE5D7f52A8aBd23551e91248151CA5A13353C65",
    collateral_asset_on_chain_id="0x2893294412a4c8f915f75892b395ebbf6859ec246ec365c3b1f56f47c3a0a5d",
    collateral_decimals=6,
)

"""
Identical to the MAINNET_CONFIG, but with a different signing domain.
Use it for accounts that were created before the signing domain was changed.
"""
MAINNET_CONFIG_LEGACY_SIGNING_DOMAIN = EndpointConfig(
    chain_rpc_url="https://cloudflare-eth.com",
    api_base_url="https://api.extended.exchange/api/v1",
    stream_url="wss://api.extended.exchange/stream.extended.exchange/v1",
    onboarding_url="https://api.extended.exchange",
    signing_domain="x10.exchange",
    collateral_asset_contract="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    asset_operations_contract="0x1cE5D7f52A8aBd23551e91248151CA5A13353C65",
    collateral_asset_on_chain_id="0x2893294412a4c8f915f75892b395ebbf6859ec246ec365c3b1f56f47c3a0a5d",
    collateral_decimals=6,
)



================================================
FILE: x10/perpetual/contract.py
================================================
import json
import os
from decimal import Decimal
from typing import Callable

from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3 import Web3

from x10.errors import X10Error
from x10.perpetual.configuration import EndpointConfig
from x10.utils.log import get_logger

LOGGER = get_logger(__name__)


class InsufficientAllowance(X10Error):
    pass


DEFAULT_API_TIMEOUT = 30

ABI_FOLDER = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "abi",
)
STARK_PERPETUAL_ABI = "stark-perpetual.json"
ERC20_ABI = "erc20.json"


def call_stark_perpetual_withdraw_balance(
    get_eth_private_key: Callable[[], str],
    config: EndpointConfig,
) -> Decimal:
    signing_account: LocalAccount = Account.from_key(get_eth_private_key())
    web3_provider = Web3.HTTPProvider(config.chain_rpc_url, request_kwargs={"timeout": DEFAULT_API_TIMEOUT})
    web3 = Web3(web3_provider)
    checksum_asset_operations_address = Web3.to_checksum_address(config.asset_operations_contract)
    asset_operations_contract = web3.eth.contract(
        address=checksum_asset_operations_address,
        abi=json.load(open(os.path.join(ABI_FOLDER, STARK_PERPETUAL_ABI), "r")),
    )
    withdrawable_amount = asset_operations_contract.functions.getWithdrawalBalance(
        int(signing_account.address, 16), int(config.collateral_asset_on_chain_id, 16)
    ).call()

    asset_erc20_checksum_address = Web3.to_checksum_address(config.collateral_asset_contract)
    asset_erc20_contract = web3.eth.contract(
        address=asset_erc20_checksum_address,
        abi=json.load(open(os.path.join(ABI_FOLDER, ERC20_ABI), "r")),
    )
    decimals = asset_erc20_contract.functions.decimals().call()
    return Decimal(withdrawable_amount).scaleb(-decimals)


def call_erc20_approve(
    human_readable_amount: Decimal,
    get_eth_private_key: Callable[[], str],
    config: EndpointConfig,
) -> str:
    web3_provider = Web3.HTTPProvider(config.chain_rpc_url, request_kwargs={"timeout": DEFAULT_API_TIMEOUT})
    web3 = Web3(web3_provider)
    asset_erc20_checksum_address = Web3.to_checksum_address(config.collateral_asset_contract)
    asset_erc20_contract = web3.eth.contract(
        address=asset_erc20_checksum_address,
        abi=json.load(open(os.path.join(ABI_FOLDER, ERC20_ABI), "r")),
    )
    spender = Web3.to_checksum_address(config.asset_operations_contract)
    amount_to_approve = int(human_readable_amount * 10 ** asset_erc20_contract.functions.decimals().call())
    method = asset_erc20_contract.functions.approve(spender, amount_to_approve)
    signing_account: LocalAccount = Account.from_key(get_eth_private_key())
    LOGGER.info(
        f"approving spender: {spender} for {amount_to_approve} on behalf of l1 account: {signing_account.address}"
    )
    signed_transaction = signing_account.sign_transaction(
        method.build_transaction(
            {
                "from": signing_account.address,
                "nonce": web3.eth.get_transaction_count(signing_account.address),
            }
        ),
    )
    web3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    return signed_transaction.hash.hex()


def call_stark_perpetual_deposit(
    l2_vault: int,
    l2_key: str,
    config: EndpointConfig,
    human_readable_amount: Decimal,
    get_eth_private_key: Callable[[], str],
) -> str:
    signing_account: LocalAccount = Account.from_key(get_eth_private_key())
    LOGGER.info(
        f"Depositing into vault: {l2_vault}, l2_key: {l2_key}, amount: {human_readable_amount}, as l1 account: {signing_account.address}"  # noqa
    )
    web3_provider = Web3.HTTPProvider(config.chain_rpc_url, request_kwargs={"timeout": DEFAULT_API_TIMEOUT})
    web3 = Web3(web3_provider)
    checksum_asset_operations_address = Web3.to_checksum_address(config.asset_operations_contract)
    asset_operations_contract = web3.eth.contract(
        address=checksum_asset_operations_address,
        abi=json.load(open(os.path.join(ABI_FOLDER, STARK_PERPETUAL_ABI), "r")),
    )

    asset_erc20_checksum_address = Web3.to_checksum_address(config.collateral_asset_contract)
    asset_erc20_contract = web3.eth.contract(
        address=asset_erc20_checksum_address,
        abi=json.load(open(os.path.join(ABI_FOLDER, ERC20_ABI), "r")),
    )

    decimals = asset_erc20_contract.functions.decimals().call()
    amount_to_deposit = int(human_readable_amount * 10**decimals)
    allowance_amount = asset_erc20_contract.functions.allowance(
        signing_account.address,
        checksum_asset_operations_address,
    ).call()

    if allowance_amount < amount_to_deposit:
        raise InsufficientAllowance(
            f"Insufficient allowance. Required: {amount_to_deposit}, current: {allowance_amount}"
        )

    method = asset_operations_contract.functions.deposit(
        int(l2_key, base=16),
        int(config.collateral_asset_on_chain_id, base=16),
        l2_vault,
        amount_to_deposit,
    )
    signed_transaction = signing_account.sign_transaction(
        method.build_transaction(
            {
                "from": signing_account.address,
                "nonce": web3.eth.get_transaction_count(signing_account.address),
            }
        ),
    )
    web3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    return signed_transaction.hash.hex()


def call_stark_perpetual_withdraw(
    config: EndpointConfig,
    get_eth_private_key: Callable[[], str],
) -> str:
    signing_account: LocalAccount = Account.from_key(get_eth_private_key())

    web3_provider = Web3.HTTPProvider(config.chain_rpc_url, request_kwargs={"timeout": DEFAULT_API_TIMEOUT})
    web3 = Web3(web3_provider)

    checksum_contract_address = Web3.to_checksum_address(config.asset_operations_contract)
    checksum_eth_address = Web3.to_checksum_address(signing_account.address)

    asset_operations_contract = web3.eth.contract(
        address=checksum_contract_address,
        abi=json.load(open(os.path.join(ABI_FOLDER, STARK_PERPETUAL_ABI), "r")),
    )

    method = asset_operations_contract.functions.withdraw(
        int(checksum_eth_address, base=16),
        int(config.collateral_asset_on_chain_id, base=16),
    )

    signed_transaction = signing_account.sign_transaction(
        method.build_transaction(
            {
                "from": signing_account.address,
                "nonce": web3.eth.get_transaction_count(signing_account.address),
            }
        ),
    )
    web3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    return signed_transaction.hash.hex()



================================================
FILE: x10/perpetual/fees.py
================================================
from decimal import Decimal

from x10.utils.model import X10BaseModel


class TradingFeeModel(X10BaseModel):
    market: str
    maker_fee_rate: Decimal
    taker_fee_rate: Decimal


DEFAULT_FEES = TradingFeeModel(
    market="BTC-USD",
    maker_fee_rate=(Decimal("2") / Decimal("10000")),
    taker_fee_rate=(Decimal("5") / Decimal("10000")),
)



================================================
FILE: x10/perpetual/funding_rates.py
================================================
from decimal import Decimal

from pydantic import AliasChoices, Field

from x10.utils.model import X10BaseModel


class FundingRateModel(X10BaseModel):
    market: str = Field(validation_alias=AliasChoices("market", "m"), serialization_alias="m")
    funding_rate: Decimal = Field(validation_alias=AliasChoices("funding_rate", "f"), serialization_alias="f")
    timestamp: int = Field(validation_alias=AliasChoices("timestamp", "T"), serialization_alias="T")



================================================
FILE: x10/perpetual/markets.py
================================================
from decimal import ROUND_CEILING, Decimal
from functools import cached_property
from typing import List

from x10.perpetual.assets import Asset
from x10.utils.model import X10BaseModel


class RiskFactorConfig(X10BaseModel):
    upper_bound: Decimal
    risk_factor: Decimal

    @cached_property
    def max_leverage(self) -> Decimal:
        return round(Decimal(1) / self.risk_factor, 2)


class MarketStatsModel(X10BaseModel):
    daily_volume: Decimal
    daily_volume_base: Decimal
    daily_price_change: Decimal
    daily_low: Decimal
    daily_high: Decimal
    last_price: Decimal
    ask_price: Decimal
    bid_price: Decimal
    mark_price: Decimal
    index_price: Decimal
    funding_rate: Decimal
    next_funding_rate: int
    open_interest: Decimal
    open_interest_base: Decimal


class TradingConfigModel(X10BaseModel):
    min_order_size: Decimal
    min_order_size_change: Decimal
    min_price_change: Decimal
    max_market_order_value: Decimal
    max_limit_order_value: Decimal
    max_position_value: Decimal
    max_leverage: Decimal
    max_num_orders: int
    limit_price_cap: Decimal
    limit_price_floor: Decimal
    risk_factor_config: List[RiskFactorConfig]

    @cached_property
    def price_precision(self) -> int:
        return abs(int(self.min_price_change.log10().to_integral_exact(ROUND_CEILING)))

    @cached_property
    def quantity_precision(self) -> int:
        return abs(int(self.min_order_size_change.log10().to_integral_exact(ROUND_CEILING)))

    def max_leverage_for_position_value(self, position_value: Decimal) -> Decimal:
        filtered = [x for x in self.risk_factor_config if x.upper_bound >= position_value]
        return filtered[0].max_leverage if filtered else Decimal(0)

    def max_position_value_for_leverage(self, leverage: Decimal) -> Decimal:
        filtered = [x for x in self.risk_factor_config if x.max_leverage >= leverage]
        return filtered[-1].upper_bound if filtered else Decimal(0)


class L2ConfigModel(X10BaseModel):
    type: str
    collateral_id: str
    collateral_resolution: int
    synthetic_id: str
    synthetic_resolution: int


class MarketModel(X10BaseModel):
    name: str
    asset_name: str
    asset_precision: int
    collateral_asset_name: str
    collateral_asset_precision: int
    active: bool
    market_stats: MarketStatsModel
    trading_config: TradingConfigModel
    l2_config: L2ConfigModel

    @cached_property
    def synthetic_asset(self) -> Asset:
        return Asset(
            id=1,
            name=self.asset_name,
            precision=self.asset_precision,
            active=self.active,
            is_collateral=False,
            settlement_external_id=self.l2_config.synthetic_id,
            settlement_resolution=self.l2_config.synthetic_resolution,
            l1_external_id="",
            l1_resolution=0,
        )

    @cached_property
    def collateral_asset(self) -> Asset:
        return Asset(
            id=2,
            name=self.collateral_asset_name,
            precision=self.collateral_asset_precision,
            active=self.active,
            is_collateral=True,
            settlement_external_id=self.l2_config.collateral_id,
            settlement_resolution=self.l2_config.collateral_resolution,
            l1_external_id="",
            l1_resolution=0,
        )



================================================
FILE: x10/perpetual/order_object.py
================================================
from datetime import datetime, timedelta
from decimal import Decimal
from typing import Callable, Optional, Tuple

from x10.perpetual.accounts import StarkPerpetualAccount
from x10.perpetual.amounts import (
    ROUNDING_BUY_CONTEXT,
    ROUNDING_FEE_CONTEXT,
    ROUNDING_SELL_CONTEXT,
    HumanReadableAmount,
    StarkOrderAmounts,
)
from x10.perpetual.fees import DEFAULT_FEES, TradingFeeModel
from x10.perpetual.markets import MarketModel
from x10.perpetual.orders import (
    OrderSide,
    OrderType,
    PerpetualOrderModel,
    SelfTradeProtectionLevel,
    SettlementSignatureModel,
    StarkDebuggingOrderAmountsModel,
    StarkSettlementModel,
    TimeInForce,
)
from x10.utils.date import to_epoch_millis, utc_now
from x10.utils.starkex import generate_nonce, hash_order


def create_order_object(
    account: StarkPerpetualAccount,
    market: MarketModel,
    amount_of_synthetic: Decimal,
    price: Decimal,
    side: OrderSide,
    post_only: bool = False,
    previous_order_id: Optional[str] = None,
    expire_time: Optional[datetime] = None,
    order_external_id: Optional[str] = None,
    time_in_force: TimeInForce = TimeInForce.GTT,
    self_trade_protection_level: SelfTradeProtectionLevel = SelfTradeProtectionLevel.ACCOUNT,
) -> PerpetualOrderModel:
    """
    Creates an order object to be placed on the exchange using the `place_order` method.
    """
    fees = account.trading_fee.get(market.name, DEFAULT_FEES)

    return __create_order_object(
        market,
        amount_of_synthetic,
        price,
        side,
        account.vault,
        fees,
        account.sign,
        account.public_key,
        False,
        expire_time,
        post_only=post_only,
        previous_order_external_id=previous_order_id,
        order_external_id=order_external_id,
        time_in_force=time_in_force,
        self_trade_protection_level=self_trade_protection_level,
    )


def __create_order_object(
    market: MarketModel,
    synthetic_amount: Decimal,
    price: Decimal,
    side: OrderSide,
    collateral_position_id: int,
    fees: TradingFeeModel,
    signer: Callable[[int], Tuple[int, int]],
    public_key: int,
    exact_only: bool = False,
    expire_time: Optional[datetime] = None,
    post_only: bool = False,
    previous_order_external_id: Optional[str] = None,
    order_external_id: Optional[str] = None,
    time_in_force: TimeInForce = TimeInForce.GTT,
    self_trade_protection_level: SelfTradeProtectionLevel = SelfTradeProtectionLevel.ACCOUNT,
) -> PerpetualOrderModel:
    if exact_only:
        raise NotImplementedError("`exact_only` option is not supported yet")

    if expire_time is None:
        expire_time = utc_now() + timedelta(hours=8)

    nonce = generate_nonce()
    is_buying_synthetic = side == OrderSide.BUY
    rounding_context = ROUNDING_BUY_CONTEXT if is_buying_synthetic else ROUNDING_SELL_CONTEXT

    collateral_amount_human = HumanReadableAmount(synthetic_amount * price, market.collateral_asset)
    synthetic_amount_human = HumanReadableAmount(synthetic_amount, market.synthetic_asset)

    fee = HumanReadableAmount(
        fees.taker_fee_rate * collateral_amount_human.value,
        market.collateral_asset,
    )

    amounts = StarkOrderAmounts(
        collateral_amount_internal=collateral_amount_human,
        synthetic_amount_internal=synthetic_amount_human,
        fee_amount_internal=fee,
        fee_rate=fees.taker_fee_rate,
        rounding_context=rounding_context,
    )
    debugging_amounts = StarkDebuggingOrderAmountsModel(
        collateral_amount=Decimal(amounts.collateral_amount_internal.to_stark_amount(amounts.rounding_context).value),
        fee_amount=Decimal(amounts.fee_amount_internal.to_stark_amount(ROUNDING_FEE_CONTEXT).value),
        synthetic_amount=Decimal(amounts.synthetic_amount_internal.to_stark_amount(amounts.rounding_context).value),
    )

    order_hash = hash_order(
        amounts=amounts,
        is_buying_synthetic=is_buying_synthetic,
        nonce=nonce,
        position_id=collateral_position_id,
        expiration_timestamp=expire_time,
    )

    (order_signature_r, order_signature_s) = signer(order_hash)
    settlement = StarkSettlementModel(
        signature=SettlementSignatureModel(r=order_signature_r, s=order_signature_s),
        stark_key=public_key,
        collateral_position=Decimal(collateral_position_id),
    )

    order_id = str(order_hash) if order_external_id is None else order_external_id
    order = PerpetualOrderModel(
        id=order_id,
        market=market.name,
        type=OrderType.LIMIT,
        side=side,
        qty=synthetic_amount_human.value,
        price=price,
        post_only=post_only,
        time_in_force=time_in_force,
        expiry_epoch_millis=to_epoch_millis(expire_time),
        fee=amounts.fee_rate,
        self_trade_protection_level=self_trade_protection_level,
        nonce=Decimal(nonce),
        cancel_id=previous_order_external_id,
        settlement=settlement,
        debugging_amounts=debugging_amounts,
    )

    return order



================================================
FILE: x10/perpetual/orderbook.py
================================================
import asyncio
import dataclasses
import decimal
from typing import Callable, Iterable, Tuple

from sortedcontainers import SortedDict  # type: ignore[import-untyped]

from x10.perpetual.configuration import EndpointConfig
from x10.perpetual.orderbooks import OrderbookUpdateModel
from x10.perpetual.stream_client.stream_client import PerpetualStreamClient
from x10.utils.http import StreamDataType


@dataclasses.dataclass
class OrderBookEntry:
    price: decimal.Decimal
    amount: decimal.Decimal

    def __repr__(self) -> str:
        return f"OrderBookEntry(price={self.price}, amount={self.amount})"


@dataclasses.dataclass
class ImpactDetails:
    price: decimal.Decimal
    amount: decimal.Decimal


class OrderBook:
    @staticmethod
    async def create(
        endpoint_config: EndpointConfig,
        market_name: str,
        best_ask_change_callback: Callable[[OrderBookEntry], None] | None = None,
        best_bid_change_callback: Callable[[OrderBookEntry], None] | None = None,
        start=False,
    ) -> "OrderBook":
        ob = OrderBook(
            endpoint_config,
            market_name,
            best_ask_change_callback,
            best_bid_change_callback,
        )
        if start:
            await ob.start_orderbook()
        return ob

    def __init__(
        self,
        endpoint_config: EndpointConfig,
        market_name: str,
        best_ask_change_callback: Callable[[OrderBookEntry], None] | None = None,
        best_bid_change_callback: Callable[[OrderBookEntry], None] | None = None,
    ) -> None:
        self.__stream_client = PerpetualStreamClient(api_url=endpoint_config.stream_url)
        self.__market_name = market_name
        self.__task: asyncio.Task | None = None
        self._bid_prices: SortedDict[decimal.Decimal, OrderBookEntry] = SortedDict()
        self._ask_prices: SortedDict[decimal.Decimal, OrderBookEntry] = SortedDict()
        self.best_ask_change_callback = best_ask_change_callback
        self.best_bid_change_callback = best_bid_change_callback

    def update_orderbook(self, data: OrderbookUpdateModel):
        best_bid_before_update = self.best_bid()
        for bid in data.bid:
            if bid.price in self._bid_prices:
                existing_bid_entry: OrderBookEntry = self._bid_prices.get(bid.price)
                existing_bid_entry.amount = existing_bid_entry.amount + bid.qty
                if existing_bid_entry.amount == 0:
                    del self._bid_prices[bid.price]
            else:
                self._bid_prices[bid.price] = OrderBookEntry(
                    price=bid.price,
                    amount=bid.qty,
                )
        now_best_bid = self.best_bid()
        if now_best_bid and best_bid_before_update != now_best_bid:
            if self.best_bid_change_callback:
                self.best_bid_change_callback(now_best_bid)

        best_ask_before_update = self.best_ask()
        for ask in data.ask:
            if ask.price in self._ask_prices:
                existing_ask_entry: OrderBookEntry = self._ask_prices.get(ask.price)
                existing_ask_entry.amount = existing_ask_entry.amount + ask.qty
                if existing_ask_entry.amount == 0:
                    del self._ask_prices[ask.price]
            else:
                self._ask_prices[ask.price] = OrderBookEntry(
                    price=ask.price,
                    amount=ask.qty,
                )
        now_best_ask = self.best_ask()
        if now_best_ask and best_ask_before_update != now_best_ask:
            if self.best_ask_change_callback:
                self.best_ask_change_callback(now_best_ask)

    def init_orderbook(self, data: OrderbookUpdateModel):
        for bid in data.bid:
            self._bid_prices[bid.price] = OrderBookEntry(
                price=bid.price,
                amount=bid.qty,
            )
        for ask in data.ask:
            self._ask_prices[ask.price] = OrderBookEntry(
                price=ask.price,
                amount=ask.qty,
            )

    async def start_orderbook(self) -> asyncio.Task:
        loop = asyncio.get_running_loop()

        async def inner():
            async with self.__stream_client.subscribe_to_orderbooks(self.__market_name) as stream:
                async for event in stream:
                    if event.type == StreamDataType.SNAPSHOT.value:
                        self.init_orderbook(event.data)
                    elif event.type == StreamDataType.DELTA.value:
                        self.update_orderbook(event.data)

        self.__task = loop.create_task(inner())
        return self.__task

    def stop_orderbook(self):
        if self.__task:
            self.__task.cancel()
            self.__task = None

    def best_bid(self) -> OrderBookEntry | None:
        try:
            entry = self._bid_prices.peekitem(-1)
            return entry[1]
        except IndexError:
            return None

    def best_ask(self) -> OrderBookEntry | None:
        try:
            entry = self._ask_prices.peekitem(0)
            return entry[1]
        except IndexError:
            return None

    def __price_impact_notional(
        self, notional: decimal.Decimal, levels: Iterable[Tuple[decimal.Decimal, OrderBookEntry]]
    ):
        remaining_to_spend = notional
        total_amount = decimal.Decimal(0)
        weighted_sum = decimal.Decimal(0)
        for price, entry in levels:
            available_at_price = entry.amount
            amount_to_purchase = min(remaining_to_spend / price, available_at_price)
            if remaining_to_spend <= 0:
                break
            if available_at_price <= 0:
                continue
            take = amount_to_purchase
            spent = take * price
            weighted_sum += take * price
            total_amount += take
            remaining_to_spend -= spent

        if remaining_to_spend > 0:
            return None
        average_price = weighted_sum / total_amount
        return ImpactDetails(price=average_price, amount=total_amount)

    def __price_impact_qty(self, qty: decimal.Decimal, levels: Iterable[Tuple[decimal.Decimal, OrderBookEntry]]):
        remaining_qty = qty
        total_amount = decimal.Decimal(0)
        total_spent = decimal.Decimal(0)
        for price, entry in levels:
            available_at_price = entry.amount
            take = min(remaining_qty, available_at_price)
            if remaining_qty <= 0:
                break
            if available_at_price <= 0:
                continue
            total_spent += take * price
            total_amount += take
            remaining_qty -= take

        if remaining_qty > 0:
            return None
        average_price = total_spent / total_amount
        return ImpactDetails(price=average_price, amount=total_amount)

    def calculate_price_impact_notional(self, notional: decimal.Decimal, side: str) -> ImpactDetails | None:
        if notional <= 0:
            return None
        if side == "SELL":
            if not self._bid_prices:
                return None
            return self.__price_impact_notional(notional, reversed(self._bid_prices.items()))
        elif side == "BUY":
            if not self._ask_prices:
                return None
            return self.__price_impact_notional(notional, self._ask_prices.items())
        return None

    def calculate_price_impact_qty(self, qty: decimal.Decimal, side: str) -> ImpactDetails | None:
        if qty <= 0:
            return None
        if side == "SELL":
            if not self._bid_prices:
                return None
            return self.__price_impact_qty(qty, reversed(self._bid_prices.items()))
        elif side == "BUY":
            if not self._ask_prices:
                return None
            return self.__price_impact_qty(qty, self._ask_prices.items())
        return None



================================================
FILE: x10/perpetual/orderbooks.py
================================================
from decimal import Decimal
from typing import List

from pydantic import AliasChoices, Field

from x10.utils.model import X10BaseModel


class OrderbookQuantityModel(X10BaseModel):
    qty: Decimal = Field(validation_alias=AliasChoices("qty", "q"), serialization_alias="q")
    price: Decimal = Field(validation_alias=AliasChoices("price", "p"), serialization_alias="p")


class OrderbookUpdateModel(X10BaseModel):
    market: str = Field(validation_alias=AliasChoices("market", "m"), serialization_alias="m")
    bid: List[OrderbookQuantityModel] = Field(validation_alias=AliasChoices("bid", "b"), serialization_alias="b")
    ask: List[OrderbookQuantityModel] = Field(validation_alias=AliasChoices("ask", "a"), serialization_alias="a")



================================================
FILE: x10/perpetual/orders.py
================================================
from decimal import Decimal
from enum import Enum
from typing import Optional

from x10.utils.model import HexValue, SettlementSignatureModel, X10BaseModel


class TimeInForce(Enum):
    GTT = "GTT"
    IOC = "IOC"
    FOK = "FOK"


class OrderSide(Enum):
    BUY = "BUY"
    SELL = "SELL"


class OrderType(Enum):
    LIMIT = "LIMIT"
    CONDITIONAL = "CONDITIONAL"
    MARKET = "MARKET"
    TPSL = "TPSL"


class OrderTpslType(Enum):
    ORDER = "ORDER"
    POSITION = "POSITION"


class OrderStatus(Enum):
    # Technical status
    UNKNOWN = "UNKNOWN"

    NEW = "NEW"
    UNTRIGGERED = "UNTRIGGERED"
    PARTIALLY_FILLED = "PARTIALLY_FILLED"
    FILLED = "FILLED"
    CANCELLED = "CANCELLED"
    EXPIRED = "EXPIRED"
    REJECTED = "REJECTED"


class OrderStatusReason(Enum):
    # Technical status
    UNKNOWN = "UNKNOWN"

    NONE = "NONE"
    UNKNOWN_MARKET = "UNKNOWN_MARKET"
    DISABLED_MARKET = "DISABLED_MARKET"
    NOT_ENOUGH_FUNDS = "NOT_ENOUGH_FUNDS"
    NO_LIQUIDITY = "NO_LIQUIDITY"
    INVALID_FEE = "INVALID_FEE"
    INVALID_QTY = "INVALID_QTY"
    INVALID_PRICE = "INVALID_PRICE"
    INVALID_VALUE = "INVALID_VALUE"
    UNKNOWN_ACCOUNT = "UNKNOWN_ACCOUNT"
    SELF_TRADE_PROTECTION = "SELF_TRADE_PROTECTION"
    POST_ONLY_FAILED = "POST_ONLY_FAILED"
    REDUCE_ONLY_FAILED = "REDUCE_ONLY_FAILED"
    INVALID_EXPIRE_TIME = "INVALID_EXPIRE_TIME"
    POSITION_TPSL_CONFLICT = "POSITION_TPSL_CONFLICT"
    INVALID_LEVERAGE = "INVALID_LEVERAGE"
    PREV_ORDER_NOT_FOUND = "PREV_ORDER_NOT_FOUND"
    PREV_ORDER_TRIGGERED = "PREV_ORDER_TRIGGERED"
    TPSL_OTHER_SIDE_FILLED = "TPSL_OTHER_SIDE_FILLED"
    PREV_ORDER_CONFLICT = "PREV_ORDER_CONFLICT"
    ORDER_REPLACED = "ORDER_REPLACED"
    POST_ONLY_MODE = "POST_ONLY_MODE"
    REDUCE_ONLY_MODE = "REDUCE_ONLY_MODE"
    TRADING_OFF_MODE = "TRADING_OFF_MODE"


class OrderTriggerPriceType(Enum):
    # Technical status
    UNKNOWN = "UNKNOWN"

    MARK = "MARK"
    INDEX = "INDEX"
    LAST = "LAST"


class OrderTriggerDirection(Enum):
    # Technical status
    UNKNOWN = "UNKNOWN"

    UP = "UP"
    DOWN = "DOWN"


class OrderPriceType(Enum):
    # Technical status
    UNKNOWN = "UNKNOWN"

    MARKET = "MARKET"
    LIMIT = "LIMIT"


class SelfTradeProtectionLevel(Enum):
    DISABLED = "DISABLED"
    ACCOUNT = "ACCOUNT"
    CLIENT = "CLIENT"


class StarkSettlementModel(X10BaseModel):
    signature: SettlementSignatureModel
    stark_key: HexValue
    collateral_position: Decimal


class StarkDebuggingOrderAmountsModel(X10BaseModel):
    collateral_amount: Decimal
    fee_amount: Decimal
    synthetic_amount: Decimal


class CreateOrderConditionalTriggerModel(X10BaseModel):
    trigger_price: Decimal
    trigger_price_type: OrderTriggerPriceType
    direction: OrderTriggerDirection
    execution_price_type: OrderPriceType


class CreateOrderTpslTriggerModel(X10BaseModel):
    trigger_price: Decimal
    trigger_price_type: OrderTriggerPriceType
    price: Decimal
    price_type: OrderPriceType
    settlement: StarkSettlementModel
    debugging_amounts: Optional[StarkDebuggingOrderAmountsModel] = None


class PerpetualOrderModel(X10BaseModel):
    id: str
    market: str
    type: OrderType
    side: OrderSide
    qty: Decimal
    price: Decimal
    reduce_only: bool = False
    post_only: bool = False
    time_in_force: TimeInForce
    expiry_epoch_millis: int
    fee: Decimal
    nonce: Decimal
    self_trade_protection_level: SelfTradeProtectionLevel
    cancel_id: Optional[str] = None
    settlement: Optional[StarkSettlementModel] = None
    trigger: Optional[CreateOrderConditionalTriggerModel] = None
    tp_sl_type: Optional[OrderTpslType] = None
    take_profit: Optional[CreateOrderTpslTriggerModel] = None
    stop_loss: Optional[CreateOrderTpslTriggerModel] = None
    debugging_amounts: Optional[StarkDebuggingOrderAmountsModel] = None


class PlacedOrderModel(X10BaseModel):
    id: int
    external_id: str


class OpenOrderModel(X10BaseModel):
    id: int
    account_id: int
    external_id: str
    market: str
    type: OrderType
    side: OrderSide
    status: OrderStatus
    status_reason: Optional[OrderStatusReason] = None
    price: Decimal
    average_price: Optional[Decimal] = None
    qty: Decimal
    filled_qty: Optional[Decimal] = None
    reduce_only: bool
    post_only: bool
    payed_fee: Optional[Decimal] = None
    created_time: int
    updated_time: int
    expiry_time: Optional[int] = None



================================================
FILE: x10/perpetual/positions.py
================================================
from decimal import Decimal
from enum import Enum
from typing import Optional

from x10.utils.model import X10BaseModel


class ExitType(Enum):
    TRADE = "TRADE"
    LIQUIDATION = "LIQUIDATION"
    ADL = "ADL"


class PositionSide(Enum):
    LONG = "LONG"
    SHORT = "SHORT"


class PositionModel(X10BaseModel):
    id: int
    account_id: int
    market: str
    side: PositionSide
    leverage: Decimal
    size: Decimal
    value: Decimal
    open_price: Decimal
    mark_price: Decimal
    liquidation_price: Optional[Decimal] = None
    unrealised_pnl: Decimal
    realised_pnl: Decimal
    tp_price: Optional[Decimal] = None
    sl_price: Optional[Decimal] = None
    adl: Optional[int] = None
    created_at: int
    updated_at: int


class PositionHistoryModel(X10BaseModel):
    id: int
    account_id: int
    market: str
    side: PositionSide
    leverage: Decimal
    size: Decimal
    open_price: Decimal
    exit_type: Optional[ExitType] = None
    exit_price: Optional[Decimal] = None
    realised_pnl: Decimal
    created_time: int
    closed_time: Optional[int] = None



================================================
FILE: x10/perpetual/trades.py
================================================
from decimal import Decimal
from enum import Enum

from pydantic import AliasChoices, Field

from x10.perpetual.orders import OrderSide
from x10.utils.model import X10BaseModel


class TradeType(Enum):
    TRADE = "TRADE"
    LIQUIDATION = "LIQUIDATION"
    DELEVERAGE = "DELEVERAGE"


class PublicTradeModel(X10BaseModel):
    id: int = Field(validation_alias=AliasChoices("id", "i"), serialization_alias="i")
    market: str = Field(validation_alias=AliasChoices("market", "m"), serialization_alias="m")
    side: OrderSide = Field(validation_alias=AliasChoices("side", "S"), serialization_alias="S")
    trade_type: TradeType = Field(validation_alias=AliasChoices("trade_type", "tT"), serialization_alias="tT")
    timestamp: int = Field(validation_alias=AliasChoices("timestamp", "T"), serialization_alias="T")
    price: Decimal = Field(validation_alias=AliasChoices("price", "p"), serialization_alias="p")
    qty: Decimal = Field(validation_alias=AliasChoices("qty", "q"), serialization_alias="q")


class AccountTradeModel(X10BaseModel):
    id: int
    account_id: int
    market: str
    order_id: int
    side: OrderSide
    price: Decimal
    qty: Decimal
    value: Decimal
    fee: Decimal
    is_taker: bool
    trade_type: TradeType
    created_time: int



================================================
FILE: x10/perpetual/transfer_object.py
================================================
import math
from datetime import timedelta
from decimal import Decimal
from typing import List

from x10.perpetual.accounts import AccountModel, StarkPerpetualAccount
from x10.perpetual.configuration import EndpointConfig
from x10.perpetual.transfers import (
    OnChainPerpetualTransferModel,
    StarkTransferSettlement,
)
from x10.utils.date import utc_now
from x10.utils.model import SettlementSignatureModel
from x10.utils.starkex import generate_nonce, get_transfer_msg

SECONDS_IN_HOUR = 60 * 60
ASSET_ID_FEE = 0
MAX_AMOUNT_FEE = 0


def find_account_by_id(accounts: List[AccountModel], account_id: int):
    return next((account for account in accounts if account.id == account_id), None)


def calc_expiration_timestamp():
    expire_time = utc_now() + timedelta(days=7)
    expire_time_with_buffer = expire_time + timedelta(days=14)
    expire_time_with_buffer_as_hours = math.ceil(expire_time_with_buffer.timestamp() / SECONDS_IN_HOUR)

    return expire_time_with_buffer_as_hours


def create_transfer_object(
    from_vault: int,
    from_l2_key: str,
    to_vault: int,
    to_l2_key: str,
    amount: Decimal,
    config: EndpointConfig,
    stark_account: StarkPerpetualAccount,
) -> OnChainPerpetualTransferModel:
    expiration_timestamp = calc_expiration_timestamp()
    scaled_amount = amount.scaleb(config.collateral_decimals)
    stark_amount = scaled_amount.to_integral_exact()

    nonce = generate_nonce()
    transfer_hash = get_transfer_msg(
        asset_id=int(config.collateral_asset_on_chain_id, base=16),
        asset_id_fee=ASSET_ID_FEE,
        sender_position_id=from_vault,
        receiver_position_id=to_vault,
        receiver_public_key=int(to_l2_key, base=16),
        src_fee_position_id=from_vault,
        nonce=nonce,
        amount=int(stark_amount),
        max_amount_fee=MAX_AMOUNT_FEE,
        expiration_timestamp=expiration_timestamp,
    )
    (transfer_signature_r, transfer_signature_s) = stark_account.sign(transfer_hash)

    settlement = StarkTransferSettlement(
        amount=int(stark_amount),
        asset_id=int(config.collateral_asset_on_chain_id, base=16),
        expiration_timestamp=expiration_timestamp,
        nonce=nonce,
        receiver_position_id=to_vault,
        receiver_public_key=int(to_l2_key, 16),
        sender_position_id=from_vault,
        sender_public_key=from_l2_key if isinstance(from_l2_key, int) else int(from_l2_key, 16),
        signature=SettlementSignatureModel(r=transfer_signature_r, s=transfer_signature_s),
    )

    return OnChainPerpetualTransferModel(
        from_vault=from_vault,
        to_vault=to_vault,
        amount=amount,
        settlement=settlement,
        transferred_asset=config.collateral_asset_on_chain_id,
    )



================================================
FILE: x10/perpetual/transfers.py
================================================
from decimal import Decimal

from x10.perpetual.orders import SettlementSignatureModel
from x10.utils.model import HexValue, X10BaseModel


class StarkTransferSettlement(X10BaseModel):
    amount: int
    asset_id: HexValue
    expiration_timestamp: int
    nonce: int
    receiver_position_id: int
    receiver_public_key: HexValue
    sender_position_id: int
    sender_public_key: HexValue
    signature: SettlementSignatureModel


class PerpetualTransferModel(X10BaseModel):
    from_account: int
    to_account: int
    amount: Decimal
    transferred_asset: str
    settlement: StarkTransferSettlement


class OnChainPerpetualTransferModel(X10BaseModel):
    from_vault: int
    to_vault: int
    amount: Decimal
    settlement: StarkTransferSettlement
    transferred_asset: str



================================================
FILE: x10/perpetual/withdrawal_object.py
================================================
import math
from datetime import timedelta
from decimal import Decimal

from x10.perpetual.accounts import StarkPerpetualAccount
from x10.perpetual.configuration import EndpointConfig
from x10.perpetual.withdrawals import PerpetualSlowWithdrawal, StarkWithdrawalSettlement
from x10.utils.date import utc_now
from x10.utils.model import SettlementSignatureModel
from x10.utils.starkex import generate_nonce, get_withdrawal_to_address_msg

SECONDS_IN_HOUR = 60 * 60


def calc_expiration_timestamp():
    expire_time = utc_now() + timedelta(days=15)
    expire_time_with_buffer = expire_time + timedelta(days=14)
    expire_time_with_buffer_as_hours = math.ceil(expire_time_with_buffer.timestamp() / SECONDS_IN_HOUR)

    return expire_time_with_buffer_as_hours


def create_withdrawal_object(
    amount: Decimal,
    eth_address: str,
    stark_account: StarkPerpetualAccount,
    config: EndpointConfig,
    description: str | None = None,
) -> PerpetualSlowWithdrawal:
    expiration_timestamp = calc_expiration_timestamp()
    stark_amount = (amount.scaleb(config.collateral_decimals)).to_integral_exact()

    nonce = generate_nonce()
    withdrawal_hash = get_withdrawal_to_address_msg(
        asset_id_collateral=int(config.collateral_asset_on_chain_id, base=16),
        position_id=stark_account.vault,
        eth_address=eth_address,
        nonce=nonce,
        expiration_timestamp=expiration_timestamp,
        amount=int(stark_amount),
    )
    (withdrawal_signature_r, withdrawal_signature_s) = stark_account.sign(withdrawal_hash)

    settlement = StarkWithdrawalSettlement(
        amount=int(stark_amount),
        collateral_asset_id=int(config.collateral_asset_on_chain_id, base=16),
        eth_address=int(eth_address, base=16),
        expiration_timestamp=expiration_timestamp,
        nonce=nonce,
        position_id=stark_account.vault,
        public_key=stark_account.public_key,
        signature=SettlementSignatureModel(
            r=withdrawal_signature_r,
            s=withdrawal_signature_s,
        ),
    )

    return PerpetualSlowWithdrawal(amount=amount, settlement=settlement, description=description)



================================================
FILE: x10/perpetual/withdrawals.py
================================================
from decimal import Decimal
from typing import Literal

from x10.utils.model import HexValue, SettlementSignatureModel, X10BaseModel


class StarkWithdrawalSettlement(X10BaseModel):
    amount: int
    collateral_asset_id: HexValue
    eth_address: HexValue
    expiration_timestamp: int
    nonce: int
    position_id: int
    public_key: HexValue
    signature: SettlementSignatureModel


class PerpetualWithdrawalModel(X10BaseModel):
    type: Literal["SLOW_SELF"]
    account_id: int
    amount: Decimal
    asset: str
    settlement: StarkWithdrawalSettlement


class PerpetualSlowWithdrawal(X10BaseModel):
    amount: Decimal
    settlement: StarkWithdrawalSettlement
    description: str | None



================================================
FILE: x10/perpetual/abi/erc20.json
================================================
[
    {
        "constant": true,
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_spender",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_from",
                "type": "address"
            },
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "decimals",
        "outputs": [
            {
                "name": "",
                "type": "uint8"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "name": "balance",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            },
            {
                "name": "_spender",
                "type": "address"
            }
        ],
        "name": "allowance",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "payable": true,
        "stateMutability": "payable",
        "type": "fallback"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": true,
                "name": "spender",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "name": "from",
                "type": "address"
            },
            {
                "indexed": true,
                "name": "to",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    }
]


================================================
FILE: x10/perpetual/abi/stark-perpetual.json
================================================
[
    {
        "stateMutability": "payable",
        "type": "fallback"
    },
    {
        "inputs": [],
        "name": "VERSION",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "configurationDelay",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "name": "configurationHash",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes4",
                "name": "selector",
                "type": "bytes4"
            }
        ],
        "name": "getSubContract",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "globalConfigurationHash",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes4",
                "name": "selector",
                "type": "bytes4"
            }
        ],
        "name": "handlingContractId",
        "outputs": [
            {
                "internalType": "string",
                "name": "id",
                "type": "string"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "initialize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "stateMutability": "payable",
        "type": "receive"
    },
    {
        "anonymous": false,
        "inputs": [],
        "name": "LogFrozen",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "acceptedGovernor",
                "type": "address"
            }
        ],
        "name": "LogNewGovernorAccepted",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "nominatedGovernor",
                "type": "address"
            }
        ],
        "name": "LogNominatedGovernor",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [],
        "name": "LogNominationCancelled",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "entry",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "string",
                "name": "entryId",
                "type": "string"
            }
        ],
        "name": "LogRegistered",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "entry",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "string",
                "name": "entryId",
                "type": "string"
            }
        ],
        "name": "LogRemovalIntent",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "entry",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "string",
                "name": "entryId",
                "type": "string"
            }
        ],
        "name": "LogRemoved",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "removedGovernor",
                "type": "address"
            }
        ],
        "name": "LogRemovedGovernor",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [],
        "name": "LogUnFrozen",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "DEPOSIT_CANCEL_DELAY",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "FREEZE_GRACE_PERIOD",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "MAIN_GOVERNANCE_INFO_TAG",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "MAX_FORCED_ACTIONS_REQS_PER_BLOCK",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "MAX_VERIFIER_COUNT",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "UNFREEZE_DELAY",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "VERIFIER_REMOVAL_DELAY",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "verifier",
                "type": "address"
            }
        ],
        "name": "announceAvailabilityVerifierRemovalIntent",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "verifier",
                "type": "address"
            }
        ],
        "name": "announceVerifierRemovalIntent",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getRegisteredAvailabilityVerifiers",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "_verifers",
                "type": "address[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getRegisteredVerifiers",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "_verifers",
                "type": "address[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "verifierAddress",
                "type": "address"
            }
        ],
        "name": "isAvailabilityVerifier",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "isFrozen",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "verifierAddress",
                "type": "address"
            }
        ],
        "name": "isVerifier",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "mainAcceptGovernance",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "mainCancelNomination",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "testGovernor",
                "type": "address"
            }
        ],
        "name": "mainIsGovernor",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newGovernor",
                "type": "address"
            }
        ],
        "name": "mainNominateNewGovernor",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "governorForRemoval",
                "type": "address"
            }
        ],
        "name": "mainRemoveGovernor",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "verifier",
                "type": "address"
            },
            {
                "internalType": "string",
                "name": "identifier",
                "type": "string"
            }
        ],
        "name": "registerAvailabilityVerifier",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "verifier",
                "type": "address"
            },
            {
                "internalType": "string",
                "name": "identifier",
                "type": "string"
            }
        ],
        "name": "registerVerifier",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "verifier",
                "type": "address"
            }
        ],
        "name": "removeAvailabilityVerifier",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "verifier",
                "type": "address"
            }
        ],
        "name": "removeVerifier",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "unFreeze",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "ownerKey",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "quantizedAmount",
                "type": "uint256"
            }
        ],
        "name": "LogAssetWithdrawalAllowed",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "depositorEthKey",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "nonQuantizedAmount",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "quantizedAmount",
                "type": "uint256"
            }
        ],
        "name": "LogDeposit",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            }
        ],
        "name": "LogDepositCancel",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "nonQuantizedAmount",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "quantizedAmount",
                "type": "uint256"
            }
        ],
        "name": "LogDepositCancelReclaimed",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            }
        ],
        "name": "LogDepositNftCancelReclaimed",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "depositorEthKey",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "nonQuantizedAmount",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "quantizedAmount",
                "type": "uint256"
            }
        ],
        "name": "LogDepositWithTokenId",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "nonQuantizedAmount",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "quantizedAmount",
                "type": "uint256"
            }
        ],
        "name": "LogDepositWithTokenIdCancelReclaimed",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "ownerKey",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "nonQuantizedAmount",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "quantizedAmount",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            }
        ],
        "name": "LogMintWithdrawalPerformed",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "ownerKey",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "quantizedAmount",
                "type": "uint256"
            }
        ],
        "name": "LogMintableWithdrawalAllowed",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "depositorEthKey",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            }
        ],
        "name": "LogNftDeposit",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "ownerKey",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            }
        ],
        "name": "LogNftWithdrawalAllowed",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "ownerKey",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            }
        ],
        "name": "LogNftWithdrawalPerformed",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            }
        ],
        "name": "LogSystemAssetType",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "tokenAdmin",
                "type": "address"
            }
        ],
        "name": "LogTokenAdminAdded",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "tokenAdmin",
                "type": "address"
            }
        ],
        "name": "LogTokenAdminRemoved",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "bytes",
                "name": "assetInfo",
                "type": "bytes"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "quantum",
                "type": "uint256"
            }
        ],
        "name": "LogTokenRegistered",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "ownerKey",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "nonQuantizedAmount",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "quantizedAmount",
                "type": "uint256"
            }
        ],
        "name": "LogWithdrawalAllowed",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "ownerKey",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "nonQuantizedAmount",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "quantizedAmount",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            }
        ],
        "name": "LogWithdrawalPerformed",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "ownerKey",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "nonQuantizedAmount",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "quantizedAmount",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            }
        ],
        "name": "LogWithdrawalWithTokenIdPerformed",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "calculateAssetIdWithTokenId",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "mintingBlob",
                "type": "bytes"
            }
        ],
        "name": "calculateMintableAssetId",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "quantizedAmount",
                "type": "uint256"
            }
        ],
        "name": "deposit",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            }
        ],
        "name": "depositCancel",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "quantizedAmount",
                "type": "uint256"
            }
        ],
        "name": "depositERC1155",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "quantizedAmount",
                "type": "uint256"
            }
        ],
        "name": "depositERC20",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            }
        ],
        "name": "depositEth",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "depositNft",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "depositNftReclaim",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            }
        ],
        "name": "depositReclaim",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "quantizedAmount",
                "type": "uint256"
            }
        ],
        "name": "depositWithTokenId",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            }
        ],
        "name": "depositWithTokenIdReclaim",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            }
        ],
        "name": "getAssetInfo",
        "outputs": [
            {
                "internalType": "bytes",
                "name": "assetInfo",
                "type": "bytes"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            }
        ],
        "name": "getCancellationRequest",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "request",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            }
        ],
        "name": "getDepositBalance",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "ownerKey",
                "type": "uint256"
            }
        ],
        "name": "getEthKey",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            }
        ],
        "name": "getQuantizedDepositBalance",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "presumedAssetType",
                "type": "uint256"
            }
        ],
        "name": "getQuantum",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "quantum",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getSystemAssetType",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "ownerKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            }
        ],
        "name": "getWithdrawalBalance",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            }
        ],
        "name": "isAssetRegistered",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "testedAdmin",
                "type": "address"
            }
        ],
        "name": "isTokenAdmin",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "operator",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "",
                "type": "bytes"
            }
        ],
        "name": "onERC721Received",
        "outputs": [
            {
                "internalType": "bytes4",
                "name": "",
                "type": "bytes4"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "assetInfo",
                "type": "bytes"
            }
        ],
        "name": "registerSystemAssetType",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "",
                "type": "bytes"
            }
        ],
        "name": "registerToken",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "",
                "type": "bytes"
            },
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "name": "registerToken",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newAdmin",
                "type": "address"
            }
        ],
        "name": "registerTokenAdmin",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "oldAdmin",
                "type": "address"
            }
        ],
        "name": "unregisterTokenAdmin",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "ownerKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            }
        ],
        "name": "withdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "ownerKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "mintingBlob",
                "type": "bytes"
            }
        ],
        "name": "withdrawAndMint",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "ownerKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "withdrawNft",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "ownerKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "assetType",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "withdrawWithTokenId",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "bytes32",
                "name": "configHash",
                "type": "bytes32"
            }
        ],
        "name": "LogAssetConfigurationApplied",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "bytes32",
                "name": "configHash",
                "type": "bytes32"
            }
        ],
        "name": "LogAssetConfigurationRegistered",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "bytes32",
                "name": "configHash",
                "type": "bytes32"
            }
        ],
        "name": "LogAssetConfigurationRemoved",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "bytes32",
                "name": "configHash",
                "type": "bytes32"
            }
        ],
        "name": "LogGlobalConfigurationApplied",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "bytes32",
                "name": "configHash",
                "type": "bytes32"
            }
        ],
        "name": "LogGlobalConfigurationRegistered",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "bytes32",
                "name": "configHash",
                "type": "bytes32"
            }
        ],
        "name": "LogGlobalConfigurationRemoved",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "operator",
                "type": "address"
            }
        ],
        "name": "LogOperatorAdded",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "operator",
                "type": "address"
            }
        ],
        "name": "LogOperatorRemoved",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "bytes32",
                "name": "stateTransitionFact",
                "type": "bytes32"
            }
        ],
        "name": "LogStateTransitionFact",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "sequenceNumber",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "batchId",
                "type": "uint256"
            }
        ],
        "name": "LogUpdateState",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            },
            {
                "internalType": "bytes32",
                "name": "configHash",
                "type": "bytes32"
            }
        ],
        "name": "applyAssetConfigurationChange",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "configHash",
                "type": "bytes32"
            }
        ],
        "name": "applyGlobalConfigurationChange",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "quantizedAmount",
                "type": "uint256"
            }
        ],
        "name": "escape",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getActionCount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "actionIndex",
                "type": "uint256"
            }
        ],
        "name": "getActionHashByIndex",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "starkKeyA",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "starkKeyB",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultIdA",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultIdB",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "collateralAssetId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "syntheticAssetId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountCollateral",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountSynthetic",
                "type": "uint256"
            },
            {
                "internalType": "bool",
                "name": "aIsBuyingSynthetic",
                "type": "bool"
            },
            {
                "internalType": "uint256",
                "name": "nonce",
                "type": "uint256"
            }
        ],
        "name": "getForcedTradeRequest",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "quantizedAmount",
                "type": "uint256"
            }
        ],
        "name": "getForcedWithdrawalRequest",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getGlobalConfigCode",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getLastBatchId",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getOrderRoot",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getOrderTreeHeight",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getRollupTreeHeight",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getRollupVaultRoot",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getSequenceNumber",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getValidiumTreeHeight",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getValidiumVaultRoot",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "testedOperator",
                "type": "address"
            }
        ],
        "name": "isOperator",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            },
            {
                "internalType": "bytes32",
                "name": "configHash",
                "type": "bytes32"
            }
        ],
        "name": "registerAssetConfigurationChange",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "configHash",
                "type": "bytes32"
            }
        ],
        "name": "registerGlobalConfigurationChange",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newOperator",
                "type": "address"
            }
        ],
        "name": "registerOperator",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "assetId",
                "type": "uint256"
            },
            {
                "internalType": "bytes32",
                "name": "configHash",
                "type": "bytes32"
            }
        ],
        "name": "removeAssetConfigurationChange",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "configHash",
                "type": "bytes32"
            }
        ],
        "name": "removeGlobalConfigurationChange",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "removedOperator",
                "type": "address"
            }
        ],
        "name": "unregisterOperator",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256[]",
                "name": "programOutput",
                "type": "uint256[]"
            },
            {
                "internalType": "uint256[]",
                "name": "applicationData",
                "type": "uint256[]"
            }
        ],
        "name": "updateState",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "starkKeyA",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "starkKeyB",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "vaultIdA",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "vaultIdB",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "collateralAssetId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "syntheticAssetId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amountCollateral",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amountSynthetic",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "bool",
                "name": "aIsBuyingSynthetic",
                "type": "bool"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "nonce",
                "type": "uint256"
            }
        ],
        "name": "LogForcedTradeRequest",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "quantizedAmount",
                "type": "uint256"
            }
        ],
        "name": "LogForcedWithdrawalRequest",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "ethKey",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "sender",
                "type": "address"
            }
        ],
        "name": "LogUserRegistered",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "starkKeyA",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "starkKeyB",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultIdA",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultIdB",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "collateralAssetId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "syntheticAssetId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountCollateral",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountSynthetic",
                "type": "uint256"
            },
            {
                "internalType": "bool",
                "name": "aIsBuyingSynthetic",
                "type": "bool"
            },
            {
                "internalType": "uint256",
                "name": "submissionExpirationTime",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "nonce",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "signature",
                "type": "bytes"
            },
            {
                "internalType": "bool",
                "name": "premiumCost",
                "type": "bool"
            }
        ],
        "name": "forcedTradeRequest",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "quantizedAmount",
                "type": "uint256"
            },
            {
                "internalType": "bool",
                "name": "premiumCost",
                "type": "bool"
            }
        ],
        "name": "forcedWithdrawalRequest",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "starkKeyA",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "starkKeyB",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultIdA",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultIdB",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "collateralAssetId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "syntheticAssetId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountCollateral",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountSynthetic",
                "type": "uint256"
            },
            {
                "internalType": "bool",
                "name": "aIsBuyingSynthetic",
                "type": "bool"
            },
            {
                "internalType": "uint256",
                "name": "nonce",
                "type": "uint256"
            }
        ],
        "name": "freezeRequest",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vaultId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "quantizedAmount",
                "type": "uint256"
            }
        ],
        "name": "freezeRequest",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "ethKey",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "starkSignature",
                "type": "bytes"
            }
        ],
        "name": "registerEthAddress",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "starkKey",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "starkSignature",
                "type": "bytes"
            }
        ],
        "name": "registerSender",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]



================================================
FILE: x10/perpetual/simple_client/simple_trading_client.py
================================================
import asyncio
import dataclasses
import time
from decimal import Decimal
from typing import Awaitable, Dict, Union, cast

from x10.perpetual.accounts import AccountStreamDataModel, StarkPerpetualAccount
from x10.perpetual.configuration import EndpointConfig
from x10.perpetual.markets import MarketModel
from x10.perpetual.order_object import create_order_object
from x10.perpetual.orders import (
    OpenOrderModel,
    OrderSide,
    OrderStatus,
    PerpetualOrderModel,
)
from x10.perpetual.stream_client.perpetual_stream_connection import (
    PerpetualStreamConnection,
)
from x10.perpetual.stream_client.stream_client import PerpetualStreamClient
from x10.perpetual.trading_client.markets_information_module import (
    MarketsInformationModule,
)
from x10.perpetual.trading_client.order_management_module import OrderManagementModule
from x10.utils.http import WrappedStreamResponse


async def condition_to_awaitable(condition: asyncio.Condition) -> Awaitable:
    async def __inner():
        async with condition:
            await condition.wait()

    return await __inner()


class TimedOpenOrderModel(OpenOrderModel):
    start_nanos: int
    end_nanos: int
    operation_ms: float

    def __init__(self, start_nanos: int, end_nanos: int, open_order: OpenOrderModel):
        super().__init__(
            **dict(
                open_order.model_dump(),
                **{
                    "start_nanos": start_nanos,
                    "end_nanos": end_nanos,
                    "operation_ms": (end_nanos - start_nanos) / 1_000_000,
                },
            )
        )


@dataclasses.dataclass
class TimedCancel:
    start_nanos: int
    end_nanos: int
    operation_ms: float


@dataclasses.dataclass
class OrderWaiter:
    condition: asyncio.Condition
    open_order: None | TimedOpenOrderModel
    start_nanos: int


@dataclasses.dataclass
class CancelWaiter:
    condition: asyncio.Condition
    start_nanos: int
    end_nanos: int | None


class BlockingTradingClient:
    def __init__(self, endpoint_config: EndpointConfig, account: StarkPerpetualAccount):
        self.__endpoint_config = endpoint_config
        self.__account = account
        self.__market_module = MarketsInformationModule(endpoint_config, api_key=account.api_key)
        self.__orders_module = OrderManagementModule(endpoint_config, api_key=account.api_key)
        self.__markets: Union[None, Dict[str, MarketModel]] = None
        self.__stream_client: PerpetualStreamClient = PerpetualStreamClient(api_url=endpoint_config.stream_url)
        self.__account_stream: Union[
            None,
            PerpetualStreamConnection[WrappedStreamResponse[AccountStreamDataModel]],
        ] = None
        self.__order_waiters: Dict[str, OrderWaiter] = {}
        self.__cancel_waiters: Dict[int, CancelWaiter] = {}
        self.__orders_task: Union[None, asyncio.Task] = None
        self.__stream_lock = asyncio.Lock()

    async def handle_cancel(self, order_id: int):
        if order_id not in self.__cancel_waiters:
            return
        cancel_waiter = self.__cancel_waiters.get(order_id)
        if not cancel_waiter:
            return
        if cancel_waiter.condition:
            async with cancel_waiter.condition:
                cancel_waiter.end_nanos = time.time_ns()
                cancel_waiter.condition.notify_all()

    async def handle_update(self, order: OpenOrderModel):
        if order.external_id not in self.__order_waiters:
            return
        order_waiter = self.__order_waiters.get(order.external_id)
        if not order_waiter:
            return
        if order_waiter.condition:
            async with order_waiter.condition:
                order_waiter.open_order = TimedOpenOrderModel(
                    start_nanos=order_waiter.start_nanos,
                    end_nanos=time.time_ns(),
                    open_order=order,
                )
                order_waiter.condition.notify_all()

    async def handle_order(self, order: OpenOrderModel):
        if order.status == OrderStatus.CANCELLED.value:
            await self.handle_cancel(order.id)
        else:
            await self.handle_update(order)

    async def ___order_stream(self):
        async for event in self.__account_stream:
            if not (event.data and event.data.orders):
                continue
            for order in event.data.orders:
                await self.handle_order(order)

    async def cancel_order(self, order_id: int) -> TimedCancel:
        awaitable: Awaitable
        if order_id in self.__cancel_waiters:
            awaitable = condition_to_awaitable(self.__cancel_waiters[order_id].condition)
        else:
            self.__cancel_waiters[order_id] = CancelWaiter(
                asyncio.Condition(), start_nanos=time.time_ns(), end_nanos=None
            )
            cancel_task = asyncio.create_task(self.__orders_module.cancel_order(order_id))
            awaitable = asyncio.gather(
                cancel_task,
                asyncio.wait_for(condition_to_awaitable(self.__cancel_waiters[order_id].condition), 5),
                return_exceptions=False,
            )

        cancel_waiter = self.__cancel_waiters[order_id]
        end_nanos = None
        if cancel_waiter.end_nanos:
            end_nanos = cancel_waiter.end_nanos
        else:
            await awaitable
            end_nanos = self.__cancel_waiters[order_id].end_nanos
        del self.__cancel_waiters[order_id]
        end_nanos = cast(int, end_nanos)
        return TimedCancel(
            start_nanos=cancel_waiter.start_nanos,
            end_nanos=end_nanos,
            operation_ms=(end_nanos - cancel_waiter.start_nanos) / 1_000_000,
        )

    async def get_markets(self) -> Dict[str, MarketModel]:
        if not self.__markets:
            markets = await self.__market_module.get_markets()
            self.__markets = {m.name: m for m in markets.data}
        return self.__markets

    async def create_and_place_order(
        self,
        market_name: str,
        amount_of_synthetic: Decimal,
        price: Decimal,
        side: OrderSide,
        post_only: bool = False,
        previous_order_id: str | None = None,
    ) -> TimedOpenOrderModel:
        market = (await self.get_markets()).get(market_name)
        if not market:
            raise ValueError(f"Market '{market_name}' not found.")

        if not self.__account_stream:
            await self.__stream_lock.acquire()
            if not self.__account_stream:
                self.__account_stream = await self.__stream_client.subscribe_to_account_updates(self.__account.api_key)
                self.__orders_task = asyncio.create_task(self.___order_stream())
            self.__stream_lock.release()

        order: PerpetualOrderModel = create_order_object(
            account=self.__account,
            market=market,
            amount_of_synthetic=amount_of_synthetic,
            price=price,
            side=side,
            post_only=post_only,
            previous_order_id=previous_order_id,
        )

        if order.id in self.__order_waiters:
            raise ValueError(f"order with {order.id} hash already placed")

        self.__order_waiters[order.id] = OrderWaiter(asyncio.Condition(), None, start_nanos=time.time_ns())
        placed_order_task = asyncio.create_task(self.__orders_module.place_order(order))
        order_waiter = self.__order_waiters[order.id]
        if order_waiter.open_order:
            return order_waiter.open_order
        async with order_waiter.condition:
            await asyncio.gather(
                placed_order_task,
                asyncio.wait_for(order_waiter.condition.wait(), 5),
                return_exceptions=False,
            )
            open_model = self.__order_waiters[order.id].open_order
            del self.__order_waiters[order.id]
            if not open_model:
                raise ValueError("No Fill or Placement received for order")
            return open_model



================================================
FILE: x10/perpetual/stream_client/__init__.py
================================================
from x10.perpetual.stream_client.stream_client import (  # noqa: F401
    PerpetualStreamClient,
)



================================================
FILE: x10/perpetual/stream_client/perpetual_stream_connection.py
================================================
from types import TracebackType
from typing import AsyncIterator, Generic, Optional, Type, TypeVar

import websockets
from websockets import WebSocketClientProtocol

from x10.config import USER_AGENT
from x10.utils.http import RequestHeader
from x10.utils.log import get_logger
from x10.utils.model import X10BaseModel

LOGGER = get_logger(__name__)

StreamMsgResponseType = TypeVar("StreamMsgResponseType", bound=X10BaseModel)


class PerpetualStreamConnection(Generic[StreamMsgResponseType]):
    __stream_url: str
    __msg_model_class: Type[StreamMsgResponseType]
    __api_key: Optional[str]
    __msgs_count: int
    __websocket: Optional[WebSocketClientProtocol]

    def __init__(
        self,
        stream_url: str,
        msg_model_class: Type[StreamMsgResponseType],
        api_key: Optional[str],
    ):
        super().__init__()

        self.__stream_url = stream_url
        self.__msg_model_class = msg_model_class
        self.__api_key = api_key
        self.__msgs_count = 0
        self.__websocket = None

    async def send(self, data):
        await self.__websocket.send(data)

    async def recv(self) -> StreamMsgResponseType:
        return await self.__receive()

    async def close(self):
        assert self.__websocket is not None
        assert not self.__websocket.closed

        await self.__websocket.close()

        LOGGER.debug("Stream closed: %s", self.__stream_url)

    @property
    def msgs_count(self):
        return self.__msgs_count

    @property
    def closed(self):
        assert self.__websocket is not None

        return self.__websocket.closed

    def __aiter__(self) -> AsyncIterator[StreamMsgResponseType]:
        return self

    async def __anext__(self) -> StreamMsgResponseType:
        assert self.__websocket is not None

        if self.__websocket.closed:
            raise StopAsyncIteration

        return await self.__receive()

    async def __receive(self) -> StreamMsgResponseType:
        assert self.__websocket is not None

        data = await self.__websocket.recv()
        self.__msgs_count += 1

        return self.__msg_model_class.model_validate_json(data)

    def __await__(self):
        return self.__await_impl__().__await__()

    async def __aenter__(self):
        # Calls `self.__await__()` implicitly
        return await self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ):
        await self.close()

    async def __await_impl__(self):
        extra_headers = {
            RequestHeader.USER_AGENT.value: USER_AGENT,
        }

        if self.__api_key is not None:
            extra_headers[RequestHeader.API_KEY.value] = self.__api_key

        self.__websocket = await websockets.connect(self.__stream_url, extra_headers=extra_headers)

        LOGGER.debug("Connected to stream: %s", self.__stream_url)

        return self



================================================
FILE: x10/perpetual/stream_client/stream_client.py
================================================
from typing import Dict, List, Optional, Type

from x10.perpetual.accounts import AccountStreamDataModel
from x10.perpetual.candles import CandleInterval, CandleModel, CandleType
from x10.perpetual.funding_rates import FundingRateModel
from x10.perpetual.orderbooks import OrderbookUpdateModel
from x10.perpetual.stream_client.perpetual_stream_connection import (
    PerpetualStreamConnection,
    StreamMsgResponseType,
)
from x10.perpetual.trades import PublicTradeModel
from x10.utils.http import WrappedStreamResponse, get_url


class PerpetualStreamClient:
    """
    X10 Perpetual Stream Client for the X10 WebSocket v1.
    """

    __api_url: str

    def __init__(self, *, api_url: str):
        super().__init__()

        self.__api_url = api_url

    def subscribe_to_orderbooks(self, market_name: Optional[str] = None):
        """
        https://api.docs.extended.exchange/#orderbooks-stream
        """

        url = self.__get_url("/orderbooks/<market?>", market=market_name)
        return self.__connect(url, WrappedStreamResponse[OrderbookUpdateModel])

    def subscribe_to_public_trades(self, market_name: Optional[str] = None):
        """
        https://api.docs.extended.exchange/#trades-stream
        """

        url = self.__get_url("/publicTrades/<market?>", market=market_name)
        return self.__connect(url, WrappedStreamResponse[List[PublicTradeModel]])

    def subscribe_to_funding_rates(self, market_name: Optional[str] = None):
        """
        https://api.docs.extended.exchange/#funding-rates-stream
        """

        url = self.__get_url("/funding/<market?>", market=market_name)
        return self.__connect(url, WrappedStreamResponse[FundingRateModel])

    def subscribe_to_candles(self, market_name: str, candle_type: CandleType, interval: CandleInterval):
        """
        https://api.docs.extended.exchange/#candles-stream
        """

        url = self.__get_url(
            "/candles/<market>/<candle_type>",
            market=market_name,
            candle_type=candle_type,
            query={
                "interval": interval,
            },
        )
        return self.__connect(url, WrappedStreamResponse[List[CandleModel]])

    def subscribe_to_account_updates(self, api_key: str):
        """
        https://api.docs.extended.exchange/#account-updates-stream
        """

        url = self.__get_url("/account")
        return self.__connect(url, WrappedStreamResponse[AccountStreamDataModel], api_key)

    def __get_url(self, path: str, *, query: Optional[Dict[str, str | List[str]]] = None, **path_params) -> str:
        return get_url(f"{self.__api_url}{path}", query=query, **path_params)

    @staticmethod
    def __connect(
        stream_url: str,
        msg_model_class: Type[StreamMsgResponseType],
        api_key: Optional[str] = None,
    ) -> PerpetualStreamConnection[StreamMsgResponseType]:
        return PerpetualStreamConnection(stream_url, msg_model_class, api_key)



================================================
FILE: x10/perpetual/trading_client/__init__.py
================================================
from x10.perpetual.trading_client.trading_client import (  # noqa: F401
    PerpetualTradingClient,
)



================================================
FILE: x10/perpetual/trading_client/account_module.py
================================================
from decimal import Decimal
from typing import Callable, List, Optional

from x10.perpetual.accounts import AccountLeverage
from x10.perpetual.assets import (
    AssetOperationModel,
    AssetOperationStatus,
    AssetOperationType,
)
from x10.perpetual.balances import BalanceModel
from x10.perpetual.contract import call_stark_perpetual_deposit
from x10.perpetual.fees import TradingFeeModel
from x10.perpetual.orders import OpenOrderModel, OrderSide, OrderType
from x10.perpetual.positions import PositionHistoryModel, PositionModel, PositionSide
from x10.perpetual.trades import AccountTradeModel, TradeType
from x10.perpetual.trading_client.base_module import BaseModule
from x10.perpetual.transfer_object import create_transfer_object
from x10.perpetual.withdrawal_object import create_withdrawal_object
from x10.utils.http import (
    WrappedApiResponse,
    send_get_request,
    send_patch_request,
    send_post_request,
)
from x10.utils.model import EmptyModel


class AccountModule(BaseModule):
    async def get_balance(self) -> WrappedApiResponse[BalanceModel]:
        """
        https://api.docs.extended.exchange/#get-balance
        """

        url = self._get_url("/user/balance")
        return await send_get_request(await self.get_session(), url, BalanceModel, api_key=self._get_api_key())

    async def get_positions(
        self, *, market_names: Optional[List[str]] = None, position_side: Optional[PositionSide] = None
    ) -> WrappedApiResponse[List[PositionModel]]:
        """
        https://api.docs.extended.exchange/#get-positions
        """

        url = self._get_url("/user/positions", query={"market": market_names, "side": position_side})
        return await send_get_request(await self.get_session(), url, List[PositionModel], api_key=self._get_api_key())

    async def get_positions_history(
        self,
        market_names: Optional[List[str]] = None,
        position_side: Optional[PositionSide] = None,
        cursor: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> WrappedApiResponse[List[PositionHistoryModel]]:
        """
        https://api.docs.extended.exchange/#get-positions-history
        """

        url = self._get_url(
            "/user/positions/history",
            query={"market": market_names, "side": position_side, "cursor": cursor, "limit": limit},
        )
        return await send_get_request(
            await self.get_session(), url, List[PositionHistoryModel], api_key=self._get_api_key()
        )

    async def get_open_orders(
        self,
        market_names: Optional[List[str]] = None,
        order_type: Optional[OrderType] = None,
        order_side: Optional[OrderSide] = None,
    ) -> WrappedApiResponse[List[OpenOrderModel]]:
        """
        https://api.docs.extended.exchange/#get-open-orders
        """

        url = self._get_url(
            "/user/orders",
            query={"market": market_names, "type": order_type, "side": order_side},
        )
        return await send_get_request(await self.get_session(), url, List[OpenOrderModel], api_key=self._get_api_key())

    async def get_orders_history(
        self,
        market_names: Optional[List[str]] = None,
        order_type: Optional[OrderType] = None,
        order_side: Optional[OrderSide] = None,
        cursor: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> WrappedApiResponse[List[OpenOrderModel]]:
        """
        https://api.docs.extended.exchange/#get-orders-history
        """

        url = self._get_url(
            "/user/orders/history",
            query={"market": market_names, "type": order_type, "side": order_side, "cursor": cursor, "limit": limit},
        )
        return await send_get_request(await self.get_session(), url, List[OpenOrderModel], api_key=self._get_api_key())

    async def get_trades(
        self,
        market_names: List[str],
        trade_side: Optional[OrderSide] = None,
        trade_type: Optional[TradeType] = None,
    ) -> WrappedApiResponse[List[AccountTradeModel]]:
        """
        https://api.docs.extended.exchange/#get-trades
        """

        url = self._get_url(
            "/user/trades",
            query={"market": market_names, "side": trade_side, "type": trade_type},
        )

        return await send_get_request(
            await self.get_session(), url, List[AccountTradeModel], api_key=self._get_api_key()
        )

    async def get_fees(self, *, market_names: List[str]) -> WrappedApiResponse[List[TradingFeeModel]]:
        """
        https://api.docs.extended.exchange/#get-fees
        """

        url = self._get_url("/user/fees", query={"market": market_names})
        return await send_get_request(await self.get_session(), url, List[TradingFeeModel], api_key=self._get_api_key())

    async def get_leverage(self, market_names: List[str]) -> WrappedApiResponse[List[AccountLeverage]]:
        """
        https://api.docs.extended.exchange/#get-current-leverage
        """

        url = self._get_url("/user/leverage", query={"market": market_names})
        return await send_get_request(await self.get_session(), url, List[AccountLeverage], api_key=self._get_api_key())

    async def update_leverage(self, market_name: str, leverage: Decimal) -> WrappedApiResponse[EmptyModel]:
        """
        https://api.docs.extended.exchange/#update-leverage
        """

        url = self._get_url("/user/leverage")
        request_model = AccountLeverage(market=market_name, leverage=leverage)
        return await send_patch_request(
            await self.get_session(),
            url,
            EmptyModel,
            json=request_model.to_api_request_json(),
            api_key=self._get_api_key(),
        )

    async def transfer(
        self,
        to_vault: int,
        to_l2_key: str,
        amount: Decimal,
    ) -> WrappedApiResponse[EmptyModel]:
        from_vault = self._get_stark_account().vault
        from_l2_key = self._get_stark_account().public_key
        url = self._get_url("/user/transfer/onchain")
        request_model = create_transfer_object(
            from_vault=from_vault,
            from_l2_key=from_l2_key,
            to_vault=to_vault,
            to_l2_key=to_l2_key,
            amount=amount,
            config=self._get_endpoint_config(),
            stark_account=self._get_stark_account(),
        )

        return await send_post_request(
            await self.get_session(),
            url,
            EmptyModel,
            json=request_model.to_api_request_json(),
            api_key=self._get_api_key(),
        )

    async def slow_withdrawal(
        self,
        amount: Decimal,
        eth_address: str,
    ) -> WrappedApiResponse[int]:
        url = self._get_url("/user/withdrawal/onchain")
        request_model = create_withdrawal_object(
            amount=amount,
            eth_address=eth_address,
            stark_account=self._get_stark_account(),
            config=self._get_endpoint_config(),
        )

        payload = request_model.to_api_request_json()
        return await send_post_request(
            await self.get_session(),
            url,
            int,
            json=payload,
            api_key=self._get_api_key(),
        )

    async def asset_operations(
        self,
        operations_type: Optional[List[AssetOperationType]] = None,
        operations_status: Optional[List[AssetOperationStatus]] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        cursor: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> WrappedApiResponse[List[AssetOperationModel]]:
        url = self._get_url(
            "/user/assetOperations",
            query={
                "type": [operation_type.name for operation_type in operations_type] if operations_type else None,
                "status": [operation_status.name for operation_status in operations_status]
                if operations_status
                else None,
                "startTime": start_time,
                "endTime": end_time,
                "cursor": cursor,
                "limit": limit,
            },
        )
        return await send_get_request(
            await self.get_session(), url, List[AssetOperationModel], api_key=self._get_api_key()
        )

    async def deposit(self, amount: Decimal, get_eth_private_key: Callable[[], str]) -> str:
        stark_account = self.__stark_account

        if not stark_account:
            raise ValueError("Stark account is not set")

        return call_stark_perpetual_deposit(
            l2_vault=stark_account.vault,
            l2_key=stark_account.public_key,
            config=self._get_endpoint_config(),
            human_readable_amount=amount,
            get_eth_private_key=get_eth_private_key,
        )



================================================
FILE: x10/perpetual/trading_client/base_module.py
================================================
from typing import Dict, Optional

import aiohttp

from x10.errors import X10Error
from x10.perpetual.accounts import StarkPerpetualAccount
from x10.perpetual.configuration import EndpointConfig
from x10.utils.http import CLIENT_TIMEOUT, get_url


class BaseModule:
    __endpoint_config: EndpointConfig
    __api_key: Optional[str]
    __stark_account: Optional[StarkPerpetualAccount]
    __session: Optional[aiohttp.ClientSession]

    def __init__(
        self,
        endpoint_config: EndpointConfig,
        *,
        api_key: Optional[str] = None,
        stark_account: Optional[StarkPerpetualAccount] = None,
    ):
        super().__init__()
        self.__endpoint_config = endpoint_config
        self.__api_key = api_key
        self.__stark_account = stark_account
        self.__session = None

    def _get_url(self, path: str, *, query: Optional[Dict] = None, **path_params) -> str:
        return get_url(f"{self.__endpoint_config.api_base_url}{path}", query=query, **path_params)

    def _get_endpoint_config(self) -> EndpointConfig:
        return self.__endpoint_config

    def _get_api_key(self):
        if not self.__api_key:
            raise X10Error("API key is not set")

        return self.__api_key

    def _get_stark_account(self):
        if not self.__stark_account:
            raise X10Error("Stark account is not set")

        return self.__stark_account

    async def get_session(self) -> aiohttp.ClientSession:
        if self.__session is None:
            created_session = aiohttp.ClientSession(timeout=CLIENT_TIMEOUT)
            self.__session = created_session

        return self.__session

    async def close_session(self):
        if self.__session:
            await self.__session.close()
            self.__session = None



================================================
FILE: x10/perpetual/trading_client/info_module.py
================================================
from x10.perpetual.trading_client.base_module import BaseModule
from x10.utils.http import send_get_request
from x10.utils.model import X10BaseModel


class _SettingsModel(X10BaseModel):
    stark_ex_contract_address: str


class InfoModule(BaseModule):
    async def get_settings(self):
        url = self._get_url("/info/settings")
        return await send_get_request(await self.get_session(), url, _SettingsModel)



================================================
FILE: x10/perpetual/trading_client/markets_information_module.py
================================================
from datetime import datetime
from typing import List, Optional

from x10.perpetual.candles import CandleInterval, CandleModel, CandleType
from x10.perpetual.funding_rates import FundingRateModel
from x10.perpetual.markets import MarketModel, MarketStatsModel
from x10.perpetual.orderbooks import OrderbookUpdateModel
from x10.perpetual.trading_client.base_module import BaseModule
from x10.utils.date import to_epoch_millis
from x10.utils.http import send_get_request


class MarketsInformationModule(BaseModule):
    async def get_markets(self, *, market_names: Optional[List[str]] = None):
        """
        https://api.docs.extended.exchange/#get-markets
        """

        url = self._get_url("/info/markets", query={"market": market_names})
        return await send_get_request(await self.get_session(), url, List[MarketModel])

    async def get_market_statistics(self, *, market_name: str):
        """
        https://api.docs.extended.exchange/#get-market-statistics
        """

        url = self._get_url("/info/markets/<market>/stats", market=market_name)
        return await send_get_request(await self.get_session(), url, MarketStatsModel)

    async def get_candles_history(
        self,
        *,
        market_name: str,
        candle_type: CandleType,
        interval: CandleInterval,
        limit: Optional[int] = None,
        end_time: Optional[datetime] = None,
    ):
        """
        https://api.docs.extended.exchange/#get-candles-history
        """

        url = self._get_url(
            "/info/candles/<market>/<candle_type>",
            market=market_name,
            candle_type=candle_type,
            query={
                "interval": interval,
                "limit": limit,
                "endTime": to_epoch_millis(end_time) if end_time else None,
            },
        )
        return await send_get_request(await self.get_session(), url, List[CandleModel])

    async def get_funding_rates_history(self, *, market_name: str, start_time: datetime, end_time: datetime):
        """
        https://api.docs.extended.exchange/#get-funding-rates-history
        """

        url = self._get_url(
            "/info/<market>/funding",
            market=market_name,
            query={
                "startTime": to_epoch_millis(start_time),
                "endTime": to_epoch_millis(end_time),
            },
        )
        return await send_get_request(await self.get_session(), url, List[FundingRateModel])

    async def get_orderbook_snapshot(self, *, market_name: str):
        """
        https://api.docs.extended.exchange/#get-market-order-book
        """

        url = self._get_url("/info/markets/<market>/orderbook", market=market_name)
        return await send_get_request(await self.get_session(), url, OrderbookUpdateModel)



================================================
FILE: x10/perpetual/trading_client/order_management_module.py
================================================
from typing import List, Optional

from x10.perpetual.orders import PerpetualOrderModel, PlacedOrderModel
from x10.perpetual.trading_client.base_module import BaseModule
from x10.utils.http import send_delete_request, send_post_request
from x10.utils.log import get_logger
from x10.utils.model import EmptyModel, X10BaseModel

LOGGER = get_logger(__name__)


class _MassCancelRequestModel(X10BaseModel):
    order_ids: Optional[List[int]] = None
    external_order_ids: Optional[List[str]] = None
    markets: Optional[List[str]] = None
    cancel_all: Optional[bool] = None


class OrderManagementModule(BaseModule):
    async def place_order(self, order: PerpetualOrderModel):
        """
        Placed new order on the exchange.

        :param order: Order object created by `create_order_object` method.

        https://api.docs.extended.exchange/#create-order
        """
        LOGGER.debug("Placing an order: id=%s", order.id)

        url = self._get_url("/user/order")
        response = await send_post_request(
            await self.get_session(),
            url,
            PlacedOrderModel,
            json=order.to_api_request_json(),
            api_key=self._get_api_key(),
        )
        return response

    async def cancel_order(self, order_id: int):
        """
        https://api.docs.extended.exchange/#cancel-order
        """

        url = self._get_url("/user/order/<order_id>", order_id=order_id)
        return await send_delete_request(await self.get_session(), url, EmptyModel, api_key=self._get_api_key())

    async def cancel_order_by_external_id(self, order_external_id: str):
        """
        https://api.docs.extended.exchange/#cancel-order
        """

        url = self._get_url("/user/order", query={"externalId": order_external_id})
        return await send_delete_request(await self.get_session(), url, EmptyModel, api_key=self._get_api_key())

    async def mass_cancel(
        self,
        *,
        order_ids: Optional[List[int]] = None,
        external_order_ids: Optional[List[str]] = None,
        markets: Optional[List[str]] = None,
        cancel_all: Optional[bool] = False,
    ):
        """
        https://api.docs.extended.exchange/#mass-cancel
        """

        url = self._get_url("/user/order/massCancel")
        request_model = _MassCancelRequestModel(
            order_ids=order_ids,
            external_order_ids=external_order_ids,
            markets=markets,
            cancel_all=cancel_all,
        )
        return await send_post_request(
            await self.get_session(),
            url,
            EmptyModel,
            json=request_model.to_api_request_json(exclude_none=True),
            api_key=self._get_api_key(),
        )



================================================
FILE: x10/perpetual/trading_client/trading_client.py
================================================
from datetime import datetime
from decimal import Decimal
from typing import Dict, Optional

from x10.perpetual.accounts import StarkPerpetualAccount
from x10.perpetual.configuration import EndpointConfig
from x10.perpetual.markets import MarketModel
from x10.perpetual.order_object import create_order_object
from x10.perpetual.orders import (
    OrderSide,
    PlacedOrderModel,
    SelfTradeProtectionLevel,
    TimeInForce,
)
from x10.perpetual.trading_client.account_module import AccountModule
from x10.perpetual.trading_client.info_module import InfoModule
from x10.perpetual.trading_client.markets_information_module import (
    MarketsInformationModule,
)
from x10.perpetual.trading_client.order_management_module import OrderManagementModule
from x10.utils.http import WrappedApiResponse
from x10.utils.log import get_logger

LOGGER = get_logger(__name__)


class PerpetualTradingClient:
    """
    X10 Perpetual Trading Client for the X10 REST API v1.
    """

    __markets: Dict[str, MarketModel] | None
    __stark_account: StarkPerpetualAccount

    __info_module: InfoModule
    __markets_info_module: MarketsInformationModule
    __account_module: AccountModule
    __order_management_module: OrderManagementModule

    async def place_order(
        self,
        market_name: str,
        amount_of_synthetic: Decimal,
        price: Decimal,
        side: OrderSide,
        post_only: bool = False,
        previous_order_id=None,
        expire_time: Optional[datetime] = None,
        time_in_force: TimeInForce = TimeInForce.GTT,
        self_trade_protection_level: SelfTradeProtectionLevel = SelfTradeProtectionLevel.ACCOUNT,
    ) -> WrappedApiResponse[PlacedOrderModel]:
        if not self.__stark_account:
            raise ValueError("Stark account is not set")

        if not self.__markets:
            markets = await self.__markets_info_module.get_markets()
            self.__markets = {m.name: m for m in markets.data}

        market = self.__markets.get(market_name)
        if not market:
            raise ValueError(f"Market {market_name} not found")

        order = create_order_object(
            self.__stark_account,
            market,
            amount_of_synthetic,
            price,
            side,
            post_only,
            previous_order_id,
            expire_time,
            time_in_force=time_in_force,
            self_trade_protection_level=self_trade_protection_level,
        )

        return await self.__order_management_module.place_order(order)

    async def close(self):
        await self.__markets_info_module.close_session()
        await self.__account_module.close_session()
        await self.__order_management_module.close_session()

    def __init__(self, endpoint_config: EndpointConfig, stark_account: StarkPerpetualAccount | None = None):
        api_key = stark_account.api_key if stark_account else None

        self.__markets = None

        if stark_account:
            self.__stark_account = stark_account

        self.__info_module = InfoModule(endpoint_config)
        self.__markets_info_module = MarketsInformationModule(endpoint_config, api_key=api_key)
        self.__account_module = AccountModule(endpoint_config, api_key=api_key, stark_account=stark_account)
        self.__order_management_module = OrderManagementModule(endpoint_config, api_key=api_key)

    @property
    def info(self):
        return self.__info_module

    @property
    def markets_info(self):
        return self.__markets_info_module

    @property
    def account(self):
        return self.__account_module

    @property
    def orders(self):
        return self.__order_management_module



================================================
FILE: x10/perpetual/user_client/__init__.py
================================================
[Empty file]


================================================
FILE: x10/perpetual/user_client/l1_signing.py
================================================
[Empty file]


================================================
FILE: x10/perpetual/user_client/onboarding.py
================================================
import re
from dataclasses import dataclass
from datetime import datetime, timezone

from eth_account.messages import SignableMessage, encode_typed_data
from eth_account.signers.local import LocalAccount

from vendor.starkware.crypto import signature as stark_sign
from x10.perpetual.accounts import AccountModel
from x10.utils.model import X10BaseModel

register_action = "REGISTER"
sub_account_action = "CREATE_SUB_ACCOUNT"


class OnboardedClientModel(X10BaseModel):
    l1_address: str
    default_account: AccountModel


@dataclass
class StarkKeyPair:
    private: int
    public: int

    @property
    def public_hex(self) -> str:
        return hex(self.public)

    @property
    def private_hex(self) -> str:
        return hex(self.private)


@dataclass
class AccountRegistration:
    account_index: int
    wallet: str
    tos_accepted: bool
    time: datetime
    action: str

    def __post_init__(self):
        self.time_string = self.time.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    def to_signable_message(self, signing_domain) -> SignableMessage:
        domain = {"name": signing_domain}

        message = {
            "accountIndex": self.account_index,
            "wallet": self.wallet,
            "tosAccepted": self.tos_accepted,
            "time": self.time_string,
            "action": self.action,
        }
        types = {
            "EIP712Domain": [
                {"name": "name", "type": "string"},
            ],
            "AccountRegistration": [
                {"name": "accountIndex", "type": "int8"},
                {"name": "wallet", "type": "address"},
                {"name": "tosAccepted", "type": "bool"},
                {"name": "time", "type": "string"},
                {"name": "action", "type": "string"},
            ],
        }
        primary_type = "AccountRegistration"
        structured_data = {
            "types": types,
            "domain": domain,
            "primaryType": primary_type,
            "message": message,
        }
        return encode_typed_data(full_message=structured_data)

    def to_json(self):
        return {
            "accountIndex": self.account_index,
            "wallet": self.wallet,
            "tosAccepted": self.tos_accepted,
            "time": self.time_string,
            "action": self.action,
        }


@dataclass
class SubAccountOnboardingPayload:
    l2_key: int
    l2_r: int
    l2_s: int
    account_registration: AccountRegistration
    description: str

    def to_json(self):
        return {
            "l2Key": hex(self.l2_key),
            "l2Signature": {
                "r": hex(self.l2_r),
                "s": hex(self.l2_s),
            },
            "accountCreation": self.account_registration.to_json(),
            "description": self.description,
        }


@dataclass
class OnboardingPayLoad:
    l1_signature: str
    l2_key: int
    l2_r: int
    l2_s: int
    account_registration: AccountRegistration
    referral_code: str | None = None

    def to_json(self):
        return {
            "l1Signature": self.l1_signature,
            "l2Key": hex(self.l2_key),
            "l2Signature": {
                "r": hex(self.l2_r),
                "s": hex(self.l2_s),
            },
            "accountCreation": self.account_registration.to_json(),
            "referralCode": self.referral_code,
        }


def get_registration_struct_to_sign(
    account_index: int, address: str, timestamp: datetime, action: str
) -> AccountRegistration:
    return AccountRegistration(
        account_index=account_index,
        wallet=address,
        tos_accepted=True,
        time=timestamp,
        action=action,
    )


def get_key_derivation_struct_to_sign(account_index: int, address: str, signing_domain: str) -> SignableMessage:
    primary_type = "AccountCreation"
    domain = {"name": signing_domain}
    message = {
        "accountIndex": account_index,
        "wallet": address,
        "tosAccepted": True,
    }
    types = {
        "EIP712Domain": [
            {"name": "name", "type": "string"},
        ],
        "AccountCreation": [
            {"name": "accountIndex", "type": "int8"},
            {"name": "wallet", "type": "address"},
            {"name": "tosAccepted", "type": "bool"},
        ],
    }
    structured_data = {
        "types": types,
        "domain": domain,
        "primaryType": primary_type,
        "message": message,
    }
    return encode_typed_data(full_message=structured_data)


def get_private_key_from_eth_signature(eth_signature: str) -> int:
    eth_sig_truncated = re.sub("^0x", "", eth_signature)
    r = eth_sig_truncated[:64]
    return stark_sign.grind_key(int(r, 16), stark_sign.EC_ORDER)


def get_l2_keys_from_l1_account(l1_account: LocalAccount, account_index: int, signing_domain: str) -> StarkKeyPair:
    struct = get_key_derivation_struct_to_sign(
        account_index=account_index,
        address=l1_account.address,
        signing_domain=signing_domain,
    )
    s = l1_account.sign_message(struct)
    private = get_private_key_from_eth_signature(s.signature.hex())
    public = stark_sign.private_to_stark_key(private)
    return StarkKeyPair(private=private, public=public)


def get_onboarding_payload(
    account: LocalAccount,
    signing_domain: str,
    key_pair: StarkKeyPair,
    time: datetime | None = None,
    referral_code: str | None = None,
) -> OnboardingPayLoad:
    if time is None:
        time = datetime.now(timezone.utc)

    registration_payload = get_registration_struct_to_sign(
        account_index=0, address=account.address, timestamp=time, action=register_action
    )
    l1_signature = account.sign_message(
        registration_payload.to_signable_message(signing_domain=signing_domain)
    ).signature.hex()
    l2_message = stark_sign.pedersen_hash(int(account.address, 16), key_pair.public)
    l2_r, l2_s = stark_sign.sign(msg_hash=l2_message, priv_key=key_pair.private)
    onboarding_payload = OnboardingPayLoad(
        l1_signature=l1_signature,
        l2_key=key_pair.public,
        l2_r=l2_r,
        l2_s=l2_s,
        account_registration=registration_payload,
        referral_code=referral_code,
    )
    return onboarding_payload


def get_sub_account_creation_payload(
    account_index: int, l1_address: str, key_pair: StarkKeyPair, description: str, time: datetime | None = None
):
    if time is None:
        time = datetime.now(timezone.utc)

    registration_payload = get_registration_struct_to_sign(
        account_index=account_index,
        address=l1_address,
        timestamp=time,
        action=sub_account_action,
    )

    l2_message = stark_sign.pedersen_hash(int(l1_address, 16), key_pair.public)
    l2_r, l2_s = stark_sign.sign(msg_hash=l2_message, priv_key=key_pair.private)

    return SubAccountOnboardingPayload(
        l2_key=key_pair.public,
        l2_r=l2_r,
        l2_s=l2_s,
        account_registration=registration_payload,
        description=description,
    )



================================================
FILE: x10/perpetual/user_client/user_client.py
================================================
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal
from typing import Callable, Dict, List, Optional

import aiohttp
from eth_account import Account
from eth_account.messages import encode_defunct
from eth_account.signers.local import LocalAccount

from x10.errors import X10Error
from x10.perpetual.accounts import AccountModel, ApiKeyRequestModel, ApiKeyResponseModel
from x10.perpetual.configuration import EndpointConfig
from x10.perpetual.contract import (
    call_stark_perpetual_withdraw,
    call_stark_perpetual_withdraw_balance,
)
from x10.perpetual.user_client.onboarding import (
    OnboardedClientModel,
    StarkKeyPair,
    get_l2_keys_from_l1_account,
    get_onboarding_payload,
    get_sub_account_creation_payload,
)
from x10.utils.http import (  # WrappedApiResponse,; send_get_request,; send_patch_request,
    CLIENT_TIMEOUT,
    get_url,
    send_get_request,
    send_post_request,
)

L1_AUTH_SIGNATURE_HEADER = "L1_SIGNATURE"
L1_MESSAGE_TIME_HEADER = "L1_MESSAGE_TIME"
ACTIVE_ACCOUNT_HEADER = "X-X10-ACTIVE-ACCOUNT"


class SubAccountExists(X10Error):
    pass


@dataclass
class OnBoardedAccount:
    account: AccountModel
    l2_key_pair: StarkKeyPair


class UserClient:
    __endpoint_config: EndpointConfig
    __l1_private_key: Callable[[], str]
    __session: Optional[aiohttp.ClientSession] = None

    def __init__(
        self,
        endpoint_config: EndpointConfig,
        l1_private_key: Callable[[], str],
    ):
        super().__init__()
        self.__endpoint_config = endpoint_config
        self.__l1_private_key = l1_private_key

    def _get_url(self, base_url: str, path: str, *, query: Optional[Dict] = None, **path_params) -> str:
        return get_url(f"{base_url}{path}", query=query, **path_params)

    async def get_session(self) -> aiohttp.ClientSession:
        if self.__session is None:
            created_session = aiohttp.ClientSession(timeout=CLIENT_TIMEOUT)
            self.__session = created_session

        return self.__session

    async def close_session(self):
        if self.__session:
            await self.__session.close()
            self.__session = None

    async def onboard(self, referral_code: Optional[str] = None):
        signing_account: LocalAccount = Account.from_key(self.__l1_private_key())
        key_pair = get_l2_keys_from_l1_account(
            l1_account=signing_account, account_index=0, signing_domain=self.__endpoint_config.signing_domain
        )
        payload = get_onboarding_payload(
            signing_account,
            signing_domain=self.__endpoint_config.signing_domain,
            key_pair=key_pair,
            referral_code=referral_code,
        )
        url = self._get_url(self.__endpoint_config.onboarding_url, path="/auth/onboard")
        onboarding_response = await send_post_request(
            await self.get_session(), url, OnboardedClientModel, json=payload.to_json()
        )

        onboarded_client = onboarding_response.data
        if onboarded_client is None:
            raise ValueError("No account data returned from onboarding")

        return OnBoardedAccount(account=onboarded_client.default_account, l2_key_pair=key_pair)

    async def onboard_subaccount(self, account_index: int, description: str | None = None):
        request_path = "/auth/onboard/subaccount"
        if description is None:
            description = f"Subaccount {account_index}"

        signing_account: LocalAccount = Account.from_key(self.__l1_private_key())
        time = datetime.now(timezone.utc)
        auth_time_string = time.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        l1_message = f"{request_path}@{auth_time_string}".encode(encoding="utf-8")
        signable_message = encode_defunct(l1_message)
        l1_signature = signing_account.sign_message(signable_message)
        key_pair = get_l2_keys_from_l1_account(
            l1_account=signing_account,
            account_index=account_index,
            signing_domain=self.__endpoint_config.signing_domain,
        )
        payload = get_sub_account_creation_payload(
            account_index=account_index,
            l1_address=signing_account.address,
            key_pair=key_pair,
            description=description,
        )
        headers = {
            L1_AUTH_SIGNATURE_HEADER: l1_signature.signature.hex(),
            L1_MESSAGE_TIME_HEADER: auth_time_string,
        }
        url = self._get_url(self.__endpoint_config.onboarding_url, path=request_path)

        try:
            onboarding_response = await send_post_request(
                await self.get_session(),
                url,
                AccountModel,
                json=payload.to_json(),
                request_headers=headers,
                response_code_to_exception={409: SubAccountExists},
            )
            onboarded_account = onboarding_response.data
        except SubAccountExists:
            client_accounts = await self.get_accounts()
            account_with_index = [
                account for account in client_accounts if account.account.account_index == account_index
            ]
            if not account_with_index:
                raise SubAccountExists("Subaccount already exists but not found in client accounts")
            onboarded_account = account_with_index[0].account
        if onboarded_account is None:
            raise ValueError("No account data returned from onboarding")
        return OnBoardedAccount(account=onboarded_account, l2_key_pair=key_pair)

    async def get_accounts(self) -> List[OnBoardedAccount]:
        request_path = "/api/v1/user/accounts"
        signing_account: LocalAccount = Account.from_key(self.__l1_private_key())
        time = datetime.now(timezone.utc)
        auth_time_string = time.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        l1_message = f"{request_path}@{auth_time_string}".encode(encoding="utf-8")
        signable_message = encode_defunct(l1_message)
        l1_signature = signing_account.sign_message(signable_message)
        headers = {
            L1_AUTH_SIGNATURE_HEADER: l1_signature.signature.hex(),
            L1_MESSAGE_TIME_HEADER: auth_time_string,
        }
        url = self._get_url(self.__endpoint_config.onboarding_url, path=request_path)
        response = await send_get_request(await self.get_session(), url, List[AccountModel], request_headers=headers)
        accounts = response.data or []

        return [
            OnBoardedAccount(
                account=account,
                l2_key_pair=get_l2_keys_from_l1_account(
                    l1_account=signing_account,
                    account_index=account.account_index,
                    signing_domain=self.__endpoint_config.signing_domain,
                ),
            )
            for account in accounts
        ]

    async def create_account_api_key(self, account: AccountModel, description: str | None) -> str:
        request_path = "/api/v1/user/account/api-key"
        if description is None:
            description = "trading api key for account {}".format(account.id)

        signing_account: LocalAccount = Account.from_key(self.__l1_private_key())
        time = datetime.now(timezone.utc)
        auth_time_string = time.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        l1_message = f"{request_path}@{auth_time_string}".encode(encoding="utf-8")
        signable_message = encode_defunct(l1_message)
        l1_signature = signing_account.sign_message(signable_message)
        headers = {
            L1_AUTH_SIGNATURE_HEADER: l1_signature.signature.hex(),
            L1_MESSAGE_TIME_HEADER: auth_time_string,
            ACTIVE_ACCOUNT_HEADER: str(account.id),
        }
        url = self._get_url(self.__endpoint_config.onboarding_url, path=request_path)
        request = ApiKeyRequestModel(description=description)
        response = await send_post_request(
            await self.get_session(),
            url,
            ApiKeyResponseModel,
            json=request.to_api_request_json(),
            request_headers=headers,
        )
        response_data = response.data
        if response_data is None:
            raise ValueError("No API key data returned from onboarding")
        return response_data.key

    async def perform_l1_withdrawal(self) -> str:
        return call_stark_perpetual_withdraw(config=self.__endpoint_config, get_eth_private_key=self.__l1_private_key)

    async def available_l1_withdrawal_balance(self) -> Decimal:
        return call_stark_perpetual_withdraw_balance(self.__l1_private_key, self.__endpoint_config)



================================================
FILE: x10/utils/__init__.py
================================================
[Empty file]


================================================
FILE: x10/utils/date.py
================================================
from datetime import datetime, timezone


def utc_now():
    return datetime.now(tz=timezone.utc)


def to_epoch_millis(value: datetime):
    assert value.tzinfo == timezone.utc, "`value` must be in UTC"

    return int(value.timestamp() * 1000)



================================================
FILE: x10/utils/http.py
================================================
import itertools
import re
from enum import Enum
from typing import Any, Dict, Generic, List, Optional, Sequence, Type, TypeVar, Union

import aiohttp
from aiohttp import ClientResponse, ClientTimeout
from pydantic import GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema

from x10.config import DEFAULT_REQUEST_TIMEOUT_SECONDS, USER_AGENT
from x10.errors import X10Error
from x10.utils.log import get_logger
from x10.utils.model import X10BaseModel

LOGGER = get_logger(__name__)
CLIENT_TIMEOUT = ClientTimeout(total=DEFAULT_REQUEST_TIMEOUT_SECONDS)

ApiResponseType = TypeVar("ApiResponseType", bound=Union[int, X10BaseModel, Sequence[X10BaseModel]])


class RateLimitException(X10Error):
    pass


class NotAuthorizedException(X10Error):
    pass


class RequestHeader(Enum):
    ACCEPT = "Accept"
    API_KEY = "X-Api-Key"
    CONTENT_TYPE = "Content-Type"
    USER_AGENT = "User-Agent"


class ResponseStatus(Enum):
    OK = "OK"
    ERROR = "ERROR"


class ResponseError(X10BaseModel):
    code: int
    message: str


class Pagination(X10BaseModel):
    cursor: Optional[int] = None
    count: int


class WrappedApiResponse(X10BaseModel, Generic[ApiResponseType]):
    status: ResponseStatus
    data: Optional[ApiResponseType] = None
    error: Optional[ResponseError] = None
    pagination: Optional[Pagination] = None


class StreamDataType(Enum):
    # Technical status
    UNKNOWN = "UNKNOWN"

    BALANCE = "BALANCE"
    DELTA = "DELTA"
    DEPOSIT = "DEPOSIT"
    ORDER = "ORDER"
    POSITION = "POSITION"
    SNAPSHOT = "SNAPSHOT"
    TRADE = "TRADE"
    TRANSFER = "TRANSFER"
    WITHDRAWAL = "WITHDRAWAL"

    @classmethod
    def __get_pydantic_core_schema__(cls, _source_type: Any, _handler: GetCoreSchemaHandler) -> CoreSchema:
        return core_schema.no_info_plain_validator_function(lambda v: v if v in cls._value2member_map_ else cls.UNKNOWN)


class WrappedStreamResponse(X10BaseModel, Generic[ApiResponseType]):
    type: Optional[StreamDataType] = None
    data: Optional[ApiResponseType] = None
    error: Optional[str] = None
    ts: int
    seq: int


def parse_response_to_model(
    response_text: str, model_class: Type[ApiResponseType]
) -> WrappedApiResponse[ApiResponseType]:
    # Read this to get more context re the type ignore:
    # https://github.com/python/mypy/issues/13619
    return WrappedApiResponse[model_class].model_validate_json(response_text)  # type: ignore[valid-type]


def get_url(template: str, *, query: Optional[Dict[str, str | List[str]]] = None, **path_params):
    def replace_path_param(match: re.Match[str]):
        matched_value = match.group(1)
        is_param_optional = matched_value.endswith("?")
        param_key = matched_value[:-1] if is_param_optional else matched_value
        param_value = path_params.get(param_key, "") if is_param_optional else path_params[param_key]

        return str(param_value) if param_value is not None else ""

    def serialize_query_param(param_key: str, param_value: Union[str, List[str]]):
        if isinstance(param_value, list):
            return itertools.chain.from_iterable(
                [serialize_query_param(param_key, item) for item in param_value if item is not None]
            )
        elif isinstance(param_value, Enum):
            return [f"{param_key}={param_value.value}"]
        elif param_value is not None:
            return [f"{param_key}={param_value}"]
        else:
            return []

    template = re.sub(r"<(\??[^<>]+)>", replace_path_param, template)
    template = template.rstrip("/")

    if query:
        query_parts = []

        for key, value in query.items():
            query_parts.extend(serialize_query_param(key, value))

        template += "?" + "&".join(query_parts)

    return template


async def send_get_request(
    session: aiohttp.ClientSession,
    url: str,
    model_class: Type[ApiResponseType],
    *,
    api_key: Optional[str] = None,
    request_headers: Optional[Dict[str, str]] = None,
    response_code_to_exception: Optional[Dict[int, Type[Exception]]] = None,
) -> WrappedApiResponse[ApiResponseType]:
    headers = __get_headers(api_key=api_key, request_headers=request_headers)
    LOGGER.debug("Sending GET %s", url)
    async with session.get(url, headers=headers) as response:
        response_text = await response.text()
        handle_known_errors(url, response_code_to_exception, response, response_text)
        return parse_response_to_model(response_text, model_class)


async def send_post_request(
    session: aiohttp.ClientSession,
    url: str,
    model_class: Type[ApiResponseType],
    *,
    json: Any = None,
    api_key: Optional[str] = None,
    request_headers: Optional[Dict[str, str]] = None,
    response_code_to_exception: Optional[Dict[int, Type[Exception]]] = None,
) -> WrappedApiResponse[ApiResponseType]:
    headers = __get_headers(api_key=api_key, request_headers=request_headers)
    LOGGER.debug("Sending POST %s, headers=%s", url, headers)
    async with session.post(url, json=json, headers=headers) as response:
        response_text = await response.text()
        handle_known_errors(url, response_code_to_exception, response, response_text)
        response_model = parse_response_to_model(response_text, model_class)
        if (response_model.status != ResponseStatus.OK.value) or (response_model.error is not None):
            LOGGER.error("Error response from POST %s: %s", url, response_model.error)
            raise ValueError(f"Error response from POST {url}: {response_model.error}")
        return response_model


async def send_patch_request(
    session: aiohttp.ClientSession,
    url: str,
    model_class: Type[ApiResponseType],
    *,
    json: Any = None,
    api_key: Optional[str] = None,
    request_headers: Optional[Dict[str, str]] = None,
    response_code_to_exception: Optional[Dict[int, Type[Exception]]] = None,
) -> WrappedApiResponse[ApiResponseType]:
    headers = __get_headers(api_key=api_key, request_headers=request_headers)
    LOGGER.debug("Sending PATCH %s, headers=%s, data=%s", url, headers, json)
    async with session.patch(url, json=json, headers=headers) as response:
        response_text = await response.text()
        if response_text == "":
            LOGGER.error("Empty HTTP %s response from PATCH %s", response.status, url)
            response_text = '{"status": "OK"}'
        handle_known_errors(url, response_code_to_exception, response, response_text)
        return parse_response_to_model(response_text, model_class)


async def send_delete_request(
    session: aiohttp.ClientSession,
    url: str,
    model_class: Type[ApiResponseType],
    *,
    api_key: Optional[str] = None,
    request_headers: Optional[Dict[str, str]] = None,
    response_code_to_exception: Optional[Dict[int, Type[Exception]]] = None,
):
    headers = __get_headers(api_key=api_key, request_headers=request_headers)
    LOGGER.debug("Sending DELETE %s, headers=%s", url, headers)
    async with session.delete(url, headers=headers) as response:
        response_text = await response.text()
        handle_known_errors(url, response_code_to_exception, response, response_text)
        return parse_response_to_model(response_text, model_class)


def handle_known_errors(
    url, response_code_handler: Optional[Dict[int, Type[Exception]]], response: ClientResponse, response_text: str
):
    if response.status == 401:
        LOGGER.error("Unauthorized response from POST %s: %s", url, response_text)
        raise NotAuthorizedException(f"Unauthorized response from POST {url}: {response_text}")

    if response.status == 429:
        LOGGER.error("Rate limited response from POST %s: %s", url, response_text)
        raise RateLimitException(f"Rate limited response from POST {url}: {response}")

    if response_code_handler and response.status in response_code_handler:
        raise response_code_handler[response.status](response_text)

    if response.status > 299:
        LOGGER.error("Error response from POST %s: %s", url, response_text)
        raise ValueError(f"Error response from POST {url}: code {response.status} - {response_text}")


def __get_headers(*, api_key: Optional[str] = None, request_headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    headers = {
        RequestHeader.ACCEPT.value: "application/json",
        RequestHeader.CONTENT_TYPE.value: "application/json",
        RequestHeader.USER_AGENT.value: USER_AGENT,
    }

    if api_key:
        headers[RequestHeader.API_KEY.value] = api_key

    if request_headers:
        headers.update(request_headers)

    return headers



================================================
FILE: x10/utils/log.py
================================================
import logging


def get_logger(name: str):
    return logging.getLogger(name)



================================================
FILE: x10/utils/model.py
================================================
import inspect

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
from pydantic.fields import AliasChoices, FieldInfo
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated


class X10BaseModel(BaseModel):
    model_config = ConfigDict(frozen=True, extra="ignore", use_enum_values=True)

    # Read this to get more context why `alias_generator` can't be used:
    # https://github.com/pydantic/pydantic/discussions/7877
    # `AliasChoices` is used to support both "from json" (e.g. `Model.model_validate_json(...)` -- camel case required)
    # and "manual" (e.g. `Model(...)` -- snake case required) models creation.
    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)

        for key in inspect.get_annotations(cls):
            key_alias = to_camel(key)

            if key_alias == key:
                continue

            try:
                attr = getattr(cls, key)
            except AttributeError:
                field_info = Field(validation_alias=AliasChoices(key, key_alias), serialization_alias=key_alias)
                setattr(cls, key, field_info)
            else:
                if isinstance(attr, FieldInfo):
                    if attr.validation_alias is None:
                        attr.validation_alias = AliasChoices(key, key_alias)
                    if attr.serialization_alias is None:
                        attr.serialization_alias = key_alias
                else:
                    field_info = Field(
                        default=attr,
                        validation_alias=AliasChoices(key, key_alias),
                        serialization_alias=key_alias,
                    )
                    setattr(cls, key, field_info)

    def to_pretty_json(self):
        return self.model_dump_json(indent=4)

    def to_api_request_json(self, *, exclude_none: bool = False):
        return self.model_dump(mode="json", by_alias=True, exclude_none=exclude_none)


HexValue = Annotated[
    int,
    PlainSerializer(lambda x: hex(x), return_type=str, when_used="json"),
    BeforeValidator(lambda x: int(x, 16) if not isinstance(x, int) else x),
]


class EmptyModel(X10BaseModel):
    pass


class SettlementSignatureModel(X10BaseModel):
    r: HexValue
    s: HexValue



================================================
FILE: x10/utils/starkex.py
================================================
import math
import random
from datetime import datetime, timedelta
from typing import Callable

from x10.perpetual.amounts import ROUNDING_FEE_CONTEXT, StarkAmount, StarkOrderAmounts
from x10.utils.log import get_logger

LOGGER = get_logger(__name__)

OP_LIMIT_ORDER_WITH_FEES = 3
OP_TRANSFER = 4
OP_CONDITIONAL_TRANSFER = 5
OP_WITHDRAWAL_TO_ADDRESS = 7

HOURS_IN_DAY = 24
SETTLEMENT_BUFFER_HOURS = HOURS_IN_DAY * 7
SECONDS_IN_HOUR = 60 * 60


def import_pedersen_hash_func():
    try:
        from fast_stark_crypto import pedersen_hash as ph_fast

        def _pedersen_hash(first: int, second: int) -> int:
            return ph_fast(first, second)

    except ImportError as e:
        from vendor.starkware.crypto.signature import pedersen_hash as ph_slow

        LOGGER.warning("COULD NOT IMPORT RUST CRYPTO - USING SLOW PYTHON PEDERSEN IMPL: %s", e.msg)

        def _pedersen_hash(first: int, second: int) -> int:
            return ph_slow(first, second)

    return _pedersen_hash


def import_sign_func():
    try:
        from fast_stark_crypto import sign as __sign_fast

        from vendor.starkware.crypto.signature import generate_k_rfc6979

        def _sign(private_key: int, msg_hash: int) -> tuple[int, int]:
            return __sign_fast(
                private_key=private_key,
                msg_hash=msg_hash,
                k=generate_k_rfc6979(msg_hash=msg_hash, priv_key=private_key),
            )

    except ImportError as e:
        from vendor.starkware.crypto.signature import sign as __sign_slow

        LOGGER.warning("COULD NOT IMPORT RUST CRYPTO - USING SLOW PYTHON SIGN IMPL: %s", e.msg)

        def _sign(private_key: int, msg_hash: int) -> tuple[int, int]:
            return __sign_slow(priv_key=private_key, msg_hash=msg_hash)

    return _sign


pedersen_hash = import_pedersen_hash_func()
sign = import_sign_func()


def get_conditional_transfer_msg(
    asset_id: int,
    asset_id_fee: int,
    receiver_public_key: int,
    condition: int,
    sender_position_id: int,
    receiver_position_id: int,
    src_fee_position_id: int,
    nonce: int,
    amount: int,
    max_amount_fee: int,
    expiration_timestamp: int,
    hash_function: Callable[[int, int], int] = pedersen_hash,
) -> int:
    assert 0 <= amount < 2**64
    assert 0 <= asset_id < 2**250
    assert 0 <= asset_id_fee < 2**250
    assert 0 <= condition < 2**251
    assert 0 <= expiration_timestamp < 2**32
    assert 0 <= src_fee_position_id < 2**64
    assert 0 <= max_amount_fee < 2**64
    assert 0 <= nonce < 2**32
    assert 0 <= receiver_position_id < 2**64
    assert 0 <= receiver_public_key < 2**251
    assert 0 <= sender_position_id < 2**64

    return get_conditional_transfer_msg_without_bounds(
        asset_id,
        asset_id_fee,
        receiver_public_key,
        condition,
        sender_position_id,
        receiver_position_id,
        src_fee_position_id,
        nonce,
        amount,
        max_amount_fee,
        expiration_timestamp,
        hash_function=hash_function,
    )


def get_conditional_transfer_msg_without_bounds(
    asset_id: int,
    asset_id_fee: int,
    receiver_public_key: int,
    condition: int,
    sender_position_id: int,
    receiver_position_id: int,
    src_fee_position_id: int,
    nonce: int,
    amount: int,
    max_amount_fee: int,
    expiration_timestamp: int,
    hash_function: Callable[[int, int], int] = pedersen_hash,
) -> int:
    msg = hash_function(asset_id, asset_id_fee)
    msg = hash_function(msg, receiver_public_key)
    msg = hash_function(msg, condition)

    packed_message0 = sender_position_id
    packed_message0 = packed_message0 * 2**64 + receiver_position_id
    packed_message0 = packed_message0 * 2**64 + src_fee_position_id
    packed_message0 = packed_message0 * 2**32 + nonce
    msg = hash_function(msg, packed_message0)
    packed_message1 = OP_CONDITIONAL_TRANSFER
    packed_message1 = packed_message1 * 2**64 + amount
    packed_message1 = packed_message1 * 2**64 + max_amount_fee
    packed_message1 = packed_message1 * 2**32 + expiration_timestamp
    packed_message1 = packed_message1 * 2**81  # Padding.
    return hash_function(msg, packed_message1)


def get_transfer_msg(
    asset_id: int,
    asset_id_fee: int,
    receiver_public_key: int,
    sender_position_id: int,
    receiver_position_id: int,
    src_fee_position_id: int,
    nonce: int,
    amount: int,
    max_amount_fee: int,
    expiration_timestamp: int,
    hash_function: Callable[[int, int], int] = pedersen_hash,
) -> int:
    assert 0 <= amount < 2**64
    assert 0 <= asset_id < 2**250
    assert 0 <= asset_id_fee < 2**250
    assert 0 <= expiration_timestamp < 2**32
    assert 0 <= max_amount_fee < 2**64
    assert 0 <= nonce < 2**32
    assert 0 <= receiver_position_id < 2**64
    assert 0 <= receiver_public_key < 2**251
    assert 0 <= sender_position_id < 2**64
    assert 0 <= src_fee_position_id < 2**64

    return get_transfer_msg_without_bounds(
        asset_id,
        asset_id_fee,
        receiver_public_key,
        sender_position_id,
        receiver_position_id,
        src_fee_position_id,
        nonce,
        amount,
        max_amount_fee,
        expiration_timestamp,
        hash_function=hash_function,
    )


def get_transfer_msg_without_bounds(
    asset_id: int,
    asset_id_fee: int,
    receiver_public_key: int,
    sender_position_id: int,
    receiver_position_id: int,
    src_fee_position_id: int,
    nonce: int,
    amount: int,
    max_amount_fee: int,
    expiration_timestamp: int,
    hash_function: Callable[[int, int], int] = pedersen_hash,
) -> int:
    msg = hash_function(asset_id, asset_id_fee)
    msg = hash_function(msg, receiver_public_key)

    packed_message0 = sender_position_id
    packed_message0 = packed_message0 * 2**64 + receiver_position_id
    packed_message0 = packed_message0 * 2**64 + src_fee_position_id
    packed_message0 = packed_message0 * 2**32 + nonce
    msg = hash_function(msg, packed_message0)
    packed_message1 = OP_TRANSFER
    packed_message1 = packed_message1 * 2**64 + amount
    packed_message1 = packed_message1 * 2**64 + max_amount_fee
    packed_message1 = packed_message1 * 2**32 + expiration_timestamp
    packed_message1 = packed_message1 * 2**81  # Padding.
    return hash_function(msg, packed_message1)


def get_withdrawal_to_address_msg(
    asset_id_collateral: int,
    position_id: int,
    eth_address: str,
    nonce: int,
    expiration_timestamp: int,
    amount: int,
    hash_function: Callable[[int, int], int] = pedersen_hash,
) -> int:
    assert 0 <= asset_id_collateral < 2**250
    assert 0 <= nonce < 2**32
    assert 0 <= position_id < 2**64
    assert 0 <= expiration_timestamp < 2**32
    assert 0 <= amount < 2**64
    assert 0 <= int(eth_address, 16) < 2**160

    return get_withdrawal_to_address_msg_without_bounds(
        asset_id_collateral,
        position_id,
        eth_address,
        nonce,
        expiration_timestamp,
        amount,
        hash_function=hash_function,
    )


def get_withdrawal_to_address_msg_without_bounds(
    asset_id_collateral: int,
    position_id: int,
    eth_address: str,
    nonce: int,
    expiration_timestamp: int,
    amount: int,
    hash_function: Callable[[int, int], int] = pedersen_hash,
) -> int:
    eth_address_int = int(eth_address, 16)

    packed_message = OP_WITHDRAWAL_TO_ADDRESS
    packed_message = packed_message * 2**64 + position_id
    packed_message = packed_message * 2**32 + nonce
    packed_message = packed_message * 2**64 + amount
    packed_message = packed_message * 2**32 + expiration_timestamp
    packed_message = packed_message * 2**49  # Padding.
    return hash_function(hash_function(asset_id_collateral, eth_address_int), packed_message)


def get_limit_order_msg(
    asset_id_synthetic: int,
    asset_id_collateral: int,
    is_buying_synthetic: int,
    asset_id_fee: int,
    amount_synthetic: int,
    amount_collateral: int,
    max_amount_fee: int,
    nonce: int,
    position_id: int,
    expiration_timestamp: int,
    hash_function: Callable[[int, int], int] = pedersen_hash,
) -> int:
    # Synthetic asset IDs are generated by the exchange based on other crypto currency counterparts.
    assert 0 <= asset_id_synthetic < 2**128
    # Collateral asset ID is linked to a smart contract as part of its hash_function. Its range is
    # larger than synthetic asset IDs in order to reduce the chance of a collision of IDs.
    assert 0 <= asset_id_collateral < 2**250
    assert 0 <= asset_id_fee < 2**250
    assert 0 <= amount_synthetic < 2**64
    assert 0 <= amount_collateral < 2**64
    assert 0 <= max_amount_fee < 2**64
    assert 0 <= nonce < 2**32
    assert 0 <= position_id < 2**64
    assert 0 <= expiration_timestamp < 2**32

    return get_limit_order_msg_without_bounds(
        asset_id_synthetic,
        asset_id_collateral,
        is_buying_synthetic,
        asset_id_fee,
        amount_synthetic,
        amount_collateral,
        max_amount_fee,
        nonce,
        position_id,
        expiration_timestamp,
        hash_function=hash_function,
    )


def get_limit_order_msg_without_bounds(
    asset_id_synthetic: int,
    asset_id_collateral: int,
    is_buying_synthetic: int,
    asset_id_fee: int,
    amount_synthetic: int,
    amount_collateral: int,
    max_amount_fee: int,
    nonce: int,
    position_id: int,
    expiration_timestamp: int,
    hash_function: Callable[[int, int], int] = pedersen_hash,
) -> int:
    if is_buying_synthetic:
        asset_id_sell, asset_id_buy = asset_id_collateral, asset_id_synthetic
        amount_sell, amount_buy = amount_collateral, amount_synthetic
    else:
        asset_id_sell, asset_id_buy = asset_id_synthetic, asset_id_collateral
        amount_sell, amount_buy = amount_synthetic, amount_collateral

    msg = hash_function(asset_id_sell, asset_id_buy)
    msg = hash_function(msg, asset_id_fee)
    packed_message0 = amount_sell
    packed_message0 = packed_message0 * 2**64 + amount_buy
    packed_message0 = packed_message0 * 2**64 + max_amount_fee
    packed_message0 = packed_message0 * 2**32 + nonce
    msg = hash_function(msg, packed_message0)
    packed_message1 = OP_LIMIT_ORDER_WITH_FEES
    packed_message1 = packed_message1 * 2**64 + position_id
    packed_message1 = packed_message1 * 2**64 + position_id
    packed_message1 = packed_message1 * 2**64 + position_id
    packed_message1 = packed_message1 * 2**32 + expiration_timestamp
    packed_message1 = packed_message1 * 2**17  # Padding.
    return hash_function(msg, packed_message1)


#####################################################################################
# get_price_msg: gets as input:                                                     #
#   oracle: a 40-bit number, describes the oracle (e.g., hex encoding of "Maker")   #
#   price: a 120-bit number                                                         #
#   asset: a 211-bit number                                                         #
#   timestamp: a 32 bit number, represents seconds since Unix epoch                 #
# Outputs a number which is less than FIELD_PRIME, which can be used as data        #
# to sign on in the sign method. This number is obtained by applying pedersen hash  #
# on the following two numbers:                                                     #
#                                                                                   #
# first number:                                                                     #
# --------------------------------------------------------------------------------- #
# | asset_name (rest of the number)  - 211 bits       |   oracle_name (40 bits)   | #
# --------------------------------------------------------------------------------- #
#                                                                                   #
# second number:                                                                    #
# --------------------------------------------------------------------------------- #
# | 0 (92 bits)         | price (120 bits)              |   timestamp (32 bits)   | #
# --------------------------------------------------------------------------------- #
#####################################################################################


def get_price_msg(
    oracle_name: int,
    asset_pair: int,
    timestamp: int,
    price: int,
    hash_function=pedersen_hash,
):
    assert 0 <= oracle_name < 2**40
    assert 0 <= asset_pair < 2**128
    assert 0 <= timestamp < 2**32
    assert 0 <= price < 2**120

    # The first number to hash_function is the oracle name (e.g., Maker) in the 40 LSB, then the
    # asset name.
    first_number = (asset_pair << 40) + oracle_name

    # The second number is timestamp in the 32 LSB, then the price.
    second_number = (price << 32) + timestamp

    return hash_function(first_number, second_number)


def hash_order(
    amounts: StarkOrderAmounts,
    is_buying_synthetic: bool,
    nonce: int,
    position_id: int,
    expiration_timestamp: datetime,
) -> int:
    amount_synthetic: StarkAmount = amounts.synthetic_amount_internal.to_stark_amount(
        rounding_context=amounts.rounding_context
    )
    amount_collateral: StarkAmount = amounts.collateral_amount_internal.to_stark_amount(
        rounding_context=amounts.rounding_context
    )
    max_fee: StarkAmount = amounts.fee_amount_internal.to_stark_amount(rounding_context=ROUNDING_FEE_CONTEXT)
    synthetic_asset = amount_synthetic.asset
    collateral_asset = amount_collateral.asset

    expire_time_with_buffer = expiration_timestamp + timedelta(days=14)
    expire_time_with_buffer_as_hours = math.ceil(expire_time_with_buffer.timestamp() / SECONDS_IN_HOUR)

    return get_limit_order_msg(
        int(synthetic_asset.settlement_external_id, base=16),
        int(collateral_asset.settlement_external_id, base=16),
        1 if is_buying_synthetic else 0,
        int(collateral_asset.settlement_external_id, base=16),
        amount_synthetic.value,
        amount_collateral.value,
        max_fee.value,
        nonce,
        position_id,
        expire_time_with_buffer_as_hours,
        pedersen_hash,
    )


def generate_nonce():
    # Aligned with the JS implementation (2^31 as the upper bound, not 2^32).
    # https://github.com/starkware-libs/starkware-crypto-utils/blob/dev/src/js/signature.ts#L327
    return random.randint(0, 2**31 - 1)



================================================
FILE: x10/utils/string.py
================================================
import string


def is_hex_string(s: str, check_prefix: bool = True):
    if check_prefix and not s.startswith("0x"):
        return False

    string_to_check = s if not check_prefix else s[2:]

    return s.isalnum() and all(c in string.hexdigits for c in string_to_check)



================================================
FILE: .devcontainer/devcontainer.json
================================================
// For format details, see https://aka.ms/devcontainer.json. For config options, see the
// README at: https://github.com/devcontainers/templates/tree/main/src/python
{
	"name": "Python 3",
	// Or use a Dockerfile or Docker Compose file. More info: https://containers.dev/guide/dockerfile
	"image": "mcr.microsoft.com/devcontainers/python:1-3.12-bookworm",
	"customizations": {
		"vscode": {
			"extensions": [
				"github.vscode-github-actions"
			]
		}
	}

	// Features to add to the dev container. More info: https://containers.dev/features.
	// "features": {},

	// Use 'forwardPorts' to make a list of ports inside the container available locally.
	// "forwardPorts": [],

	// Use 'postCreateCommand' to run commands after the container is created.
	// "postCreateCommand": "pip3 install --user -r requirements.txt",

	// Configure tool-specific properties.
	// "customizations": {},

	// Uncomment to connect as root instead. More info: https://aka.ms/dev-containers-non-root.
	// "remoteUser": "root"
}



================================================
FILE: .github/CODEOWNERS
================================================
# Default owners
* @dmitrykrasovskih @alexex10 @ex10ded



================================================
FILE: .github/pull_request_template.md
================================================
## Changes
- [Describe your changes here]
- ...



================================================
FILE: .github/workflows/build-release.yml
================================================
name: Build and Publish Package

on:
  workflow_dispatch:
  release:
    types:
      - published
      
jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install Poetry
        run: |
          pip install --upgrade pip==25.0
          pip install poetry==1.8.3

      - name: Build and Publish
        run: |
          poetry config pypi-token.pypi ${{ secrets.PYPI_TOKEN }}
          poetry build
          poetry publish



================================================
FILE: .github/workflows/code-checks.yml
================================================
name: Code checks

on:
  workflow_dispatch:
  pull_request:
    branches: [ main ]
    types: [ opened, reopened, synchronize, ready_for_review ]

jobs:
  code-checks:
    if: github.event.pull_request.draft == false
    timeout-minutes: 10
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.10-dev'

      - name: Setup poetry
        run: |
          pip install --upgrade pip==25.0
          pip install poetry==1.8.3
          poetry config virtualenvs.create false

      - name: Update apt cache
        run: sudo apt-get update

      - name: Install system packages
        run: sudo apt-get install -y build-essential libgmp-dev

      - name: Install deps
        run: poetry install --no-root

      - name: Run linter
        run: make lint

      - name: Run unit-tests
        run: make test


