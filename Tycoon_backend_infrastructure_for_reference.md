# Backend Infrastructure Overview for Perp Tycoon

This document provides a comprehensive overview of the backend infrastructure for the Perp Tycoon project, based on the project's documentation and file structure.

## 1. High-Level Architecture

The backend is not a single monolithic application but a collection of services and smart contracts that work together to support the Flutter frontend. The main components are:

-   **Python Trading Service**: A microservice that handles real-world trading operations.
-   **Starknet Smart Contracts**: On-chain programs that manage game logic like experience points (XP), NFTs, and gasless transactions.
-   **Deployment Scripts**: Automation for compiling and deploying smart contracts.
-   **RAG Knowledge Base Backend**: A development support tool that provides contextual information to developers.
-   **External APIs**: Third-party services for trading and gas sponsorship.

```
┌───────────────────┐      ┌──────────────────────────┐
│ Flutter Frontend  │◄─────► Python Trading Service │
└───────────────────┘      │ (FastAPI)                │
       ▲                   └──────────────────────────┘
       │                                ▲
       │                                │
┌───────────────────┐      ┌──────────────────────────┐
│ Starknet Contracts│      │  Extended Exchange API   │
│ (Cairo)           │      │  (3rd Party)             │
└───────────────────┘      └──────────────────────────┘
       ▲
       │
┌───────────────────┐
│ AVNU Paymaster    │
│ (3rd Party)       │
└───────────────────┘
```

## 2. Python Trading Service

This service acts as the bridge between the game and a real-world trading exchange.

-   **Purpose**: To execute the "one real trade per day" feature. It receives requests from the Flutter app, formats them for the external exchange, and manages the trade execution.
-   **Location**: `/Users/admin/tycoon-project/python_trading_service/`
-   **Framework**: FastAPI

### Implementation Details

-   **`/Users/admin/tycoon-project/python_trading_service/main.py`**: The main FastAPI server entry point. It defines endpoints for getting market data, checking account balances, and creating orders. It integrates the StarkEx signature logic before sending requests to the Extended Exchange.
-   **`/Users/admin/tycoon-project/python_trading_service/extended_exchange_format.py`**: A key utility script that precisely replicates the message hashing and signing algorithm required by the Extended Exchange API. This ensures that all trading requests from the service are valid and secure.
-   **`/Users/admin/tycoon-project/python_trading_service/starkex_crypto.py`**: Handles the core cryptographic operations for generating StarkEx-compatible signatures, which is a critical component for authenticating with the exchange.

## 3. Starknet Smart Contracts

The on-chain backbone of the game's reward and progression system.

-   **Purpose**: To provide a decentralized, transparent, and secure way to manage player achievements and assets.
-   **Location**: `/Users/admin/tycoon-project/contracts/`
-   **Platform**: Starknet
-   **Language**: Cairo (indicated by `Scarb.toml` files)

### Implementation Details

The core logic for each contract is defined in a `.cairo` file, which is then included as a module in the `lib.cairo` entry point for each contract package.

-   **XP System**:
    -   **Path**: `/Users/admin/tycoon-project/contracts/streetcred_xp/src/lib.cairo`
    -   **Description**: Manages player XP on-chain. The logic, likely in `xp_system.cairo`, handles adding XP and tracking leaderboards.
-   **Achievement NFTs**:
    -   **Path**: `/Users/admin/tycoon-project/contracts/street_art_nft/src/lib.cairo`
    -   **Description**: Mints NFTs to reward players for in-game achievements. The implementation in `street_art.cairo` defines the NFT's properties and minting rules.
-   **Paymaster**:
    -   **Path**: `/Users/admin/tycoon-project/contracts/streetcred_paymaster/src/lib.cairo`
    -   **Description**: Implements a paymaster to sponsor transaction fees (gas). The logic in `avnu_paymaster.cairo` integrates with the AVNU service to provide a seamless, gas-free experience for the player.

## 4. Deployment Infrastructure

This component contains the scripts necessary to compile and deploy the Starknet smart contracts.

-   **Purpose**: To automate the deployment process, ensuring consistency and reducing manual error.
-   **Location**: `/Users/admin/tycoon-project/scripts/deployment/`

### Implementation Details

-   **`/Users/admin/tycoon-project/scripts/deployment/real_deploy_contracts.py`**: A comprehensive Python script that orchestrates the entire deployment workflow. Its responsibilities include:
    -   Compiling the Cairo contracts using `scarb`.
    -   Declaring and deploying the contracts to a specified Starknet network (e.g., Sepolia, Mainnet).
    -   Configuring the necessary permissions between the deployed contracts (e.g., authorizing the XP contract to mint NFTs).
    -   Generating a Dart configuration file (`lib/config/real_contract_config.dart`) containing the live contract addresses for use in the Flutter application.

## 5. RAG Knowledge Base Backend

This is a supporting service for the development team, not a user-facing production service.

-   **Purpose**: To provide a Retrieval-Augmented Generation (RAG) system. It allows developers to ask natural language questions about the codebase and documentation and receive intelligent, context-aware answers.
-   **Location**: `/Users/admin/tycoon-project/knowledge_base/backend/`
-   **Framework**: FastAPI
-   **Database**: ChromaDB (a vector database for semantic search)
-   **Key Files**:
    -   `main.py`: The FastAPI server for the RAG service.
    -   `claude_search.py`: Implements the search logic, likely optimized for a specific LLM (Claude).
    -   `code_aware_chunker.py`: A script to intelligently parse and chunk code files for better indexing and retrieval.
-   **Functionality**: It indexes the entire project (code and docs) and exposes a search endpoint (e.g., `http://localhost:8000/search/claude`) for developer queries.

## 6. External Service Integrations

The project relies on key third-party services to function.

-   **Extended Exchange API**: This is the external trading platform where real trades are executed. The Python Trading Service is the client for this API. The project requires an `EXTENDED_API_KEY` and `EXTENDED_VAULT_ID` to connect to it.
-   **AVNU Paymaster**: This service is used in conjunction with the `streetcred_paymaster` contract to sponsor gas fees on Starknet, enabling the gasless transaction feature.

## Summary of Technologies

-   **Programming Languages**: Python (for backend services), Cairo (for smart contracts)
-   **Frameworks**: FastAPI (for backend services)
-   **Blockchain**: Starknet
-   **Database**: ChromaDB (for the RAG system)
-   **Deployment**: Docker, Vercel, Firebase, Custom Python Scripts
