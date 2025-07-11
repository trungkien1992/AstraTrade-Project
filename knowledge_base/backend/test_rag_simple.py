#!/usr/bin/env python3
"""
Simplified Multi-Platform RAG System Testing
Direct testing of core RAG components without FastAPI dependencies
"""

import asyncio
import json
import logging
import time
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from pathlib import Path
import statistics
import sys
import os

# Add current directory to Python path
sys.path.insert(0, '/Users/admin/AstraTrade-Project/knowledge_base/backend')

# Import core components directly
from categorization_system import AstraTradeCategorizer, DocumentCategory, PlatformType
from optimization_manager import RAGOptimizationManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class TestResult:
    """Test result for RAG system testing"""
    query: str
    platform: str
    category: str
    confidence: float
    keywords: List[str]
    importance: str
    doc_type: str
    tags: List[str]
    success: bool
    error: Optional[str] = None

class SimpleRAGTester:
    """Simplified testing suite for RAG components"""
    
    def __init__(self):
        self.categorizer = AstraTradeCategorizer()
        self.optimizer = RAGOptimizationManager()
        self.test_results: List[TestResult] = []
        
        # Test queries for each platform
        self.test_queries = {
            "extended_exchange": [
                "How to place a buy order using Extended Exchange API?",
                "What are the authentication requirements for Extended Exchange?",
                "How to get real-time market data from Extended Exchange?",
                "Extended Exchange order book depth API documentation",
                "How to cancel orders on Extended Exchange?"
            ],
            "x10_python_sdk": [
                "How to install X10 Python SDK?",
                "Python example for placing trades with X10 SDK",
                "X10 Python SDK authentication setup",
                "How to get account balance using X10 Python?",
                "X10 SDK async trading client implementation"
            ],
            "starknet_dart": [
                "How to connect to Starknet using Dart SDK?",
                "Starknet.dart wallet integration example",
                "How to invoke smart contracts with Starknet Dart?",
                "Flutter app with Starknet.dart setup guide",
                "Starknet Dart account management"
            ],
            "cairo_lang": [
                "How to write ERC-20 token in Cairo?",
                "Cairo smart contract deployment guide",
                "Cairo felt252 data type usage",
                "Cairo contract storage and events",
                "Cairo testing and debugging best practices"
            ],
            "avnu_paymaster": [
                "How to implement AVNU paymaster for gasless transactions?",
                "AVNU paymaster integration with Starknet",
                "Gas sponsorship setup using AVNU",
                "AVNU paymaster fee calculation",
                "Account abstraction with AVNU paymaster"
            ],
            "web3auth": [
                "How to integrate Web3Auth for social login?",
                "Web3Auth multi-factor authentication setup",
                "Web3Auth private key management",
                "Web3Auth wallet connection flow",
                "Web3Auth custom authentication providers"
            ],
            "chipi_pay": [
                "How to integrate ChipiPay payment gateway?",
                "ChipiPay cryptocurrency payment processing",
                "ChipiPay webhook implementation",
                "ChipiPay subscription payment setup",
                "ChipiPay multi-currency support"
            ]
        }
    
    def test_categorization(self, query: str, platform: str) -> TestResult:
        """Test categorization for a single query"""
        
        try:
            start_time = time.time()
            
            # Generate sample content based on query and platform
            sample_content = self._generate_sample_content(query, platform)
            
            # Test categorization
            categorization = self.categorizer.categorize_document(
                content=sample_content,
                file_path=f"{platform}_documentation.md"
            )
            
            processing_time = time.time() - start_time
            
            # Log performance
            self.optimizer.log_query_performance(
                query=query,
                response_time=processing_time,
                similarity_score=categorization.confidence,
                result_count=len(categorization.keywords),
                platform=platform,
                category=categorization.category.value
            )
            
            return TestResult(
                query=query,
                platform=platform,
                category=categorization.category.value,
                confidence=categorization.confidence,
                keywords=categorization.keywords,
                importance=categorization.importance,
                doc_type=categorization.doc_type,
                tags=categorization.tags,
                success=True
            )
            
        except Exception as e:
            logger.error(f"Test failed for query '{query}' on platform '{platform}': {e}")
            return TestResult(
                query=query,
                platform=platform,
                category="error",
                confidence=0.0,
                keywords=[],
                importance="low",
                doc_type="error",
                tags=[],
                success=False,
                error=str(e)
            )
    
    def _generate_sample_content(self, query: str, platform: str) -> str:
        """Generate sample content for testing based on query and platform"""
        
        # Platform-specific content templates
        platform_templates = {
            "extended_exchange": """
            Extended Exchange Trading API Documentation
            
            This guide covers the Extended Exchange REST API for trading operations.
            
            Authentication: All requests require API key authentication using HMAC-SHA256.
            
            Place Order Endpoint:
            POST /api/v1/order
            
            Parameters:
            - symbol: Trading pair (e.g., BTC/USDT)
            - side: buy or sell
            - type: market or limit
            - quantity: Order quantity
            - price: Order price for limit orders
            
            Market Data:
            GET /api/v1/ticker/24hr
            Get 24hr ticker statistics for all symbols
            
            Order Book:
            GET /api/v1/depth
            Get order book depth for a symbol
            """,
            
            "x10_python_sdk": """
            X10 Python SDK Documentation
            
            Installation:
            pip install x10-python-sdk
            
            Quick Start:
            from x10_sdk import TradingClient
            
            client = TradingClient(api_key="your_key", api_secret="your_secret")
            
            # Get account balance
            balance = await client.get_account_balance()
            
            # Place order
            order = await client.place_order(
                symbol="BTC/USDT",
                side="buy",
                type="limit",
                quantity=0.1,
                price=50000
            )
            
            # Get trading history
            history = await client.get_trading_history()
            """,
            
            "starknet_dart": """
            Starknet.dart SDK Documentation
            
            Installation:
            dependencies:
              starknet: ^0.7.0
            
            Usage:
            import 'package:starknet/starknet.dart';
            
            // Connect to Starknet
            final provider = JsonRpcProvider(nodeUri: "https://starknet-mainnet.public.blastapi.io");
            
            // Create account
            final account = Account(
              address: "0x123...",
              signer: signer,
              provider: provider
            );
            
            // Invoke contract
            final result = await account.invoke(
              contractAddress: "0x456...",
              selector: "transfer",
              calldata: [recipient, amount]
            );
            
            // Flutter integration for mobile wallet
            class WalletWidget extends StatefulWidget {
              // Widget implementation
            }
            """,
            
            "cairo_lang": """
            Cairo Language Documentation
            
            ERC-20 Token Implementation:
            
            #[starknet::contract]
            mod ERC20Token {
                use starknet::storage::{StoragePointerReadAccess, StoragePointerWriteAccess};
                
                #[storage]
                struct Storage {
                    name: felt252,
                    symbol: felt252,
                    decimals: u8,
                    total_supply: felt252,
                    balances: LegacyMap<felt252, felt252>,
                    allowances: LegacyMap<(felt252, felt252), felt252>,
                }
                
                #[constructor]
                fn constructor(
                    ref self: ContractState,
                    name: felt252,
                    symbol: felt252,
                    decimals: u8,
                    initial_supply: felt252,
                    recipient: felt252
                ) {
                    self.name.write(name);
                    self.symbol.write(symbol);
                    self.decimals.write(decimals);
                    self.total_supply.write(initial_supply);
                    self.balances.write(recipient, initial_supply);
                }
                
                #[external(v0)]
                fn transfer(ref self: ContractState, recipient: felt252, amount: felt252) -> bool {
                    let caller = get_caller_address();
                    self._transfer(caller, recipient, amount);
                    true
                }
            }
            """,
            
            "avnu_paymaster": """
            AVNU Paymaster Documentation
            
            Gasless Transaction Implementation:
            
            The AVNU Paymaster enables gasless transactions on Starknet by sponsoring gas fees.
            
            Setup:
            1. Register with AVNU Paymaster service
            2. Configure paymaster contract address
            3. Implement user operations with paymaster data
            
            Example Integration:
            import { PaymasterProvider } from '@avnu/paymaster-sdk';
            
            const paymaster = new PaymasterProvider({
              paymasterAddress: "0x789...",
              sponsorshipPolicy: "free-tier"
            });
            
            // Create sponsored transaction
            const sponsoredTx = await paymaster.sponsorUserOperation({
              target: contractAddress,
              calldata: encodedCalldata,
              value: 0
            });
            
            // Submit transaction
            const result = await account.execute(sponsoredTx);
            
            Account Abstraction Benefits:
            - Improved user experience
            - Reduced onboarding friction
            - Flexible fee payment options
            """,
            
            "web3auth": """
            Web3Auth Documentation
            
            Social Login Integration:
            
            Web3Auth provides seamless authentication for Web3 applications.
            
            Setup:
            npm install @web3auth/modal
            
            Implementation:
            import { Web3Auth } from "@web3auth/modal";
            
            const web3auth = new Web3Auth({
              clientId: "your-client-id",
              chainConfig: {
                chainNamespace: "eip155",
                chainId: "0x1"
              }
            });
            
            // Initialize
            await web3auth.initModal();
            
            // Login with social provider
            const provider = await web3auth.connect();
            
            // Get user info
            const user = await web3auth.getUserInfo();
            
            // Get private key (non-custodial)
            const privateKey = await provider.request({
              method: "eth_private_key"
            });
            
            Multi-Factor Authentication:
            - SMS verification
            - Email verification
            - Biometric authentication
            - Social recovery
            """,
            
            "chipi_pay": """
            ChipiPay Payment Gateway Documentation
            
            Cryptocurrency Payment Processing:
            
            ChipiPay enables merchants to accept cryptocurrency payments.
            
            Integration:
            1. Create merchant account
            2. Generate API keys
            3. Configure webhooks
            4. Implement payment flow
            
            Example:
            import { ChipiPaySDK } from 'chipi-pay-sdk';
            
            const chipiPay = new ChipiPaySDK({
              apiKey: 'your-api-key',
              environment: 'production'
            });
            
            // Create payment
            const payment = await chipiPay.createPayment({
              amount: 100,
              currency: 'USDT',
              orderId: 'order-123',
              webhookUrl: 'https://yoursite.com/webhook'
            });
            
            // Process webhook
            app.post('/webhook', (req, res) => {
              const event = chipiPay.verifyWebhook(req.body, req.headers);
              
              if (event.type === 'payment.completed') {
                // Update order status
                updateOrderStatus(event.data.orderId, 'paid');
              }
            });
            
            Supported Currencies:
            - Bitcoin (BTC)
            - Ethereum (ETH)
            - USDT, USDC
            - Custom tokens
            """
        }
        
        # Get base content for platform
        base_content = platform_templates.get(platform, "Generic documentation content")
        
        # Add query-specific content
        query_lower = query.lower()
        if "authentication" in query_lower or "auth" in query_lower:
            base_content += "\n\nAuthentication is required for all API operations."
        if "install" in query_lower or "setup" in query_lower:
            base_content += "\n\nInstallation and setup instructions are provided above."
        if "example" in query_lower:
            base_content += "\n\nCode examples and samples are included for reference."
        
        return base_content
    
    def run_all_tests(self) -> Dict[str, Any]:
        """Run all categorization tests"""
        
        logger.info("Starting comprehensive categorization testing...")
        
        all_results = []
        platform_summaries = {}
        
        for platform, queries in self.test_queries.items():
            logger.info(f"Testing platform: {platform}")
            
            platform_results = []
            for query in queries:
                result = self.test_categorization(query, platform)
                platform_results.append(result)
                all_results.append(result)
            
            # Calculate platform summary
            successful_tests = [r for r in platform_results if r.success]
            avg_confidence = statistics.mean([r.confidence for r in platform_results if r.success]) if successful_tests else 0
            
            platform_summaries[platform] = {
                "total_tests": len(platform_results),
                "successful_tests": len(successful_tests),
                "success_rate": len(successful_tests) / len(platform_results) if platform_results else 0,
                "avg_confidence": avg_confidence,
                "categories_detected": list(set([r.category for r in platform_results if r.success])),
                "avg_keywords": statistics.mean([len(r.keywords) for r in platform_results if r.success]) if successful_tests else 0
            }
        
        # Store results
        self.test_results = all_results
        
        # Generate overall summary
        successful_tests = [r for r in all_results if r.success]
        overall_summary = {
            "total_tests": len(all_results),
            "successful_tests": len(successful_tests),
            "overall_success_rate": len(successful_tests) / len(all_results) if all_results else 0,
            "avg_confidence": statistics.mean([r.confidence for r in all_results if r.success]) if successful_tests else 0,
            "unique_categories": len(set([r.category for r in all_results if r.success])),
            "total_keywords": sum([len(r.keywords) for r in all_results if r.success]),
            "avg_keywords_per_test": statistics.mean([len(r.keywords) for r in all_results if r.success]) if successful_tests else 0
        }
        
        # Get optimization metrics
        optimization_metrics = self.optimizer.analyze_performance()
        
        return {
            "overall_summary": overall_summary,
            "platform_summaries": platform_summaries,
            "optimization_metrics": {
                "query_count": optimization_metrics.query_count,
                "avg_response_time": optimization_metrics.avg_response_time,
                "avg_similarity_score": optimization_metrics.avg_similarity_score,
                "error_rate": optimization_metrics.error_rate,
                "optimization_suggestions": optimization_metrics.optimization_suggestions
            },
            "test_results": [
                {
                    "query": r.query,
                    "platform": r.platform,
                    "category": r.category,
                    "confidence": r.confidence,
                    "keywords": r.keywords,
                    "importance": r.importance,
                    "doc_type": r.doc_type,
                    "tags": r.tags,
                    "success": r.success,
                    "error": r.error
                }
                for r in all_results
            ]
        }
    
    def save_test_results(self, results: Dict[str, Any], filename: str = "rag_categorization_test_results.json"):
        """Save test results to file"""
        
        output_path = Path("/Users/admin/AstraTrade-Project/knowledge_base/backend") / filename
        
        # Add metadata
        results["metadata"] = {
            "test_date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "test_type": "categorization_system",
            "platforms_tested": list(self.test_queries.keys()),
            "total_queries": sum(len(queries) for queries in self.test_queries.values()),
            "features_tested": [
                "Document categorization",
                "Platform detection",
                "Keyword extraction",
                "Importance assessment",
                "Document type classification",
                "Tag generation"
            ]
        }
        
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=2)
        
        logger.info(f"Test results saved to {output_path}")
        return output_path

def main():
    """Main testing function"""
    
    tester = SimpleRAGTester()
    
    try:
        # Run all tests
        results = tester.run_all_tests()
        
        # Save results
        output_file = tester.save_test_results(results)
        
        # Print summary
        print("\n" + "="*80)
        print("ENHANCED RAG CATEGORIZATION SYSTEM TEST RESULTS")
        print("="*80)
        
        overall = results["overall_summary"]
        print(f"Total Tests: {overall['total_tests']}")
        print(f"Successful Tests: {overall['successful_tests']}")
        print(f"Success Rate: {overall['overall_success_rate']:.2%}")
        print(f"Average Confidence: {overall['avg_confidence']:.2f}")
        print(f"Unique Categories Detected: {overall['unique_categories']}")
        print(f"Total Keywords Extracted: {overall['total_keywords']}")
        print(f"Average Keywords per Test: {overall['avg_keywords_per_test']:.1f}")
        
        print("\nPLATFORM BREAKDOWN:")
        print("-" * 50)
        
        for platform, summary in results["platform_summaries"].items():
            print(f"{platform.upper()}: {summary['success_rate']:.1%} success "
                  f"({summary['successful_tests']}/{summary['total_tests']} tests)")
            print(f"  Average Confidence: {summary['avg_confidence']:.2f}")
            print(f"  Categories Detected: {', '.join(summary['categories_detected'])}")
            print(f"  Average Keywords: {summary['avg_keywords']:.1f}")
            print()
        
        print("\nSYSTEM PERFORMANCE:")
        print("-" * 50)
        
        opt_metrics = results["optimization_metrics"]
        print(f"Processing Time: {opt_metrics['avg_response_time']:.3f}s average")
        print(f"Quality Score: {opt_metrics['avg_similarity_score']:.2f}")
        print(f"Error Rate: {opt_metrics['error_rate']:.2%}")
        
        if opt_metrics['optimization_suggestions']:
            print(f"Optimization Suggestions: {len(opt_metrics['optimization_suggestions'])}")
        
        print(f"\nDetailed results saved to: {output_file}")
        
        # Return success/failure
        return overall['overall_success_rate'] > 0.9  # 90% success rate threshold
        
    except Exception as e:
        logger.error(f"Testing failed: {e}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)