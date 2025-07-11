# Claude Code Sonnet 4 RAG Enhancement Implementation Plan

## 🎯 Executive Summary

Transform the StreetCred RAG system into an optimal development companion for Claude Code sessions by implementing larger context windows, code-aware chunking, and intelligent query routing.

## 📋 Current System Analysis

### Existing Infrastructure
- **Location**: `knowledge_base/backend/`
- **Stack**: FastAPI + ChromaDB + Sentence Transformers
- **Current Limitations**:
  - Chunk size: 1000 chars (too small for code context)
  - Basic text splitting (breaks code structure)
  - No code relationship understanding

## 🚀 Implementation Plan

### Week 1: Core Context Enhancement

#### Day 1-2: Configuration & Infrastructure Updates

**1. Update RAG Configuration**
```python
# File: knowledge_base/backend/main.py

# Update RAG_CONFIG
RAG_CONFIG = {
    "chroma_db_path": "../system/chroma_db",
    "collection_name": "streetcred_knowledge_base",
    "embedding_model": "sentence-transformers/all-MiniLM-L6-v2",
    "chunk_size": 4000,          # Increased from 1000
    "chunk_overlap": 800,        # Increased from 200
    "max_results": 15,           # Increased from 10
    "similarity_threshold": 0.7,
    "claude_context_size": 8000, # New: Special size for Claude
    "code_aware_chunking": True, # New: Enable code-aware splitting
}
```

**2. Create Code-Aware Chunker Module**
```python
# File: knowledge_base/backend/code_aware_chunker.py

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from pathlib import Path
import re
import ast

@dataclass
class CodeChunk:
    content: str
    metadata: Dict[str, Any]
    start_line: int
    end_line: int
    chunk_type: str  # 'function', 'class', 'import_block', 'documentation'
    
class CodeAwareChunker:
    """Intelligently chunks code while preserving logical units"""
    
    def __init__(self, config: Dict[str, Any]):
        self.max_chunk_size = config.get('claude_context_size', 8000)
        self.chunk_overlap = config.get('chunk_overlap', 800)
        self.language_patterns = self._build_language_patterns()
    
    def chunk_file(self, file_path: str, content: str) -> List[CodeChunk]:
        """Chunk a file based on its type and content"""
        file_ext = Path(file_path).suffix.lstrip('.')
        
        if file_ext in ['py', 'python']:
            return self._chunk_python(content, file_path)
        elif file_ext in ['dart']:
            return self._chunk_dart(content, file_path)
        elif file_ext in ['cairo']:
            return self._chunk_cairo(content, file_path)
        elif file_ext in ['md', 'markdown']:
            return self._chunk_markdown(content, file_path)
        else:
            return self._chunk_generic(content, file_path)
    
    def _chunk_python(self, content: str, file_path: str) -> List[CodeChunk]:
        """Python-specific chunking"""
        chunks = []
        
        try:
            tree = ast.parse(content)
            
            # Extract imports as a separate chunk
            imports = []
            for node in ast.walk(tree):
                if isinstance(node, (ast.Import, ast.ImportFrom)):
                    imports.append(ast.get_source_segment(content, node))
            
            if imports:
                chunks.append(CodeChunk(
                    content='\n'.join(imports),
                    metadata={
                        'file_path': file_path,
                        'language': 'python',
                        'chunk_type': 'imports'
                    },
                    start_line=1,
                    end_line=len(imports),
                    chunk_type='import_block'
                ))
            
            # Extract classes and functions
            for node in ast.walk(tree):
                if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                    chunk_content = ast.get_source_segment(content, node)
                    if chunk_content and len(chunk_content) < self.max_chunk_size:
                        chunks.append(CodeChunk(
                            content=chunk_content,
                            metadata={
                                'file_path': file_path,
                                'language': 'python',
                                'name': node.name,
                                'type': type(node).__name__
                            },
                            start_line=node.lineno,
                            end_line=node.end_lineno,
                            chunk_type='function' if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) else 'class'
                        ))
        except:
            # Fallback to pattern-based chunking
            return self._chunk_by_patterns(content, file_path, 'python')
        
        return chunks
    
    def _chunk_dart(self, content: str, file_path: str) -> List[CodeChunk]:
        """Dart-specific chunking"""
        chunks = []
        
        # Pattern for Dart classes and functions
        class_pattern = r'class\s+(\w+).*?{[\s\S]*?^}'
        function_pattern = r'^\s*((?:static\s+)?(?:final\s+)?(?:Future<.*?>|void|\w+)\s+\w+\s*\([^)]*\)\s*(?:async\s*)?{[\s\S]*?^})'
        
        # Extract classes
        for match in re.finditer(class_pattern, content, re.MULTILINE):
            chunks.append(CodeChunk(
                content=match.group(0),
                metadata={
                    'file_path': file_path,
                    'language': 'dart',
                    'class_name': match.group(1),
                    'type': 'class'
                },
                start_line=content[:match.start()].count('\n') + 1,
                end_line=content[:match.end()].count('\n') + 1,
                chunk_type='class'
            ))
        
        # Extract functions
        for match in re.finditer(function_pattern, content, re.MULTILINE):
            chunks.append(CodeChunk(
                content=match.group(0),
                metadata={
                    'file_path': file_path,
                    'language': 'dart',
                    'type': 'function'
                },
                start_line=content[:match.start()].count('\n') + 1,
                end_line=content[:match.end()].count('\n') + 1,
                chunk_type='function'
            ))
        
        return chunks
```

#### Day 3-4: Enhanced Search Implementation

**1. Create Claude-Optimized Search Module**
```python
# File: knowledge_base/backend/claude_search.py

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import asyncio

@dataclass
class ClaudeSearchResult:
    results: List[Dict[str, Any]]
    total_context_size: int
    query_type: str
    related_files: List[str]
    cross_references: Dict[str, List[str]]

class ClaudeOptimizedSearch:
    """Search optimized for Claude Code development context"""
    
    def __init__(self, rag_system, collection):
        self.rag_system = rag_system
        self.collection = collection
        self.file_relationship_map = {}
        self.import_graph = {}
    
    async def search_for_claude(self, query: str, context_type: str = "development") -> ClaudeSearchResult:
        """Enhanced search that provides larger, more relevant context"""
        
        # Step 1: Analyze query intent
        intent = self._analyze_query_intent(query)
        
        # Step 2: Perform base search with larger result set
        base_results = await self._perform_base_search(query, max_results=20)
        
        # Step 3: Expand context based on code relationships
        expanded_results = await self._expand_code_context(base_results, intent)
        
        # Step 4: Find related files and cross-references
        related_files = self._find_related_files(expanded_results)
        cross_refs = self._build_cross_references(expanded_results)
        
        # Step 5: Optimize for Claude's context window
        optimized_results = self._optimize_for_claude(expanded_results, max_size=8000)
        
        return ClaudeSearchResult(
            results=optimized_results,
            total_context_size=sum(len(r['content']) for r in optimized_results),
            query_type=intent,
            related_files=related_files,
            cross_references=cross_refs
        )
    
    def _analyze_query_intent(self, query: str) -> str:
        """Determine what Claude is trying to do"""
        query_lower = query.lower()
        
        if any(word in query_lower for word in ['error', 'bug', 'fix', 'issue', 'problem']):
            return 'debug'
        elif any(word in query_lower for word in ['add', 'implement', 'create', 'feature']):
            return 'feature'
        elif any(word in query_lower for word in ['refactor', 'improve', 'optimize']):
            return 'refactor'
        elif any(word in query_lower for word in ['test', 'testing', 'unit', 'integration']):
            return 'testing'
        else:
            return 'understand'
    
    async def _expand_code_context(self, base_results: List[Dict], intent: str) -> List[Dict]:
        """Expand context based on code relationships"""
        expanded = base_results.copy()
        
        for result in base_results:
            file_path = result.get('metadata', {}).get('file_path', '')
            
            # Add related files based on imports
            if file_path in self.import_graph:
                for imported_file in self.import_graph[file_path]:
                    related_chunks = await self._get_file_chunks(imported_file)
                    expanded.extend(related_chunks[:2])  # Add top chunks from related files
            
            # Add test files for feature/refactor intents
            if intent in ['feature', 'refactor']:
                test_file = self._find_test_file(file_path)
                if test_file:
                    test_chunks = await self._get_file_chunks(test_file)
                    expanded.extend(test_chunks[:1])
        
        return expanded
```

**2. Update Main RAG Endpoints**
```python
# File: knowledge_base/backend/main.py (additions)

from claude_search import ClaudeOptimizedSearch, ClaudeSearchResult

# Initialize Claude-optimized search
claude_search = None

@app.on_event("startup")
async def startup_event():
    """Initialize RAG system on startup"""
    await rag_system.initialize()
    global claude_search
    claude_search = ClaudeOptimizedSearch(rag_system, rag_system.collection)

@app.post("/search/claude", response_model=Dict[str, Any])
async def search_for_claude(request: QueryRequest):
    """Claude-optimized search endpoint with larger context"""
    result = await claude_search.search_for_claude(
        query=request.query,
        context_type=request.category or "development"
    )
    
    return {
        "results": result.results,
        "total_context_size": result.total_context_size,
        "query_type": result.query_type,
        "related_files": result.related_files,
        "cross_references": result.cross_references,
        "optimized_for": "claude_code_sonnet_4"
    }

@app.post("/index/code_aware")
async def index_with_code_awareness(background_tasks: BackgroundTasks):
    """Re-index with code-aware chunking"""
    background_tasks.add_task(reindex_with_code_aware_chunking)
    return {"status": "started", "message": "Code-aware indexing initiated"}
```

#### Day 5: Testing & Validation

**1. Create Test Suite**
```python
# File: knowledge_base/backend/tests/test_claude_enhancements.py

import pytest
from code_aware_chunker import CodeAwareChunker
from claude_search import ClaudeOptimizedSearch

def test_code_aware_chunking():
    """Test that code-aware chunking preserves logical units"""
    chunker = CodeAwareChunker({'claude_context_size': 8000})
    
    python_code = '''
import asyncio
from typing import List

class GameStateProvider:
    def __init__(self):
        self.state = {}
    
    async def update_state(self, key: str, value: Any):
        self.state[key] = value
        await self.notify_listeners()
    
    async def notify_listeners(self):
        # Notify all listeners
        pass
'''
    
    chunks = chunker.chunk_file('test.py', python_code)
    
    # Should have import chunk and class chunk
    assert len(chunks) >= 2
    assert any(c.chunk_type == 'import_block' for c in chunks)
    assert any(c.chunk_type == 'class' for c in chunks)

def test_claude_search_context_size():
    """Test that Claude search returns appropriate context sizes"""
    # Test implementation
    pass
```

### Week 2: Advanced Context Understanding

#### Day 6-7: Project Structure Indexing

**1. Create Project Structure Analyzer**
```python
# File: knowledge_base/backend/project_structure.py

from pathlib import Path
from typing import Dict, List, Set, Optional
import ast
import re

class ProjectStructureAnalyzer:
    """Analyzes and indexes project structure for better context understanding"""
    
    def __init__(self):
        self.file_graph = {}
        self.import_map = {}
        self.class_hierarchy = {}
        self.function_calls = {}
    
    def analyze_project(self, project_path: str) -> Dict[str, Any]:
        """Analyze entire project structure"""
        project_path = Path(project_path)
        
        # Build file tree
        file_tree = self._build_file_tree(project_path)
        
        # Analyze dependencies
        for file_path in self._get_all_files(project_path, ['.py', '.dart', '.cairo']):
            self._analyze_file_dependencies(file_path)
        
        # Build relationship graphs
        self._build_relationship_graphs()
        
        return {
            'file_tree': file_tree,
            'import_graph': self.import_map,
            'class_hierarchy': self.class_hierarchy,
            'function_calls': self.function_calls,
            'entry_points': self._find_entry_points(),
            'core_files': self._identify_core_files()
        }
    
    def _analyze_file_dependencies(self, file_path: Path):
        """Analyze dependencies for a single file"""
        content = file_path.read_text()
        
        if file_path.suffix == '.py':
            self._analyze_python_dependencies(file_path, content)
        elif file_path.suffix == '.dart':
            self._analyze_dart_dependencies(file_path, content)
```

#### Day 8-9: Cross-Reference System

**1. Implement Cross-Reference Builder**
```python
# File: knowledge_base/backend/cross_reference.py

class CrossReferenceSystem:
    """Builds and manages cross-references between code elements"""
    
    def __init__(self, project_analyzer):
        self.project_analyzer = project_analyzer
        self.reference_map = {}
        self.concept_map = {}
    
    def build_references(self, project_path: str):
        """Build comprehensive cross-reference map"""
        
        # Analyze project structure first
        structure = self.project_analyzer.analyze_project(project_path)
        
        # Build references for:
        # 1. Function calls and definitions
        # 2. Class usage and inheritance
        # 3. Import relationships
        # 4. Configuration usage
        # 5. Test-to-implementation mapping
        
        self._build_function_references(structure)
        self._build_class_references(structure)
        self._build_test_mappings(structure)
        
    def get_related_context(self, file_path: str, element_name: str) -> List[Dict]:
        """Get all related context for a code element"""
        related = []
        
        # Find where element is defined
        definition = self._find_definition(element_name)
        if definition:
            related.append(definition)
        
        # Find where element is used
        usages = self._find_usages(element_name)
        related.extend(usages)
        
        # Find related tests
        tests = self._find_related_tests(element_name)
        related.extend(tests)
        
        return related
```

#### Day 10: Development Context Packages

**1. Create Context Package System**
```python
# File: knowledge_base/backend/context_packages.py

class DevelopmentContextPackages:
    """Pre-built context packages for common development scenarios"""
    
    def __init__(self, rag_system):
        self.rag_system = rag_system
        self.packages = {}
        self._build_default_packages()
    
    def _build_default_packages(self):
        """Build default context packages"""
        
        # Trading System Package
        self.packages['trading_system'] = {
            'name': 'StreetCred Trading System',
            'files': [
                'lib/services/real_starknet_service.dart',
                'lib/services/contract_service.dart',
                'lib/providers/xp_provider.dart',
                'python_trading_service/main.py',
                'python_trading_service/starkex_crypto.py'
            ],
            'docs': [
                'docs/ARCHITECTURE.md',
                'docs/SESSION_PROGRESS_2025_01_09.md'
            ],
            'contracts': [
                'contracts/streetcred_xp/src/xp_system.cairo',
                'contracts/streetcred_paymaster/src/avnu_paymaster.cairo'
            ]
        }
        
        # Smart Contract Package
        self.packages['smart_contracts'] = {
            'name': 'Cairo Smart Contracts',
            'files': [
                'contracts/streetcred_xp/src/xp_system.cairo',
                'contracts/street_art_nft/src/street_art.cairo',
                'contracts/streetcred_paymaster/src/avnu_paymaster.cairo'
            ],
            'docs': [
                'docs/CAIRO_CONTRACTS_README.md'
            ],
            'scripts': [
                'scripts/deployment/real_deploy_contracts.py',
                'scripts/deployment/real_deploy_contracts.sh'
            ]
        }
    
    async def get_package(self, package_name: str) -> Dict[str, Any]:
        """Get a complete context package"""
        if package_name not in self.packages:
            return None
        
        package_def = self.packages[package_name]
        package_content = []
        
        # Collect all file contents
        for file_list_key in ['files', 'docs', 'contracts', 'scripts']:
            if file_list_key in package_def:
                for file_path in package_def[file_list_key]:
                    content = await self._get_file_content(file_path)
                    if content:
                        package_content.append({
                            'file_path': file_path,
                            'content': content,
                            'type': file_list_key
                        })
        
        return {
            'name': package_def['name'],
            'contents': package_content,
            'total_size': sum(len(c['content']) for c in package_content)
        }
```

### Week 3: Optimization & Monitoring

#### Day 11-12: Performance Optimization

**1. Add Caching Layer**
```python
# File: knowledge_base/backend/cache_manager.py

from functools import lru_cache
import hashlib
import json
from datetime import datetime, timedelta

class CacheManager:
    """Manages caching for Claude-optimized searches"""
    
    def __init__(self, cache_duration_minutes=60):
        self.cache = {}
        self.cache_duration = timedelta(minutes=cache_duration_minutes)
    
    def get_cache_key(self, query: str, context_type: str) -> str:
        """Generate cache key for query"""
        combined = f"{query}:{context_type}"
        return hashlib.md5(combined.encode()).hexdigest()
    
    def get(self, query: str, context_type: str) -> Optional[Dict]:
        """Get cached result if available and not expired"""
        key = self.get_cache_key(query, context_type)
        
        if key in self.cache:
            entry = self.cache[key]
            if datetime.now() - entry['timestamp'] < self.cache_duration:
                return entry['data']
        
        return None
    
    def set(self, query: str, context_type: str, data: Dict):
        """Cache search result"""
        key = self.get_cache_key(query, context_type)
        self.cache[key] = {
            'data': data,
            'timestamp': datetime.now()
        }
```

**2. Add Usage Analytics**
```python
# File: knowledge_base/backend/analytics.py

class ClaudeUsageAnalytics:
    """Track Claude's usage patterns for optimization"""
    
    def __init__(self):
        self.query_log = []
        self.performance_metrics = []
        self.popular_files = {}
        self.query_patterns = {}
    
    def log_query(self, query: str, intent: str, results_count: int, response_time: float):
        """Log query for analysis"""
        self.query_log.append({
            'timestamp': datetime.now(),
            'query': query,
            'intent': intent,
            'results_count': results_count,
            'response_time': response_time
        })
        
        # Track query patterns
        if intent not in self.query_patterns:
            self.query_patterns[intent] = 0
        self.query_patterns[intent] += 1
    
    def log_file_access(self, file_path: str):
        """Track which files are accessed most"""
        if file_path not in self.popular_files:
            self.popular_files[file_path] = 0
        self.popular_files[file_path] += 1
    
    def get_optimization_suggestions(self) -> List[str]:
        """Generate optimization suggestions based on usage"""
        suggestions = []
        
        # Suggest pre-loading popular files
        top_files = sorted(self.popular_files.items(), key=lambda x: x[1], reverse=True)[:10]
        suggestions.append(f"Pre-load these popular files: {[f[0] for f in top_files]}")
        
        # Suggest optimizing for common query patterns
        top_intents = sorted(self.query_patterns.items(), key=lambda x: x[1], reverse=True)
        suggestions.append(f"Optimize for these query types: {[i[0] for i in top_intents]}")
        
        return suggestions
```

#### Day 13-14: Integration & Testing

**1. Update Main Application**
```python
# File: knowledge_base/backend/main.py (final updates)

# Import new modules
from code_aware_chunker import CodeAwareChunker
from project_structure import ProjectStructureAnalyzer
from cross_reference import CrossReferenceSystem
from context_packages import DevelopmentContextPackages
from cache_manager import CacheManager
from analytics import ClaudeUsageAnalytics

# Initialize components
code_chunker = CodeAwareChunker(RAG_CONFIG)
project_analyzer = ProjectStructureAnalyzer()
cross_ref_system = CrossReferenceSystem(project_analyzer)
context_packages = DevelopmentContextPackages(rag_system)
cache_manager = CacheManager()
analytics = ClaudeUsageAnalytics()

@app.get("/claude/status")
async def get_claude_optimization_status():
    """Get status of Claude optimizations"""
    return {
        "chunk_size": RAG_CONFIG['chunk_size'],
        "claude_context_size": RAG_CONFIG['claude_context_size'],
        "code_aware_chunking": RAG_CONFIG['code_aware_chunking'],
        "cached_queries": len(cache_manager.cache),
        "usage_analytics": {
            "total_queries": len(analytics.query_log),
            "popular_files": list(analytics.popular_files.keys())[:5],
            "query_patterns": analytics.query_patterns
        },
        "optimization_suggestions": analytics.get_optimization_suggestions()
    }

@app.get("/claude/packages")
async def list_context_packages():
    """List available context packages"""
    return {
        "packages": list(context_packages.packages.keys()),
        "descriptions": {k: v['name'] for k, v in context_packages.packages.items()}
    }

@app.get("/claude/package/{package_name}")
async def get_context_package(package_name: str):
    """Get a specific context package"""
    package = await context_packages.get_package(package_name)
    if not package:
        raise HTTPException(status_code=404, detail="Package not found")
    return package
```

**2. Create Integration Tests**
```bash
# File: knowledge_base/backend/test_claude_integration.sh

#!/bin/bash
echo "Testing Claude Code Optimizations..."

# Test 1: Code-aware chunking
echo "Test 1: Code-aware chunking"
curl -X POST http://localhost:8000/index/code_aware

sleep 5

# Test 2: Claude-optimized search
echo "Test 2: Claude search with large context"
curl -X POST http://localhost:8000/search/claude \
  -H "Content-Type: application/json" \
  -d '{"query": "How does the trading service integrate with StarkEx signatures?", "category": "development"}'

# Test 3: Context packages
echo "Test 3: Get trading system context package"
curl http://localhost:8000/claude/package/trading_system

# Test 4: Check optimization status
echo "Test 4: Claude optimization status"
curl http://localhost:8000/claude/status
```

## 📊 Success Metrics & Monitoring

### Performance Targets
- **Chunk Size**: 4000 chars (4x improvement)
- **Context Window**: 8000 chars for Claude
- **Search Response**: <100ms
- **Cache Hit Rate**: >60%

### Usage Tracking
```python
# Add to each Claude search endpoint
start_time = time.time()
result = await claude_search.search_for_claude(query)
response_time = time.time() - start_time

analytics.log_query(query, result.query_type, len(result.results), response_time)
```

## 🎯 Deployment Checklist

### Week 1 Deliverables
- [ ] Code-aware chunking implemented
- [ ] Claude-optimized search endpoint live
- [ ] 4000 char chunk size active
- [ ] Basic testing complete

### Week 2 Deliverables
- [ ] Project structure indexing complete
- [ ] Cross-reference system active
- [ ] Context packages available
- [ ] Integration tests passing

### Week 3 Deliverables
- [ ] Caching layer operational
- [ ] Analytics dashboard available
- [ ] Performance optimized
- [ ] Full documentation updated

## 🚀 Quick Start Commands

```bash
# 1. Update dependencies
cd knowledge_base/backend
pip install -r requirements.txt

# 2. Run migrations/updates
python update_for_claude.py

# 3. Re-index with code awareness
curl -X POST http://localhost:8000/index/code_aware

# 4. Test Claude search
curl -X POST http://localhost:8000/search/claude \
  -H "Content-Type: application/json" \
  -d '{"query": "trading service implementation"}'

# 5. Check status
curl http://localhost:8000/claude/status
```

This implementation plan transforms the StreetCred RAG system into an optimal tool for Claude Code Sonnet 4, providing larger context windows, intelligent code understanding, and efficient development workflows.