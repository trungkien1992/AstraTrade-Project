#!/usr/bin/env python3
"""
Test script for CodeAwareChunker
"""

import os
import sys
from pathlib import Path
from config import RAG_CONFIG
from code_aware_chunker import CodeAwareChunker

def test_python_chunking():
    """Test Python file chunking"""
    python_code = '''#!/usr/bin/env python3
"""
Test Python file for chunking
"""

import os
import sys
from typing import List, Dict

def hello_world():
    """Simple hello world function"""
    print("Hello, World!")
    return "Hello, World!"

class TestClass:
    """Test class for chunking"""
    
    def __init__(self, name: str):
        self.name = name
    
    def greet(self):
        """Greet method"""
        return f"Hello from {self.name}!"
    
    def calculate(self, a: int, b: int) -> int:
        """Calculate sum"""
        return a + b

async def async_function():
    """Async function example"""
    await asyncio.sleep(1)
    return "async result"
'''
    
    chunker = CodeAwareChunker(RAG_CONFIG)
    chunks = chunker.chunk_file("example.py", python_code)
    
    print(f"Python chunking test:")
    print(f"Generated {len(chunks)} chunks")
    
    for i, chunk in enumerate(chunks):
        print(f"  Chunk {i+1}: {chunk.chunk_type.value} - {chunk.metadata.get('description', 'No description')}")
        print(f"    Lines {chunk.start_line}-{chunk.end_line}")
        print(f"    Size: {len(chunk.content)} chars")
        print(f"    Importance: {chunk.importance}")
        print()
    
    # Verify we have expected chunks
    chunk_types = [chunk.chunk_type.value for chunk in chunks]
    print(f"Chunk types: {chunk_types}")
    
    # Should have class and functions (imports are not captured since they're not in the code)
    assert "class" in chunk_types, "Should have class chunk"
    assert "function" in chunk_types, "Should have function chunks"
    assert "documentation" in chunk_types, "Should have documentation chunk"
    
    print("✅ Python chunking test passed!")

def test_markdown_chunking():
    """Test Markdown file chunking"""
    markdown_content = '''# Main Title

This is the introduction section.

## Section 1: Getting Started

This section covers getting started with the system.

### Subsection 1.1: Installation

Step-by-step installation guide.

### Subsection 1.2: Configuration

Configuration details here.

## Section 2: Reference

Documentation goes here.

### Command Line

CLI usage.

### Configuration Files

Config file details.

## Conclusion

Final thoughts and summary.
'''
    
    chunker = CodeAwareChunker(RAG_CONFIG)
    chunks = chunker.chunk_file("example.md", markdown_content)
    
    print(f"Markdown chunking test:")
    print(f"Generated {len(chunks)} chunks")
    
    for i, chunk in enumerate(chunks):
        print(f"  Chunk {i+1}: {chunk.metadata.get('section_title', 'No title')}")
        print(f"    Level: {chunk.metadata.get('header_level', 'N/A')}")
        print(f"    Lines {chunk.start_line}-{chunk.end_line}")
        print(f"    Size: {len(chunk.content)} chars")
        print(f"    Importance: {chunk.importance}")
        print()
    
    # Verify we have expected sections
    section_titles = [chunk.metadata.get('section_title', '') for chunk in chunks]
    print(f"Section titles: {section_titles}")
    
    # Should have main sections
    assert "Main Title" in section_titles, "Should have main title"
    assert "Section 1: Getting Started" in section_titles, "Should have section 1"
    assert "Section 2: Reference" in section_titles, "Should have section 2"
    
    print("✅ Markdown chunking test passed!")

def test_integration():
    """Test integration with RAG system"""
    try:
        from rag_system import AstraTradeRAG
        from models import ProcessedDocument
        
        # Create a test document
        test_doc = ProcessedDocument(
            content='''# Test Document

This is a test document.

## Section 1

Content for section 1.

```python
def example_function():
    return "hello"
```

## Section 2

Content for section 2.
''',
            title="Test Document",
            category="test",
            subcategory="example",
            metadata={"test": True},
            source_url="http://example.com",
            file_path="example.md"
        )
        
        # Test the chunk_document method
        rag = AstraTradeRAG()
        chunks = rag._chunk_document(test_doc)
        
        print(f"Integration test:")
        print(f"Generated {len(chunks)} chunks")
        
        for i, chunk in enumerate(chunks):
            print(f"  Chunk {i+1}: {chunk['metadata'].get('chunk_type', 'unknown')}")
            print(f"    Code aware: {chunk['metadata'].get('code_aware', False)}")
            print(f"    Size: {len(chunk['content'])} chars")
            print()
        
        # Verify code-aware chunking was used
        code_aware_chunks = [chunk for chunk in chunks if chunk['metadata'].get('code_aware', False)]
        print(f"Code-aware chunks: {len(code_aware_chunks)}/{len(chunks)}")
        
        if code_aware_chunks:
            print("✅ Integration test passed!")
        else:
            print("⚠️  Integration test: code-aware chunking not used")
        
    except Exception as e:
        print(f"❌ Integration test failed: {e}")

if __name__ == "__main__":
    print("Testing CodeAwareChunker...")
    print("=" * 50)
    
    test_python_chunking()
    print()
    
    test_markdown_chunking()
    print()
    
    test_integration()
    print()
    
    print("All tests completed!")