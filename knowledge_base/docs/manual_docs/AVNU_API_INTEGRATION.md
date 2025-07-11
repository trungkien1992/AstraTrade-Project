# AVNU API Integration Guide

## 📋 Overview

This document provides comprehensive integration details for AVNU's gasless transaction API based on available documentation and our StreetCred implementation.

## 🔗 API Base URLs

```
Production: https://starknet.api.avnu.fi
Testnet: https://starknet-sepolia.api.avnu.fi  
Swagger UI: https://starknet.api.avnu.fi/swagger-ui/index.html#/
Documentation: https://doc.avnu.fi
```

## 🔐 Authentication

### API Key Requirements
- **Sponsors (dApps)**: Require API key from AVNU admins
- **Users**: No API key needed for basic gasless transactions
- **Rate Limiting**: Implemented (exact limits not specified)

### Account Compatibility
- **Supported Wallets**: ArgentX, Braavos
- **Class Hashes**: Specific class hashes whitelisted
- **Compatibility Check**: Use compatibility endpoint before transactions

## 📊 Core API Endpoints

### 1. Gasless Transaction Endpoints

#### Check Account Compatibility
```http
GET /api/v1/gasless/compatibility/{account_address}
```

**Response:**
```json
{
  "compatible": true,
  "class_hash": "0x...",
  "supported_features": ["gasless", "paymaster"]
}
```

#### Prepare Gasless Transaction
```http
POST /api/v1/gasless/prepare
```

**Request:**
```json
{
  "account_address": "0x...",
  "calls": [
    {
      "contract_address": "0x...",
      "entry_point_selector": "0x...",
      "calldata": ["0x..."]
    }
  ],
  "max_fee": "0x...",
  "nonce": "0x..."
}
```

**Response:**
```json
{
  "typed_data": {
    "types": {...},
    "primary_type": "Transaction",
    "domain": {...},
    "message": {...}
  },
  "transaction_hash": "0x...",
  "max_fee": "0x..."
}
```

#### Execute Gasless Transaction
```http
POST /api/v1/gasless/execute
```

**Request:**
```json
{
  "account_address": "0x...",
  "typed_data": {...},
  "signature": ["0x...", "0x..."],
  "sponsor_id": "optional_sponsor_id"
}
```

**Response:**
```json
{
  "transaction_hash": "0x...",
  "status": "RECEIVED",
  "gas_fee_paid_by": "sponsor",
  "estimated_fee": "0x..."
}
```

### 2. Sponsor Management Endpoints

#### Add Credits (Sponsor Only)
```http
POST /api/v1/sponsor/credits
```

**Request:**
```json
{
  "amount": "1000000000000000000",
  "token": "ETH"
}
```

#### Set Account Rewards
```http
POST /api/v1/sponsor/rewards
```

**Request:**
```json
{
  "account_address": "0x...",
  "daily_limit": "100000000000000000",
  "monthly_limit": "1000000000000000000"
}
```

#### Get Sponsor Activity
```http
GET /api/v1/sponsor/activity
```

**Response:**
```json
{
  "total_sponsored": "5000000000000000000",
  "transactions_count": 150,
  "daily_spent": "50000000000000000",
  "remaining_credits": "995000000000000000"
}
```

### 3. Gas Token Price Endpoints

#### Get Gas Token Prices
```http
GET /api/v1/gasless/prices
```

**Response:**
```json
{
  "ETH": {
    "price_usd": "2500.50",
    "gas_price_wei": "1000000000"
  },
  "STRK": {
    "price_usd": "1.25",
    "gas_price_wei": "500000000"
  },
  "USDC": {
    "price_usd": "1.00",
    "exchange_rate_eth": "0.0004"
  }
}
```

### 4. Market Data Endpoints

#### Get Markets
```http
GET /api/v1/markets
```

**Response:**
```json
[
  {
    "base_token": "ETH",
    "quote_token": "USDC",
    "price": "2500.50",
    "volume_24h": "1500000.00"
  }
]
```

## 🛠️ SDK Integration

### TypeScript SDK
```bash
npm install @avnu/avnu-sdk
npm install @avnu/gasless-sdk
```

### Basic Usage
```typescript
import { fetchQuotes, executeSwap } from '@avnu/avnu-sdk';
import { prepareGaslessTransaction, executeGaslessTransaction } from '@avnu/gasless-sdk';

// Regular swap with gas
const quotes = await fetchQuotes({
  sellTokenAddress: ethAddress,
  buyTokenAddress: usdcAddress,
  sellAmount: '1000000000000000000',
  takerAddress: account.address
});

await executeSwap(account, quotes[0]);

// Gasless transaction
const gaslessPrep = await prepareGaslessTransaction({
  account: account.address,
  calls: swapCalls,
  maxFee: quotes[0].gasless_max_fee
});

const signature = await account.signTypedData(gaslessPrep.typed_data);

const result = await executeGaslessTransaction({
  ...gaslessPrep,
  signature: signature
});
```

### Dart/Flutter Integration
```dart
dependencies:
  avnu_provider: ^latest_version
```

```dart
import 'package:avnu_provider/avnu_provider.dart';

final avnuProvider = AvnuPaymasterProvider(
  baseUrl: 'https://starknet.api.avnu.fi',
  apiKey: 'your_api_key', // For sponsors only
);

// Check compatibility
final compatible = await avnuProvider.checkCompatibility(userAddress);

// Prepare gasless transaction
final prepared = await avnuProvider.prepareGaslessTransaction(
  accountAddress: userAddress,
  calls: tradeCalls,
  maxFee: estimatedFee,
);

// Execute with signature
final result = await avnuProvider.executeGaslessTransaction(
  prepared: prepared,
  signature: userSignature,
);
```

## 🔒 Security Considerations

### Signature Validation
- Use EIP-712 typed data signing
- Validate all transaction parameters
- Implement nonce management
- Check signature format compliance

### Rate Limiting
- Implement client-side rate limiting
- Handle 429 responses gracefully
- Use exponential backoff for retries

### Error Handling
```typescript
try {
  const result = await executeGaslessTransaction(params);
} catch (error) {
  switch (error.code) {
    case 'INSUFFICIENT_CREDITS':
      // Handle sponsor credit exhaustion
      break;
    case 'INCOMPATIBLE_ACCOUNT':
      // Handle unsupported wallet
      break;
    case 'RATE_LIMITED':
      // Implement backoff strategy
      break;
    default:
      // Handle unexpected errors
  }
}
```

## 📊 Response Formats

### Success Response
```json
{
  "success": true,
  "data": {...},
  "timestamp": "2025-01-08T12:00:00Z"
}
```

### Error Response
```json
{
  "success": false,
  "error": {
    "code": "INVALID_SIGNATURE",
    "message": "Transaction signature validation failed",
    "details": {...}
  },
  "timestamp": "2025-01-08T12:00:00Z"
}
```

## 🧪 Testing

### Testnet Configuration
```typescript
const testnetConfig = {
  baseUrl: 'https://starknet-sepolia.api.avnu.fi',
  chainId: 'SN_SEPOLIA',
  apiKey: process.env.AVNU_TESTNET_API_KEY
};
```

### Mock Responses
```typescript
// For development/testing
const mockGaslessResponse = {
  transaction_hash: '0x123...',
  status: 'RECEIVED',
  gas_fee_paid_by: 'sponsor',
  estimated_fee: '0x5af3107a4000'
};
```

## 🚀 Best Practices

### 1. Transaction Preparation
- Always validate account compatibility first
- Check sponsor credits before transaction
- Implement proper nonce management
- Use appropriate max_fee estimation

### 2. User Experience
- Show gasless status in UI
- Display sponsor information
- Provide fallback to regular transactions
- Implement loading states and error feedback

### 3. Performance
- Cache compatibility checks
- Batch multiple transactions when possible
- Implement connection pooling
- Use async/await patterns

### 4. Monitoring
- Track gasless transaction success rates
- Monitor sponsor credit usage
- Log transaction hashes for debugging
- Implement health checks

## 📈 Integration Metrics

### Success Metrics
- Gasless transaction completion rate
- Average transaction confirmation time
- User adoption of gasless features
- Sponsor credit utilization

### Error Monitoring
- Transaction failure rates by error type
- API response time tracking
- Rate limiting occurrences
- Account compatibility issues

---

**Last Updated**: 2025-01-08  
**API Version**: v1  
**Status**: Active Integration  
**Support**: [AVNU Documentation](https://doc.avnu.fi)

> **Note**: This documentation is based on available AVNU resources and our implementation experience. For the most current API specifications, refer to the official [AVNU Swagger documentation](https://starknet.api.avnu.fi/swagger-ui/index.html#/).