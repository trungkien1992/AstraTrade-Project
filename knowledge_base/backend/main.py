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

import time
import logging
from typing import Dict, Any
from chromadb.utils import embedding_functions
from langchain.text_splitter import RecursiveCharacterTextSplitter

from fastapi import FastAPI, HTTPException, BackgroundTasks, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Local imports
from config import RAG_CONFIG
from models import QueryRequest, QueryResponse, IndexRequest, IndexResponse, StatsResponse
from rag_system import AstraTradeRAG

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
    background_tasks.add_task(rag_system.index_astratrade_documentation, request.force_reindex)
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