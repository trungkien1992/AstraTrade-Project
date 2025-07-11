NAV

json

Extended API Documentation

Introduction

Python SDK

Mainnet

Testnet

Allowed HTTP Verbs

Authentication

Rate Limits

Pagination

Public REST-API

Get markets

Get market statistics

Get market order book

Get market last trades

Get candles history

Get funding rates history

Get open interest history

Private REST-API

Account

Get balance

Get deposits, withdrawals, transfers history

Get positions

Get positions history

Get open orders

Get orders history

Get order by id

Get orders by externalId

Get trades

Get funding payments

Get current leverage

Update leverage

Get fees

Order management

Create or edit order

Cancel order

Mass Cancel

Mass Auto-Cancel (Dead Man's Switch)

Deposits

Create transfer

Withdrawals

Create slow withdrawal

Referrals

Get affiliate data

Get referral status

Get referral links

Get referral dashboard

Use referral link

Create referral link code

Update referral link code

Rewards

Public WebSocket streams

Order book stream

Trades stream

Funding rates stream

Candles stream

Mark price stream

Index price stream

Private WebSocket streams

Account updates stream

Error responses

Extended API Documentation By using the Extended API, you agree to the Extended Terms & Privacy Policy. If you do not agree to the foregoing terms, do not use the Extended API. Introduction

This documentation is a work in progress and will be updated regularly based on user feedback and the addition of new functionality.

Welcome to the Extended API Documentation! This guide is designed to assist traders and developers in integrating with our hybrid perpetuals exchange.

Extended operates as a hybrid Central Limit Order Book (CLOB) exchange. While order processing, matching, position risk assessment, and transaction sequencing are handled off-chain, trade settlement occurs on-chain through the StarkEx Layer 2 engine.

StarkEx, built by Starkware, is a battle-tested scalability solution that brings lightning-fast transaction processing to the forefront, guaranteeing an unparalleled trading experience. This is achieved while preserving complete trustlessness and transparency through three key mechanisms embedded into StarkEx:

On-chain validations of the trading logic ensure that fraudulent or incorrect transactions, including liquidations, contrary to the on-chain trading logic are never permitted. The mark prices, which determine the liquidability of positions, are obtained from multiple independent oracle providers to prevent potential price manipulation and ensure fair and accurate asset valuation within our ecosystem. Extended utilizes 5 Stork nodes to define the median mark price. Publication of zero-knowledge (ZK) proofs on the Ethereum Layer 1 blockchain validates Layer 2 transactions, ensuring both their integrity and security.

For deeper insights on Extended Exchange, please refer to the blogs Extended Vision and Architecture.

To optimize high-frequency trading performance, the Extended API operates asynchronously. This means that when you place an order, it immediately returns an order ID, even before the order is officially recorded in the book. To track your order status in real time, it's essential to subscribe to the Order WebSocket stream. This stream delivers instant updates about any changes to your orders, including confirmations, cancellations, and rejections, enabling you to manage your trading strategies effectively. Python SDK

SDK configuration

from dataclasses import dataclass

@dataclass class EndpointConfig: chain_rpc_url: str api_base_url: str stream_url: str onboarding_url: str signing_domain: str collateral_asset_contract: str asset_operations_contract: str collateral_asset_on_chain_id: str collateral_decimals: int

TESTNET_CONFIG = EndpointConfig( chain_rpc_url="https://rpc.sepolia.org", api_base_url="https://api.testnet.extended.exchange/api/v1", stream_url="wss://api.testnet.extended.exchange/stream.extended.exchange/v1", onboarding_url="https://api.testnet.extended.exchange", signing_domain="testnet.x10.exchange", collateral_asset_contract="0x0c9165046063b7bcd05c6924bbe05ed535c140a1", asset_operations_contract="0x7f0C670079147C5c5C45eef548E55D2cAc53B391", collateral_asset_on_chain_id="0x31857064564ed0ff978e687456963cba09c2c6985d8f9300a1de4962fafa054", collateral_decimals=6, )

TESTNET_CONFIG_LEGACY_SIGNING_DOMAIN = EndpointConfig( chain_rpc_url="https://rpc.sepolia.org", api_base_url="https://api.testnet.extended.exchange/api/v1", stream_url="wss://api.testnet.extended.exchange/stream.extended.exchange/v1", onboarding_url="https://api.testnet.extended.exchange", signing_domain="x10.exchange", collateral_asset_contract="0x0c9165046063b7bcd05c6924bbe05ed535c140a1", asset_operations_contract="0x7f0C670079147C5c5C45eef548E55D2cAc53B391", collateral_asset_on_chain_id="0x31857064564ed0ff978e687456963cba09c2c6985d8f9300a1de4962fafa054", collateral_decimals=6, )

MAINNET_CONFIG = EndpointConfig( chain_rpc_url="https://cloudflare-eth.com", api_base_url="https://api.extended.exchange/api/v1", stream_url="wss://api.extended.exchange/stream.extended.exchange/v1", onboarding_url="https://api.extended.exchange", signing_domain="extended.exchange", collateral_asset_contract="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", asset_operations_contract="0x1cE5D7f52A8aBd23551e91248151CA5A13353C65", collateral_asset_on_chain_id="0x2893294412a4c8f915f75892b395ebbf6859ec246ec365c3b1f56f47c3a0a5d", collateral_decimals=6, )

The SDK and the SDK documentation will be updated regularly to include additional functionality and more examples. The SDK documentation refers to X10, the previous name for Extended.

To enhance your algorithmic trading experience, Extended (former X10) has released the 0.3.0-alpha version of our Python SDK.

Getting Started:

For installation instructions, please refer to the description provided. For reference implementations, explore the examples folder. For SDK configuration, please refer to the config description.

Supported Features:

Account creation and authorisation. Order Management. Account Management. Deposits, Transfers and Withdrawals. Market Information.

We are committed to enhancing the SDK with more functionalities based on user feedback and evolving market needs. Mainnet Our Mainnet is running on Ethereum.

Base URL for the Mainnet API endpoints: https://api.extended.exchange/. Testnet Our Testnet is running on Sepolia.

Base URL for the Testnet API endpoints: https://api.testnet.extended.exchange/.

On the testnet, users can claim $100,000 worth of test USDC per day for each L1 wallet. This can be done by clicking the 'Claim' button in the 'Account' section, located at the bottom right of the Extended Testnet Trade screen. Allowed HTTP Verbs GET: Retrieves a resource or list of resources.

POST: Creates a resource.

PATCH: Updates a resource.

DELETE: Deletes a resource. Authentication Due to the trustless and self-custody nature of the Extended exchange, transactions involving user funds require not only an API Key but also a valid Stark signature.

For order management, both an API Key and Stark signatures are necessary. For other endpoints, only the API Key signature is required. Stark signatures are generated using a private Stark key. Account Creation, API and Stark Key Management Currently, accounts can be created through the SDK or through the User Interface.

To create an account through the SDK, please refer to the onboarding example.

To create an account through the User Interface, connect your wallet on extended.exchange, and your first Extended account will be created.

You can create up to ten Extended sub-accounts per one L1 wallet address. You can add and manage all sub-accounts associated with your connected L1 wallet in the 'Account' section, located at the bottom right of the Extended Trade screen.

On the API management page, you can obtain API keys, Stark keys, and Vault numbers for each of your sub-accounts. Note that each sub-account is a separate StarkEx vault and therefore has unique API and Stark keys. Authenticate Using API Key Extended employs a simplified authentication scheme for API access. Authenticate by using your API key, which should be included in an HTTP header as follows: X-Api-Key: <API_KEY_FROM_API_MANAGEMENT_PAGE_OF_UI>. Mandatory headers Both for REST and WebSocket API requests, the User-Agent header is mandatory. Rate Limits REST API endpoints are subject to rate limits. For real-time data, consider using the WebSockets API instead.

All REST API endpoints are throttled by IP address. Currently, the rate limit is set at 1,000 requests per minute, shared across all endpoints. We plan to increase these limits as our system expands. If you require an increase in the rate limit now, please reach out to our team on Discord.

Higher rate limit of 60,000 requests per 5 minutes apply for the market makers.

When a REST API rate limit is exceeded, a 429 status code will be returned. Pagination

Paginated response schema:

type PaginatedResponse = { "status": "ok" | "error" "data": object | object[] | string | number, "error": { "code": number, "message": string }, "pagination": { "cursor": number // Current cursor "count": number // Count of the items in the response } }

General not paginated response schema:

type GeneralResponse = { "status": "ok" | "error", "data": object | object[] | string | number, "error": { "code": number, "message": string } }

The Extended API uses a cursor-based pagination model across all endpoints that may return large volumes of items.

Items are automatically sorted in descending order by ID unless otherwise specified in the endpoint description. As IDs increase over time, the most recent items are always returned first.

Pagination parameters are passed via the query string. These parameters include:

Parameter Required Type Description

cursor no number Determines the offset of the returned result. It represents the ID of the item after which you want to retrieve the next result. To get the next result page, use the cursor from the pagination section of the previous response.

limit no number The maximum number of items that should be returned.

Public REST-API The following Public REST API endpoints enable users to access comprehensive information about available markets, their configurations, and trading statistics. Get markets HTTP Request GET /api/v1/info/markets?market={market}

Get a list of available markets, their configurations, and trading statistics.

To request data for several markets, use the following format: GET /api/v1/info/markets?market=market1&market2.

Please note that the margin schedule by market is not covered by this endpoint. For more details on the margin schedule, please refer to the documentation. Market statuses

Status Description

ACTIVE Market is active, and all types of orders are permitted.

REDUCE_ONLY Market is in reduce only mode, and only reduce only orders are allowed.

DELISTED Market is delisted, and trading is no longer permitted.

PRELISTED Market is in prelisting stage, and trading not yet available.

DISABLED Market is completly disabled, and trading is not allowed.

Query Parameters

Parameter Required Type Description

market no string[] List of names of the requested markets.

Response example:

{ "status": "ok", "data": [ { "name": "BTC-USD", "assetName": "BTC", "assetPrecision": 6, "collateralAssetName": "USD", "collateralAssetPrecision": 6, "active": true, "status": "ACTIVE", "marketStats": { "dailyVolume": "39659164065", "dailyVolumeBase": "39659164065", "dailyPriceChangePercentage": "5.57", "dailyLow": "39512", "dailyHigh": "42122", "lastPrice": "42000", "askPrice": "42005", "bidPrice": "39998", "markPrice": "39950", "indexPrice": "39940", "fundingRate": "0.001", "nextFundingRate": 1701563440, "openInterest": "1245.2", "openInterestBase": "1245.2" }, "tradingConfig": { "minOrderSize": "0.001", "minOrderSizeChange": "0.001", "minPriceChange": "0.001", "maxMarketOrderValue": "1000000", "maxLimitOrderValue": "5000000", "maxPositionValue": "10000000", "maxLeverage": "50", "maxNumOrders": "200", "limitPriceCap": "0.05", "limitPriceFloor": "0.05" }, "l2Config": { "type": "STARKX", "collateralId": "0x35596841893e0d17079c27b2d72db1694f26a1932a7429144b439ba0807d29c", "collateralResolution": 1000000, "syntheticId": "0x4254432d3130000000000000000000", "syntheticResolution": 10000000000 } } ] }

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

data[].name yes string Name of the market.

data[].assetName yes string Name of the base asset.

data[].assetPrecision yes number Number of decimals for the base asset.

data[].collateralAssetName yes string Name of the collateral asset.

data[].collateralAssetPrecision yes number Number of decimals for the collateral asset.

data[].active yes boolean Indicates if the market is currently active. Can be true or false.

data[].status yes string Market status.

data[].marketStats.dailyVolume yes string Trading volume of the market in the previous 24 hours in the collateral asset.

data[].marketStats.dailyVolumeBase yes string Trading volume of the market in the previous 24 hours in the base asset.

data[].marketStats.dailyPriceChange yes string Absolute price change of the last trade price over the past 24 hours.

data[].marketStats.dailyPriceChangePercentage yes string Percent price change of the last trade price over the past 24 hours.

data[].marketStats.dailyLow yes string Lowest trade price over the past 24 hours.

data[].marketStats.dailyHigh yes string Highest trade price over the past 24 hours.

data[].marketStats.lastPrice yes string Last price of the market.

data[].marketStats.askPrice yes string Current best ask price of the market.

data[].marketStats.bidPrice yes string Current best bid price of the market.

data[].marketStats.markPrice yes string Current mark price of the market.

data[].marketStats.indexPrice yes string Current index price of the market.

data[].marketStats.fundingRate yes string Current funding rate, calculated every minute.

data[].marketStats.nextFundingRate yes number Timestamp of the next funding update.

data[].marketStats.openInterest yes string Open interest in collateral asset.

data[].marketStats.openInterestBase yes string Open interest in base asset.

data[].tradingConfig.minOrderSize yes string Minimum order size for the market.

data[].tradingConfig.minOrderSizeChange yes string Minimum order size change for the market.

data[].tradingConfig.minPriceChange yes string Minimum price change for the market.

data[].tradingConfig.maxMarketOrderValue yes string Maximum market order value for the market.

data[].tradingConfig.maxLimitOrderValue yes string Maximum limit order value for the market.

data[].tradingConfig.maxPositionValue yes string Maximum position value for the market.

data[].tradingConfig.maxLeverage yes string Maximum leverage available for the market.

data[].tradingConfig.maxNumOrders yes string Maximum number of open orders for the market.

data[].tradingConfig.limitPriceCap yes string Limit order price cap.

data[].tradingConfig.limitPriceFloor yes string Limit order floor ratio.

data[].l2Config.type yes string Type of Layer 2 solution. Currently, only 'STARKX' is supported.

data[].l2Config.collateralId yes string StarkEx collateral asset ID.

data[].l2Config.collateralResolution yes number Collateral asset resolution, the number of quantums (StarkEx units) that fit within one "human-readable" unit of the collateral asset.

data[].l2Config.syntheticId yes string StarkEx synthetic asset ID.

data[].l2Config.syntheticResolution yes number Synthetic asset resolution, the number of quantums (StarkEx units) that fit within one "human-readable" unit of the synthetic asset.

Get market statistics HTTP Request GET /api/v1/info/markets/{market}/stats

Get the latest trading statistics for an individual market.

Please note that the returned funding rate represents the most recent funding rate, which is calculated every minute. URL Parameters

Parameter Required Type Description

market yes string Name of the requested market.

Successful response example:

{ "status": "OK", "data": { "dailyVolume": "10283410.122959", "dailyVolumeBase": "3343.1217", "dailyPriceChange": "-26.00", "dailyPriceChangePercentage": "-0.0084", "dailyLow": "3057.98", "dailyHigh": "3133.53", "lastPrice": "3085.70", "askPrice": "3089.05", "bidPrice": "3087.50", "markPrice": "3088.439710293828", "indexPrice": "3089.556987078441", "fundingRate": "-0.000059", "nextFundingRate": 1716192000000, "openInterest": "35827242.257619", "openInterestBase": "11600.4344", "deleverageLevels": { "shortPositions": [ { "level": 1, "rankingLowerBound": "-1354535.1454" }, { "level": 2, "rankingLowerBound": "-6.3450" }, { "level": 3, "rankingLowerBound": "-0.3419" }, { "level": 4, "rankingLowerBound": "0.0000" } ], "longPositions": [ { "level": 1, "rankingLowerBound": "-2978.4427" }, { "level": 2, "rankingLowerBound": "0.0000" }, { "level": 3, "rankingLowerBound": "0.0000" }, { "level": 4, "rankingLowerBound": "0.0001" } ] } } }

Error response example:

{ "status": "ERROR", "error": { "code": "NOT_FOUND", "message": "Market not found" } }

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

data.dailyVolume yes string Trading volume of the market in the previous 24 hours in the collateral asset.

data.dailyVolumeBase yes string Trading volume of the market in the previous 24 hours in the base asset.

data.dailyPriceChange yes string Absolute price change of the last trade price over the past 24 hours.

data.dailyPriceChangePercentage yes string Percent price change of the last trade price over the past 24 hours.

data.dailyLow yes string Lowest trade price over the past 24 hours.

data.dailyHigh yes string Highest trade price over the past 24 hours.

data.lastPrice yes string Last price of the market.

data.askPrice yes string Current best ask price of the market.

data.bidPrice yes string Current best bid price of the market.

data.markPrice yes string Current mark price of the market.

data.indexPrice yes string Current index price of the market.

data.fundingRate yes string Current funding rate, calculated every minute.

data.nextFundingRate yes number Timestamp of the next funding update.

data.openInterest yes string Open interest in collateral asset.

data.openInterestBase yes string Open interest in base asset.

data.deleverageLevels yes enum Auto Deleveraging (ADL) levels for long and short positions, ranging from level 1 (lowest risk) to level 4 (highest risk) of ADL. For details, please refer to the documentation.

Get market order book HTTP Request GET /api/v1/info/markets/{market}/orderbook

Get the latest orderbook for an individual market. URL Parameters

Parameter Required Type Description

market yes string Name of the requested market.

Successful response example:

{ "status": "OK", "data": { "market": "BTC-USD", "bid": [ { "qty": "0.04852", "price": "61827.7" }, { "qty": "0.50274", "price": "61820.5" } ], "ask": [ { "qty": "0.04852", "price": "61840.3" }, { "qty": "0.4998", "price": "61864.1" } ] } }

Error response example:

{ "status": "ERROR", "error": { "code": "NOT_FOUND", "message": "Market not found" } }

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

data.market yes string Market name.

data.bid yes object[] List of bid orders.

data.bid[].qty yes string Qty for the price level.

data.bid[].price yes string Bid price.

data.ask yes object[] List of ask orders.

data.ask[].qty yes string Qty for the price level.

data.ask[].price yes string Ask price.

Get market last trades HTTP Request GET /api/v1/info/markets/{market}/trades

Get the latest trade for an individual market. URL Parameters

Parameter Required Type Description

market yes string Name of the requested market.

Successful response example:

{ "status": "OK", "data": [ { "i": 1844000421446684673, "m": "BTC-USD", "S": "SELL", "tT": "TRADE", "T": 1728478935001, "p": "61998.5", "q": "0.04839" }, { "i": 1844000955650019328, "m": "BTC-USD", "S": "SELL", "tT": "TRADE", "T": 1728479062365, "p": "61951.4", "q": "0.00029" } ] }

Error response example:

{ "status": "ERROR", "error": { "code": "NOT_FOUND", "message": "Market not found" } }

Response

Parameter Type Description

data[].i number Trade ID.

data[].m string Market name.

data[].S string Side of taker trades. Can be BUY or SELL.

data[].tT string Trade type. Can be TRADE, LIQUIDATION or DELEVERAGE.

data[].T number Timestamp (in epoch milliseconds) when the trade happened.

data[].p string Trade price.

data[].q string Trade quantity in base asset.

Get candles history HTTP Request GET /api/v1/info/candles/{market}/{candleType}

Get the candles history for an individual market for the timeframe specified in the request. Candles are sorted by timestamp in descending order.

Available price types include:

Trades (last) price: GET /api/v1/info/candles/{market}/trades. Mark price: GET /api/v1/info/candles/{market}/mark-prices. Index price: GET /api/v1/info/candles/{market}/index-prices.

The endpoint returns a maximum of 10,000 records. URL Parameters

Parameter Required Type Description

market yes string Name of the requested market.

candleType yes string Price type. Can be trades, mark-prices, or index-prices.

Query Parameters

Parameter Required Type Description

interval yes string The time interval between data points.

limit yes number The maximum number of items that should be returned.

endTime no number End timestamp (in epoch milliseconds) for the requested period.

Response example:

{ "status": "OK", "data": [ { "o": "65206.2", "l": "65206.2", "h": "65206.2", "c": "65206.2", "v": "0.0", "T": 1715797320000 } ] }

Response

Parameter Required Type Description

status yes string Can be OK or ERROR

data[].o yes string Open price.

data[].c yes string Close price.

data[].h yes string Highest price.

data[].l yes string Lowest price.

data[].v yes string Trading volume (Only for trades candles).

data[].T yes number Starting timestamp (in epoch milliseconds) for the candle.

Get funding rates history HTTP Request GET /api/v1/info/{market}/funding?startTime={startTime}&endTime={endTime}

Get the funding rates history for an individual market for the timeframe specified in the request. The funding rates are sorted by timestamp in descending order.

The endpoint returns a maximum of 10,000 records; pagination should be used to access records beyond this limit.

While the funding rate is calculated every minute, it is only applied once per hour. The records represent the 1-hour rates that were applied for the payment of funding fees.

For details on how the funding rate is calculated on Extended, please refer to the documentation. URL Parameters

Parameter Required Type Description

market yes string Names of the requested market.

Query Parameters

Parameter Required Type Description

startTime yes number Starting timestamp (in epoch milliseconds) for the requested period.

endTime yes number Ending timestamp (in epoch milliseconds) for the requested period.

cursor no number Determines the offset of the returned result. To get the next result page, you can use the cursor from the pagination section of the previous response.

limit no number Maximum number of items that should be returned.

Response example:

{ "status": "OK", "data": [ { "m": "BTC-USD", "T": 1701563440, "f": "0.001" } ], "pagination": { "cursor": 1784963886257016832, "count": 1 } }

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

data[].m yes string Name of the requested market.

data[].T yes number Timestamp (in epoch milliseconds) when the funding rate was calculated and applied.

data[].f yes string Funding rates used for funding fee payments.

Get open interest history HTTP Request GET /api/v1/info/{market}/open-interests?interval={interval}&startTime={startTime}&endTime={endTime}

Get the open interest history for an individual market for the timeframe specified in the request. The open interests are sorted by timestamp in descending order.

The endpoint returns a maximum of 300 records; proper combination of start and end time should be used to access records beyond this limit. URL Parameters

Parameter Required Type Description

market yes string Names of the requested market.

Query Parameters

Parameter Required Type Description

startTime yes number Starting timestamp (in epoch milliseconds) for the requested period.

endTime yes number Ending timestamp (in epoch milliseconds) for the requested period.

interval yes enum P1H for hour and P1D for day

limit no number Maximum number of items that should be returned.

Response example:

{ "status": "OK", "data": [ { "i": "151193.8952300000000000", "I": "430530.0000000000000000", "t": 1749513600000 }, { "i": "392590.9522500000000000", "I": "1147356.0000000000000000", "t": 1749600000000 }, { "i": "397721.7285100000000000", "I": "1224362.0000000000000000", "t": 1749686400000 } ] }

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

data[].i yes string Open interest in USD.

data[].I yes string Open interest in synthetic asset.

data[].t yes number Timestamp (in epoch milliseconds) when the funding rate was calculated and applied.

Private REST-API Account You can create up to ten Extended sub-accounts for each L1 wallet address. For more details, please refer to the Authentication section of the API Documentation.

The Private API endpoints listed below grant access to details specific to each sub-account, such as balances, transactions, positions, orders, trades, and the fee rates applied. Additionally, there are endpoints for retrieving the current leverage and adjusting it.

Please note that all endpoints in this section will only return records for the authenticated sub-account. Get balance HTTP Request GET /api/v1/user/balance

Get key balance details for the authenticated sub-account:

Account Balance = Deposits - Withdrawals + Realised PnL. Equity = Account Balance + Unrealised PnL. Available Balance for Trading = Equity - Initial Margin Requirement. Available Balance for Withdrawals = max(0, Wallet Balance + min(0,Unrealised PnL) - Initial Margin Requirement). Unrealised PnL = The sum of unrealised PnL across open positions, calculated as Position Size * (Mark Price - Entry Price). Initial Margin Requirement for a given market = Max(Abs(Position Value + Value of Buy Orders), Abs(Position Value + Value of Sell Orders))*1/Leverage. Account Margin Ratio = Maintenance Margin requirement of all open positions / Equity. Liquidation is triggered when Account Margin Ratio > 100%. Account Exposure = Sum(All positions value) Account Leverage = Exposure / Equity.

Response example:

{ "status": "OK", "data": { "collateralName": "USDC", "balance": "13500", "equity": "12000", "availableForTrade": "1200", "availableForWithdrawal": "100", "unrealisedPnl": "-10.1", "initialMargin": "160", "marginRatio": "1.5", "exposure": "12751.859629", "leverage": "1275.1860", "updatedTime": 1701563440 } }

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

data.collateralName yes string Name of the collateral asset used for the account.

data.balance yes string Account balance expressed in the collateral asset, also known as Wallet balance.

data.equity yes string Equity of the account.

data.availableForTrade yes string Available Balance for Trading.

data.availableForWithdrawal yes string Available Balance for Withdrawals.

data.unrealisedPnl yes string Current unrealised PnL of the account.

data.initialMargin yes string Collateral used to open the positions and orders.

data.marginRatio yes string Margin ratio of the account.

data.exposure yes string Exposure of the account.

data.leverage yes string Leverage of the account.

data.updatedTime yes number Timestamp (in epoch milliseconds) when the server generated the balance message.

Get deposits, withdrawals, transfers history HTTP Request GET /api/v1/user/assetOperations?&type={type}&status={status}

Get the history of deposits, withdrawals, and transfers between sub-accounts for the authenticated sub-account. Optionally, the request can be filtered by a specific transaction type or status.

The endpoint returns 50 records per page; pagination should be used to access records beyond this limit. Transactions are sorted by timestamp in descending order. Transactions types

Status Description

DEPOSIT Deposit.

CLAIM Testing funds claim. Available only on Extended Testnet.

TRANSFER Transfer between sub-accounts within one L1 wallet.

SLOW_WITHDRAWAL Slow withdrawal.

FAST_WITHDRAWAL Fast withdrawal.

Transactions statuses

Status Description

CREATED Transaction created on Extended.

IN_PROGRESS Transaction is being processed by Extended or StarkEx.

READY_FOR_CLAIM Slow withdrawal or rejected deposit ready for claim.

COMPLETED Transaction completed.

REJECTED Transaction rejected.

Response example:

{ "status": "OK", "data": [ { "id": "1236", "type": "TRANSFER", "status": "COMPLETED", "amount": "-5.0000000000000000", "fee": "0", "asset": 1, "time": 1722627477268, "accountId": 3001, "counterpartyAccountId": 3025 }, { "id": "0x3e8adae72bd576efa0410f3b18f3fe77b638d6fdd8fb49c0b38309ccc01839ac:0x029398cecc60f4e68c3ebeb28fa98df003ac4e0328b086aad5496a4d56815ccc:0xe7", "type": "DEPOSIT", "status": "COMPLETED", "amount": "10.0000000000000000", "fee": "0", "asset": 1, "time": 1722607553870, "accountId": 3001, "transactionHash": "0x3e8adae72bd576efa0410f3b18f3fe77b638d6fdd8fb49c0b38309ccc01839ac" }, { "id": "1235", "type": "SLOW_WITHDRAWAL", "status": "COMPLETED", "amount": "-5.0000000000000000", "fee": "0", "asset": 1, "time": 1722607138130, "accountId": 3001, "transactionHash": "0xfd8d1bc06ee36b1a4b0bd98377818ac9a22b2346920aa2eb20015d4356a66319" }, { "id": "1234", "type": "FAST_WITHDRAWAL", "status": "COMPLETED", "amount": "-5.0000000000000000", "fee": "4.2057230000000000", "asset": 1, "time": 1722607127646, "accountId": 3011, "transactionHash": "0x3babb6d6b0eecc62e47f71ff7873381312f25c91d576072f1d0b332a25d035b5" } ], "pagination": { "cursor": 23, "count": 23 } }

Query Parameters

Parameter Required Type Description

type no string Transaction type. Refer to the list of transaction types in the endpoint description above.

status no string Transaction status. Refer to the list of statuses in the endpoint description above.

cursor no

Determines the offset of the returned result. It represents the ID of the item after which you want to retrieve the next result. To get the next result page, you can use the cursor from the pagination section of the previous response.

limit no number Maximum number of items that should be returned.

Response

Parameter Required Type Description

status yes string Response status. Can be OK or ERROR.

data[].id yes number or string Transaction ID. A number assigned by Extended for transfers and withdrawals. An onchain id string for deposits.

data[].type yes string Transaction type. Refer to the list of transaction types in the endpoint description above.

data[].status yes string Transaction status. Refer to the list of statuses in the endpoint description above.

data[].amount yes string Transaction amount, absolute value in collateral asset.

data[].fee yes string Fee paid.

data[].asset yes string Collateral asset name.

data[].time yes number Timestamp (epoch milliseconds) when the transaction was updated.

data[].accountId yes number Account ID; source account for transfers and withdrawals; destination account for deposits.

data[].counterpartyAccountId no number Account ID; destination account for transfers.

data[].transactionHash no string Onchain transaction hash. Not available for transfers.

Get positions HTTP Request GET /api/v1/user/positions?market={market}&side={side}

Get all open positions for the authenticated sub-account. Optionally, the request can be filtered by a specific market or position side (long or short).

To request data for multiple markets, use the following format: GET /api/v1/user/positions?market=market1&market2. Query Parameters

Parameter Required Type Description

market no string List of names of the requested markets.

side no string Position side. Can be LONG or SHORT.

Response example:

{ "status": "OK", "data": [ { "id": 1, "accountId": 1, "market": "BTC-USD", "side": "LONG", "leverage": "10", "size": "0.1", "value": "4000", "openPrice": "39000", "markPrice": "40000", "liquidationPrice": "38200", "margin": "20", "unrealisedPnl": "1000", "realisedPnl": "1.2", "tpTriggerPrice": "41000", "tpLimitPrice": "41500", "slTriggerPrice": "39500", "slLimitPrice": "39000", "adl": "2.5", "maxPositionSize": "0.2", "createdTime": 1701563440000, "updatedTime": 1701563440 } ] }

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

data[].id yes number Position ID assigned by Extended.

data[].accountId yes number Account ID.

data[].market yes string Market name.

data[].side yes string Position side. Can be LONG or SHORT.

data[].leverage yes string Position leverage.

data[].size yes string Position size, absolute value in base asset.

data[].value yes string Position value, absolute value in collateral asset.

data[].openPrice yes string Position's open (entry) price.

data[].markPrice yes string Current mark price of the market.

data[].liquidationPrice yes string Position's liquidation price.

data[].margin yes string Position's margin in collateral asset.

data[].unrealisedPnl yes string Position's Unrealised PnL.

data[].realisedPnl yes string Position's Realised PnL.

data[].tpTriggerPrice no string Take Profit Trigger price.

data[].tpLimitPrice no string Take Profit Limit price.

data[].slTriggerPrice no string Stop Loss Trigger price.

data[].slLimitPrice no string Stop Loss Limit price.

data[].maxPositionSize yes string Maximum allowed position size, absolute value in base asset.

data[].adl yes string Position's Auto-Deleveraging (ADL) ranking in the queue, expressed as a percentile. A value closer to 100 indicates a higher likelihood of being ADLed.

data[].createdTime yes number Timestamp (epoch milliseconds) when the position was created.

data[].updatedTime yes number Timestamp (epoch milliseconds) when the position was updated.

Get positions history HTTP Request GET /api/v1/user/positions/history?market={market}&side={side}

Get all open and closed positions for the authenticated sub-account. Optionally, the request can be filtered by a specific market or position side (long or short).

To request data for several markets, use the following format: GET /api/v1/user/positions/history?market=market1&market2.

The endpoint returns a maximum of 10,000 records; pagination should be used to access records beyond this limit. Query Parameters

Parameter Required Type Description

market no string List of names of the requested markets.

side no string Position side. Can be long or short.

cursor no number Determines the offset of the returned result. It represents the ID of the item after which you want to retrieve the next result. To get the next result page, you can use the cursor from the pagination section of the previous response.

limit no number Maximum number of items that should be returned.

Response example:

{ "status": "OK", "data": [ { "id": 1784963886257016832, "accountId": 1, "market": "BTC-USD", "side": "LONG", "exitType": "TRADE", "leverage": "10", "size": "0.1", "maxPositionSize": "0.2", "openPrice": "39000", "exitPrice": "40000", "realisedPnl": "1.2", "createdTime": 1701563440000, "closedTime": 1701563440 } ], "pagination": { "cursor": 1784963886257016832, "count": 1 } }

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

data[].id yes number Position ID assigned by Extended.

data[].accountId yes number Account ID.

data[].market yes string Market name.

data[].side yes string Position side. Can be LONG or SHORT.

data[].exitType no string The exit type of the last trade that reduced the position. Can be TRADE, LIQUIDATION, or DELEVERAGE.

data[].leverage yes string Position leverage.

data[].size yes string Position size, absolute value in base asset.

data[].maxPositionSize yes string Maximum position size during the position's lifetime, absolute value in base asset.

data[].openPrice yes string The weighted average price of trades that contributed to increasing the position.

data[].exitPrice no string The weighted average price of trades that contributed to decreasing the position.

data[].realisedPnl yes string Position Realised PnL.

data[].createdTime yes number Timestamp (in epoch milliseconds) when the position was created.

data[].closedTime no number Timestamp (in epoch milliseconds) when the position was closed, applicable only for closed positions.

Get open orders HTTP Request GET /api/v1/user/orders?market={market}&type={type}&side={side}

Get all open orders for the authenticated sub-account. Optionally, the request can be filtered by a specific market or order type (limit, conditional, or tpsl).

Open orders correspond to the following order statuses from the list below: new, partially filled, untriggered.

To request data for several markets, use the following format: GET /api/v1/user/orders?market=market1&market2. Order statuses

Status Description

NEW Order in the order book, unfilled.

PARTIALLY_FILLED Order in the order book, partially filled.

FILLED Order fully filled.

UNTRIGGERED Conditional order waiting for the trigger price.

CANCELLED Order cancelled.

REJECTED Order rejected.

EXPIRED Order expired.

TRIGGERED Technical status, transition from UNTRIGGERED to NEW.

Order status reasons (when cancelled or rejected)

Reason Description

NONE Order was accepted.

UNKNOWN Technical status reason.

UNKNOWN_MARKET Market does not exist.

DISABLED_MARKET Market is not active.

NOT_ENOUGH_FUNDS Insufficient balance to create order.

NO_LIQUIDITY Not enough liquidity in the market to execute the order.

INVALID_FEE Fee specified in the create order request is invalid.

INVALID_QTY Quantity specified is invalid.

INVALID_PRICE Price specified is invalid.

INVALID_VALUE Order exceeds the maximum value.

UNKNOWN_ACCOUNT Account does not exist.

SELF_TRADE_PROTECTION Order cancelled to prevent self-trading.

POST_ONLY_FAILED Order could not be posted as a post-only order.

REDUCE_ONLY_FAILED Reduce-only order failed due to position size conflict.

INVALID_EXPIRE_TIME Expiration time specified is invalid.

POSITION_TPSL_CONFLICT TPSL order for the entire position already exists.

INVALID_LEVERAGE Leverage specified is invalid.

PREV_ORDER_NOT_FOUND The order to be replaced does not exist.

PREV_ORDER_TRIGGERED The order to be replaced has been triggered and cannot be replaced.

TPSL_OTHER_SIDE_FILLED The opposite side of a TP/SL order has been filled.

PREV_ORDER_CONFLICT Conflict with an existing order during replacement.

ORDER_REPLACED Order has been replaced by another order.

POST_ONLY_MODE Exchange is in post-only mode, only post-only orders are allowed.

REDUCE_ONLY_MODE Exchange is in reduce-only mode, only reduce-only orders are allowed.

TRADING_OFF_MODE Trading is currently disabled.

NEGATIVE_EQUITY Account has negative equity.

ACCOUNT_LIQUIDATION Account is under liquidation.

Query Parameters

Parameter Required Type Description

market no string List of names of the requested markets.

type no string Order type. Can be LIMIT, CONDITIONAL or TPSL.

side no string Order side. Can be BUY or SELL.

Response example:

{ "status": "OK", "data": [ { "id": 1775511783722512384, "accountId": 3017, "externalId": "2554612759479898620327573136214120486511160383028978112799136270841501275076", "market": "ETH-USD", "type": "LIMIT", "side": "BUY", "status": "PARTIALLY_FILLED", "price": "3300", "averagePrice": "3297.00", "qty": "0.2", "filledQty": "0.1", "payedFee": "0.0120000000000000", "trigger": { "triggerPrice": "3300", "triggerPriceType": "LAST", "triggerPriceDirection": "UP", "executionPriceType": "MARKET" }, "takeProfit": { "triggerPrice": "3500", "triggerPriceType": "LAST", "price": "3340", "priceType": "MARKET" }, "stopLoss": { "triggerPrice": "2800", "triggerPriceType": "LAST", "price": "2660", "priceType": "MARKET" }, "reduceOnly": false, "postOnly": false, "createdTime": 1701563440000, "updatedTime": 1701563440000, "timeInForce": "FOK", "expireTime": 1712754771819 } ] }

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

data[].id yes number Order ID assigned by Extended.

data[].externalId yes string Order ID assigned by user.

data[].accountId yes number Account ID.

data[].market yes string Market name.

data[].status yes string Order status.

data[].statusReason no string Reason for REJECTED or CANCELLED status.

data[].type yes string Order type. Can be LIMIT, CONDITIONAL or TPSL.

data[].side yes string Order side. Can be BUY or SELL.

data[].price no string Worst accepted price in the collateral asset.

data[].averagePrice no string Actual filled price, empty if not filled.

data[].qty yes string Order size in base asset.

data[].filledQty no string Actual filled quantity in base asset.

data[].payedFee no string Paid fee.

data[].reduceOnly no boolean Whether the order is Reduce-only.

data[].postOnly no boolean Whether the order is Post-only.

data[].trigger.triggerPrice no string Trigger price for conditional orders.

data[].trigger.triggerPriceType no string Trigger price type . Can be LAST, MARK or INDEX.

data[].trigger.triggerPriceDirection no string Indicates whether the order should be triggered when the price is above or below the set trigger price. It can be UP (the order will be triggered when the price reaches or surpasses the set trigger price) or DOWN (the order will be triggered when the price reaches or drops below the set trigger price).

data[].trigger.executionPriceType no string Execution price type. Can be LIMIT or MARKET.

data[].tpSlType no string TPSL type determining TPSL order size. Can be ORDER or POSITION.

data[].takeProfit.triggerPrice no string Take Profit Trigger price.

data[].takeProfit.triggerPriceType no string Take Profit Trigger price type. Can be LAST, MARK or INDEX.

data[].takeProfit.price no string Take Profit order price.

data[].takeProfit.priceType no string Indicates whether the Take profit order should be executed as MARKET or LIMIT order.

data[].stopLoss.triggerPrice no string Stop loss Trigger price.

data[].stopLoss.triggerPriceType no string Stop Loss Trigger price type. Can be LAST, MARK or INDEX.

data[].stopLoss.price no string Stop loss order price.

data[].stopLoss.priceType no string Indicates whether the Stop loss order should be executed as MARKET or LIMIT order.

data[].createdTime yes number Timestamp (in epoch milliseconds) of order creation.

data[].updatedTime yes number Timestamp (in epoch milliseconds) of order update.

data[].timeInForce yes string Time-in-force. Can be GTT (Good till time), FOK (Fill or kill) or IOC (Immediate or cancel).

data[].expireTime yes number Timestamp (in epoch milliseconds) when the order expires.

Get orders history HTTP Request GET /api/v1/user/orders/history?market={market}&type={type}&side={side}&id={id}&externalId={externalId}

Get orders history for the authenticated sub-account. Optionally, the request can be filtered by a specific market or order type (limit, market, conditional, or tpsl).

Orders history corresponds to the following order statuses from the list below: filled, cancelled, rejected, expired.

To request data for several markets, use the following format: GET /api/v1/user/orders/history?market=market1&market2.

The endpoint returns a maximum of 10,000 records; pagination should be used to access records beyond this limit. The records for non-filled orders are available only for the past 7 days. Order statuses

Status Description

NEW Order in the order book, unfilled.

PARTIALLY_FILLED Order in the order book, partially filled.

FILLED Order fully filled.

UNTRIGGERED Conditional order waiting for the trigger price.

CANCELLED Order cancelled.

REJECTED Order rejected.

EXPIRED Order expired.

TRIGGERED Technical status, transition from UNTRIGGERED to NEW.

Query Parameters

Parameter Required Type Description

id no number List of internal Ids of the requested orders.

externalId no string[] List of external Ids of the requested orders.

market no string[] List of names of the requested markets.

type no string Order type. Can be limit, market, conditional or tpsl.

side no string Order side. Can be buy or sell.

cursor no number Determines the offset of the returned result. It represents the ID of the item after which you want to retrieve the next result. To get the next result page, you can use the cursor from the pagination section of the previous response.

limit no number Maximum number of items that should be returned.

Response example:

{ "status": "OK", "data": [ { "id": 1784963886257016832, "externalId": "ExtId-1", "accountId": 1, "market": "BTC-USD", "status": "FILLED", "type": "LIMIT", "side": "BUY", "price": "39000", "averagePrice": "39000", "qty": "0.2", "filledQty": "0.1", "payedFee": "0.0120000000000000", "reduceOnly": false, "postOnly": false, "trigger": { "triggerPrice": "34000", "triggerPriceType": "LAST", "triggerPriceDirection": "UP", "executionPriceType": "MARKET" }, "tpslType": "ORDER", "takeProfit": { "triggerPrice": "34000", "triggerPriceType": "LAST", "price": "35000", "priceType": "MARKET", "starkExSignature": "" }, "stopLoss": { "triggerPrice": "34000", "triggerPriceType": "LAST", "price": "35000", "priceType": "MARKET", "starkExSignature": "" }, "createdTime": 1701563440000, "updatedTime": 1701563440000, "timeInForce": "FOK", "expireTime": 1706563440 } ], "pagination": { "cursor": 1784963886257016832, "count": 1 } }

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

data[].id yes number Order ID assigned by Extended.

data[].externalId yes string Order ID assigned by user.

data[].accountId yes number Account ID.

data[].market yes string Market name.

data[].status yes string Order status.

data[].statusReason no string Reason for REJECTED or CANCELLED status.

data[].type yes string Order type. Can be LIMIT, MARKET, CONDITIONAL or TPSL.

data[].side yes string Order side. Can be BUY or SELL.

data[].price no string Worst accepted price in the collateral asset.

data[].averagePrice no string Actual filled price, empty if not filled.

data[].qty yes string Order size in base asset.

data[].filledQty no string Actual filled quantity in base asset.

data[].payedFee no string Paid fee.

data[].reduceOnly no boolean Whether the order is Reduce-only.

data[].postOnly no boolean Whether the order is Post-only.

data[].trigger.triggerPrice no string Trigger price for conditional orders.

data[].trigger.triggerPriceType no string Trigger price type . Can be LAST, MARK or INDEX.

data[].trigger.triggerPriceDirection no string Indicates whether the order should be triggered when the price is above or below the set trigger price. It can be UP (the order will be triggered when the price reaches or surpasses the set trigger price) or DOWN (the order will be triggered when the price reaches or drops below the set trigger price).

data[].trigger.executionPriceType no string Execution price type. Can be LIMIT or MARKET.

data[].tpSlType no string TPSL type determining TPSL order size. Can be ORDER or POSITION.

data[].takeProfit.triggerPrice no string Take Profit Trigger price.

data[].takeProfit.triggerPriceType no string Take Profit Trigger price type. Can be LAST, MARK or INDEX.

data[].takeProfit.price no string Take Profit order price.

data[].takeProfit.priceType no string Indicates whether the Take profit order should be executed as MARKET or LIMIT order.

data[].stopLoss.triggerPrice no string Stop loss Trigger price.

data[].stopLoss.triggerPriceType no string Stop Loss Trigger price type. Can be LAST, MARK or INDEX.

data[].stopLoss.price no string Stop loss order price.

data[].stopLoss.priceType no string Indicates whether the Stop loss order should be executed as MARKET or LIMIT order.

data[].createdTime yes number Timestamp (in epoch milliseconds) of order creation.

data[].updatedTime yes number Timestamp (in epoch milliseconds) of order update.

data[].timeInForce yes string Time-in-force. Can be GTT (Good till time), FOK (Fill or kill) or IOC (Immediate or cancel).

data[].expireTime yes number Timestamp (in epoch milliseconds) when the order expires.

Get order by id HTTP Request `GET /api/v1/user/orders/{id}

Get order by id for the authenticated sub-account. Order statuses

Status Description

NEW Order in the order book, unfilled.

PARTIALLY_FILLED Order in the order book, partially filled.

FILLED Order fully filled.

UNTRIGGERED Conditional order waiting for the trigger price.

CANCELLED Order cancelled.

REJECTED Order rejected.

EXPIRED Order expired.

TRIGGERED Technical status, transition from UNTRIGGERED to NEW.

URL Parameters

Parameter Required Type Description

id yes number Order to be retrieved, ID assigned by Extended.

Response example:

{ "status": "OK", "data": { "id": 1784963886257016832, "externalId": "ExtId-1", "accountId": 1, "market": "BTC-USD", "status": "FILLED", "type": "LIMIT", "side": "BUY", "price": "39000", "averagePrice": "39000", "qty": "0.2", "filledQty": "0.1", "payedFee": "0.0120000000000000", "reduceOnly": false, "postOnly": false, "trigger": { "triggerPrice": "34000", "triggerPriceType": "LAST", "triggerPriceDirection": "UP", "executionPriceType": "MARKET" }, "tpslType": "ORDER", "takeProfit": { "triggerPrice": "34000", "triggerPriceType": "LAST", "price": "35000", "priceType": "MARKET", "starkExSignature": "" }, "stopLoss": { "triggerPrice": "34000", "triggerPriceType": "LAST", "price": "35000", "priceType": "MARKET", "starkExSignature": "" }, "createdTime": 1701563440000, "updatedTime": 1701563440000, "timeInForce": "FOK", "expireTime": 1706563440 } }

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

data.id yes number Order ID assigned by Extended.

data.externalId yes string Order ID assigned by user.

data.accountId yes number Account ID.

data.market yes string Market name.

data.status yes string Order status.

data.statusReason no string Reason for REJECTED or CANCELLED status.

data.type yes string Order type. Can be LIMIT, MARKET, CONDITIONAL or TPSL.

data.side yes string Order side. Can be BUY or SELL.

data.price no string Worst accepted price in the collateral asset.

data.averagePrice no string Actual filled price, empty if not filled.

data.qty yes string Order size in base asset.

data.filledQty no string Actual filled quantity in base asset.

data.payedFee no string Paid fee.

data.reduceOnly no boolean Whether the order is Reduce-only.

data.postOnly no boolean Whether the order is Post-only.

data.trigger.triggerPrice no string Trigger price for conditional orders.

data.trigger.triggerPriceType no string Trigger price type . Can be LAST, MARK or INDEX.

data.trigger.triggerPriceDirection no string Indicates whether the order should be triggered when the price is above or below the set trigger price. It can be UP (the order will be triggered when the price reaches or surpasses the set trigger price) or DOWN (the order will be triggered when the price reaches or drops below the set trigger price).

data.trigger.executionPriceType no string Execution price type. Can be LIMIT or MARKET.

data.tpSlType no string TPSL type determining TPSL order size. Can be ORDER or POSITION.

data.takeProfit.triggerPrice no string Take Profit Trigger price.

data.takeProfit.triggerPriceType no string Take Profit Trigger price type. Can be LAST, MARK or INDEX.

data.takeProfit.price no string Take Profit order price.

data.takeProfit.priceType no string Indicates whether the Take profit order should be executed as MARKET or LIMIT order.

data.stopLoss.triggerPrice no string Stop loss Trigger price.

data.stopLoss.triggerPriceType no string Stop Loss Trigger price type. Can be LAST, MARK or INDEX.

data.stopLoss.price no string Stop loss order price.

data.stopLoss.priceType no string Indicates whether the Stop loss order should be executed as MARKET or LIMIT order.

data.createdTime yes number Timestamp (in epoch milliseconds) of order creation.

data.updatedTime yes number Timestamp (in epoch milliseconds) of order update.

data.timeInForce yes string Time-in-force. Can be GTT (Good till time), FOK (Fill or kill) or IOC (Immediate or cancel).

data.expireTime yes number Timestamp (in epoch milliseconds) when the order expires.

Get orders by externalId HTTP Request `GET /api/v1/user/orders/external/{externalId}

Get orders by externalId for the authenticated sub-account. Order statuses

Status Description

NEW Order in the order book, unfilled.

PARTIALLY_FILLED Order in the order book, partially filled.

FILLED Order fully filled.

UNTRIGGERED Conditional order waiting for the trigger price.

CANCELLED Order cancelled.

REJECTED Order rejected.

EXPIRED Order expired.

TRIGGERED Technical status, transition from UNTRIGGERED to NEW.

URL Parameters

Parameter Required Type Description

externalId yes number Order to be retrieved, ID assigned by user.

Response example:

{ "status": "OK", "data": [ { "id": 1784963886257016832, "externalId": "ExtId-1", "accountId": 1, "market": "BTC-USD", "status": "FILLED", "type": "LIMIT", "side": "BUY", "price": "39000", "averagePrice": "39000", "qty": "0.2", "filledQty": "0.1", "payedFee": "0.0120000000000000", "reduceOnly": false, "postOnly": false, "trigger": { "triggerPrice": "34000", "triggerPriceType": "LAST", "triggerPriceDirection": "UP", "executionPriceType": "MARKET" }, "tpslType": "ORDER", "takeProfit": { "triggerPrice": "34000", "triggerPriceType": "LAST", "price": "35000", "priceType": "MARKET", "starkExSignature": "" }, "stopLoss": { "triggerPrice": "34000", "triggerPriceType": "LAST", "price": "35000", "priceType": "MARKET", "starkExSignature": "" }, "createdTime": 1701563440000, "updatedTime": 1701563440000, "timeInForce": "FOK", "expireTime": 1706563440 } ] }

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

data[].id yes number Order ID assigned by Extended.

data[].externalId yes string Order ID assigned by user.

data[].accountId yes number Account ID.

data[].market yes string Market name.

data[].status yes string Order status.

data[].statusReason no string Reason for REJECTED or CANCELLED status.

data[].type yes string Order type. Can be LIMIT, MARKET, CONDITIONAL or TPSL.

data[].side yes string Order side. Can be BUY or SELL.

data[].price no string Worst accepted price in the collateral asset.

data[].averagePrice no string Actual filled price, empty if not filled.

data[].qty yes string Order size in base asset.

data[].filledQty no string Actual filled quantity in base asset.

data[].payedFee no string Paid fee.

data[].reduceOnly no boolean Whether the order is Reduce-only.

data[].postOnly no boolean Whether the order is Post-only.

data[].trigger.triggerPrice no string Trigger price for conditional orders.

data[].trigger.triggerPriceType no string Trigger price type . Can be LAST, MARK or INDEX.

data[].trigger.triggerPriceDirection no string Indicates whether the order should be triggered when the price is above or below the set trigger price. It can be UP (the order will be triggered when the price reaches or surpasses the set trigger price) or DOWN (the order will be triggered when the price reaches or drops below the set trigger price).

data[].trigger.executionPriceType no string Execution price type. Can be LIMIT or MARKET.

data[].tpSlType no string TPSL type determining TPSL order size. Can be ORDER or POSITION.

data[].takeProfit.triggerPrice no string Take Profit Trigger price.

data[].takeProfit.triggerPriceType no string Take Profit Trigger price type. Can be LAST, MARK or INDEX.

data[].takeProfit.price no string Take Profit order price.

data[].takeProfit.priceType no string Indicates whether the Take profit order should be executed as MARKET or LIMIT order.

data[].stopLoss.triggerPrice no string Stop loss Trigger price.

data[].stopLoss.triggerPriceType no string Stop Loss Trigger price type. Can be LAST, MARK or INDEX.

data[].stopLoss.price no string Stop loss order price.

data[].stopLoss.priceType no string Indicates whether the Stop loss order should be executed as MARKET or LIMIT order.

data[].createdTime yes number Timestamp (in epoch milliseconds) of order creation.

data[].updatedTime yes number Timestamp (in epoch milliseconds) of order update.

data[].timeInForce yes string Time-in-force. Can be GTT (Good till time), FOK (Fill or kill) or IOC (Immediate or cancel).

data[].expireTime yes number Timestamp (in epoch milliseconds) when the order expires.

Get trades HTTP Request GET /api/v1/user/trades?market={market}&type={type}&side={side}

Get trades history for the authenticated sub-account. Optionally, the request can be filtered by a specific market, by trade type (trade, liquidation or deleverage) and side (buy or sell).

To request data for several markets, use the following format: GET /api/v1/user/trades?market=market1&market2.

The endpoint returns a maximum of 10,000 records; pagination should be used to access records beyond this limit. Query Parameters

Parameter Required Type Description

market no string List of names of the requested markets.

type no string Trade type. Can be trade, liquidation or deleverage.

side no string Order side. Can be buy or sell.

Response example:

{ "status": "OK", "data": [ { "id": 1784963886257016832, "accountId": 3017, "market": "BTC-USD", "orderId": 9223372036854775808, "externalId": "ext-1", "side": "BUY", "price": "58853.4000000000000000", "qty": "0.0900000000000000", "value": "5296.8060000000000000", "fee": "0.0000000000000000", "tradeType": "DELEVERAGE", "createdTime": 1701563440000, "isTaker": true } ], "pagination": { "cursor": 1784963886257016832, "count": 1 } }

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

data[].id yes number Trade ID assigned by Extended.

data[].accountId yes number Account ID.

data[].market yes string Market name.

data[].orderId yes string Order ID assigned by Extended.

data[].externalOrderId yes string Order ID assigned by user. Populated only on websocket stream.

data[].side yes string Order side. Can be BUY or SELL.

data[].averagePrice yes string Actual filled price.

data[].filledQty yes string Actual filled quantity in base asset.

data[].value yes string Actual filled absolute nominal value in collateral asset.

data[].fee yes string Paid fee.

data[].isTaker yes boolean Whether the trade was executed as a taker.

data[].tradeType yes string Trade type. Can be TRADE (for regular trades), LIQUIDATION (for liquidaton trades) or DELEVERAGE (for ADL trades).

data[].createdTime yes number Timestamp (in epoch milliseconds) when the trade happened.

Get funding payments HTTP Request GET /api/v1/user/funding/history?market={market}&side={side}&fromTime={fromTime}

Get funding payments history for the authenticated sub-account. Optionally, the request can be filtered by a specific market, by side (long or short) and from time as a start point.

To request data for several markets, use the following format: GET /api/v1/user/funding/history?market=market1&market2.

The endpoint returns a maximum of 10,000 records; pagination should be used to access records beyond this limit. Query Parameters

Parameter Required Type Description

market no string List of names of the requested markets.

side no string Position side. Can be long or short.

fromTime yes number Starting timestamp (in epoch milliseconds).

Response example:

{ "status": "OK", "data": [ { "id": 8341, "accountId": 3137, "market": "BNB-USD", "positionId": 1821237954501148672, "side": "LONG", "size": "1.116", "value": "560.77401888", "markPrice": "502.48568", "fundingFee": "0", "fundingRate": "0", "paidTime": 1723147241346 } ], "pagination": { "cursor": 8341, "count": 1 } }

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

data[].id yes number Funding payment ID assigned by Extended.

data[].accountId yes number Account ID.

data[].market yes string Market name.

data[].positionId yes number Position ID assigned by Extended.

data[].side yes string Position side. Can be LONG or SHORT.

data[].value yes string Position value at funding payment time.

data[].markPrice yes string Mark price at funding payment time

data[].fundingFee yes string Funding payment size.

data[].fundingRate yes string Funding rate.

data[].paidTime yes number Timestamp (in epoch milliseconds) when the funding payment happened.

Get current leverage HTTP Request GET /api/v1/user/leverage?market={market}

Get current leverage for the authenticated sub-account. You can get current leverage for all markets, a single market, or multiple specific markets.

To request data for several markets, use the format GET/api/v1/user/leverage?market=market1&market=market2. Query Parameters

Parameter Required Type Description

market no string Name of the requested market.

Response example:

{ "status": "OK", "data": [ { "market": "SOL-USD", "leverage": "10" } ] }

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

data.market yes string Market name.

data.leverage yes string Current leverage.

Update leverage HTTP Request PATCH /api/v1/user/leverage

Update leverage for an individual market.

Modifying your leverage will impact your Available balance and Initial Margin requirements of your open position and orders in the market.

To adjust your leverage, you must meet two requirements: - The total value of your open position and triggered orders must remain below the maximum position value allowed for the selected leverage. - Your Available balance must be sufficient to cover the additional Margin requirements (if any) associated with the new leverage.

Failure to meet either of these criteria will result in an error.

For details on Margin requirements, please refer to the documentation.

Request example:

{ "market": "BTC-USD", "leverage": "10" }

Body Parameters

Parameter Required Type Description

market yes string Name of the requested market.

leverage yes string Target leverage.

Response example:

{ "status": "OK", "data": { "market": "BTC-USD", "leverage": "10" } }

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

data.market yes string Market name.

data.leverage yes string Updated leverage.

Get fees HTTP Request GET /api/v1/user/fees?market={market}

Get current fees for the sub-account.

Fees on Extended are determined by:

The type of order: Maker vs. Taker, The cumulative trading volume over the past 30 days.

For details on the Fee Schedule, please refer to the documentation. Query Parameters

Parameter Required Type Description

market no string Name of the requested market.

Response example:

{ "status": "OK", "data": [ { "market": "BTC-USD", "makerFeeRate": "0.0002", "takerFeeRate": "0.0005" } ] }

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

data.market yes string Market name.

data.makerFeeRate yes string Maker fee rate.

data.takerFeeRate yes string Taker fee rate.

Order management The Private API endpoints listed below allow you to create, cancel, and manage orders from the authenticated sub-account. StarkEx-Specific Logic Extended's use of the StarkEx Layer 2 engine introduces unique elements to order creation that differ from centralized exchanges:

StarkKey Signature: Required for all order management endpoints. For details, please refer to the reference implementation in the Python SDK. Price Parameter: All orders, including market orders, require a price as a mandatory parameter. Fee Parameter: All orders require a fee as a mandatory parameter. The Fee parameter represents the maximum fee a user is willing to pay for an order. Use the maker fee for Post-only orders and the taker fee for all other orders. Enter the fee in decimal format (e.g., 0.1 for 10%). To view current fees, utilize the Get fees endpoint, which displays applicable fee rates. Expiration Timestamp: All orders, including Fill or Kill and Immediate or Cancel orders, require an expiration timestamp as a mandatory parameter. When submitting orders via the API, enter the expiration time as an epoch timestamp in milliseconds. On the Mainnet, the maximum allowable expiration time is 90 days from the order creation date. On the Testnet, 28 days from the order creation date. Market Orders: StarkEx does not natively support market orders. On the UI, market orders are created as limit IOC (Immediate-or-Cancel) orders with a price parameter set to ensure immediate execution. For example, Market Buy Orders are set at the best ask price multiplied by 1.05, and Market Sell Orders at the best bid price multiplied by 0.95 (subtracting 5%). TPSL Orders: Orders with Take Profit and/or Stop Loss require multiple signatures. Please refer to the (documentation)[https://docs.extended.exchange/extended-resources/trading/order-types] to see supported types of TPSL orders.

Create or edit order HTTP Request POST /api/v1/user/order

Create a new order or edit (replace) an open order. When you create an order via our REST API, the initial response will confirm whether the order has been successfully accepted. Please be aware that, although rare, orders can be canceled or rejected by the Matching Engine even after acceptance at the REST API level. To receive real-time updates on your order status, it is crucial to subscribe to the Account updates WebSocket stream. This stream provides immediate notifications of any changes to your orders, including confirmations, cancellations, and rejections, allowing you to manage your trading strategies effectively.

Currently, we support limit, market, conditional and tpsl order types, along with reduce-only and post-only settings. For API trading, we offer the following Time-in-force settings: GTT (Good till time - default), FOK (Fill or kill) and IOC (Immediate or cancel). On the Mainnet, the maximum allowable expiration time for GTT orders is 90 days from the order creation date. On the Testnet, 28 days from the order creation date. For details on supported order types and settings, please refer to the documentation

To successfully place an order, it must meet the following requirements:

Trading Rules. For detailed information, please refer to the trading rules documentation. Order Cost Requirements. For detailed information, please refer to the order cost documentation. Margin Schedule Requirements. For detailed information, please refer to the margin schedule documentation. Price requirements, which are described below.

Price requirements

Limit Orders

Long Limit Orders: Order Price ≤ Mark Price * (1+Limit Order Price Cap) Short Limit Orders: Order Price ≥ Mark Price * (1-Limit Order Floor Ratio)

Market Orders

Long Market Order: Order Price ≤ Mark Price * (1 + 15%) Short Market Order: Order Price ≥ Mark Price * (1 - 15%)

Conditional Orders

Short Conditional Orders: Order Price ≥ Trigger price * (1-Limit Order Floor Ratio) Long Conditional Orders: Order Price ≤ Trigger Price * (1+Limit Order Price Cap) If a conditional order is triggered at placement, we apply the same validations as those for limit and market orders.

TPSL Orders

Entry order: Buy; TPSL order: Sell.

Validation Stop loss Take profit

Trigger price validation Trigger price < Entry order price Trigger price > Entry order price.

Limit price validation Order Price ≥ Trigger price * (1-Limit Order Floor Ratio) Order Price ≥ Trigger price * (1-Limit Order Floor Ratio)

Entry order: Sell; TPSL order: Buy.

Validation Stop loss Take profit

Trigger price validation Trigger price > Entry order price. Trigger price < Entry order price.

Limit price validation Order Price ≤ Trigger Price * (1+Limit Order Price Cap) Order Price ≤ Trigger Price * (1+Limit Order Price Cap)

Orders Edit To edit (replace) an open order, add its ID as the cancelId parameter. You can edit multiple parameters at once. Editing is available for all orders except for triggered TPSL orders.

Order editing and validations:

If any updated parameter fails the validations described above, all updates will be rejected. If validations fail at the REST API level, the initial open order remains unchanged. In the rare event that validations pass at the REST API level but fail at the Matching Engine, both the updated order and the initial open order will be cancelled.

Editable Order Parameters:

For All Order Types (except triggered TPSL orders): Order price and Execution Order Price Type (market or limit) For All Order Types (except untriggered entire position TPSL orders and triggered TPSL orders): Order size For Conditional and Untriggered TPSL Orders: Trigger price For Conditional Orders: Trigger price direction (up or down) For Non-TPSL Orders: All TPSL parameters

Self trade protection Self-trade protection is a mechanism designed to prevent orders from the same client or sub-account from executing against each other.

When two orders from the same client or sub-account are about to match, the system evaluates the self-trade protection level specified by the taker order to determine how to handle the potential self-match.

Value Description

DISABLED Self trade protection is disabled

ACCOUNT Trades within same sub-account are disabled, trades between sub-accounts are enabled.

CLIENT Trades within same sub-account and between sub-accounts are disabled.

Request

Request example:

{ "id": "e581a9ca-c3a2-4318-9706-3f36a2b858d3", "market": "BTC-USDT", "type": "CONDITIONAL", "side": "BUY", "qty": "1", "price": "1000", "timeInForce": "GTT", "expiryEpochMillis": 1715884049245, "fee": "0.0002", "nonce": "876542", "settlement": { "signature": { "r": "0x17a89cb97c64f546d2dc9189e1ef73547487b228945dcda406cd0e4b8301bd3", "s": "0x385b65811a0fc92f109d5ebc30731efd158ee4e502945cd2fcb35a4947b045e" }, "starkKey": "0x23830b00378d17755775b5a73a5967019222997eb2660c2dbfbc74877c2730f", "collateralPosition": "4272448241247734333" }, "reduceOnly": true, "postOnly": false, "selfTradeProtectionLevel": "ACCOUNT", "trigger": { "triggerPrice": "12000", "triggerPriceType": "LAST", "direction": "UP", "executionPriceType": "LIMIT" }, "tpSlType": "ORDER", "takeProfit": { "triggerPrice": "1050", "triggerPriceType": "LAST", "price": "1300", "priceType": "LIMIT", "settlement": { "signature": { "r": "0x5b45f0fb2b8e075f6a5f9b4c039ccf1c01c56aa212c63f943337b920103c3a1", "s": "0x46133ab89d90a3ae2a3a7680d2a27e30fa015c0c4979931164c51b52b27758a" }, "starkKey": "0x23830b00378d17755775b5a73a5967019222997eb2660c2dbfbc74877c2730f", "collateralPosition": "4272448241247734333" } }, "stopLoss": { "triggerPrice": "950", "triggerPriceType": "LAST", "price": "900", "priceType": "LIMIT", "settlement": { "signature": { "r": "0x5033ad23fe851d16ceec5dd99f2f0c9585c5abec3f09ec89a32a961536ba55", "s": "0x1234ee151a8b5c68efb4adaa2eaf1dcc4a5107d4446274a69389ef8abd2dcf" }, "starkKey": "0x23830b00378d17755775b5a73a5967019222997eb2660c2dbfbc74877c2730f", "collateralPosition": "4272448241247734333" } } }

Body Parameters

Parameter Required Type Description

id yes string Order ID assigned by user.

market yes string Market name.

type yes string Order type. Can be limit, market, conditional or tpsl.

side yes string Order side. Can be buy or sell.

qty yes string Order size in base asset.

price yes string Worst accepted price in collateral asset. Note that price is optional for a tpsl type position.

reduceOnly no boolean Whether the order should be Reduce-only.

postOnly no boolean Whether the order should be Post-only.

timeInForce yes string Time-in-force setting. Can be GTT (Good till time), FOK (Fill or kill) or IOC (Immediate or cancel). This parameter will default to GTT.

expiryEpochMillis yes number Timestamp (in epoch milliseconds) when the order expires if not filled. Cannot exceed 3 months from the order creation time.

fee yes string Highest accepted fee for the trade, expressed in decimal format (e.g., 0.1 for 10%). Use the maker fee for Post-only orders and the taker fee for all other orders.

cancelId no string External ID of the order that this order is replacing.

settlement yes object StarkKey signature, including nonce and signed order parameters. For details, please refer to the Python SDK reference implementation.

nonce yes string Nonce is part of the settlement and must be a number ≥1 and ≤2^31. Please make sure to check the Python SDK reference implementation.

selfTradeProtectionLevel yes string Level of self trade protection. Can be DISABLED, ACCOUNT(default) and CLIENT.

trigger.triggerPrice no string Price threshold for triggering a conditional order.

trigger.triggerPriceType no string Type of price used for the order triggering. Can be last, mark or index.

trigger.triggerPriceDirection no string Indicates whether the order should be triggered when the price is above or below the set trigger price. It can be up (the order will be triggered when the price reaches or surpasses the set trigger price) or down (the order will be triggered when the price reaches or drops below the set trigger price).

trigger.executionPriceType no string Type of price used for the order execution. Can be limit or market.

tpSlType no string TPSL type determining TPSL order size. Can be order or position.

takeProfit.triggerPrice no string Take Profit Trigger price.

takeProfit.triggerPriceType no string Type of price used for the Take Profit order triggering. Can be last, mark or index.

takeProfit.price no string Take Profit order price.

takeProfit.priceType no string Indicates whether the Take profit order should be executed as market or limit order.

takeProfit.settlement no object StarkKey signature, including nonce and signed order parameters. For details, please refer to the Python SDK reference implementation.

triggerPrice no string Stop loss Trigger price.

stopLoss.triggerPriceType no string Type of price used for the Stop Loss order triggering. Can be last, mark or index.

stopLoss.price no string Stop loss order price.

stopLoss.priceType no string Indicates whether the Stop loss order should be executed as market or limit order.

stopLoss.settlement no object StarkKey signature, including nonce and signed order parameters. For details, please refer to the Python SDK reference implementation.

Response example:

{ "status": "OK", "data": { "id": 1791389621914243072, "externalId": "31097979600959341921260192820644698907062844065707793749567497227004358262" } }

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

data.id yes number Order ID assigned by Extended.

data.externalId yes string Order ID assigned by user.

Cancel order HTTP Request DELETE /api/v1/user/order/{id}

Cancel an individual order by Extended ID.

The cancellation process is asynchronous; the endpoint returns only the status of the cancellation. URL Parameters

Parameter Required Type Description

id yes number Order to be canceled, ID assigned by Extended.

DELETE /api/v1/user/order?externalId={externalId}

Cancel an individual order by user ID.

The cancellation process is asynchronous; the endpoint returns only the status of the cancellation. URL Parameters

Parameter Required Type Description

externalId yes string Order to be canceled, Order ID assigned by user.

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

Mass Cancel HTTP Request POST /api/v1/user/order/massCancel

Mass Cancel enables the cancellation of multiple orders by ID, by specific market, or for all orders within an account.

The cancellation process is asynchronous; the endpoint returns only the status of the cancellation request.

Although all parameters are optional, at least one must be specified.

Request example:

{ "orderIds": [ 1, 2 ], "externalOrderIds": [ "ExtId-1", "ExtId-2" ], "markets": [ "BTC-USD", "ETH-USD" ], "cancelAll": true }

Body Parameters

Parameter Required Type Description

markets no string[] Market names where all orders should be cancelled.

cancelAll no boolean Indicates whether all open orders for the account should be cancelled.

orderIds no number[] Cancel by Extended IDs.

externalOrderIds no string[] Cancel by external IDs.

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

Mass Auto-Cancel (Dead Man's Switch) HTTP Request POST /api/v1/user/deadmanswitch?countdownTime={countdownTime}

The dead man's switch automatically cancels all open orders for the account at the end of the specified countdown if no Mass Auto-Cancel request is received within this timeframe. Setting the time to zero will remove any outstanding scheduled cancellations.

Positions and account status are not affected by the dead man's switch. Request Parameters

Parameter Required Type Description

countdownTime yes number Time till Scheduled Mass Cancel (in seconds), should be non-negative. Setting the time to zero will remove any outstanding scheduled cancellations.

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

Deposits To deposit, please invoke the StarkEx contract. The contract address is 0x1cE5D7f52A8aBd23551e91248151CA5A13353C65.

Currently, we only support USDC deposits via the Ethereum network. Create transfer HTTP Request POST /api/v1/user/transfer

Create a transfer between sub-accounts associated with the same L1 wallet. Request

Request example:

{ "fromAccount": 3004, "toAccount": 7349, "amount": "1000", "transferredAsset": "USD", "settlement": { "amount": 1000000000, "assetId": "0x31857064564ed0ff978e687456963cba09c2c6985d8f9300a1de4962fafa054", "expirationTimestamp": 478932, "nonce": 758978120, "receiverPositionId": 104350, "receiverPublicKey": "0x3895139a98a6168dc8b0db251bcd0e6dcf97fd1e96f7a87d9bd3f341753a844", "senderPositionId": 100005, "senderPublicKey": "0x3895139a98a6168dc8b0db251bcd0e6dcf97fd1e96f7a87d9bd3f341753a844", "signature": { "r": "6be1839e2ca76484a1a0fcaca9cbbe3792a23656d42ecee306c31e65aadb877", "s": "7b8f81258e16f0f90cd12f02e81427e54b4ebf7646e9b14b57f74c2cb44bff6" } } }

Body Parameters

Parameter Required Type Description

fromAccount yes number Source account ID.

toAccount yes number Destination account ID.

amount yes string Transfer amount, absolute value in collateral asset.

transferredAsset yes string Collateral asset name.

settlement yes object Transfer object StarkKey signature (including nonce and transfer parameters). For details, please refer to the Python SDK.

Response example:

{ "status": "OK", "data": { "validSignature": true, "id": 1820778187672010752 } }

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

data.validSignature yes boolean Indicates whether the signature is valid.

data.id yes number Transfer ID assigned by Extended.

Withdrawals We support two types of withdrawals: fast and slow. Slow withdrawals can be made through both the API and UI, while fast withdrawals are available only via the UI. Withdrawals are permitted only to L1 wallets associated with the authorised account.

Extended doesn't charge fees on both types of withdrawals, but there are differences in processing. Slow withdrawals: Slow withdrawals involve a two-step process. The first step initiates your withdrawal request, which is processed on Layer 2. Once your funds are ready (this can take up to 12 hours), you can claim them to your wallet.

To initiate a slow withdrawal, send a "Create Slow Withdrawal" request as described below or use the corresponding SDK method slow_withdrawal, signed with a private L2 key.

To check if your funds are available for claim, use SDK method call_stark_perpetual_withdraw_balance.

To claim available funds, use SDK method call_stark_perpetual_withdraw, signed with a private L1 key.

Gas fee selection is currently not supported through the API. The gas value will be populated using the estimate_gas() function with an additional buffer of 100,000 gas up to the gasLimit of the latest block.

There is no maximum limit on the amount for slow withdrawals. Fast withdrawals: Processed almost instantly with a daily limit of $50,000 per calendar day.

A charge of 2x the current gas fee is applied to ensure transaction settlement in the event of gas cost volatility.

In rare instances, fast withdrawals may be unavailable due to liquidity gaps in the exchange's L1 wallet. If this occurs, please consider using slow withdrawals or try again later.

Fast withdrawals are not available for Market Makers and other institutional clients. Create slow withdrawal HTTP Request POST /api/v1/user/withdrawal

Create a slow withdrawal to the L1 wallet associated with the authorised account. To avoid rejection, ensure that the withdrawal amount does not exceed your Available Balance for Withdrawals.

Available Balance for Withdrawals = max(0, Wallet Balance + min(0,Unrealised PnL) - Initial Margin Requirement). Request

Request example: json { "type": "SLOW_SELF", "accountId": 3004, "amount": "1000", "asset": "USD", "settlement": { "amount": 1000000000, "collateralAssetId": "0x31857064564ed0ff978e687456963cba09c2c6985d8f9300a1de4962fafa054", "ethAddress": "0x1CE5161147db031d838F4BCDf86412C176d5a0D3", "expirationTimestamp": 479125, "nonce": 1696065254, "positionId": 100005, "publicKey": "0x3895139a98a6168dc8b0db251bcd0e6dcf97fd1e96f7a87d9bd3f341753a844", "signature": { "r": "34947b8a82c268d484dc5b879014a70acd6f071db2d80c356f47c5c56e8041d", "s": "37d5b153c786ba6b8b75a594e2e86f710404f0f045ac243a8db0002ff3aed27" } } }

Body Parameters

Parameter Required Type Description

type yes string For slow withdrawals, the type should be SLOW_SELF.

accountId yes number Source account ID.

amount yes string Withdrawal amount, absolute value in collateral asset.

asset yes string Collateral asset name.

settlement yes object Withdrawal object StarkKey signature (including nonce and withdrawal parameters). For details, please refer to the Python SDK.

Response example: json { "status": "OK", "data": 1820796462590083072 }

Response

Parameter Required Type Description

status yes string Can be OK or ERROR.

data yes number Withdrawal ID, assigned by Extended.

Referrals Extended provides a referral program. The following API endpoints allow you to issue referral codes and retrieve your referral statistics. Glossary

Referral – A client who was invited by another client.

Referee – A client who invited another client.

Affiliate – A client who successfully applied to the Affiliate Program.

Subaffiliate – A referral who is also an affiliate, and whose referee is an affiliate as well.

Referred volume – The trading volume of all clients referred by the user (non-transitive).

Rebate – The reward paid to the referee, derived from the trading fees of his referrals.

Rebate rate – The percentage of fees paid by the referral that the referee receives. Rebate = rebate_rate * (trading_fees - rewards_to_other_programs)

Referral schedule – A set of rules (tiers) that determine the rebate rate based on the referred volume.

Shared objects TIER

Parameter Required Type Description

totalVolume yes number Minimum 30 days referred volume for the rebate rate

rebateRate yes number The rebate rate

volumeLimitPerReferral yes number Maximum trading volume eligible for discount per referral

Example: json { "totalVolume": "0", "rebateRate": "0.1", "volumeLimitPerReferral": "0" }

REFERRAL_SCHEDULE

Parameter Required Type Description

tiers yes object[] List

Example: json { "tiers": [ { "totalVolume": "0", "rebateRate": "0.1", "volumeLimitPerReferral": "0" } ] }

REFERRAL_GROUP

A group determining referral program rules

Parameter Required Type Description

id yes number

schedule yes object REFERRAL_SCHEDULE

subaffiliateRate yes number Rebate rate that referee gains from subaffiliate referral rebates

Example: json { "id": 1, "schedule": { "tiers": [ { "totalVolume": "0", "rebateRate": "0.1", "volumeLimitPerReferral": "0" } ] }, "subaffiliateRate": "0.1" }

AFFILIATE Example: json { "clientId": 42, "name": "ABC", "onboarded": 1746784655000, "mainGroup": { "id": 1, "schedule": { "tiers": [ { "totalVolume": "0", "rebateRate": "0.1", "volumeLimitPerReferral": "0" } ] }, "subaffiliateRate": "0" }, "d30ReferredVolume": "2000" }

Response

Parameter Required Type Description

clientId yes number

name yes string

onboarded yes number Unix timestamp

mainGroup yes number Main REFERRAL_GROUP of current user

d30ReferredVolume yes number Maximum volume that referral can trade using his discount

protectionPeriodGroup no number

REFERRAL_GROUP of current user during protection period

protectionPeriodUntil no number Unix timestamp. Upper bound of protection period

PERIOD Enum that determines period for fetching data

Values: text DAY, WEEK, MONTH, YEAR, ALL

GRANULARITY: Enum that determines period for grouping data Values: text DAY, WEEK, MONTH

Get affiliate data GET /api/user/affiliate

If user is an affiliate returns his affiliate data, otherwise returns 404

Response example: json { "clientId": 42, "name": "ABC", "onboarded": 1746784655000, "mainGroup": { "id": 1, "schedule": { "tiers": [ { "totalVolume": "0", "rebateRate": "0.1", "volumeLimitPerReferral": "0" } ] }, "subaffiliateRate": "0" }, "d30ReferredVolume": "2000" }

Response See AFFILIATE

Get referral status GET /api/user/referrals/status

Returns status of referral program for the user

Response example: json { "active": true, "limit": 10000, "tradedVolume": 100 }

Response

Parameter Required Type Description

active yes boolean Is program active for the user. (Is user able to issue codes)

limit yes number Trading volume that user has to achieve to enable program

tradedVolume yes number Current traded volume of user

Get referral links GET /api/user/referrals/links

Returns referral links issued by the user

Response example: json [ { "id": "ABC", "issuedBy": 42, "issuedAt": 1746785907329, "label": "ABC", "isDefault": true, "hiddenAtUi": false, "overallRebates": "50" } ]

Response

Parameter Required Type Description

id yes string Link id

issuedBy yes number Referral client id

issuedAt yes number Unix timestamp. When the link was issued

label yes string User provided label for the link

isDefault yes boolean Is link default for the client

hiddenAtUi yes boolean Is link visible for the client

overallRebates yes number Total Rebates

Get referral dashboard GET /api/user/referrals/dashboard?period={PERIOD}

Returns referral program statistic for the dashboard Request parameters

Parameter Required Type Description

PERIOD yes string The PERIOD of the statistic

Response example:

{ "referralLinkToDirectKeyMetrics": { "ABC": { "rebateEarned": { "current": "200", "previous": "100" }, "totalFeesPaid": { "current": "2000", "previous": "1000" }, "tradingVolume": { "current": "20000", "previous": "10000" }, "activeTraders": { "current": 200, "previous": 100 } } }, "subaffiliateToKeyMetrics": { "2": { "rebateEarned": { "current": "200", "previous": "100" }, "subaffiliateEarnings": { "current": "2500", "previous": "1250" } } }, "activeSubaffiliates": { "current": 1, "previous": 0 }, "affiliates": [ { "clientId": 2, "name": "RUSLAN", "onboarded": 1746792229516, "mainGroup": { "id": 1, "schedule": { "tiers": [ { "totalVolume": "0", "rebateRate": "0.1", "volumeLimitPerReferral": "0" } ] }, "subaffiliateRate": "0" } } ], "users": [ { "firstTradedOn": 1746792228516, "wallet": "0x42...a8a91", "rebate": "100", "tradedVolume": "10000", "totalFees": "1000" } ], "daily": [ { "date": "2025-05-09", "subaffiliates": [ { "id": 2, "rebate": "5", "activeUsers": 2, "referredTradingVolume": "100", "earnings": "10" } ], "links": [ { "link": "ABC", "rebate": "10", "activeUsers": 4, "referredTradingVolume": "200", "referredFees": "20", "referredL30Volume": "2000" } ] }, { "date": "2025-05-08", "subaffiliates": [], "links": [] } ], "weekly": [ { "date": "2025-05-09", "subaffiliates": [], "links": [] }, { "date": "2025-05-02", "subaffiliates": [], "links": [] } ], "monthly": [ { "date": "2025-05-09", "subaffiliates": [], "links": [] }, { "date": "2025-04-11", "subaffiliates": [], "links": [] }, { "date": "2025-04-13", "subaffiliates": [], "links": [] } ] }

Response CurrentToPrevious<T>:

Parameter Required Type Description

current yes object <T> data for current period

previous yes object <T> data for previous period

DirectKeyMetrics:

Parameter Required Type Description

rebateEarned yes object CurrentToPrevious<Number>. Rebates earned during period

totalFeesPaid yes object CurrentToPrevious<Number>. Total amount of fees paid by referrals during period

tradingVolume yes object CurrentToPrevious<Number>. Referred volume during period

activeTraders yes object CurrentToPrevious<Number>. Active traders count during period

SubaffiliateKeyMetrics:

Parameter Required Type Description

rebateEarned yes object CurrentToPrevious<Number>. Rebates earned during period

subaffiliateEarnings yes object CurrentToPrevious<Number>. Total rebates earned by subaffiliates during period

UserStat:

Parameter Required Type Description

firstTradedOn no number Unix timestamp. Time when the client made a first trade

wallet yes string Masked user wallet

referredBy no number Referee of this referral

referralLink no string Referral link code used by referral

rebate yes number Rebate

tradedVolume yes number Traded volume of the referral during period

totalFees yes number Total fees paid by the referral during period

SubaffiliateStat:

Parameter Required Type Description

id yes number Client id

rebate yes number Transitive Rebate earned by client. (Rebate from referrals of his referrals)

activeUsers yes number Count of client active referrals

referredTradingVolume yes number

Referred volume of client

earnings yes number

Rebate of client

LinkStat:

Parameter Required Type Description

link yes string Referral link code

rebate yes number

Rebate earned by link

activeUsers yes number Count of active referrals invited by link

referredTradingVolume yes number

Referred volume by link

referredFees yes number Total fees paid by referrals invited by link

referredL30Volume yes number Last 30 days Referred volume invited by link

AffiliateStat:

Parameter Required Type Description

date yes string Last date of granular period

subaffiliates yes object[] List<SubaffiliateStat> stats of granular period grouped by subaffiliates

links yes object[] List<LinkStat> stats of granular period grouped by links

Response:

Parameter Required Type Description

referralLinkToDirectKeyMetrics yes object Map Metrics aggregated by referral codes

subaffiliateToKeyMetrics yes object Map Metrics aggregated by subaffiliates

activeSubaffiliates yes number Active subaffiliates count

affiliates yes object[] List<Affiliate> Subaffiliates active during period

users yes object[] List<UserStat> User stats active during period

daily yes object[] List<AffiliateStat> Stats during period with granularity 1 day

weekly yes object[] List<AffiliateStat> Stats during period with granularity 1 week

monthly yes object[] List<AffiliateStat> Stats during period with granularity 1 month

Use referral link POST /api/user/referrals/links

Use referral link Request

Request example: json { "code": "ABC" }

Create referral link code POST /api/user/referrals

Create referral link code Request

Request example: json { "id": "ABC", "isDefault": true, "hiddenAtUi": false }

Update referral link code PUT /api/user/referrals

Update referral link code Request

Request example: json { "id": "ABC", "isDefault": true, "hiddenAtUi": false }

Rewards Endpoints related to rewards allow users to retrieve their earned rewards and leaderboard statistics. Get Earned Rewards HTTP Request GET /api/v1/user/rewards/earned

Retrieves the rewards earned by the authenticated client across different seasons and epochs. Authentication This endpoint requires authentication.

Response example:

{ "status": "OK", "data": [ { "seasonId": 1, "epochRewards": [ { "epochId": 1, "startDate": "2023-01-01T00:00:00Z", "endDate": "2023-01-31T23:59:59Z", "pointsReward": "50.25" } ] } ] }

Response

Parameter Type Description

data[].seasonId number The ID of the reward season.

data[].epochRewards array List of rewards earned in each epoch.

data[].epochRewards.epochId number The ID of the epoch.

data[].epochRewards.startDate string The start date of the epoch (ISO format).

data[].epochRewards.endDate string The end date of the epoch (ISO format).

data[].epochRewards.pointsReward string The number of points earned in the epoch.

Get Reward Leaderboard Stats HTTP Request GET /api/v1/user/rewards/leaderboard/stats

Retrieves the leaderboard statistics for the authenticated client, including total points, rank, and reward leagues. Authentication This endpoint requires authentication.

Response example:

{ "status": "OK", "data": { "totalPoints": "1250.75", "rank": 42, "tradingRewardLeague": "QUEEN", "liquidityRewardLeague": "PAWN", "referralRewardLeague": "KING" } }

Response

Parameter Type Description

totalPoints string The total number of points earned.

rank number The client's rank on the leaderboard.

tradingRewardLeague string The client's league for trading rewards.

liquidityRewardLeague string The client's league for liquidity rewards.

referralRewardLeague string The client's league for referral rewards.

Reward League Values The following table describes the possible values for the reward league fields (tradingRewardLeague, liquidityRewardLeague, referralRewardLeague):

Value Description

KING King league - highest rewards tier.

QUEEN Queen league - second highest tier.

ROOK Rook league - advanced rewards tier.

KNIGHT Knight league - intermediate rewards tier.

PAWN Pawn league - entry level rewards tier.

Public WebSocket streams Extended offers a WebSocket API for streaming updates.

Connect to the WebSocket streams using wss://api.extended.exchange as the host.

The server sends pings every 15 seconds and expects a pong response within 10 seconds. Although the server does not require pings from the client, it will respond with a pong if one is received. Order book stream HTTP Request GET /stream.extended.exchange/v1/orderbooks/{market}

Subscribe to the orderbooks stream for a specific market or for all available markets. If the market parameter is not submitted, the stream will include data for all available markets.

In the current version we support the following depth specifications:

Full orderbook. Push frequency: 100ms. The initial response from the stream will be a snapshot of the order book. Subsequent snapshot updates will occur every minute, while updates between snapshots are delivered in delta format, reflecting only changes since the last update. Best Bid & Ask updates are always provided as snapshots. Best bid & ask. Push frequency: real-time. To subscribe for Best bid & ask use GET /stream.extended.exchange/v1/orderbooks/{market}?depth=1. Best bid & ask updates are always snapshots.

URL Parameters

Parameter Required Type Description

market no string Select an individual market. If not specified, the subscription includes all markets.

Query Parameters

Parameter Required Type Description

depth no string Specify '1' to receive updates for best bid & ask only.

Response example:

{ "ts": 1701563440000, "type": "SNAPSHOT", "data": { "m": "BTC-USD", "b": [ { "p": "25670", "q": "0.1" } ], "a": [ { "p": "25770", "q": "0.1" } ] }, "seq": 1 }

Response

Parameter Type Description

type string Type of message. Can be SNAPSHOT or DELTA.

ts number Timestamp (in epoch milliseconds) when the system generated the data.

data.m string Market name.

data.t string Type of message. Can be SNAPSHOT or DELTA.

data.b object[] List of bid orders. For a snapshot, bids are sorted by price in descending order.

data.b[].p string Bid price.

data.b[].q string Bid size. For a snapshot, this represents the absolute size; for a delta, the change in size.

data.a object[] List of ask orders. For a snapshot, asks are sorted by price in ascending order.

data.a[].p string Ask price.

data.a[].q string Ask size. For a snapshot, this represents the absolute size; for a delta, the change in size.

seq number Monothonic sequence number. '1' corresponds to the first snapshot, and all subsequent numbers correspond to deltas. If a client receives a sequence out of order, it should reconnect.

Trades stream HTTP Request GET /stream.extended.exchange/v1/publicTrades/{market}

Subscribe to the trades stream for a specific market or for all available markets. If the market parameter is not submitted, the stream will include data for all available markets.

Historical trades data is currently available only for an authorised account through the Private REST-API. URL Parameters

Parameter Required Type Description

market no string Select an individual market. If not specified, the subscription includes all markets.

Response example:

{ "ts": 1701563440000, "data": [ { "m": "BTC-USD", "S": "BUY", "tT": "TRADE", "T": 1701563440000, "p": "25670", "q": "0.1", "i": 25124 } ], "seq": 2 }

Response

Parameter Type Description

ts number Timestamp (in epoch milliseconds) when the system generated the data.

data[].m string Market name.

data[].S string Side of taker trades. Can be BUY or SELL.

data[].tT string Trade type. Can be TRADE, LIQUIDATION or DELEVERAGE.

data[].T number Timestamp (in epoch milliseconds) when the trade happened.

data[].p string Trade price.

data[].q string Trade quantity in base asset.

data[].i number Trade ID.

seq number Monotonic sequence: Since there are no deltas, clients can skip trades that arrive out of sequence.

Funding rates stream HTTP Request GET /stream.extended.exchange/v1/funding/{market}

Subscribe to the funding rates stream for a specific market or for all available markets. If the market parameter is not submitted, the stream will include data for all available markets.

For historical funding rates data, use the Get funding rates history endpoint.

While the funding rate is calculated every minute, it is applied only once per hour. The records include only those funding rates that were used for funding fee payments. URL Parameters

Parameter Required Type Description

market no string Select an individual market. If not specified, the subscription includes all markets.

Response example:

{ "ts": 1701563440000, "data": { "m": "BTC-USD", "T": 1701563440000, "f": "0.001" }, "seq": 2 }

Response

Parameter Type Description

ts number Timestamp (in epoch milliseconds) when the system generated the data.

data[].m string Market name.

data[].T number Timestamp (in epoch milliseconds) when the funding rate was calculated and applied.

data[].f string Funding rates that were applied for funding fee payments.

seq number Monotonic sequence: Since there are no deltas, clients can skip funding rates that arrive out of sequence.

Candles stream HTTP Request GET /stream.extended.exchange/v1/candles/{market}/{candleType}?interval={interval}

Subscribe to the candles stream for a specific market.

The interval parameter should be specified in the ISO 8601 duration format. Available intervals include:

P30D (Calendar month) P7D (Calendar week) PT24H PT12H PT8H PT4H PT2H PT1H PT30M PT15M PT5M PT1M

Trades price response example:

{ "ts": 1695738675123, "data": [ { "T": 1695738674000, "o": "1000.0000", "l": "800.0000", "h": "2400.0000", "c": "2100.0000", "v": "10.0000" } ], "seq": 1 }

Mark and Index price response example:

{ "ts": 1695738675123, "data": [ { "T": 1695738674000, "o": "1000.0000", "l": "800.0000", "h": "2400.0000", "c": "2100.0000" } ], "seq": 1 }

Available price types include:

Trades price: GET /stream.extended.exchange/v1/candles/{market}/trades?interval=PT1M Mark price: GET /stream.extended.exchange/v1/candles/{market}/mark-prices?interval=PT1M Index price: GET /stream.extended.exchange/v1/candles/{market}/index-prices?interval=PT1M

Push frequency: 1-10s. URL Parameters

Parameter Required Type Description

market yes string Select an individual market.

candleType yes string Price type. Can be trades, mark-prices or index-prices.

Query Parameters

Parameter Required Type Description

interval yes string Duration of candle (duration in ISO 8601).

Response

Parameter Type Description

ts number Timestamp (in epoch milliseconds) when the system generated the data.

data[].T number Starting timestamp (in epoch milliseconds) of the candle.

data[].o string Open price.

data[].c string Close price.

data[].h string Highest price.

data[].l string Lowest price.

data[].v string Trading volume (only for trade candles).

seq number Monothonic sequence number. '1' corresponds to the first snapshot, and all subsequent numbers correspond to deltas. If a client receives a sequence out of order, it should reconnect.

Mark price stream HTTP Request GET /stream.extended.exchange/v1/prices/mark/{market}

Subscribe to the mark price stream for a specific market or for all available markets. If the market parameter is not submitted, the stream will include data for all available markets.

Mark prices are used for calculating unrealized PnL and as a reference for liquidation processes. The stream provides real-time updates whenever mark prices change. URL Parameters

Parameter Required Type Description

market no string Select an individual market. If not specified, the subscription includes all markets.

Response example:

{ "type": "MP", "data": { "m": "BTC-USD", "p": "25670", "ts": 1701563440000 }, "ts": 1701563440000, "seq": 1, "sourceEventId": null }

Response

Parameter Type Description

type string Type identifier for mark price stream ("MP").

data.m string Market name.

data.p string Mark price value.

data.ts number Timestamp (in epoch milliseconds) when the price was calculated.

ts number Timestamp (in epoch milliseconds) when the system generated the data.

seq number Monotonic sequence number. Clients can use this to ensure they process messages in the correct order. If a client receives a sequence out of order, it should reconnect.

sourceEventId number ID of the source event that triggered this update (null for regular updates).

Index price stream HTTP Request GET /stream.extended.exchange/v1/prices/index/{market}

Subscribe to the index price stream for a specific market or for all available markets. If the market parameter is not submitted, the stream will include data for all available markets.

Index prices represent the underlying market price derived from various external sources. These prices are used as a reference for funding rate calculations and other platform mechanisms. URL Parameters

Parameter Required Type Description

market no string Select an individual market. If not specified, the subscription includes all markets.

Response example:

{ "type": "IP", "data": { "m": "BTC-USD", "p": "25680", "ts": 1701563440000 }, "ts": 1701563440000, "seq": 1, "sourceEventId": null }

Response

Parameter Type Description

type string Type identifier for index price stream ("IP").

data.m string Market name.

data.p string Index price value.

data.ts number Timestamp (in epoch milliseconds) when the price was calculated.

ts number Timestamp (in epoch milliseconds) when the system generated the data.

seq number Monotonic sequence number. Clients can use this to ensure they process messages in the correct order. If a client receives a sequence out of order, it should reconnect.

sourceEventId number ID of the source event that triggered this update (null for regular updates).

Private WebSocket streams Connect to the WebSocket streams using ws://api.extended.exchange as the host.

The server sends pings every 15 seconds and expects a pong response within 10 seconds. Although the server does not require pings from clients, it will respond with a pong if it receives one. Account updates stream HTTP Request GET /stream.extended.exchange/v1/account

Orders updates response example:

{ "type": "ORDER", "data": { "orders": [ { "id": 1791181340771614723, "accountId": 1791181340771614721, "externalId": "-1771812132822291885", "market": "BTC-USD", "type": "LIMIT", "side": "BUY", "status": "NEW", "price": "12400.000000", "averagePrice": "13140.000000", "qty": "10.000000", "filledQty": "3.513000", "payedFee": "0.513000", "trigger": { "triggerPrice": "1220.00000", "triggerPriceType": "LAST", "direction": "UP", "executionPriceType": "LIMIT" }, "tpSlType": "ORDER", "takeProfit": { "triggerPrice": "1.00000", "triggerPriceType": "LAST", "price": "1.00000", "priceType": "LIMIT" }, "stopLoss": { "triggerPrice": "1.00000", "triggerPriceType": "LAST", "price": "1.00000", "priceType": "LIMIT" }, "reduceOnly": true, "postOnly": false, "createdTime": 1715885888571, "updatedTime": 1715885888571, "expireTime": 1715885888571 } ] }, "ts": 1715885884837, "seq": 1 }

Trades updates response example:

{ "type": "TRADE", "data": { "trades": [ { "id": 1784963886257016832, "accountId": 3017, "market": "BTC-USD", "orderId": 9223372036854775808, "externalOrderId": "ext-1", "side": "BUY", "price": "58853.4000000000000000", "qty": "0.0900000000000000", "value": "5296.8060000000000000", "fee": "0.0000000000000000", "tradeType": "DELEVERAGE", "createdTime": 1701563440000, "isTaker": true } ] }, "ts": 1715885884837, "seq": 1 }

Account balance updates response example:

{ "type": "BALANCE", "data": { "balance": { "collateralName": "BTC", "balance": "100.000000", "equity": "20.000000", "availableForTrade": "3.000000", "availableForWithdrawal": "4.000000", "unrealisedPnl": "1.000000", "initialMargin": "0.140000", "marginRatio": "1.500000", "updatedTime": 1699976104901, "exposure": "12751.859629", "leverage": "1275.1860" } }, "ts": 1715885952304, "seq": 1 }

Positions updates response example:

{ "type": "POSITION", "data": { "positions": [ { "id": 1791183357858545669, "accountId": 1791183357858545665, "market": "BTC-USD", "side": "SHORT", "leverage": "5.0", "size": "0.3", "value": "12751.8596295830", "openPrice": "42508.00", "markPrice": "42506.1987652769", "liquidationPrice": "75816.37", "margin": "637.59", "unrealisedPnl": "100.000000", "realisedPnl": "200.000000", "tpTriggerPrice": "1600.0000", "tpLimitPrice": "1500.0000", "slTriggerPrice": "1300.0000", "slLimitPrice": "1250.0000", "adl": 1, "createdAt": 1715886365748, "updatedAt": 1715886365748 } ] }, "ts": 1715886365748, "seq": 1 }

Subscribe to the account updates stream.

The initial responses will include comprehensive information about the account, including balance, open positions, and open orders, i.e. everything from GET /v1/user/balance, GET /v1/user/positions, GET /v1/user/orders.

Subsequent responses will contain all updates related to open orders, trades, account balance or open positions in a single message.

The response attributes will align with the responses from the corresponding REST API endpoints: Get trades, Get positions, Get open orders and Get balance. Refer to the Account section for details. Error responses Unless specified otherwise for a particular endpoint and HTTP status code, the error response model follows the general response format and includes an error code along with a descriptive message for most errors.

Error code Error Description

GENERAL

400 BadRequest Invalid or missing parameters.

401 Unauthorized Authentication failure.

403 Forbidden Access denied.

404 NotFound Resource not found.

422 UnprocessableEntity Request format is correct, but data is invalid.

500 InternalServerError Internal server error.

MARKET, ASSET & ACCOUNT

1000 AssetNotFound Asset not found.

1001 MarketNotFound Market not found.

1002 MarketDisabled Market is disabled.

1003 MarketGroupNotFound Market group not found.

1004 AccountNotFound Account not found.

1005 NotSupportedInterval Not supported interval.

1006 UnhandledError Application error.

1008 ClientNotFound Client not found.

1009 ActionNotAllowed Action is not allowed.

1010 MaintenanceMode Maintenance mode.

1011 PostOnlyMode Post only mode.

1012 ReduceOnlyMode Reduce only mode.

1013 InvalidPercentage Percentage should be between 0 and 1.

1014 MarketReduceOnly Market is in reduce only mode, non-reduce only orders are not allowed.

LEVERAGE UPDATE

1049 InvalidLeverageBelowMinLeverage Leverage below min leverage.

1050 InvalidLeverageExceedsMaxLeverage Leverage exceeds max leverage.

10501 InvalidLeverageMaxPositionValueExceeded Max position value exceeded for new leverage.

1052 InvalidLeverageInsufficientMargin Insufficient margin for new leverage.

1053 InvalidLeverageInvalidPrecision Leverage has invalid precision.

STARKEX SIGNATURES

1100 InvalidStarkExPublicKey Invalid StarkEx public key.

1101 InvalidStarkExSignature Invalid StarkEx signature.

1102 InvalidStarkExVault Invalid StarkEx vault.

ORDER

1120 OrderQtyLessThanMinTradeSize Order quantity less than min trade size, based on market-specific trading rules.

1121 InvalidQtyWrongSizeIncrement Invalid quantity due to the wrong size increment, based on market-specific Minimum Change in Trade Size trading rule.

1122 OrderValueExceedsMaxOrderValue Order value exceeds max order value, based on market-specific trading rules.

1123 InvalidQtyPrecision Invalid quantity precision, currently equals to market-specific Minimum Change in Trade Size.

1124 InvalidPriceWrongPriceMovement Invalid price due to wrong price movement, based on market-specific Minimum Price Change trading rule.

1125 InvalidPricePrecision Invalid price precision, currently equals to market-specific Minimum Price Change.

1126 MaxOpenOrdersNumberExceeded Max open orders number exceeded, currently 200 orders per market.

1127 MaxPositionValueExceeded Max position value exceeded, based on the Margin schedule.

1128 InvalidTradingFees Trading fees are invalid. Refer to Order management section for details.

1129 InvalidPositionTpslQty Invalid quantity for position TP/SL.

1130 MissingOrderPrice Order price is missing.

1131 MissingTpslTrigger TP/SL order trigger is missing.

1132 NotAllowedOrderType Order type is not allowed.

1133 InvalidOrderParameters Invalid order parameters.

1134 DuplicateOrder Duplicate Order.

1135 InvalidOrderExpiration Order expiration date must be within 90 days for the Mainnet, 28 days for the Testnet.

1136 ReduceOnlyOrderSizeExceedsPositionSize Reduce-only order size exceeds open position size.

1137 ReduceOnlyOrderPositionIsMissing Position is missing for a reduce-only order.

1138 ReduceOnlyOrderPositionSameSide Position is the same side as a reduce-only order.

1139 MarketOrderMustBeIOC Market order must have time in force IOC.

1140 OrderCostExceedsBalance New order cost exceeds available balance.

1141 InvalidPriceAmount Invalid price value.

1142 EditOrderNotFound Edit order not found.

1143 MissingConditionalTrigger Conditional order trigger is missing.

1144 PostOnlyCantBeOnConditionalMarketOrder Conditional market order can't be Post-only.

1145 NonReduceOnlyOrdersNotAllowed Non reduce-only orders are not allowed.

1146 TwapOrderMustBeGTT Twap order must have time in force GTT.

1147 OpenLossExceedsEquity Open loss exceeds equity.

1148 TPSLOpenLossExceedsEquity TP/SL open loss exceeds equity.

GENERAL ACCOUNT

1500 AccountNotSelected Account not selected.

WITHDRAWAL

1600 WithdrawalAmountMustBePositive Withdrawal amount must be positive.

1601 WithdrawalDescriptionToLong Withdrawal description is too long.

1602 WithdrawalRequestDoesNotMatchSettlement Withdrawal request does not match settlement.

1603 WithdrawalEthAddressIsNotValid Withdrawal eth address is not valid.

1604 WithdrawalExpirationTimeIsTooSoon Withdrawal expiration time is too soon.

1605 WithdrawalInvalidAsset Withdrawal asset is not valid.

1606 WithdrawalEthAddressMustBeAttachedToClient Withdrawal eth address must be attached to client.

1607 WithdrawalBlockedForAccount Withdrawal blocked for the account.

1608 WithdrawalAccountDoesNotBelongToUser Withdrawal account does not belong to user.

1609 WithdrawalDisabled Withdrawal disabled at system.

1610 WithdrawalTransferFeeIsTooLow Withdrawal transfer fee is too low.

1611 WithdrawalStarkexTransferInvalidAmount Withdrawal starkex transfer invalid amount.

1612 WithdrawalStarkexTransferInvalidExpirationTime Withdrawal starkex transfer invalid expiration time.

1613 WithdrawalStarkexTransferInvalidReceiverPositionId Withdrawal starkex transfer invalid receiver position id.

1614 WithdrawalStarkexTransferInvalidReceiverPublicKey Withdrawal Starkex Transfer Invalid Receiver Public Key.

1615 WithdrawalStarkexTransferInvalidSenderPositionId Withdrawal starkex transfer invalid sender position id.

1616 WithdrawalStarkexTransferInvalidSenderPublicKey Withdrawal starkex transfer invalid sender public key.

1617 WithdrawalStarkexTransferInvalidSignature Withdrawal starkex transfer invalid signature.

1618 WithdrawalDailyLimitExceed Withdrawal daily limit exceed.

1619 WithdrawalRejectedTransfer Withdrawal connected transfer rejected.

1620 WithdrawalFailedRiskControls Withdrawal failed risk controls.

1621 WithdrawalIsNotAllowed Withdrawal is not allowed.

1622 WithdrawalIsNotAllowedForInstitutionalClient Withdrawal is not allowed for institutional client.

TRANSFERS

1650 InvalidVaultTransferAmount Vault transfer amount is incorrect.

REFERRAL CODE

1700 ReferralCodeAlreadyExist Referral code already exist.

1701 ReferralCodeInvalid Referral code is not valid.

1703 ReferralProgramIsNotEnabled Referral program is not enabled.

1704 ReferralCodeAlreadyApplied Referral code already applied.

json