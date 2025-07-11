#!/usr/bin/env python3
"""
Simple test for Markdown chunking
"""

from config import RAG_CONFIG
from code_aware_chunker import CodeAwareChunker

def test_markdown_direct():
    """Test Markdown chunking directly"""
    markdown_content = '''# Main Title

This is the introduction section.

## Section 1: Getting Started

This section covers getting started with the system.

### Subsection 1.1: Installation

Step-by-step installation guide.

## Section 2: Reference

Documentation goes here.

### Command Line

CLI usage.

## Conclusion

Final thoughts and summary.
'''
    
    chunker = CodeAwareChunker(RAG_CONFIG)
    chunks = chunker._chunk_markdown(markdown_content, "example.md")
    
    print(f"Markdown chunking test:")
    print(f"Generated {len(chunks)} chunks")
    
    for i, chunk in enumerate(chunks):
        print(f"  Chunk {i+1}: {chunk.metadata.get('section_title', 'No title')}")
        print(f"    Level: {chunk.metadata.get('header_level', 'N/A')}")
        print(f"    Lines {chunk.start_line}-{chunk.end_line}")
        print(f"    Size: {len(chunk.content)} chars")
        print(f"    First 50 chars: {chunk.content[:50]}")
        print()

if __name__ == "__main__":
    test_markdown_direct()