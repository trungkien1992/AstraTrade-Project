#!/usr/bin/env python3
"""
Configuration module for AstraTrade RAG system
"""

from typing import List
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class RAGSettings(BaseSettings):
    """AstraTrade RAG system settings with environment variable support"""
    
    # Core configuration
    chroma_db_path: str = Field(default="../system/chroma_db", description="Path to ChromaDB storage")
    collection_name: str = Field(default="astratrade_knowledge_base", description="ChromaDB collection name")
    embedding_model: str = Field(default="sentence-transformers/all-MiniLM-L6-v2", description="Embedding model name")
    
    # Security
    api_key: str = Field(description="API key for securing endpoints")
    
    # Chunking configuration
    chunk_size: int = Field(default=4000, description="Text chunk size for processing")
    chunk_overlap: int = Field(default=800, description="Overlap between chunks")
    
    # Search configuration
    max_results: int = Field(default=15, description="Maximum search results")
    similarity_threshold: float = Field(default=0.7, description="Minimum similarity threshold")
    
    # Claude-specific configuration
    claude_context_size: int = Field(default=8000, description="Special large chunks for Claude")
    
    # RAGFlow-inspired features
    code_aware_chunking: bool = Field(default=True, description="Enable intelligent code chunking")
    template_chunking: bool = Field(default=True, description="RAGFlow-inspired template chunking")
    grounded_citations: bool = Field(default=True, description="RAGFlow-inspired grounded citations")
    quality_threshold: float = Field(default=0.7, description="Quality assessment threshold")
    deep_doc_understanding: bool = Field(default=True, description="RAGFlow-inspired deep document understanding")
    multi_modal_support: bool = Field(default=True, description="Support for heterogeneous data sources")
    
    # Supported platforms
    platforms: List[str] = Field(
        default=[
            "extended_exchange",
            "x10_python_sdk", 
            "starknet_dart",
            "cairo_lang",
            "avnu_paymaster",
            "web3auth",
            "chipi_pay"
        ],
        description="AstraTrade supported platforms"
    )
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )


# Global settings instance
settings = RAGSettings()

# Backward compatibility - create dictionary for existing code
RAG_CONFIG = {
    "chroma_db_path": settings.chroma_db_path,
    "collection_name": settings.collection_name,
    "embedding_model": settings.embedding_model,
    "chunk_size": settings.chunk_size,
    "chunk_overlap": settings.chunk_overlap,
    "max_results": settings.max_results,
    "similarity_threshold": settings.similarity_threshold,
    "claude_context_size": settings.claude_context_size,
    "code_aware_chunking": settings.code_aware_chunking,
    "template_chunking": settings.template_chunking,
    "grounded_citations": settings.grounded_citations,
    "quality_threshold": settings.quality_threshold,
    "deep_doc_understanding": settings.deep_doc_understanding,
    "multi_modal_support": settings.multi_modal_support,
    "platforms": settings.platforms
}