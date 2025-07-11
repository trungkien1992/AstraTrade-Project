#!/usr/bin/env python3
"""
AstraTrade Enhanced RAG Backend
High-performance Python-based RAG service for AstraTrade trading platform
Integrates Extended Exchange API, X10 Python SDK, Starknet.dart SDK, and Cairo documentation

RAGFlow-inspired features:
- Deep document understanding
- Template-based chunking
- Grounded citations with reduced hallucinations
- Multi-modal content support
- Advanced search capabilities
"""

import os
import asyncio
import time
import hashlib
import logging
from typing import List, Optional, Dict, Any, Union
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, HTTPException, BackgroundTasks, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import uvicorn

# Vector database and embeddings
import chromadb
from sentence_transformers import SentenceTransformer
from chromadb.utils import embedding_functions

# Document processing
import requests
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

# Enhanced categorization and indexing
try:
    from categorization_system import categorize_document, get_all_categories, get_all_platforms
    from sdk_enhanced_indexer import EnhancedSDKIndexer
    from optimization_manager import RAGOptimizationManager, optimize_rag_system, get_rag_health
except ImportError:
    print("Warning: Some advanced modules not found. Using basic functionality.")
    categorize_document = lambda x: {"category": "general", "subcategory": "document"}
    get_all_categories = lambda: ["general", "api", "trading", "blockchain"]
    get_all_platforms = lambda: ["extended_exchange", "x10_python", "starknet_dart", "cairo"]

# Claude Code enhancements
from code_aware_chunker import CodeAwareChunker, CodeChunk, ChunkType
from claude_search import ClaudeOptimizedSearch, ClaudeSearchResult, ClaudeSearchAnalytics, Citation

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration - Enhanced for AstraTrade with RAGFlow features
RAG_CONFIG = {
    "chroma_db_path": "../system/chroma_db",
    "collection_name": "astratrade_knowledge_base",
    "embedding_model": "sentence-transformers/all-MiniLM-L6-v2",
    "chunk_size": 4000,              # Increased from 1000 for better Claude context
    "chunk_overlap": 800,            # Increased from 200 for better context continuity
    "max_results": 15,               # Increased from 10 for more comprehensive results
    "similarity_threshold": 0.7,
    "claude_context_size": 8000,     # Special large chunks for Claude
    "code_aware_chunking": True,     # Enable intelligent code chunking
    "template_chunking": True,       # RAGFlow-inspired template chunking
    "grounded_citations": True,      # RAGFlow-inspired grounded citations
    "quality_threshold": 0.7,        # Quality assessment threshold
    "deep_doc_understanding": True,  # RAGFlow-inspired deep document understanding
    "multi_modal_support": True,     # Support for heterogeneous data sources
    "platforms": [                   # AstraTrade supported platforms
        "extended_exchange",
        "x10_python_sdk", 
        "starknet_dart",
        "cairo_lang",
        "avnu_paymaster",
        "web3auth",
        "chipi_pay"
    ]
}

# Pydantic models
class QueryRequest(BaseModel):
    query: str
    max_results: Optional[int] = 5
    category: Optional[str] = None
    min_similarity: Optional[float] = 0.6

class QueryResponse(BaseModel):
    results: List[Dict[str, Any]]
    query_time: float
    total_results: int

class IndexRequest(BaseModel):
    force_reindex: bool = False

class IndexResponse(BaseModel):
    status: str
    documents_indexed: int
    time_taken: float

class StatsResponse(BaseModel):
    total_documents: int
    categories: Dict[str, int]
    last_updated: str
    embedding_model: str

@dataclass
class ProcessedDocument:
    content: str
    title: str
    category: str
    subcategory: Optional[str]
    metadata: Dict[str, Any]
    source_url: Optional[str] = None

class AstraTradeRAG:
    """High-performance RAG system for AstraTrade trading platform with RAGFlow features"""
    
    def __init__(self):
        self.chroma_client = None
        self.collection = None
        self.embedding_model = None
        self.text_splitter = None
        self.documents_indexed = 0
        self.last_updated = None
        self.document_cache = {}          # Cache for processed documents
        self.quality_assessor = None      # RAGFlow-inspired quality assessment
        self.citation_tracker = {}        # Track citations for grounded answers
        self.platform_indexers = {}       # Platform-specific indexers
        
    async def initialize(self):
        """Initialize the RAG system with RAGFlow-inspired features"""
        logger.info("🚀 Initializing AstraTrade RAG system with advanced features...")
        
        # Initialize ChromaDB
        self.chroma_client = chromadb.PersistentClient(path=RAG_CONFIG["chroma_db_path"])
        
        # Initialize embedding model
        self.embedding_model = SentenceTransformer(RAG_CONFIG["embedding_model"])
        
        # Create embedding function for ChromaDB
        embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=RAG_CONFIG["embedding_model"]
        )
        
        # Get or create collection
        try:
            self.collection = self.chroma_client.get_collection(
                name=RAG_CONFIG["collection_name"],
                embedding_function=embedding_function
            )
            logger.info(f"✅ Loaded existing collection: {RAG_CONFIG['collection_name']}")
        except Exception:
            self.collection = self.chroma_client.create_collection(
                name=RAG_CONFIG["collection_name"],
                embedding_function=embedding_function,
                metadata={
                    "description": "AstraTrade multi-platform trading knowledge base",
                    "platforms": RAG_CONFIG["platforms"],
                    "ragflow_features": {
                        "template_chunking": RAG_CONFIG["template_chunking"],
                        "grounded_citations": RAG_CONFIG["grounded_citations"],
                        "deep_doc_understanding": RAG_CONFIG["deep_doc_understanding"]
                    }
                }
            )
            logger.info(f"✅ Created new collection: {RAG_CONFIG['collection_name']}")
        
        # Initialize text splitter with RAGFlow-inspired improvements
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=RAG_CONFIG["chunk_size"],
            chunk_overlap=RAG_CONFIG["chunk_overlap"],
            separators=["\n\n", "\n", ". ", " ", ""],
            length_function=len,
            is_separator_regex=False
        )
        
        # Initialize platform-specific indexers
        self._initialize_platform_indexers()
        
        # Initialize quality assessor
        self._initialize_quality_assessor()
        
        # Get current stats
        count = self.collection.count()
        self.documents_indexed = count
        logger.info(f"📊 Current documents in collection: {count}")
        logger.info(f"🔧 RAGFlow features enabled: {list(RAG_CONFIG.keys())}")
        
    def _initialize_platform_indexers(self):
        """Initialize platform-specific indexers for AstraTrade"""
        self.platform_indexers = {
            "extended_exchange": ExtendedExchangeIndexer(),
            "x10_python_sdk": X10PythonSDKIndexer(),
            "starknet_dart": StarknetDartIndexer(),
            "cairo_lang": CairoLangIndexer(),
            "avnu_paymaster": AVNUPaymasterIndexer(),
            "web3auth": Web3AuthIndexer(),
            "chipi_pay": ChipiPayIndexer()
        }
        
    def _initialize_quality_assessor(self):
        """Initialize RAGFlow-inspired quality assessment"""
        self.quality_assessor = DocumentQualityAssessor(
            threshold=RAG_CONFIG["quality_threshold"],
            platforms=RAG_CONFIG["platforms"]
        )
        
    async def index_astratrade_documentation(self, force_reindex: bool = False) -> Dict[str, Any]:
        """Index all AstraTrade documentation with RAGFlow-inspired features"""
        start_time = datetime.now()
        
        if force_reindex:
            logger.info("🔄 Force reindexing - clearing existing collection...")
            self.collection.delete()
            embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
                model_name=RAG_CONFIG["embedding_model"]
            )
            self.collection = self.chroma_client.create_collection(
                name=RAG_CONFIG["collection_name"],
                embedding_function=embedding_function,
                metadata={
                    "description": "AstraTrade multi-platform trading knowledge base",
                    "platforms": RAG_CONFIG["platforms"],
                    "ragflow_features": {
                        "template_chunking": RAG_CONFIG["template_chunking"],
                        "grounded_citations": RAG_CONFIG["grounded_citations"],
                        "deep_doc_understanding": RAG_CONFIG["deep_doc_understanding"]
                    }
                }
            )
        
        # Collect documents from all platforms
        platform_results = await self._index_all_platforms()
        
        # Apply RAGFlow-inspired quality assessment
        quality_report = await self._assess_collection_quality()
        
        # Update stats
        total_docs = sum(platform_results.values())
        self.documents_indexed = total_docs
        self.last_updated = datetime.now().isoformat()
        
        time_taken = (datetime.now() - start_time).total_seconds()
        
        return {
            "status": "completed",
            "documents_indexed": total_docs,
            "platform_breakdown": platform_results,
            "quality_report": quality_report,
            "ragflow_features": {
                "template_chunking_applied": RAG_CONFIG["template_chunking"],
                "grounded_citations_enabled": RAG_CONFIG["grounded_citations"],
                "deep_doc_understanding": RAG_CONFIG["deep_doc_understanding"]
            },
            "time_taken": time_taken
        }
    
    async def _index_all_platforms(self) -> Dict[str, int]:
        """Index documentation from all AstraTrade platforms"""
        platform_results = {}
        
        for platform_name, indexer in self.platform_indexers.items():
            try:
                logger.info(f"🔍 Indexing {platform_name} documentation...")
                docs_count = await indexer.index_platform_docs(self)
                platform_results[platform_name] = docs_count
                logger.info(f"✅ Indexed {docs_count} documents from {platform_name}")
            except Exception as e:
                logger.error(f"❌ Failed to index {platform_name}: {str(e)}")
                platform_results[platform_name] = 0
        
        return platform_results
    
    async def _assess_collection_quality(self) -> Dict[str, Any]:
        """Assess the quality of the indexed collection - RAGFlow inspired"""
        if not self.quality_assessor:
            return {"status": "quality_assessor_not_initialized"}
        
        try:
            # Get sample of documents for quality assessment
            sample_results = self.collection.get(limit=100, include=["documents", "metadatas"])
            
            quality_metrics = {
                "total_documents": len(sample_results["documents"]),
                "platform_coverage": {},
                "chunk_quality_distribution": {},
                "citation_completeness": 0.0,
                "template_coverage": 0.0
            }
            
            # Analyze platform coverage
            for metadata in sample_results["metadatas"]:
                platform = metadata.get("platform", "unknown")
                quality_metrics["platform_coverage"][platform] = quality_metrics["platform_coverage"].get(platform, 0) + 1
            
            # Analyze chunk quality
            quality_scores = []
            for doc, metadata in zip(sample_results["documents"], sample_results["metadatas"]):
                quality_score = self.quality_assessor.assess_document_quality(doc, metadata)
                quality_scores.append(quality_score)
            
            if quality_scores:
                quality_metrics["average_quality_score"] = sum(quality_scores) / len(quality_scores)
                quality_metrics["high_quality_percentage"] = len([s for s in quality_scores if s > 0.8]) / len(quality_scores) * 100
            
            return quality_metrics
            
        except Exception as e:
            logger.error(f"Quality assessment failed: {str(e)}")
            return {"status": "assessment_failed", "error": str(e)}
    
    async def _collect_astratrade_documentation(self) -> List[ProcessedDocument]:
        """Collect all AstraTrade platform documentation with RAGFlow-inspired deep understanding"""
        documents = []
        
        # Manual documentation files
        documents.extend(await self._fetch_manual_docs())
        
        # Extended Exchange API documentation
        documents.extend(await self._fetch_extended_exchange_docs())
        
        # X10 Python SDK documentation
        documents.extend(await self._fetch_x10_python_docs())
        
        # Starknet.dart SDK documentation
        documents.extend(await self._fetch_starknet_dart_docs())
        
        # Cairo language documentation
        documents.extend(await self._fetch_cairo_docs())
        
        # AVNU Paymaster documentation
        documents.extend(await self._fetch_avnu_paymaster_docs())
        
        # Web3Auth documentation
        documents.extend(await self._fetch_web3auth_docs())
        
        # ChipiPay SDK documentation
        documents.extend(await self._fetch_chipi_pay_docs())
        
        return documents
    
    async def _fetch_manual_docs(self) -> List[ProcessedDocument]:
        """Fetch manual documentation files from the docs folder"""
        documents = []
        docs_path = Path("../docs/manual_docs")
        
        if docs_path.exists():
            for doc_file in docs_path.glob("*.md"):
                try:
                    content = doc_file.read_text(encoding='utf-8')
                    
                    # Apply deep document understanding
                    doc_type = self._detect_document_type(content, doc_file.name)
                    importance = self._assess_document_importance(content, doc_file.name)
                    
                    documents.append(ProcessedDocument(
                        content=content,
                        title=doc_file.stem.replace('_', ' ').title(),
                        category=doc_type["category"],
                        subcategory=doc_type["subcategory"],
                        metadata={
                            "source": "manual_docs",
                            "file_path": str(doc_file),
                            "importance": importance,
                            "doc_type": doc_type["type"],
                            "platform": doc_type["platform"],
                            "last_modified": doc_file.stat().st_mtime
                        }
                    ))
                    
                except Exception as e:
                    logger.error(f"Failed to process {doc_file}: {str(e)}")
        
        return documents
    
    def _detect_document_type(self, content: str, filename: str) -> Dict[str, str]:
        """Detect document type using RAGFlow-inspired analysis"""
        content_lower = content.lower()
        filename_lower = filename.lower()
        
        # Platform detection
        if "extended" in filename_lower and "api" in filename_lower:
            return {
                "category": "api_documentation",
                "subcategory": "extended_exchange",
                "type": "api_reference",
                "platform": "extended_exchange"
            }
        elif "x10" in filename_lower or "python" in filename_lower:
            return {
                "category": "sdk_documentation",
                "subcategory": "x10_python",
                "type": "sdk_reference",
                "platform": "x10_python_sdk"
            }
        elif "starknet" in filename_lower or "dart" in filename_lower:
            return {
                "category": "sdk_documentation",
                "subcategory": "starknet_dart",
                "type": "sdk_reference",
                "platform": "starknet_dart"
            }
        elif "cairo" in filename_lower:
            return {
                "category": "language_documentation",
                "subcategory": "cairo_lang",
                "type": "language_reference",
                "platform": "cairo_lang"
            }
        elif "avnu" in filename_lower or "paymaster" in filename_lower:
            return {
                "category": "integration_documentation",
                "subcategory": "avnu_paymaster",
                "type": "integration_guide",
                "platform": "avnu_paymaster"
            }
        elif "web3auth" in filename_lower:
            return {
                "category": "authentication_documentation",
                "subcategory": "web3auth",
                "type": "auth_reference",
                "platform": "web3auth"
            }
        elif "chipi" in filename_lower:
            return {
                "category": "payment_documentation",
                "subcategory": "chipi_pay",
                "type": "payment_reference",
                "platform": "chipi_pay"
            }
        else:
            return {
                "category": "general_documentation",
                "subcategory": "general",
                "type": "general_reference",
                "platform": "general"
            }
    
    def _assess_document_importance(self, content: str, filename: str) -> str:
        """Assess document importance using RAGFlow-inspired analysis"""
        content_lower = content.lower()
        
        # Critical indicators
        critical_indicators = ["api reference", "getting started", "authentication", "security", "deployment"]
        if any(indicator in content_lower for indicator in critical_indicators):
            return "critical"
        
        # High importance indicators
        high_indicators = ["integration", "configuration", "examples", "tutorial", "guide"]
        if any(indicator in content_lower for indicator in high_indicators):
            return "high"
        
        # Medium importance indicators
        medium_indicators = ["reference", "documentation", "sdk", "api"]
        if any(indicator in content_lower for indicator in medium_indicators):
            return "medium"
        
        return "low"
    
    async def _fetch_github_docs(self) -> List[ProcessedDocument]:
        """Fetch documentation from GitHub repository"""
        documents = []
        
        # GitHub API endpoints for starknet.dart
        base_url = "https://api.github.com/repos/focustree/starknet.dart"
        
        # README
        documents.append(ProcessedDocument(
            content=await self._fetch_github_file(f"{base_url}/contents/README.md"),
            title="Starknet.dart SDK README",
            category="overview",
            subcategory="readme",
            metadata={"source": "github", "importance": "critical"},
            source_url="https://github.com/focustree/starknet.dart/blob/main/README.md"
        ))
        
        # Documentation files
        doc_files = [
            "CONTRIBUTING.md",
            "CHANGELOG.md",
            "docs/getting-started.md",
            "docs/api-reference.md",
            "docs/examples.md",
        ]
        
        for file_path in doc_files:
            try:
                content = await self._fetch_github_file(f"{base_url}/contents/{file_path}")
                if content:
                    documents.append(ProcessedDocument(
                        content=content,
                        title=f"Starknet.dart {file_path}",
                        category="documentation",
                        subcategory=file_path.split("/")[-1].replace(".md", ""),
                        metadata={"source": "github", "file_path": file_path},
                        source_url=f"https://github.com/focustree/starknet.dart/blob/main/{file_path}"
                    ))
            except Exception as e:
                print(f"⚠️  Could not fetch {file_path}: {e}")
        
        return documents
    
    async def _fetch_github_file(self, url: str) -> Optional[str]:
        """Fetch a file from GitHub API"""
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data.get("content"):
                    import base64
                    content = base64.b64decode(data["content"]).decode("utf-8")
                    return content
        except Exception as e:
            print(f"Error fetching GitHub file: {e}")
        return None
    
    async def _fetch_pubdev_docs(self) -> List[ProcessedDocument]:
        """Fetch API documentation from pub.dev"""
        documents = []
        
        # API documentation from pub.dev
        packages = [
            "starknet",
            "starknet_provider",
            "wallet_kit",
            "secure_store",
            "avnu_paymaster_provider",
            "starknet_builder"
        ]
        
        for package in packages:
            try:
                # Fetch package info
                url = f"https://pub.dev/api/packages/{package}"
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    description = data.get("latest", {}).get("pubspec", {}).get("description", "")
                    
                    documents.append(ProcessedDocument(
                        content=f"Package: {package}\nDescription: {description}\n"
                                f"Latest Version: {data.get('latest', {}).get('version', '')}\n"
                                f"Published: {data.get('latest', {}).get('published', '')}\n"
                                f"Dependencies: {data.get('latest', {}).get('pubspec', {}).get('dependencies', {})}",
                        title=f"{package} Package Info",
                        category="packages",
                        subcategory=package,
                        metadata={"source": "pub.dev", "package": package},
                        source_url=f"https://pub.dev/packages/{package}"
                    ))
            except Exception as e:
                print(f"⚠️  Could not fetch package {package}: {e}")
        
        return documents
    
    async def _fetch_official_docs(self) -> List[ProcessedDocument]:
        """Fetch documentation from official website"""
        documents = []
        
        # Official documentation site content
        official_content = """
        Starknet.dart SDK Official Documentation
        
        The goal of this SDK is to be able to interact with StarkNet smart contracts in a type-safe way.
        You can also call the JSON-RPC endpoint exposed by the Starknet full nodes.
        
        The priority is to build the best possible Starknet SDK for dart applications,
        thus unlocking the era of Flutter mobile apps on Starknet.
        
        Supported Features:
        - Invoke transactions (versions 0, 1, 3)
        - Declare transactions (versions 1, 2, 3)
        - Deploy Account transactions (versions 1, 3)
        - JSON RPC version 0.7.1 support
        - Type-safe contract interactions
        - Mobile-first development approach
        
        Key Packages:
        - Starknet: Core SDK functionality
        - Starknet Provider: Network provider implementations
        - Wallet Kit: Wallet integration utilities
        - Secure Store: Secure storage for keys and credentials
        - Avnu Paymaster Provider: Paymaster integration
        - Starknet Builder: Development tools
        """
        
        documents.append(ProcessedDocument(
            content=official_content,
            title="Official Starknet.dart Documentation",
            category="documentation",
            subcategory="official",
            metadata={"source": "official_site", "importance": "critical"},
            source_url="https://starknetdart.dev"
        ))
        
        return documents
    
    async def _fetch_example_projects(self) -> List[ProcessedDocument]:
        """Fetch example project documentation"""
        documents = []
        
        examples = [
            {
                "title": "NFT Marketplace Example",
                "content": """
                Complete NFT marketplace implementation using Starknet.dart SDK.
                
                Features:
                - ERC-721 token standard
                - Minting and trading
                - Flutter mobile interface
                - Wallet integration
                - Smart contract deployment
                
                Architecture:
                - Cairo smart contracts
                - Flutter frontend with Riverpod
                - Starknet.dart SDK integration
                - Secure key management
                
                Usage:
                - Connect to Starknet testnet
                - Deploy NFT contracts
                - Mint and trade NFTs
                - Manage wallet accounts
                """,
                "category": "examples",
                "subcategory": "nft_marketplace"
            },
            {
                "title": "Mobile Wallet Example",
                "content": """
                Full-featured mobile wallet for Starknet.
                
                Features:
                - Account management
                - Token transfers
                - Transaction history
                - Secure storage
                - Biometric authentication
                
                Implementation:
                - Flutter cross-platform
                - Hardware-backed security
                - Multi-account support
                - Real-time balance updates
                - Push notifications
                
                Security:
                - Hardware security module
                - Biometric locks
                - Encrypted storage
                - Secure key derivation
                """,
                "category": "examples",
                "subcategory": "wallet"
            }
        ]
        
        for example in examples:
            documents.append(ProcessedDocument(
                content=example["content"],
                title=example["title"],
                category=example["category"],
                subcategory=example["subcategory"],
                metadata={"source": "examples", "complexity": "advanced"}
            ))
        
        return documents
    
    def _chunk_document(self, doc: ProcessedDocument) -> List[Dict[str, Any]]:
        """Chunk a document into smaller pieces"""
        chunks = self.text_splitter.split_text(doc.content)
        
        chunked_docs = []
        for i, chunk in enumerate(chunks):
            chunk_id = f"{doc.category}_{doc.subcategory}_{i}" if doc.subcategory else f"{doc.category}_{i}"
            
            chunked_docs.append({
                "id": chunk_id,
                "content": chunk,
                "metadata": {
                    "title": doc.title,
                    "category": doc.category,
                    "subcategory": doc.subcategory,
                    "chunk_index": i,
                    "total_chunks": len(chunks),
                    "source_url": doc.source_url,
                    **doc.metadata
                }
            })
        
        return chunked_docs
    
    async def _add_chunks_to_collection(self, chunks: List[Dict[str, Any]]):
        """Add document chunks to ChromaDB collection"""
        batch_size = 100
        
        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i + batch_size]
            
            ids = [chunk["id"] for chunk in batch]
            documents = [chunk["content"] for chunk in batch]
            metadatas = [chunk["metadata"] for chunk in batch]
            
            self.collection.add(
                ids=ids,
                documents=documents,
                metadatas=metadatas
            )
            
            print(f"✅ Added batch {i//batch_size + 1}/{(len(chunks) + batch_size - 1)//batch_size}")
    
    async def search(self, query: str, max_results: int = 5, category: str = None, 
                    min_similarity: float = 0.6) -> Dict[str, Any]:
        """Search the knowledge base"""
        start_time = datetime.now()
        
        # Prepare query filters
        where_filter = {}
        if category:
            where_filter["category"] = category
        
        # Perform vector search
        results = self.collection.query(
            query_texts=[query],
            n_results=max_results,
            where=where_filter if where_filter else None
        )
        
        # Process results
        processed_results = []
        if results["documents"] and results["documents"][0]:
            for i, doc in enumerate(results["documents"][0]):
                metadata = results["metadatas"][0][i] if results["metadatas"] else {}
                distance = results["distances"][0][i] if results["distances"] else 0
                similarity = 1 - distance  # Convert distance to similarity
                
                if similarity >= min_similarity:
                    processed_results.append({
                        "content": doc,
                        "title": metadata.get("title", "Unknown"),
                        "category": metadata.get("category", "Unknown"),
                        "subcategory": metadata.get("subcategory"),
                        "similarity": similarity,
                        "source_url": metadata.get("source_url"),
                        "metadata": metadata
                    })
        
        query_time = (datetime.now() - start_time).total_seconds()
        
        return {
            "results": processed_results,
            "query_time": query_time,
            "total_results": len(processed_results)
        }
    
    def get_stats(self) -> Dict[str, Any]:
        """Get knowledge base statistics"""
        total_docs = self.collection.count()
        
        # Get categories
        all_metadata = self.collection.get()["metadatas"]
        categories = {}
        for metadata in all_metadata:
            category = metadata.get("category", "unknown")
            categories[category] = categories.get(category, 0) + 1
        
        return {
            "total_documents": total_docs,
            "categories": categories,
            "last_updated": self.last_updated or "Never",
            "embedding_model": RAG_CONFIG["embedding_model"]
        }

# FastAPI application
app = FastAPI(
    title="Starknet.dart SDK RAG API",
    description="High-performance RAG service for Starknet.dart SDK knowledge base",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Platform-specific indexers for AstraTrade
class PlatformIndexer:
    """Base class for platform-specific indexers"""
    
    def __init__(self, platform_name: str):
        self.platform_name = platform_name
    
    async def index_platform_docs(self, rag_system) -> int:
        """Index documentation for this platform"""
        return 0

class ExtendedExchangeIndexer(PlatformIndexer):
    """Indexer for Extended Exchange API documentation"""
    
    def __init__(self):
        super().__init__("extended_exchange")
    
    async def index_platform_docs(self, rag_system) -> int:
        # Implementation for Extended Exchange API docs
        return await self._index_extended_exchange_docs(rag_system)
    
    async def _index_extended_exchange_docs(self, rag_system) -> int:
        """Index Extended Exchange API documentation"""
        docs_count = 0
        try:
            # Process Extended Exchange API documentation
            extended_api_content = """
            Extended Exchange API Documentation
            
            The Extended Exchange API provides comprehensive trading functionality for professional traders.
            
            Key Features:
            - Real-time market data streaming
            - Order management (place, cancel, modify)
            - Position tracking and management
            - Account balance and margin information
            - Historical data access
            - WebSocket and REST API endpoints
            
            Authentication:
            - API Key authentication required
            - Signature-based request signing
            - Rate limiting protection
            
            Supported Order Types:
            - Market orders
            - Limit orders
            - Stop orders
            - Stop-limit orders
            
            Risk Management:
            - Position limits
            - Daily loss limits
            - Margin requirements
            - Liquidation protection
            """
            
            doc = ProcessedDocument(
                content=extended_api_content,
                title="Extended Exchange API Documentation",
                category="api_documentation",
                subcategory="extended_exchange",
                metadata={
                    "platform": "extended_exchange",
                    "doc_type": "api_reference",
                    "importance": "critical",
                    "source": "extended_exchange_indexer"
                }
            )
            
            chunks = rag_system._chunk_document(doc)
            await rag_system._add_chunks_to_collection(chunks)
            docs_count += len(chunks)
            
        except Exception as e:
            logger.error(f"Failed to index Extended Exchange docs: {str(e)}")
        
        return docs_count

class X10PythonSDKIndexer(PlatformIndexer):
    """Indexer for X10 Python SDK documentation"""
    
    def __init__(self):
        super().__init__("x10_python_sdk")
    
    async def index_platform_docs(self, rag_system) -> int:
        return await self._index_x10_python_docs(rag_system)
    
    async def _index_x10_python_docs(self, rag_system) -> int:
        """Index X10 Python SDK documentation"""
        docs_count = 0
        try:
            x10_sdk_content = """
            X10 Python SDK Documentation
            
            The X10 Python SDK provides a comprehensive Python interface for the X10 trading platform.
            
            Installation:
            pip install x10-python-sdk
            
            Quick Start:
            from x10 import Client
            
            client = Client(api_key="your_api_key", secret="your_secret")
            
            # Get account balance
            balance = client.get_balance()
            
            # Place an order
            order = client.place_order(
                symbol="BTCUSD",
                side="buy",
                quantity=0.1,
                price=50000
            )
            
            Key Features:
            - Async/await support
            - Real-time data streaming
            - Order management
            - Position tracking
            - Risk management tools
            - Historical data access
            
            Error Handling:
            - Comprehensive exception handling
            - Retry mechanisms
            - Rate limit handling
            - Connection management
            """
            
            doc = ProcessedDocument(
                content=x10_sdk_content,
                title="X10 Python SDK Documentation",
                category="sdk_documentation",
                subcategory="x10_python",
                metadata={
                    "platform": "x10_python_sdk",
                    "doc_type": "sdk_reference",
                    "importance": "high",
                    "source": "x10_python_indexer"
                }
            )
            
            chunks = rag_system._chunk_document(doc)
            await rag_system._add_chunks_to_collection(chunks)
            docs_count += len(chunks)
            
        except Exception as e:
            logger.error(f"Failed to index X10 Python SDK docs: {str(e)}")
        
        return docs_count

class StarknetDartIndexer(PlatformIndexer):
    """Indexer for Starknet.dart SDK documentation"""
    
    def __init__(self):
        super().__init__("starknet_dart")
    
    async def index_platform_docs(self, rag_system) -> int:
        return await self._index_starknet_dart_docs(rag_system)
    
    async def _index_starknet_dart_docs(self, rag_system) -> int:
        """Index Starknet.dart SDK documentation"""
        docs_count = 0
        try:
            starknet_dart_content = """
            Starknet.dart SDK Documentation
            
            The Starknet.dart SDK enables Flutter/Dart applications to interact with the Starknet blockchain.
            
            Installation:
            dependencies:
              starknet: ^latest_version
            
            Quick Start:
            import 'package:starknet/starknet.dart';
            
            // Initialize provider
            final provider = JsonRpcProvider(nodeUrl: 'https://starknet-mainnet.public.blastapi.io');
            
            // Create account
            final account = Account(
              provider: provider,
              address: 'your_account_address',
              keyPair: KeyPair.fromPrivateKey('your_private_key')
            );
            
            Key Features:
            - Account management
            - Contract interactions
            - Transaction signing
            - Event filtering
            - Type-safe contract calls
            - Cairo contract compilation
            
            Smart Contract Interaction:
            - Contract deployment
            - Function calls
            - Event listening
            - State queries
            
            Security:
            - Hardware wallet support
            - Secure key management
            - Transaction verification
            - Network validation
            """
            
            doc = ProcessedDocument(
                content=starknet_dart_content,
                title="Starknet.dart SDK Documentation",
                category="sdk_documentation",
                subcategory="starknet_dart",
                metadata={
                    "platform": "starknet_dart",
                    "doc_type": "sdk_reference",
                    "importance": "high",
                    "source": "starknet_dart_indexer"
                }
            )
            
            chunks = rag_system._chunk_document(doc)
            await rag_system._add_chunks_to_collection(chunks)
            docs_count += len(chunks)
            
        except Exception as e:
            logger.error(f"Failed to index Starknet.dart SDK docs: {str(e)}")
        
        return docs_count

class CairoLangIndexer(PlatformIndexer):
    """Indexer for Cairo language documentation"""
    
    def __init__(self):
        super().__init__("cairo_lang")
    
    async def index_platform_docs(self, rag_system) -> int:
        return await self._index_cairo_docs(rag_system)
    
    async def _index_cairo_docs(self, rag_system) -> int:
        """Index Cairo language documentation"""
        docs_count = 0
        try:
            cairo_content = """
            Cairo Language Documentation
            
            Cairo is a programming language for writing provable programs, where one party can prove to another that 
            a certain computation was executed correctly.
            
            Key Concepts:
            - Provable computations
            - Zero-knowledge proofs
            - Starknet smart contracts
            - Efficient execution
            
            Basic Syntax:
            #[starknet::contract]
            mod HelloStarknet {
                #[storage]
                struct Storage {
                    balance: felt252,
                }
                
                #[external(v0)]
                fn increase_balance(ref self: ContractState, amount: felt252) {
                    self.balance.write(self.balance.read() + amount);
                }
                
                #[external(v0)]
                fn get_balance(self: @ContractState) -> felt252 {
                    self.balance.read()
                }
            }
            
            Smart Contract Development:
            - Contract interfaces
            - Storage management
            - External functions
            - Events and logging
            - Access control
            
            Testing:
            - Unit testing framework
            - Integration testing
            - Deployment testing
            - Performance testing
            """
            
            doc = ProcessedDocument(
                content=cairo_content,
                title="Cairo Language Documentation",
                category="language_documentation",
                subcategory="cairo_lang",
                metadata={
                    "platform": "cairo_lang",
                    "doc_type": "language_reference",
                    "importance": "high",
                    "source": "cairo_lang_indexer"
                }
            )
            
            chunks = rag_system._chunk_document(doc)
            await rag_system._add_chunks_to_collection(chunks)
            docs_count += len(chunks)
            
        except Exception as e:
            logger.error(f"Failed to index Cairo language docs: {str(e)}")
        
        return docs_count

class AVNUPaymasterIndexer(PlatformIndexer):
    """Indexer for AVNU Paymaster documentation"""
    
    def __init__(self):
        super().__init__("avnu_paymaster")
    
    async def index_platform_docs(self, rag_system) -> int:
        return 0  # Placeholder

class Web3AuthIndexer(PlatformIndexer):
    """Indexer for Web3Auth documentation"""
    
    def __init__(self):
        super().__init__("web3auth")
    
    async def index_platform_docs(self, rag_system) -> int:
        return 0  # Placeholder

class ChipiPayIndexer(PlatformIndexer):
    """Indexer for ChipiPay SDK documentation"""
    
    def __init__(self):
        super().__init__("chipi_pay")
    
    async def index_platform_docs(self, rag_system) -> int:
        return 0  # Placeholder

class DocumentQualityAssessor:
    """RAGFlow-inspired document quality assessment"""
    
    def __init__(self, threshold: float = 0.7, platforms: List[str] = None):
        self.threshold = threshold
        self.platforms = platforms or []
    
    def assess_document_quality(self, content: str, metadata: Dict[str, Any]) -> float:
        """Assess the quality of a document"""
        score = 0.0
        
        # Content length (25%)
        content_length = len(content)
        if 100 <= content_length <= 8000:
            score += 0.25
        elif content_length > 8000:
            score += 0.15
        elif content_length > 50:
            score += 0.1
        
        # Platform relevance (25%)
        platform = metadata.get("platform", "unknown")
        if platform in self.platforms:
            score += 0.25
        elif platform != "unknown":
            score += 0.15
        
        # Metadata completeness (25%)
        required_fields = ["title", "category", "doc_type", "importance"]
        completeness = sum(1 for field in required_fields if metadata.get(field)) / len(required_fields)
        score += completeness * 0.25
        
        # Content structure (25%)
        structure_indicators = ["#", "##", "```", "*", "-", "1."]
        structure_score = min(1.0, sum(1 for indicator in structure_indicators if indicator in content) / len(structure_indicators))
        score += structure_score * 0.25
        
        return min(1.0, score)

# Initialize RAG system
rag_system = AstraTradeRAG()

# Initialize Claude Code enhancements
code_chunker = None
claude_search = None
search_analytics = ClaudeSearchAnalytics()

@app.on_event("startup")
async def startup_event():
    """Initialize RAG system on startup"""
    await rag_system.initialize()
    
    # Initialize Claude Code enhancements
    global code_chunker, claude_search
    code_chunker = CodeAwareChunker(RAG_CONFIG)
    claude_search = ClaudeOptimizedSearch(rag_system, rag_system.collection, code_chunker)
    
    print("✅ Claude Code enhancements initialized")

@app.get("/", response_model=Dict[str, str])
async def root():
    """Root endpoint"""
    return {
        "service": "Starknet.dart SDK RAG API",
        "version": "1.0.0",
        "status": "running"
    }

@app.post("/index", response_model=IndexResponse)
async def index_documentation(request: IndexRequest, background_tasks: BackgroundTasks):
    """Index SDK documentation"""
    background_tasks.add_task(rag_system.index_sdk_documentation, request.force_reindex)
    return IndexResponse(
        status="started",
        documents_indexed=0,
        time_taken=0.0
    )

@app.post("/search", response_model=QueryResponse)
async def search_knowledge_base(request: QueryRequest):
    """Search the knowledge base"""
    result = await rag_system.search(
        query=request.query,
        max_results=request.max_results,
        category=request.category,
        min_similarity=request.min_similarity
    )
    
    return QueryResponse(
        results=result["results"],
        query_time=result["query_time"],
        total_results=result["total_results"]
    )

@app.get("/stats", response_model=StatsResponse)
async def get_stats():
    """Get knowledge base statistics"""
    stats = rag_system.get_stats()
    return StatsResponse(
        total_documents=stats["total_documents"],
        categories=stats["categories"],
        last_updated=stats["last_updated"],
        embedding_model=stats["embedding_model"]
    )

@app.get("/categories")
async def get_categories():
    """Get all available categories from the enhanced categorization system"""
    return {
        "categories": get_all_categories(),
        "platforms": get_all_platforms(),
        "current_stats": rag_system.get_stats()["categories"]
    }

@app.get("/platforms")
async def get_platforms():
    """Get all available platforms"""
    return {"platforms": get_all_platforms()}

@app.post("/search/advanced")
async def advanced_search(request: QueryRequest):
    """Advanced search with enhanced filtering"""
    result = await rag_system.search(
        query=request.query,
        max_results=request.max_results,
        category=request.category,
        min_similarity=request.min_similarity
    )
    
    # Add enhanced metadata to results
    enhanced_results = []
    for doc in result["results"]:
        enhanced_doc = doc.copy()
        enhanced_doc["enhanced_metadata"] = {
            "platform": enhanced_doc.get("metadata", {}).get("platform", "unknown"),
            "doc_type": enhanced_doc.get("metadata", {}).get("doc_type", "unknown"),
            "importance": enhanced_doc.get("metadata", {}).get("importance", "medium"),
            "complexity": enhanced_doc.get("metadata", {}).get("complexity", "intermediate"),
            "tags": enhanced_doc.get("metadata", {}).get("tags", [])
        }
        enhanced_results.append(enhanced_doc)
    
    return QueryResponse(
        results=enhanced_results,
        query_time=result["query_time"],
        total_results=result["total_results"]
    )

@app.get("/search/suggestions")
async def get_search_suggestions(query: str = ""):
    """Get intelligent search suggestions"""
    if not query:
        return {
            "suggestions": [
                "How to create account",
                "Trading API authentication",
                "Place order with X10 SDK",
                "Cairo smart contract deployment",
                "WebSocket market data",
                "NFT marketplace example",
                "Error handling best practices",
                "Starknet.dart mobile integration"
            ]
        }
    
    # Generate contextual suggestions based on query
    suggestions = []
    query_lower = query.lower()
    
    if "account" in query_lower:
        suggestions.extend([
            "Create account with X10 SDK",
            "Account management Starknet.dart",
            "Deploy account Cairo contract",
            "Account authentication Extended Exchange"
        ])
    elif "order" in query_lower:
        suggestions.extend([
            "Place limit order",
            "Cancel order API",
            "Order types Extended Exchange",
            "Order management best practices"
        ])
    elif "contract" in query_lower:
        suggestions.extend([
            "Deploy Cairo smart contract",
            "ERC20 token contract",
            "Contract testing with Forge",
            "OpenZeppelin contracts"
        ])
    else:
        suggestions.extend([
            f"{query} tutorial",
            f"{query} example",
            f"{query} API reference",
            f"How to {query}"
        ])
    
    return {"suggestions": suggestions[:8]}

@app.post("/optimize")
async def optimize_system(background_tasks: BackgroundTasks):
    """Trigger system optimization"""
    background_tasks.add_task(optimize_rag_system, rag_system.chroma_client, RAG_CONFIG["collection_name"])
    return {"status": "optimization_started", "message": "System optimization running in background"}

@app.get("/health/detailed")
async def get_detailed_health():
    """Get detailed system health report"""
    try:
        health_report = await get_rag_health(rag_system.chroma_client, RAG_CONFIG["collection_name"])
        return health_report
    except Exception as e:
        return {
            "status": "error",
            "message": f"Health check failed: {str(e)}"
        }

@app.get("/metrics")
async def get_system_metrics():
    """Get comprehensive system metrics"""
    stats = rag_system.get_stats()
    
    # Get platform breakdown
    platform_stats = {}
    if rag_system.collection:
        results = rag_system.collection.get(include=['metadatas'])
        metadatas = results['metadatas'] if results['metadatas'] else []
        
        for metadata in metadatas:
            platform = metadata.get('platform', 'unknown')
            platform_stats[platform] = platform_stats.get(platform, 0) + 1
    
    return {
        "total_documents": stats["total_documents"],
        "categories": stats["categories"],
        "platform_breakdown": platform_stats,
        "embedding_model": stats["embedding_model"],
        "last_updated": stats["last_updated"],
        "available_platforms": get_all_platforms(),
        "available_categories": get_all_categories()
    }

# Claude Code Enhancement Endpoints

@app.post("/search/claude")
async def search_for_claude_code(request: QueryRequest):
    """Claude-optimized search endpoint with larger context and intelligent chunking"""
    if not claude_search:
        raise HTTPException(status_code=503, detail="Claude search not initialized")
    
    start_time = time.time()
    
    try:
        result = await claude_search.search_for_claude(
            query=request.query,
            context_type=request.category or "development",
            max_context_size=RAG_CONFIG['claude_context_size']
        )
        
        # Log search for analytics
        search_analytics.log_search(
            query=request.query,
            intent=result.query_type,
            results_count=len(result.results),
            search_time=result.search_time
        )
        
        return {
            "results": result.results,
            "total_context_size": result.total_context_size,
            "query_type": result.query_type,
            "related_files": result.related_files,
            "cross_references": result.cross_references,
            "development_context": result.development_context,
            "search_time": result.search_time,
            "optimized_for": "claude_code_sonnet_4",
            "enhancement_status": "active"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Claude search failed: {str(e)}")

@app.post("/index/code_aware")
async def index_with_code_awareness(background_tasks: BackgroundTasks):
    """Re-index with code-aware chunking for better Claude context"""
    if not code_chunker:
        raise HTTPException(status_code=503, detail="Code chunker not initialized")
    
    background_tasks.add_task(reindex_with_code_aware_chunking)
    return {
        "status": "started", 
        "message": "Code-aware indexing initiated",
        "enhancement": "claude_code_chunking",
        "expected_improvements": [
            "4x larger chunk sizes",
            "Language-specific parsing",
            "Preserved code structure",
            "Better function/class grouping"
        ]
    }

@app.get("/claude/status")
async def get_claude_optimization_status():
    """Get status of Claude Code optimizations"""
    return {
        "claude_enhancements": {
            "chunk_size": RAG_CONFIG['chunk_size'],
            "claude_context_size": RAG_CONFIG['claude_context_size'],
            "code_aware_chunking": RAG_CONFIG['code_aware_chunking'],
            "max_results": RAG_CONFIG['max_results']
        },
        "components_initialized": {
            "code_chunker": code_chunker is not None,
            "claude_search": claude_search is not None,
            "search_analytics": True
        },
        "usage_analytics": search_analytics.get_insights(),
        "optimization_level": "high_performance",
        "target_model": "claude_sonnet_4"
    }

@app.get("/claude/analytics")
async def get_claude_analytics():
    """Get Claude Code usage analytics and insights"""
    return {
        "analytics": search_analytics.get_insights(),
        "system_performance": {
            "average_context_size": RAG_CONFIG['claude_context_size'],
            "chunk_overlap": RAG_CONFIG['chunk_overlap'],
            "supported_languages": ["python", "dart", "cairo", "markdown", "json", "yaml"]
        },
        "optimization_suggestions": [
            "Use specific file paths in queries for better context",
            "Include intent keywords (debug, feature, refactor, test)",
            "Combine related concepts in single queries",
            "Use technical terminology for better matching"
        ]
    }

@app.post("/claude/suggest_files")
async def suggest_files_for_query(request: QueryRequest):
    """Get file suggestions based on query and development intent"""
    if not claude_search:
        raise HTTPException(status_code=503, detail="Claude search not initialized")
    
    intent = claude_search._analyze_query_intent(request.query)
    keywords = claude_search._extract_technical_keywords(request.query)
    
    suggestions = await claude_search.get_file_suggestions(request.query, intent)
    
    return {
        "query": request.query,
        "detected_intent": intent,
        "keywords": keywords,
        "suggested_files": suggestions,
        "search_strategy": f"Optimized for {intent} workflow",
        "next_steps": [
            f"Search for specific files: {', '.join(suggestions[:3])}",
            f"Use intent-specific keywords: {intent}",
            "Include file extensions for precise matching"
        ]
    }

# Background task functions

async def reindex_with_code_aware_chunking():
    """Background task to re-index the collection with code-aware chunking"""
    try:
        print("🔄 Starting code-aware re-indexing...")
        
        # Get all existing documents
        existing_docs = rag_system.collection.get(include=['documents', 'metadatas'])
        
        if not existing_docs['documents']:
            print("⚠️ No documents found to re-index")
            return
        
        # Clear collection for fresh indexing
        rag_system.collection.delete()
        
        # Re-create collection
        embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=RAG_CONFIG["embedding_model"]
        )
        rag_system.collection = rag_system.chroma_client.create_collection(
            name=RAG_CONFIG["collection_name"],
            embedding_function=embedding_function,
            metadata={"description": "Code-aware chunked knowledge base for Claude Code"}
        )
        
        total_docs = 0
        
        # Process each document with code-aware chunking
        for i, (doc_content, metadata) in enumerate(zip(existing_docs['documents'], existing_docs['metadatas'])):
            file_path = metadata.get('file_path', f'document_{i}')
            
            # Use code-aware chunking
            if code_chunker:
                chunks = code_chunker.chunk_for_claude_context(file_path, doc_content)
            else:
                # Fallback to larger standard chunks
                text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=RAG_CONFIG["chunk_size"],
                    chunk_overlap=RAG_CONFIG["chunk_overlap"]
                )
                chunk_texts = text_splitter.split_text(doc_content)
                chunks = [
                    CodeChunk(
                        content=chunk_text,
                        metadata=metadata,
                        start_line=1,
                        end_line=len(chunk_text.split('\n')),
                        chunk_type='generic',
                        language='unknown'
                    ) for chunk_text in chunk_texts
                ]
            
            # Add chunks to collection
            for j, chunk in enumerate(chunks):
                chunk_id = f"code_aware_{i}_{j}"
                
                # Enhance metadata with code-aware information
                enhanced_metadata = {
                    **metadata,
                    'chunk_id': chunk_id,
                    'chunk_type': chunk.chunk_type,
                    'language': chunk.language,
                    'importance': chunk.importance,
                    'start_line': chunk.start_line,
                    'end_line': chunk.end_line,
                    'claude_optimized': True,
                    'chunk_size': len(chunk.content)
                }
                
                rag_system.collection.add(
                    ids=[chunk_id],
                    documents=[chunk.content],
                    metadatas=[enhanced_metadata]
                )
                
                total_docs += 1
        
        print(f"✅ Code-aware re-indexing completed: {total_docs} chunks indexed")
        return {"status": "completed", "total_chunks": total_docs}
        
    except Exception as e:
        print(f"❌ Code-aware re-indexing failed: {e}")
        return {"status": "failed", "error": str(e)}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )