#!/usr/bin/env python3
"""
Comprehensive Multi-Platform RAG System Testing
Test suite for enhanced AstraTrade RAG system with multi-platform support
"""

import asyncio
import json
import logging
import time
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from pathlib import Path
import statistics

# Import enhanced RAG components
from main import AstraTradeRAG
from categorization_system import AstraTradeCategorizer, DocumentCategory, PlatformType
from optimization_manager import RAGOptimizationManager
from claude_search import ClaudeOptimizedSearch

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class TestResult:
    """Test result for RAG system testing"""
    query: str
    platform: str
    expected_category: str
    response_time: float
    similarity_score: float
    result_count: int
    citations_count: int
    quality_score: float
    success: bool
    error: Optional[str] = None

class ComprehensiveRAGTester:
    """Comprehensive testing suite for enhanced RAG system"""
    
    def __init__(self):
        self.rag_system = None
        self.categorizer = AstraTradeCategorizer()
        self.optimizer = None
        self.test_results: List[TestResult] = []
        
        # Multi-platform test queries
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
        
        # Expected categories for validation
        self.expected_categories = {
            "extended_exchange": ["trading_api", "authentication", "market_data", "api_reference"],
            "x10_python_sdk": ["python_sdk", "trading_api", "authentication", "example_code"],
            "starknet_dart": ["dart_sdk", "wallet_integration", "smart_contract", "flutter_sdk"],
            "cairo_lang": ["cairo_lang", "smart_contract", "example_code", "best_practices"],
            "avnu_paymaster": ["paymaster", "starknet", "smart_contract", "configuration"],
            "web3auth": ["authentication", "wallet_integration", "web3_sdk", "tutorial"],
            "chipi_pay": ["payment", "api_reference", "webhook", "configuration"]
        }
    
    async def setup_rag_system(self):
        """Setup RAG system for testing"""
        try:
            logger.info("Setting up enhanced RAG system...")
            
            # Initialize RAG system
            self.rag_system = AstraTradeRAG()
            await self.rag_system.initialize()
            
            # Initialize optimizer
            self.optimizer = RAGOptimizationManager(
                chroma_client=self.rag_system.chroma_client,
                collection_name="astratrade_knowledge_base"
            )
            
            logger.info("RAG system setup completed successfully")
            return True
            
        except Exception as e:
            logger.error(f"Failed to setup RAG system: {e}")
            return False
    
    async def run_platform_tests(self, platform: str, queries: List[str]) -> List[TestResult]:
        """Run tests for a specific platform"""
        
        logger.info(f"Testing platform: {platform}")
        platform_results = []
        
        for query in queries:
            try:
                start_time = time.time()
                
                # Perform search
                search_results = await self.rag_system.search(
                    query=query,
                    max_results=5,
                    min_similarity=0.25
                )
                
                response_time = time.time() - start_time
                
                # Analyze results
                result_count = len(search_results.get('results', []))
                citations_count = len(search_results.get('citations', []))
                
                # Calculate average similarity score
                similarity_scores = [r.get('similarity', 0.0) for r in search_results.get('results', [])]
                avg_similarity = statistics.mean(similarity_scores) if similarity_scores else 0.0
                
                # Calculate quality score
                quality_score = self._calculate_quality_score(search_results, platform)
                
                # Validate category detection
                expected_cats = self.expected_categories.get(platform, [])
                detected_category = self._detect_result_category(search_results)
                success = detected_category in expected_cats if expected_cats else True
                
                # Log query performance
                self.optimizer.log_query_performance(
                    query=query,
                    response_time=response_time,
                    similarity_score=avg_similarity,
                    result_count=result_count,
                    platform=platform,
                    category=detected_category
                )
                
                # Create test result
                test_result = TestResult(
                    query=query,
                    platform=platform,
                    expected_category=detected_category,
                    response_time=response_time,
                    similarity_score=avg_similarity,
                    result_count=result_count,
                    citations_count=citations_count,
                    quality_score=quality_score,
                    success=success
                )
                
                platform_results.append(test_result)
                logger.info(f"Query '{query[:50]}...' - Results: {result_count}, Time: {response_time:.2f}s")
                
            except Exception as e:
                error_result = TestResult(
                    query=query,
                    platform=platform,
                    expected_category="error",
                    response_time=0.0,
                    similarity_score=0.0,
                    result_count=0,
                    citations_count=0,
                    quality_score=0.0,
                    success=False,
                    error=str(e)
                )
                platform_results.append(error_result)
                logger.error(f"Query '{query[:50]}...' failed: {e}")
        
        return platform_results
    
    def _calculate_quality_score(self, search_results: Dict[str, Any], platform: str) -> float:
        """Calculate quality score for search results"""
        
        results = search_results.get('results', [])
        if not results:
            return 0.0
        
        # Factors for quality assessment
        similarity_scores = [r.get('similarity', 0.0) for r in results]
        avg_similarity = statistics.mean(similarity_scores)
        
        # Check for platform-specific content
        platform_matches = 0
        for result in results:
            content = result.get('content', '').lower()
            if platform.replace('_', ' ') in content:
                platform_matches += 1
        
        platform_relevance = platform_matches / len(results)
        
        # Check for citations
        citations = search_results.get('citations', [])
        citation_score = min(len(citations) / 3, 1.0)  # Normalize to 1.0
        
        # Calculate weighted quality score
        quality_score = (
            avg_similarity * 0.5 +
            platform_relevance * 0.3 +
            citation_score * 0.2
        )
        
        return quality_score
    
    def _detect_result_category(self, search_results: Dict[str, Any]) -> str:
        """Detect the category of search results"""
        
        results = search_results.get('results', [])
        if not results:
            return "unknown"
        
        # Use categorizer to detect category from first result
        first_result = results[0]
        content = first_result.get('content', '')
        
        categorization = self.categorizer.categorize_document(content)
        return categorization.category.value
    
    async def run_comprehensive_tests(self) -> Dict[str, Any]:
        """Run comprehensive tests across all platforms"""
        
        logger.info("Starting comprehensive multi-platform RAG testing...")
        
        # Setup RAG system
        setup_success = await self.setup_rag_system()
        if not setup_success:
            return {"error": "Failed to setup RAG system", "results": []}
        
        # Run tests for each platform
        all_results = []
        platform_summaries = {}
        
        for platform, queries in self.test_queries.items():
            platform_results = await self.run_platform_tests(platform, queries)
            all_results.extend(platform_results)
            
            # Calculate platform summary
            successful_tests = [r for r in platform_results if r.success]
            platform_summaries[platform] = {
                "total_tests": len(platform_results),
                "successful_tests": len(successful_tests),
                "success_rate": len(successful_tests) / len(platform_results) if platform_results else 0,
                "avg_response_time": statistics.mean([r.response_time for r in platform_results if r.response_time > 0]) if platform_results else 0,
                "avg_similarity": statistics.mean([r.similarity_score for r in platform_results if r.similarity_score > 0]) if platform_results else 0,
                "avg_quality": statistics.mean([r.quality_score for r in platform_results if r.quality_score > 0]) if platform_results else 0
            }
        
        # Store results
        self.test_results = all_results
        
        # Generate overall summary
        successful_tests = [r for r in all_results if r.success]
        overall_summary = {
            "total_tests": len(all_results),
            "successful_tests": len(successful_tests),
            "overall_success_rate": len(successful_tests) / len(all_results) if all_results else 0,
            "avg_response_time": statistics.mean([r.response_time for r in all_results if r.response_time > 0]) if all_results else 0,
            "avg_similarity_score": statistics.mean([r.similarity_score for r in all_results if r.similarity_score > 0]) if all_results else 0,
            "avg_quality_score": statistics.mean([r.quality_score for r in all_results if r.quality_score > 0]) if all_results else 0,
            "total_citations": sum(r.citations_count for r in all_results),
            "avg_results_per_query": statistics.mean([r.result_count for r in all_results]) if all_results else 0
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
                "popular_queries": optimization_metrics.popular_queries,
                "optimization_suggestions": optimization_metrics.optimization_suggestions
            },
            "test_results": [
                {
                    "query": r.query,
                    "platform": r.platform,
                    "response_time": r.response_time,
                    "similarity_score": r.similarity_score,
                    "result_count": r.result_count,
                    "citations_count": r.citations_count,
                    "quality_score": r.quality_score,
                    "success": r.success,
                    "error": r.error
                }
                for r in all_results
            ]
        }
    
    def save_test_results(self, results: Dict[str, Any], filename: str = "rag_test_results.json"):
        """Save test results to file"""
        
        output_path = Path(__file__).parent / filename
        
        # Add metadata
        results["metadata"] = {
            "test_date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "total_platforms": len(self.test_queries),
            "total_queries": sum(len(queries) for queries in self.test_queries.values()),
            "enhanced_features": [
                "Multi-platform support (7 platforms)",
                "Template-based chunking",
                "Grounded citations",
                "Quality assessment",
                "4x larger context windows",
                "Claude Code optimization"
            ]
        }
        
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=2)
        
        logger.info(f"Test results saved to {output_path}")
        return output_path

async def main():
    """Main testing function"""
    
    tester = ComprehensiveRAGTester()
    
    try:
        # Run comprehensive tests
        results = await tester.run_comprehensive_tests()
        
        # Save results
        output_file = tester.save_test_results(results)
        
        # Print summary
        print("\n" + "="*80)
        print("COMPREHENSIVE RAG SYSTEM TEST RESULTS")
        print("="*80)
        
        overall = results["overall_summary"]
        print(f"Total Tests: {overall['total_tests']}")
        print(f"Successful Tests: {overall['successful_tests']}")
        print(f"Success Rate: {overall['overall_success_rate']:.2%}")
        print(f"Average Response Time: {overall['avg_response_time']:.2f}s")
        print(f"Average Similarity Score: {overall['avg_similarity_score']:.2f}")
        print(f"Average Quality Score: {overall['avg_quality_score']:.2f}")
        print(f"Total Citations Generated: {overall['total_citations']}")
        print(f"Average Results per Query: {overall['avg_results_per_query']:.1f}")
        
        print("\nPLATFORM BREAKDOWN:")
        print("-" * 50)
        
        for platform, summary in results["platform_summaries"].items():
            print(f"{platform.upper()}: {summary['success_rate']:.1%} success "
                  f"({summary['successful_tests']}/{summary['total_tests']} tests)")
            print(f"  Response Time: {summary['avg_response_time']:.2f}s")
            print(f"  Similarity: {summary['avg_similarity']:.2f}")
            print(f"  Quality: {summary['avg_quality']:.2f}")
            print()
        
        print("\nOPTIMIZATION INSIGHTS:")
        print("-" * 50)
        
        opt_metrics = results["optimization_metrics"]
        print(f"Query Performance: {opt_metrics['avg_response_time']:.2f}s average")
        print(f"Search Accuracy: {opt_metrics['avg_similarity_score']:.2f} similarity")
        print(f"Error Rate: {opt_metrics['error_rate']:.2%}")
        
        if opt_metrics['popular_queries']:
            print(f"Popular Queries: {len(opt_metrics['popular_queries'])} identified")
        
        if opt_metrics['optimization_suggestions']:
            print(f"Optimization Suggestions: {len(opt_metrics['optimization_suggestions'])} generated")
        
        print(f"\nDetailed results saved to: {output_file}")
        
        # Return success/failure
        return overall['overall_success_rate'] > 0.8  # 80% success rate threshold
        
    except Exception as e:
        logger.error(f"Testing failed: {e}")
        return False

if __name__ == "__main__":
    success = asyncio.run(main())
    exit(0 if success else 1)