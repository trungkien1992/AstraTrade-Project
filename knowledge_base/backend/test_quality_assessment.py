#!/usr/bin/env python3
"""
Quality Assessment Validation Testing
Test document scoring accuracy and quality algorithms across all platforms
"""

import asyncio
import json
import logging
import time
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from pathlib import Path
import statistics
import sys
import os

# Add current directory to Python path
sys.path.insert(0, '/Users/admin/AstraTrade-Project/knowledge_base/backend')

# Import components
from categorization_system import AstraTradeCategorizer, DocumentCategory, PlatformType
from optimization_manager import RAGOptimizationManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class QualityTestResult:
    """Result of quality assessment testing"""
    document_id: str
    platform: str
    category: str
    expected_quality: str
    actual_quality: str
    confidence: float
    importance_score: float
    keyword_relevance: float
    content_depth: float
    technical_accuracy: float
    overall_quality: float
    accuracy: bool
    error: Optional[str] = None

class QualityAssessmentTester:
    """Comprehensive quality assessment testing"""
    
    def __init__(self):
        self.categorizer = AstraTradeCategorizer()
        self.optimizer = RAGOptimizationManager()
        self.test_results: List[QualityTestResult] = []
        
        # Test documents with expected quality levels
        self.test_documents = {
            "high_quality": {
                "extended_exchange_api": """
                # Extended Exchange Trading API v2.0
                
                ## Overview
                Extended Exchange provides a comprehensive REST API for algorithmic trading, market data access, and account management. This API supports both spot and derivatives trading with advanced order types and real-time market data streams.
                
                ## Authentication
                All API requests require authentication using API keys with HMAC-SHA256 signatures. Generate your API keys from the dashboard and ensure proper signature generation.
                
                **Security Best Practices:**
                - Store API keys securely
                - Use IP whitelisting
                - Implement proper rate limiting
                - Never expose keys in client-side code
                
                ## Order Management
                
                ### Place Order
                ```http
                POST /api/v2/orders
                Content-Type: application/json
                X-API-Key: your-api-key
                X-Signature: calculated-signature
                X-Timestamp: current-timestamp
                
                {
                  "symbol": "BTC/USDT",
                  "side": "buy",
                  "type": "limit",
                  "quantity": "0.1",
                  "price": "45000.00",
                  "timeInForce": "GTC"
                }
                ```
                
                **Response:**
                ```json
                {
                  "orderId": "12345",
                  "symbol": "BTC/USDT",
                  "status": "NEW",
                  "side": "buy",
                  "type": "limit",
                  "quantity": "0.1",
                  "price": "45000.00",
                  "timestamp": 1640995200000
                }
                ```
                
                ### Order Types
                - **Market Orders**: Execute immediately at current market price
                - **Limit Orders**: Execute at specified price or better
                - **Stop Orders**: Trigger when price reaches stop price
                - **Stop-Limit Orders**: Combination of stop and limit orders
                
                ## Market Data
                
                ### Real-time Ticker
                ```http
                GET /api/v2/ticker/24hr?symbol=BTC/USDT
                ```
                
                ### Order Book
                ```http
                GET /api/v2/depth?symbol=BTC/USDT&limit=100
                ```
                
                ### Historical Data
                ```http
                GET /api/v2/klines?symbol=BTC/USDT&interval=1h&limit=500
                ```
                
                ## Error Handling
                All API errors follow RFC 7807 standard with detailed error codes and messages.
                
                ## Rate Limits
                - 1200 requests per minute for trading endpoints
                - 6000 requests per minute for market data endpoints
                - Weight-based rate limiting for complex operations
                
                ## SDK Integration
                Official SDKs available for Python, JavaScript, Java, and Go.
                """,
                
                "starknet_dart_guide": """
                # Starknet.dart SDK Complete Guide
                
                ## Introduction
                Starknet.dart is the official Dart SDK for Starknet blockchain integration, optimized for Flutter mobile applications. This comprehensive guide covers installation, configuration, and advanced usage patterns.
                
                ## Installation
                
                Add to your `pubspec.yaml`:
                ```yaml
                dependencies:
                  starknet: ^0.7.0
                  http: ^1.0.0
                  crypto: ^3.0.0
                ```
                
                ## Provider Configuration
                
                ### Mainnet Connection
                ```dart
                import 'package:starknet/starknet.dart';
                
                final provider = JsonRpcProvider(
                  nodeUri: Uri.parse('https://starknet-mainnet.public.blastapi.io'),
                  headers: {'Authorization': 'Bearer your-token'}
                );
                ```
                
                ### Testnet Connection
                ```dart
                final testnetProvider = JsonRpcProvider(
                  nodeUri: Uri.parse('https://starknet-goerli.public.blastapi.io')
                );
                ```
                
                ## Account Management
                
                ### Create Account
                ```dart
                // Generate new account
                final keyPair = generateKeyPair();
                final account = Account(
                  address: calculateContractAddress(keyPair.publicKey),
                  keyPair: keyPair,
                  provider: provider,
                  accountClassHash: AccountClassHash.argentX
                );
                ```
                
                ### Import Existing Account
                ```dart
                final existingAccount = Account.fromPrivateKey(
                  privateKey: 'your-private-key',
                  provider: provider
                );
                ```
                
                ## Smart Contract Interaction
                
                ### Contract Deployment
                ```dart
                final contractFactory = ContractFactory(
                  compiledContract: await loadContract('MyContract.json'),
                  provider: provider
                );
                
                final contract = await contractFactory.deploy(
                  constructorCalldata: [owner, initialSupply],
                  salt: generateSalt()
                );
                ```
                
                ### Contract Calls
                ```dart
                // Read call (view function)
                final balance = await contract.call(
                  selector: 'balanceOf',
                  calldata: [userAddress]
                );
                
                // Write call (invoke function)
                final result = await account.invoke(
                  contractAddress: contract.address,
                  selector: 'transfer',
                  calldata: [recipient, amount]
                );
                ```
                
                ## Flutter Integration
                
                ### Wallet Widget
                ```dart
                class StarknetWallet extends StatefulWidget {
                  @override
                  _StarknetWalletState createState() => _StarknetWalletState();
                }
                
                class _StarknetWalletState extends State<StarknetWallet> {
                  Account? _account;
                  String _balance = '0';
                  
                  @override
                  void initState() {
                    super.initState();
                    _initializeWallet();
                  }
                  
                  Future<void> _initializeWallet() async {
                    // Initialize account and load balance
                    _account = await loadStoredAccount();
                    if (_account != null) {
                      await _updateBalance();
                    }
                  }
                  
                  Future<void> _updateBalance() async {
                    final balance = await _account!.getBalance();
                    setState(() {
                      _balance = balance.toString();
                    });
                  }
                  
                  @override
                  Widget build(BuildContext context) {
                    return Column(
                      children: [
                        Text('Balance: $_balance ETH'),
                        ElevatedButton(
                          onPressed: _account != null ? _sendTransaction : null,
                          child: Text('Send Transaction')
                        ),
                      ],
                    );
                  }
                }
                ```
                
                ## Advanced Features
                
                ### Multicall Support
                ```dart
                final multicall = Multicall(provider: provider);
                final results = await multicall.call([
                  Call(
                    contractAddress: tokenContract,
                    selector: 'balanceOf',
                    calldata: [userAddress]
                  ),
                  Call(
                    contractAddress: tokenContract,
                    selector: 'totalSupply',
                    calldata: []
                  )
                ]);
                ```
                
                ### Event Listening
                ```dart
                final eventFilter = EventFilter(
                  contractAddress: contract.address,
                  eventName: 'Transfer'
                );
                
                provider.getEvents(eventFilter).listen((event) {
                  print('Transfer event: ${event.data}');
                });
                ```
                
                ## Security Considerations
                - Always validate contract addresses
                - Use secure key storage (Android Keystore, iOS Keychain)
                - Implement proper error handling
                - Validate transaction parameters
                
                ## Performance Optimization
                - Use connection pooling for multiple requests
                - Implement caching for frequently accessed data
                - Use batch calls when possible
                - Optimize UI updates with proper state management
                
                ## Testing
                Use testnet for development and comprehensive testing before mainnet deployment.
                """
            },
            
            "medium_quality": {
                "x10_python_basic": """
                # X10 Python SDK
                
                ## Install
                ```bash
                pip install x10-python-sdk
                ```
                
                ## Usage
                ```python
                from x10_sdk import TradingClient
                
                client = TradingClient(
                    api_key="your-key",
                    api_secret="your-secret"
                )
                
                # Get balance
                balance = client.get_balance()
                print(balance)
                
                # Place order
                order = client.place_order(
                    symbol="BTC/USDT",
                    side="buy",
                    amount=0.1,
                    price=50000
                )
                ```
                
                ## Methods
                - `get_balance()` - Get account balance
                - `place_order()` - Place trading order
                - `get_orders()` - Get order history
                - `cancel_order()` - Cancel order
                
                ## Error Handling
                ```python
                try:
                    order = client.place_order(...)
                except X10Error as e:
                    print(f"Error: {e}")
                ```
                """,
                
                "cairo_basic": """
                # Cairo Contract Example
                
                ## ERC20 Token
                ```cairo
                #[starknet::contract]
                mod ERC20 {
                    #[storage]
                    struct Storage {
                        balances: LegacyMap<felt252, u256>,
                        total_supply: u256,
                    }
                    
                    #[constructor]
                    fn constructor(ref self: ContractState, supply: u256) {
                        self.total_supply.write(supply);
                    }
                    
                    #[external(v0)]
                    fn transfer(ref self: ContractState, to: felt252, amount: u256) {
                        // Transfer logic
                    }
                }
                ```
                
                ## Deployment
                ```bash
                scarb build
                starknet deploy --class-hash 0x123...
                ```
                """
            },
            
            "low_quality": {
                "web3auth_minimal": """
                # Web3Auth
                
                Install:
                npm install @web3auth/modal
                
                Usage:
                const web3auth = new Web3Auth({clientId: "id"});
                web3auth.initModal();
                const provider = await web3auth.connect();
                """,
                
                "chipi_pay_basic": """
                ChipiPay Payment Gateway
                
                Create payment:
                POST /api/payments
                {
                  "amount": 100,
                  "currency": "USDT"
                }
                
                Webhook:
                POST /webhook
                Handle payment events
                """
            }
        }
    
    def calculate_quality_score(self, content: str, platform: str, category: str) -> Tuple[float, Dict[str, float]]:
        """Calculate comprehensive quality score for content"""
        
        scores = {}
        
        # 1. Content Length and Depth (0-1)
        word_count = len(content.split())
        if word_count < 50:
            scores['content_depth'] = 0.3
        elif word_count < 200:
            scores['content_depth'] = 0.6
        elif word_count < 500:
            scores['content_depth'] = 0.8
        else:
            scores['content_depth'] = 1.0
        
        # 2. Technical Accuracy (0-1)
        technical_indicators = [
            'api', 'endpoint', 'parameter', 'response', 'request',
            'authentication', 'authorization', 'token', 'signature',
            'error', 'exception', 'status', 'code', 'method',
            'class', 'function', 'import', 'export', 'interface'
        ]
        
        content_lower = content.lower()
        tech_matches = sum(1 for indicator in technical_indicators if indicator in content_lower)
        scores['technical_accuracy'] = min(tech_matches / 10, 1.0)
        
        # 3. Code Examples Quality (0-1)
        code_blocks = content.count('```')
        if code_blocks >= 4:
            scores['code_examples'] = 1.0
        elif code_blocks >= 2:
            scores['code_examples'] = 0.7
        elif code_blocks >= 1:
            scores['code_examples'] = 0.4
        else:
            scores['code_examples'] = 0.1
        
        # 4. Structure and Organization (0-1)
        headers = content.count('#')
        if headers >= 6:
            scores['structure'] = 1.0
        elif headers >= 4:
            scores['structure'] = 0.8
        elif headers >= 2:
            scores['structure'] = 0.6
        else:
            scores['structure'] = 0.3
        
        # 5. Platform-Specific Keywords (0-1)
        platform_keywords = {
            'extended_exchange': ['trading', 'order', 'market', 'api', 'exchange'],
            'x10_python_sdk': ['python', 'sdk', 'client', 'import', 'pip'],
            'starknet_dart': ['dart', 'flutter', 'starknet', 'contract', 'provider'],
            'cairo_lang': ['cairo', 'felt252', 'contract', 'starknet', 'storage'],
            'avnu_paymaster': ['paymaster', 'gas', 'starknet', 'transaction', 'sponsor'],
            'web3auth': ['web3auth', 'authentication', 'oauth', 'social', 'login'],
            'chipi_pay': ['chipi', 'payment', 'gateway', 'webhook', 'crypto']
        }
        
        relevant_keywords = platform_keywords.get(platform, [])
        keyword_matches = sum(1 for keyword in relevant_keywords if keyword in content_lower)
        scores['keyword_relevance'] = min(keyword_matches / len(relevant_keywords), 1.0) if relevant_keywords else 0.5
        
        # 6. Documentation Standards (0-1)
        doc_standards = [
            'overview', 'introduction', 'installation', 'setup',
            'example', 'usage', 'configuration', 'error',
            'security', 'best practice', 'performance'
        ]
        
        doc_matches = sum(1 for standard in doc_standards if standard in content_lower)
        scores['documentation_standards'] = min(doc_matches / 7, 1.0)
        
        # Calculate weighted overall score
        weights = {
            'content_depth': 0.25,
            'technical_accuracy': 0.20,
            'code_examples': 0.15,
            'structure': 0.15,
            'keyword_relevance': 0.15,
            'documentation_standards': 0.10
        }
        
        overall_score = sum(scores[key] * weights[key] for key in weights)
        
        return overall_score, scores
    
    def determine_quality_level(self, overall_score: float) -> str:
        """Determine quality level based on overall score"""
        if overall_score >= 0.75:
            return "high"
        elif overall_score >= 0.55:
            return "medium"
        elif overall_score >= 0.35:
            return "low"
        else:
            return "very_low"
    
    def test_quality_assessment(self, document_id: str, content: str, platform: str, expected_quality: str) -> QualityTestResult:
        """Test quality assessment for a single document"""
        
        try:
            start_time = time.time()
            
            # Categorize document
            categorization = self.categorizer.categorize_document(
                content=content,
                file_path=f"{platform}_{document_id}.md"
            )
            
            # Calculate quality scores
            overall_score, detailed_scores = self.calculate_quality_score(
                content, platform, categorization.category.value
            )
            
            # Determine quality level
            actual_quality = self.determine_quality_level(overall_score)
            
            # Check accuracy (remove "_quality" suffix from expected for comparison)
            expected_level = expected_quality.replace("_quality", "")
            accuracy = expected_level == actual_quality
            
            processing_time = time.time() - start_time
            
            # Log performance
            self.optimizer.log_query_performance(
                query=f"quality_assessment_{document_id}",
                response_time=processing_time,
                similarity_score=overall_score,
                result_count=len(detailed_scores),
                platform=platform,
                category=categorization.category.value
            )
            
            return QualityTestResult(
                document_id=document_id,
                platform=platform,
                category=categorization.category.value,
                expected_quality=expected_quality,
                actual_quality=actual_quality,
                confidence=categorization.confidence,
                importance_score=1.0 if categorization.importance == "high" else 0.7 if categorization.importance == "medium" else 0.4,
                keyword_relevance=detailed_scores.get('keyword_relevance', 0.0),
                content_depth=detailed_scores.get('content_depth', 0.0),
                technical_accuracy=detailed_scores.get('technical_accuracy', 0.0),
                overall_quality=overall_score,
                accuracy=accuracy
            )
            
        except Exception as e:
            logger.error(f"Quality assessment failed for {document_id}: {e}")
            return QualityTestResult(
                document_id=document_id,
                platform=platform,
                category="error",
                expected_quality=expected_quality,
                actual_quality="error",
                confidence=0.0,
                importance_score=0.0,
                keyword_relevance=0.0,
                content_depth=0.0,
                technical_accuracy=0.0,
                overall_quality=0.0,
                accuracy=False,
                error=str(e)
            )
    
    def run_quality_tests(self) -> Dict[str, Any]:
        """Run comprehensive quality assessment tests"""
        
        logger.info("Starting quality assessment validation...")
        
        all_results = []
        quality_summaries = {}
        
        # Test all document categories
        for quality_level, documents in self.test_documents.items():
            logger.info(f"Testing {quality_level} quality documents...")
            
            quality_results = []
            
            for doc_id, content in documents.items():
                # Extract platform from document ID
                platform = doc_id.split('_')[0] if '_' in doc_id else 'unknown'
                
                result = self.test_quality_assessment(doc_id, content, platform, quality_level)
                quality_results.append(result)
                all_results.append(result)
            
            # Calculate quality level summary
            accurate_tests = [r for r in quality_results if r.accuracy]
            
            quality_summaries[quality_level] = {
                "total_tests": len(quality_results),
                "accurate_tests": len(accurate_tests),
                "accuracy_rate": len(accurate_tests) / len(quality_results) if quality_results else 0,
                "avg_confidence": statistics.mean([r.confidence for r in quality_results]) if quality_results else 0,
                "avg_overall_quality": statistics.mean([r.overall_quality for r in quality_results]) if quality_results else 0,
                "avg_technical_accuracy": statistics.mean([r.technical_accuracy for r in quality_results]) if quality_results else 0,
                "avg_content_depth": statistics.mean([r.content_depth for r in quality_results]) if quality_results else 0
            }
        
        # Store results
        self.test_results = all_results
        
        # Generate overall summary
        accurate_tests = [r for r in all_results if r.accuracy]
        overall_summary = {
            "total_tests": len(all_results),
            "accurate_tests": len(accurate_tests),
            "overall_accuracy": len(accurate_tests) / len(all_results) if all_results else 0,
            "avg_confidence": statistics.mean([r.confidence for r in all_results]) if all_results else 0,
            "avg_overall_quality": statistics.mean([r.overall_quality for r in all_results]) if all_results else 0,
            "avg_technical_accuracy": statistics.mean([r.technical_accuracy for r in all_results]) if all_results else 0,
            "avg_content_depth": statistics.mean([r.content_depth for r in all_results]) if all_results else 0,
            "avg_keyword_relevance": statistics.mean([r.keyword_relevance for r in all_results]) if all_results else 0,
            "quality_distribution": {
                "high": len([r for r in all_results if r.actual_quality == "high"]),
                "medium": len([r for r in all_results if r.actual_quality == "medium"]),
                "low": len([r for r in all_results if r.actual_quality == "low"]),
                "very_low": len([r for r in all_results if r.actual_quality == "very_low"])
            }
        }
        
        # Get optimization metrics
        optimization_metrics = self.optimizer.analyze_performance()
        
        return {
            "overall_summary": overall_summary,
            "quality_summaries": quality_summaries,
            "optimization_metrics": {
                "avg_processing_time": optimization_metrics.avg_response_time,
                "error_rate": optimization_metrics.error_rate,
                "optimization_suggestions": optimization_metrics.optimization_suggestions
            },
            "detailed_results": [
                {
                    "document_id": r.document_id,
                    "platform": r.platform,
                    "category": r.category,
                    "expected_quality": r.expected_quality,
                    "actual_quality": r.actual_quality,
                    "confidence": r.confidence,
                    "importance_score": r.importance_score,
                    "keyword_relevance": r.keyword_relevance,
                    "content_depth": r.content_depth,
                    "technical_accuracy": r.technical_accuracy,
                    "overall_quality": r.overall_quality,
                    "accuracy": r.accuracy,
                    "error": r.error
                }
                for r in all_results
            ]
        }
    
    def save_test_results(self, results: Dict[str, Any], filename: str = "quality_assessment_test_results.json"):
        """Save quality assessment test results"""
        
        output_path = Path("/Users/admin/AstraTrade-Project/knowledge_base/backend") / filename
        
        # Add metadata
        results["metadata"] = {
            "test_date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "test_type": "quality_assessment_validation",
            "quality_levels_tested": list(self.test_documents.keys()),
            "total_documents": sum(len(docs) for docs in self.test_documents.values()),
            "quality_metrics": [
                "Content depth and length",
                "Technical accuracy",
                "Code examples quality",
                "Structure and organization",
                "Platform-specific keywords",
                "Documentation standards"
            ]
        }
        
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=2)
        
        logger.info(f"Quality assessment results saved to {output_path}")
        return output_path

def main():
    """Main quality assessment testing function"""
    
    tester = QualityAssessmentTester()
    
    try:
        # Run quality tests
        results = tester.run_quality_tests()
        
        # Save results
        output_file = tester.save_test_results(results)
        
        # Print summary
        print("\n" + "="*80)
        print("QUALITY ASSESSMENT VALIDATION RESULTS")
        print("="*80)
        
        overall = results["overall_summary"]
        print(f"Total Tests: {overall['total_tests']}")
        print(f"Accurate Assessments: {overall['accurate_tests']}")
        print(f"Overall Accuracy: {overall['overall_accuracy']:.2%}")
        print(f"Average Confidence: {overall['avg_confidence']:.2f}")
        print(f"Average Quality Score: {overall['avg_overall_quality']:.2f}")
        print(f"Average Technical Accuracy: {overall['avg_technical_accuracy']:.2f}")
        print(f"Average Content Depth: {overall['avg_content_depth']:.2f}")
        print(f"Average Keyword Relevance: {overall['avg_keyword_relevance']:.2f}")
        
        print("\nQUALITY DISTRIBUTION:")
        print("-" * 30)
        dist = overall['quality_distribution']
        for level, count in dist.items():
            print(f"{level.upper()}: {count} documents")
        
        print("\nQUALITY LEVEL BREAKDOWN:")
        print("-" * 50)
        
        for quality_level, summary in results["quality_summaries"].items():
            print(f"{quality_level.upper()}: {summary['accuracy_rate']:.1%} accuracy "
                  f"({summary['accurate_tests']}/{summary['total_tests']} tests)")
            print(f"  Average Quality Score: {summary['avg_overall_quality']:.2f}")
            print(f"  Average Technical Accuracy: {summary['avg_technical_accuracy']:.2f}")
            print(f"  Average Content Depth: {summary['avg_content_depth']:.2f}")
            print()
        
        print("\nSYSTEM PERFORMANCE:")
        print("-" * 50)
        
        opt_metrics = results["optimization_metrics"]
        print(f"Processing Time: {opt_metrics['avg_processing_time']:.3f}s average")
        print(f"Error Rate: {opt_metrics['error_rate']:.2%}")
        
        if opt_metrics['optimization_suggestions']:
            print(f"Optimization Suggestions: {len(opt_metrics['optimization_suggestions'])}")
        
        print(f"\nDetailed results saved to: {output_file}")
        
        # Return success/failure (85% accuracy threshold)
        return overall['overall_accuracy'] > 0.85
        
    except Exception as e:
        logger.error(f"Quality assessment testing failed: {e}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)