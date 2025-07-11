#!/usr/bin/env python3
"""
Real-world integration test for code-aware chunker
"""

import json
import requests
from pathlib import Path

def test_search_function():
    """Test searching for a specific function"""
    url = "http://localhost:8000/search"
    headers = {"Content-Type": "application/json"}
    
    # Search for a function that should exist in the codebase
    data = {
        "query": "search_for_claude",
        "max_results": 3,
        "min_similarity": 0.25
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            results = response.json()
            print(f"Search results for 'search_for_claude':")
            print(f"Found {results['total_results']} results")
            
            for i, result in enumerate(results['results']):
                print(f"  Result {i+1}:")
                print(f"    Code aware: {result.get('code_aware', 'N/A')}")
                print(f"    Chunk type: {result.get('chunk_type', 'N/A')}")
                print(f"    Language: {result.get('language', 'N/A')}")
                print(f"    Relevance: {result.get('relevance', 'N/A')}")
                print(f"    First 100 chars: {result.get('content', '')[:100]}")
                print()
            
            # Check if we found function chunks
            function_chunks = [r for r in results['results'] if r.get('chunk_type') == 'function']
            if function_chunks:
                print("✅ Found function chunks from code-aware chunking!")
                return True
            else:
                print("⚠️  No function chunks found")
                return False
        else:
            print(f"❌ Search request failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Search test failed: {e}")
        return False

def test_search_python_class():
    """Test searching for a Python class"""
    url = "http://localhost:8000/search"
    headers = {"Content-Type": "application/json"}
    
    # Search for a class that should exist
    data = {
        "query": "CodeAwareChunker",
        "max_results": 3,
        "min_similarity": 0.25
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            results = response.json()
            print(f"Search results for 'CodeAwareChunker':")
            print(f"Found {results['total_results']} results")
            
            for i, result in enumerate(results['results']):
                print(f"  Result {i+1}:")
                print(f"    Code aware: {result.get('code_aware', 'N/A')}")
                print(f"    Chunk type: {result.get('chunk_type', 'N/A')}")
                print(f"    Language: {result.get('language', 'N/A')}")
                print(f"    First 100 chars: {result.get('content', '')[:100]}")
                print()
            
            # Check if we found class chunks
            class_chunks = [r for r in results['results'] if r.get('chunk_type') == 'class']
            if class_chunks:
                print("✅ Found class chunks from code-aware chunking!")
                return True
            else:
                print("⚠️  No class chunks found")
                return False
        else:
            print(f"❌ Search request failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Search test failed: {e}")
        return False

def test_search_markdown_section():
    """Test searching for markdown sections"""
    url = "http://localhost:8000/search"
    headers = {"Content-Type": "application/json"}
    
    # Search for markdown sections
    data = {
        "query": "Getting Started",
        "max_results": 3,
        "min_similarity": 0.25
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            results = response.json()
            print(f"Search results for 'Getting Started':")
            print(f"Found {results['total_results']} results")
            
            for i, result in enumerate(results['results']):
                print(f"  Result {i+1}:")
                print(f"    Code aware: {result.get('code_aware', 'N/A')}")
                print(f"    Chunk type: {result.get('chunk_type', 'N/A')}")
                print(f"    Language: {result.get('language', 'N/A')}")
                print(f"    Section title: {result.get('section_title', 'N/A')}")
                print(f"    First 100 chars: {result.get('content', '')[:100]}")
                print()
            
            # Check if we found documentation chunks
            doc_chunks = [r for r in results['results'] if r.get('chunk_type') == 'documentation']
            if doc_chunks:
                print("✅ Found documentation chunks from code-aware chunking!")
                return True
            else:
                print("⚠️  No documentation chunks found")
                return False
        else:
            print(f"❌ Search request failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Search test failed: {e}")
        return False

def test_stats():
    """Test getting stats to see if code-aware chunking is working"""
    url = "http://localhost:8000/stats"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            stats = response.json()
            print(f"Knowledge base stats:")
            print(f"  Total documents: {stats['total_documents']}")
            print(f"  Categories: {stats['categories']}")
            print(f"  Embedding model: {stats['embedding_model']}")
            print(f"  Last updated: {stats['last_updated']}")
            print()
            return True
        else:
            print(f"❌ Stats request failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Stats test failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing real-world code-aware chunking integration...")
    print("=" * 60)
    
    # Test basic stats
    if test_stats():
        print()
        
        # Test function search
        if test_search_function():
            print()
        
        # Test class search
        if test_search_python_class():
            print()
        
        # Test markdown section search
        if test_search_markdown_section():
            print()
    
    print("Real-world integration test completed!")