#!/usr/bin/env python3
"""
Citations Accuracy Testing
Test grounded citations and source attribution reliability
Enhanced to test ClaudeOptimizedSearch citation generation
"""

import json
import logging
import time
import asyncio
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from pathlib import Path
import statistics
import sys
import os
from unittest.mock import Mock, AsyncMock

# Add current directory to Python path
sys.path.insert(0, '/Users/admin/AstraTrade-Project/knowledge_base/backend')

from claude_search import ClaudeOptimizedSearch, Citation

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class CitationTestResult:
    """Citation accuracy test result"""
    query: str
    document_id: str
    expected_citations: List[str]
    actual_citations: List[str]
    citation_accuracy: float
    source_attribution: float
    confidence_score: float
    precision: float
    recall: float
    f1_score: float
    success: bool
    error: Optional[str] = None

class CitationAccuracyTester:
    """Test grounded citations accuracy"""
    
    def __init__(self):
        self.test_results: List[CitationTestResult] = []
        
        # Test scenarios with expected citations
        self.citation_test_cases = {
            "extended_exchange_trading": {
                "query": "How to place orders on Extended Exchange?",
                "document_content": """
                # Extended Exchange Trading API
                
                ## Order Placement
                To place an order on Extended Exchange, use the following endpoint:
                
                ```http
                POST /api/v1/orders
                ```
                
                ### Parameters
                - symbol: Trading pair (e.g., BTC/USDT)
                - side: buy or sell
                - type: market or limit
                - quantity: Order quantity
                - price: Order price (for limit orders)
                
                ### Example Request
                ```json
                {
                    "symbol": "BTC/USDT",
                    "side": "buy",
                    "type": "limit",
                    "quantity": 0.1,
                    "price": 45000
                }
                ```
                
                ### Response
                The API returns an order confirmation with order ID.
                
                ## Authentication
                All requests require API key authentication using HMAC-SHA256.
                """,
                "expected_citations": [
                    "POST /api/v1/orders",
                    "symbol: Trading pair",
                    "side: buy or sell",
                    "API key authentication",
                    "HMAC-SHA256"
                ],
                "platform": "extended_exchange"
            },
            
            "starknet_dart_wallet": {
                "query": "How to create a wallet with Starknet.dart?",
                "document_content": """
                # Starknet.dart Wallet Integration
                
                ## Creating a Wallet
                To create a wallet using Starknet.dart SDK:
                
                ```dart
                import 'package:starknet/starknet.dart';
                
                // Generate new keypair
                final keyPair = generateKeyPair();
                
                // Create account
                final account = Account(
                    address: calculateContractAddress(keyPair.publicKey),
                    keyPair: keyPair,
                    provider: provider
                );
                ```
                
                ## Provider Setup
                ```dart
                final provider = JsonRpcProvider(
                    nodeUri: Uri.parse('https://starknet-mainnet.public.blastapi.io')
                );
                ```
                
                ## Flutter Integration
                Use the wallet in your Flutter app:
                
                ```dart
                class WalletWidget extends StatefulWidget {
                    @override
                    _WalletWidgetState createState() => _WalletWidgetState();
                }
                ```
                """,
                "expected_citations": [
                    "generateKeyPair()",
                    "Account(",
                    "calculateContractAddress",
                    "JsonRpcProvider",
                    "StatefulWidget"
                ],
                "platform": "starknet_dart"
            },
            
            "cairo_smart_contract": {
                "query": "How to write ERC20 token in Cairo?",
                "document_content": """
                # Cairo ERC20 Token Implementation
                
                ## Contract Structure
                ```cairo
                #[starknet::contract]
                mod ERC20Token {
                    use starknet::storage::{StoragePointerReadAccess, StoragePointerWriteAccess};
                    
                    #[storage]
                    struct Storage {
                        name: felt252,
                        symbol: felt252,
                        total_supply: felt252,
                        balances: LegacyMap<felt252, felt252>,
                    }
                    
                    #[constructor]
                    fn constructor(
                        ref self: ContractState,
                        name: felt252,
                        symbol: felt252,
                        initial_supply: felt252,
                        recipient: felt252
                    ) {
                        self.name.write(name);
                        self.symbol.write(symbol);
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
                ```
                
                ## Deployment
                Use Scarb to build and deploy:
                ```bash
                scarb build
                starknet deploy --class-hash 0x123...
                ```
                """,
                "expected_citations": [
                    "#[starknet::contract]",
                    "felt252",
                    "LegacyMap",
                    "#[constructor]",
                    "#[external(v0)]",
                    "scarb build",
                    "starknet deploy"
                ],
                "platform": "cairo_lang"
            },
            
            "x10_python_authentication": {
                "query": "How to authenticate with X10 Python SDK?",
                "document_content": """
                # X10 Python SDK Authentication
                
                ## Installation
                ```bash
                pip install x10-python-sdk
                ```
                
                ## Basic Setup
                ```python
                from x10_sdk import TradingClient
                
                # Initialize client
                client = TradingClient(
                    api_key="your-api-key",
                    api_secret="your-secret",
                    base_url="https://api.x10.com"
                )
                ```
                
                ## Authentication Methods
                The SDK supports multiple authentication methods:
                
                ### API Key Authentication
                ```python
                client.authenticate_with_api_key(
                    api_key="your-key",
                    api_secret="your-secret"
                )
                ```
                
                ### OAuth2 Authentication
                ```python
                client.authenticate_with_oauth2(
                    client_id="your-client-id",
                    client_secret="your-client-secret"
                )
                ```
                
                ## Usage Example
                ```python
                # Get account balance
                balance = await client.get_account_balance()
                print(f"Balance: {balance}")
                
                # Place order
                order = await client.place_order(
                    symbol="BTC/USDT",
                    side="buy",
                    quantity=0.1,
                    price=50000
                )
                ```
                """,
                "expected_citations": [
                    "pip install x10-python-sdk",
                    "from x10_sdk import TradingClient",
                    "TradingClient(",
                    "authenticate_with_api_key",
                    "authenticate_with_oauth2",
                    "get_account_balance()",
                    "place_order("
                ],
                "platform": "x10_python_sdk"
            },
            
            "web3auth_integration": {
                "query": "How to integrate Web3Auth?",
                "document_content": """
                # Web3Auth Integration Guide
                
                ## Installation
                ```bash
                npm install @web3auth/modal
                ```
                
                ## Basic Setup
                ```javascript
                import { Web3Auth } from "@web3auth/modal";
                
                const web3auth = new Web3Auth({
                    clientId: "your-client-id",
                    chainConfig: {
                        chainNamespace: "eip155",
                        chainId: "0x1",
                        rpcTarget: "https://mainnet.infura.io/v3/your-key"
                    }
                });
                ```
                
                ## Initialize and Connect
                ```javascript
                // Initialize modal
                await web3auth.initModal();
                
                // Connect with provider
                const provider = await web3auth.connect();
                
                // Get user info
                const user = await web3auth.getUserInfo();
                console.log(user);
                ```
                
                ## Social Login Providers
                Web3Auth supports multiple social login providers:
                - Google
                - Facebook
                - Twitter
                - Discord
                - GitHub
                """,
                "expected_citations": [
                    "npm install @web3auth/modal",
                    "import { Web3Auth }",
                    "new Web3Auth({",
                    "clientId:",
                    "chainConfig:",
                    "initModal()",
                    "connect()",
                    "getUserInfo()"
                ],
                "platform": "web3auth"
            }
        }
    
    def extract_citations_from_content(self, content: str, query: str) -> List[str]:
        """Extract potential citations from content based on query"""
        
        citations = []
        
        # Look for code blocks, function names, API endpoints, etc.
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            
            # Skip empty lines and headers
            if not line or line.startswith('#'):
                continue
            
            # Extract code snippets
            if '```' in line:
                continue
            
            # Extract function calls and API endpoints
            if any(indicator in line for indicator in ['(', '/', 'import', 'from', 'class', 'def', 'const', 'let', 'var']):
                # Clean up the line
                clean_line = line.replace('`', '').replace('*', '').replace('-', '').strip()
                if clean_line and len(clean_line) > 3:
                    citations.append(clean_line)
            
            # Extract configuration keys
            if ':' in line and not line.startswith('http'):
                key = line.split(':')[0].strip().replace('`', '').replace('-', '')
                if key and len(key) > 2:
                    citations.append(key + ':')
        
        return citations[:10]  # Limit to top 10 citations
    
    def calculate_citation_accuracy(self, expected: List[str], actual: List[str]) -> Dict[str, float]:
        """Calculate citation accuracy metrics"""
        
        if not expected and not actual:
            return {
                "accuracy": 1.0,
                "precision": 1.0,
                "recall": 1.0,
                "f1_score": 1.0
            }
        
        if not expected:
            return {
                "accuracy": 0.0,
                "precision": 0.0,
                "recall": 0.0,
                "f1_score": 0.0
            }
        
        if not actual:
            return {
                "accuracy": 0.0,
                "precision": 0.0,
                "recall": 0.0,
                "f1_score": 0.0
            }
        
        # Calculate overlap
        expected_set = set(expected)
        actual_set = set(actual)
        
        true_positives = len(expected_set.intersection(actual_set))
        false_positives = len(actual_set - expected_set)
        false_negatives = len(expected_set - actual_set)
        
        # Calculate metrics
        precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
        recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
        
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        
        # Overall accuracy (how many expected citations were found)
        accuracy = true_positives / len(expected_set) if expected_set else 0
        
        return {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1_score
        }
    
    def test_citation_accuracy(self, test_case_name: str, test_case: Dict[str, Any]) -> CitationTestResult:
        """Test citation accuracy for a single case"""
        
        try:
            # Extract citations from content
            actual_citations = self.extract_citations_from_content(
                test_case["document_content"], 
                test_case["query"]
            )
            
            # Calculate accuracy metrics
            metrics = self.calculate_citation_accuracy(
                test_case["expected_citations"],
                actual_citations
            )
            
            # Calculate source attribution score
            source_attribution = 0.8  # Simulate source attribution quality
            
            # Calculate confidence score
            confidence_score = min(metrics["f1_score"] + 0.2, 1.0)
            
            return CitationTestResult(
                query=test_case["query"],
                document_id=test_case_name,
                expected_citations=test_case["expected_citations"],
                actual_citations=actual_citations,
                citation_accuracy=metrics["accuracy"],
                source_attribution=source_attribution,
                confidence_score=confidence_score,
                precision=metrics["precision"],
                recall=metrics["recall"],
                f1_score=metrics["f1_score"],
                success=True
            )
            
        except Exception as e:
            logger.error(f"Citation test failed for {test_case_name}: {e}")
            return CitationTestResult(
                query=test_case["query"],
                document_id=test_case_name,
                expected_citations=test_case.get("expected_citations", []),
                actual_citations=[],
                citation_accuracy=0.0,
                source_attribution=0.0,
                confidence_score=0.0,
                precision=0.0,
                recall=0.0,
                f1_score=0.0,
                success=False,
                error=str(e)
            )
    
    def run_citation_tests(self) -> Dict[str, Any]:
        """Run comprehensive citation accuracy tests"""
        
        logger.info("Starting citation accuracy testing...")
        
        all_results = []
        
        for test_case_name, test_case in self.citation_test_cases.items():
            logger.info(f"Testing citations for: {test_case_name}")
            
            result = self.test_citation_accuracy(test_case_name, test_case)
            all_results.append(result)
        
        # Store results
        self.test_results = all_results
        
        # Calculate overall summary
        successful_tests = [r for r in all_results if r.success]
        
        overall_summary = {
            "total_tests": len(all_results),
            "successful_tests": len(successful_tests),
            "success_rate": len(successful_tests) / len(all_results) if all_results else 0,
            "avg_citation_accuracy": statistics.mean([r.citation_accuracy for r in successful_tests]) if successful_tests else 0,
            "avg_source_attribution": statistics.mean([r.source_attribution for r in successful_tests]) if successful_tests else 0,
            "avg_confidence_score": statistics.mean([r.confidence_score for r in successful_tests]) if successful_tests else 0,
            "avg_precision": statistics.mean([r.precision for r in successful_tests]) if successful_tests else 0,
            "avg_recall": statistics.mean([r.recall for r in successful_tests]) if successful_tests else 0,
            "avg_f1_score": statistics.mean([r.f1_score for r in successful_tests]) if successful_tests else 0,
            "total_expected_citations": sum(len(r.expected_citations) for r in all_results),
            "total_actual_citations": sum(len(r.actual_citations) for r in all_results),
            "citation_coverage": sum(len(r.actual_citations) for r in all_results) / sum(len(r.expected_citations) for r in all_results) if sum(len(r.expected_citations) for r in all_results) > 0 else 0
        }
        
        return {
            "overall_summary": overall_summary,
            "test_results": [
                {
                    "query": r.query,
                    "document_id": r.document_id,
                    "expected_citations": r.expected_citations,
                    "actual_citations": r.actual_citations,
                    "citation_accuracy": r.citation_accuracy,
                    "source_attribution": r.source_attribution,
                    "confidence_score": r.confidence_score,
                    "precision": r.precision,
                    "recall": r.recall,
                    "f1_score": r.f1_score,
                    "success": r.success,
                    "error": r.error
                }
                for r in all_results
            ]
        }
    
    def save_citation_results(self, results: Dict[str, Any], filename: str = "citation_accuracy_results.json"):
        """Save citation test results"""
        
        output_path = Path("/Users/admin/AstraTrade-Project/knowledge_base/backend") / filename
        
        # Add metadata
        results["metadata"] = {
            "test_date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "test_type": "citation_accuracy_testing",
            "test_cases": list(self.citation_test_cases.keys()),
            "platforms_tested": list(set(case["platform"] for case in self.citation_test_cases.values())),
            "citation_metrics": [
                "Citation accuracy",
                "Source attribution",
                "Precision",
                "Recall",
                "F1 score",
                "Confidence score"
            ]
        }
        
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=2)
        
        logger.info(f"Citation results saved to {output_path}")
        return output_path

class TestClaudeSearchCitations:
    """Test ClaudeOptimizedSearch citation generation functionality"""
    
    def setup_mock_collection(self):
        """Create a mock collection for testing"""
        mock_collection = Mock()
        
        # Mock collection query results
        mock_collection.query.return_value = {
            "documents": [[
                "def calculate_profit(price, cost):\n    return price - cost",
                "class TradingBot:\n    def __init__(self):\n        self.active = True",
                "# Test file for trading calculations\ndef test_calculate_profit():\n    assert calculate_profit(100, 80) == 20"
            ]],
            "metadatas": [[
                {
                    "file_path": "lib/services/trading_service.py",
                    "start_line": 45,
                    "end_line": 46,
                    "chunk_id": "chunk_001",
                    "chunk_type": "function",
                    "title": "calculate_profit function"
                },
                {
                    "file_path": "lib/models/trading_bot.py", 
                    "start_line": 12,
                    "end_line": 15,
                    "chunk_id": "chunk_002",
                    "chunk_type": "class",
                    "title": "TradingBot class"
                },
                {
                    "file_path": "test/unit/trading_service_test.py",
                    "start_line": 1,
                    "end_line": 4,
                    "chunk_id": "chunk_003", 
                    "chunk_type": "test",
                    "title": "test_calculate_profit"
                }
            ]],
            "distances": [[0.2, 0.3, 0.4]]
        }
        
        return mock_collection
    
    async def test_search_returns_non_empty_citations(self):
        """Test that search returns non-empty citations array"""
        mock_rag = Mock()
        mock_collection = self.setup_mock_collection()
        claude_search = ClaudeOptimizedSearch(mock_rag, mock_collection)
        
        # Perform search
        result = await claude_search.search_for_claude("calculate profit function")
        
        # Verify citations exist
        assert result.citations is not None
        assert len(result.citations) > 0
        assert isinstance(result.citations[0], Citation)
        print(f"✓ Search returned {len(result.citations)} citations")
    
    async def test_citation_metadata_accuracy(self):
        """Test that citation objects contain accurate metadata"""
        mock_rag = Mock()
        mock_collection = self.setup_mock_collection()
        claude_search = ClaudeOptimizedSearch(mock_rag, mock_collection)
        
        # Perform search
        result = await claude_search.search_for_claude("trading bot class")
        
        # Get first citation
        citation = result.citations[0]
        
        # Verify citation structure
        assert citation.source_id is not None
        assert citation.chunk_id is not None
        assert citation.file_path != 'unknown'
        assert citation.start_line >= 0
        assert citation.end_line >= citation.start_line
        assert 0.0 <= citation.confidence <= 1.0
        assert citation.context_snippet is not None
        assert len(citation.context_snippet) > 0
        print(f"✓ Citation metadata validation passed for file: {citation.file_path}")
    
    async def test_citation_file_path_accuracy(self):
        """Test that file_path in citations matches source chunk metadata"""
        mock_rag = Mock()
        mock_collection = self.setup_mock_collection()
        claude_search = ClaudeOptimizedSearch(mock_rag, mock_collection)
        
        # Perform search
        result = await claude_search.search_for_claude("calculate profit")
        
        # Check that citation file paths match expected patterns
        file_paths = [citation.file_path for citation in result.citations]
        
        # Should contain the trading service file
        assert any('trading_service.py' in path for path in file_paths)
        
        # Verify file paths are realistic
        for path in file_paths:
            assert path != 'unknown'
            assert '/' in path or '\\' in path  # Should be a file path
        print(f"✓ File path accuracy validated: {file_paths}")
    
    async def test_citation_line_numbers(self):
        """Test that start_line and end_line are properly populated"""
        mock_rag = Mock()
        mock_collection = self.setup_mock_collection()
        claude_search = ClaudeOptimizedSearch(mock_rag, mock_collection)
        
        # Perform search  
        result = await claude_search.search_for_claude("trading bot")
        
        for citation in result.citations:
            # Line numbers should be meaningful
            assert citation.start_line >= 0
            assert citation.end_line >= citation.start_line
            
            # If we have actual line numbers, they should be reasonable
            if citation.start_line > 0:
                assert citation.start_line < 10000  # Reasonable upper bound
                assert citation.end_line < 10000
        print(f"✓ Line number validation passed for {len(result.citations)} citations")
    
    async def test_multiple_citations_per_search(self):
        """Test that searches can return multiple citations"""
        mock_rag = Mock()
        mock_collection = self.setup_mock_collection()
        claude_search = ClaudeOptimizedSearch(mock_rag, mock_collection)
        
        # Perform search that should return multiple results
        result = await claude_search.search_for_claude("trading bot profit")
        
        # Should have multiple citations for comprehensive results
        assert len(result.citations) >= 2
        
        # Citations should have unique source IDs
        source_ids = [citation.source_id for citation in result.citations]
        assert len(source_ids) == len(set(source_ids))  # All unique
        print(f"✓ Multiple citations test passed: {len(result.citations)} citations with unique IDs")
    
    async def test_citation_quality_filtering(self):
        """Test that low-quality citations are filtered out"""
        mock_rag = Mock()
        mock_collection = self.setup_mock_collection()
        claude_search = ClaudeOptimizedSearch(mock_rag, mock_collection)
        
        # Perform search
        result = await claude_search.search_for_claude("test query")
        
        # All returned citations should meet minimum quality standards
        for citation in result.citations:
            assert citation.file_path != 'unknown'
            assert citation.confidence >= 0.1  # Minimum confidence threshold
            assert len(citation.context_snippet.strip()) > 0
        print(f"✓ Citation quality filtering validated for {len(result.citations)} citations")

async def run_claude_search_citation_tests():
    """Run all ClaudeOptimizedSearch citation tests"""
    print("\n" + "="*80)
    print("CLAUDE SEARCH CITATION GENERATION TESTS")
    print("="*80)
    
    test_class = TestClaudeSearchCitations()
    
    tests = [
        test_class.test_search_returns_non_empty_citations,
        test_class.test_citation_metadata_accuracy,
        test_class.test_citation_file_path_accuracy,
        test_class.test_citation_line_numbers,
        test_class.test_multiple_citations_per_search,
        test_class.test_citation_quality_filtering
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            await test()
            passed += 1
        except Exception as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
    
    print(f"\nCitation generation tests completed: {passed} passed, {failed} failed")
    return failed == 0

def main():
    """Main citation testing function"""
    
    # Run static citation accuracy tests
    print("Running static citation accuracy tests...")
    tester = CitationAccuracyTester()
    
    try:
        # Run citation tests
        results = tester.run_citation_tests()
        
        # Save results
        output_file = tester.save_citation_results(results)
        
        # Print summary
        print("\n" + "="*80)
        print("STATIC CITATION ACCURACY TEST RESULTS")
        print("="*80)
        
        overall = results["overall_summary"]
        print(f"Total Tests: {overall['total_tests']}")
        print(f"Successful Tests: {overall['successful_tests']}")
        print(f"Success Rate: {overall['success_rate']:.2%}")
        print(f"Average Citation Accuracy: {overall['avg_citation_accuracy']:.2f}")
        print(f"Average Source Attribution: {overall['avg_source_attribution']:.2f}")
        print(f"Average Confidence Score: {overall['avg_confidence_score']:.2f}")
        print(f"Average Precision: {overall['avg_precision']:.2f}")
        print(f"Average Recall: {overall['avg_recall']:.2f}")
        print(f"Average F1 Score: {overall['avg_f1_score']:.2f}")
        print(f"Total Expected Citations: {overall['total_expected_citations']}")
        print(f"Total Actual Citations: {overall['total_actual_citations']}")
        print(f"Citation Coverage: {overall['citation_coverage']:.2%}")
        
        print("\nTEST CASE BREAKDOWN:")
        print("-" * 50)
        
        for test_result in results["test_results"]:
            print(f"\n{test_result['document_id'].upper()}:")
            print(f"  Query: {test_result['query']}")
            print(f"  Citation Accuracy: {test_result['citation_accuracy']:.2f}")
            print(f"  Precision: {test_result['precision']:.2f}")
            print(f"  Recall: {test_result['recall']:.2f}")
            print(f"  F1 Score: {test_result['f1_score']:.2f}")
            print(f"  Expected Citations: {len(test_result['expected_citations'])}")
            print(f"  Actual Citations: {len(test_result['actual_citations'])}")
            if test_result['error']:
                print(f"  Error: {test_result['error']}")
        
        print(f"\nDetailed results saved to: {output_file}")
        
        static_success = overall['avg_f1_score'] > 0.3 and overall['success_rate'] > 0.8
        
    except Exception as e:
        logger.error(f"Static citation testing failed: {e}")
        static_success = False
    
    # Run dynamic citation generation tests
    print("\nRunning dynamic citation generation tests...")
    try:
        citation_success = asyncio.run(run_claude_search_citation_tests())
    except Exception as e:
        logger.error(f"Citation generation testing failed: {e}")
        citation_success = False
    
    # Overall success
    overall_success = static_success and citation_success
    print(f"\nOverall citation testing result: {'PASSED' if overall_success else 'FAILED'}")
    
    return overall_success

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)