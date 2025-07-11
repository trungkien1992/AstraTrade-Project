#!/usr/bin/env python3
"""
Configuration module for AstraTrade RAG system
"""

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