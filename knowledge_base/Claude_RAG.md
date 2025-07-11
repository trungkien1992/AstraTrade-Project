# Claude Code RAG Enhancement Plan

## 🎯 Primary Goal
Enhance our RAG system to be the optimal tool for Claude Code sessions, providing better context retrieval and larger context windows to maximize development efficiency.

## 📋 Current State Analysis

### ✅ What Works for Claude Code
- **FastAPI backend** with semantic search
- **Multi-platform categorization** (Extended Exchange, X10 Python, Cairo, Starknet.dart)
- **ChromaDB integration** with decent search performance
- **HTTP endpoints** that Claude can query directly

### ❌ What Limits Claude Code Effectiveness
- **Small context chunks** (1000 chars) - Claude needs bigger context
- **Basic text splitting** - loses important code structure and relationships
- **No code-aware chunking** - breaks functions, classes, and logical units
- **Limited similarity search** - misses related concepts and dependencies
- **No hierarchical context** - can't understand file/project structure
- **No code relationship mapping** - can't find related functions across files

## 🚀 Simplified Enhancement Plan

### Phase 1: Larger, Smarter Context (Week 1)

#### 1.1 Increase Context Size for Claude
**Goal**: Provide larger, more meaningful chunks that Claude can work with effectively

**Changes**:
```python
# Current configuration
RAG_CONFIG = {
    "chunk_size": 1000,        # Too small for Claude
    "chunk_overlap": 200,      # Minimal overlap
    "max_results": 10,         # Limited results
}

# Enhanced configuration for Claude Code
RAG_CONFIG = {
    "chunk_size": 4000,        # 4x larger chunks
    "chunk_overlap": 800,      # Substantial overlap for context
    "max_results": 15,         # More comprehensive results
    "claude_context_size": 8000, # Special large chunks for Claude
}
```

#### 1.2 Code-Aware Chunking
**Goal**: Respect code structure instead of arbitrary text splitting

**Implementation**:
```python
class CodeAwareChunker:
    def __init__(self):
        self.language_parsers = {
            'dart': DartParser(),
            'python': PythonParser(),
            'cairo': CairoParser(),
            'markdown': MarkdownParser(),
            'yaml': YamlParser()
        }
    
    def chunk_code_file(self, file_path: str, content: str) -> List[Chunk]:
        file_ext = Path(file_path).suffix.lstrip('.')
        parser = self.language_parsers.get(file_ext, self.language_parsers['markdown'])
        
        # Parse into logical units
        units = parser.parse_logical_units(content)
        
        # Create chunks that preserve:
        # - Complete functions/classes
        # - Import statements with usage
        # - Documentation with code
        # - Related code blocks
        
        chunks = []
        for unit in units:
            # Include context from related units
            context = self.get_related_context(unit, units)
            
            chunk = Chunk(
                content=unit.content + context,
                metadata={
                    'type': unit.type,  # 'function', 'class', 'import', etc.
                    'name': unit.name,
                    'dependencies': unit.dependencies,
                    'file_path': file_path,
                    'line_start': unit.line_start,
                    'line_end': unit.line_end,
                    'claude_optimized': True
                }
            )
            chunks.append(chunk)
        
        return chunks
```

#### 1.3 Enhanced Search for Claude Queries
**Goal**: Better understand Claude's development-focused queries

**Implementation**:
```python
class ClaudeOptimizedSearch:
    def __init__(self):
        self.query_enhancer = QueryEnhancer()
        self.context_expander = ContextExpander()
        self.code_relationship_finder = CodeRelationshipFinder()
    
    async def search_for_claude(self, query: str, context_type: str = "development") -> ClaudeSearchResult:
        # Enhance query with development context
        enhanced_query = self.query_enhancer.enhance_for_development(query)
        
        # Find relevant code chunks
        code_results = await self.find_code_chunks(enhanced_query)
        
        # Find related documentation
        doc_results = await self.find_related_docs(enhanced_query)
        
        # Expand context with related code
        expanded_results = self.context_expander.expand_context(
            code_results + doc_results,
            max_context_size=8000  # Optimized for Claude
        )
        
        return ClaudeSearchResult(
            results=expanded_results,
            total_context_size=sum(len(r.content) for r in expanded_results),
            query_type=context_type,
            claude_optimized=True
        )
```

### Phase 2: Better Context Understanding (Week 2)

#### 2.1 Project Structure Awareness
**Goal**: Help Claude understand the overall project structure

**Implementation**:
```python
class ProjectStructureIndexer:
    def __init__(self):
        self.file_analyzer = FileAnalyzer()
        self.dependency_mapper = DependencyMapper()
    
    def index_project_structure(self, project_path: str) -> ProjectIndex:
        # Analyze project structure
        structure = self.analyze_directory_structure(project_path)
        
        # Map dependencies between files
        dependencies = self.dependency_mapper.map_dependencies(project_path)
        
        # Create searchable index
        index = ProjectIndex(
            structure=structure,
            dependencies=dependencies,
            entry_points=self.find_entry_points(project_path),
            important_files=self.identify_important_files(project_path)
        )
        
        return index
    
    def get_context_for_file(self, file_path: str) -> FileContext:
        # When Claude asks about a file, provide:
        # - File purpose and role
        # - Related files and dependencies
        # - Usage examples
        # - Common patterns
        
        return FileContext(
            file_purpose=self.analyze_file_purpose(file_path),
            dependencies=self.get_file_dependencies(file_path),
            related_files=self.find_related_files(file_path),
            usage_patterns=self.extract_usage_patterns(file_path)
        )
```

#### 2.2 Cross-Reference System
**Goal**: When Claude asks about one concept, provide related concepts automatically

**Implementation**:
```python
class CrossReferenceSystem:
    def __init__(self):
        self.concept_mapper = ConceptMapper()
        self.relationship_builder = RelationshipBuilder()
    
    def build_cross_references(self, documents: List[Document]) -> CrossReferenceIndex:
        # Build relationships between:
        # - Functions and their usage
        # - Classes and their implementations
        # - APIs and their examples
        # - Concepts and their explanations
        
        relationships = {}
        
        for doc in documents:
            concepts = self.concept_mapper.extract_concepts(doc)
            for concept in concepts:
                relationships[concept.name] = self.relationship_builder.find_relationships(
                    concept, documents
                )
        
        return CrossReferenceIndex(relationships)
    
    def get_related_context(self, query: str, primary_results: List[SearchResult]) -> List[SearchResult]:
        # When Claude searches for "bot_provider.dart", also provide:
        # - Related providers that interact with it
        # - Models used by the provider
        # - Screens that use the provider
        # - Configuration related to bots
        
        related_concepts = []
        for result in primary_results:
            concepts = self.concept_mapper.extract_concepts(result.content)
            for concept in concepts:
                related = self.cross_ref_index.get_related(concept.name)
                related_concepts.extend(related)
        
        # Return additional context
        return self.search_for_concepts(related_concepts)
```

### Phase 3: Claude-Specific Optimizations (Week 3)

#### 3.1 Development Context Packages
**Goal**: Pre-package common development contexts that Claude frequently needs

**Implementation**:
```python
class DevelopmentContextPackages:
    def __init__(self):
        self.packages = {
            'game_state_management': self.build_game_state_package(),
            'trading_integration': self.build_trading_package(),
            'blockchain_contracts': self.build_blockchain_package(),
            'ui_components': self.build_ui_package(),
            'testing_framework': self.build_testing_package()
        }
    
    def get_context_package(self, package_name: str) -> ContextPackage:
        # When Claude asks about game state, provide complete package:
        # - All provider files
        # - Related models
        # - Usage examples
        # - Test files
        # - Configuration
        
        package = self.packages.get(package_name)
        if not package:
            return self.build_dynamic_package(package_name)
        
        return ContextPackage(
            name=package_name,
            files=package.files,
            documentation=package.documentation,
            examples=package.examples,
            tests=package.tests,
            total_context_size=package.total_size
        )
    
    def build_game_state_package(self) -> ContextPackage:
        # Pre-built package for game state development
        return ContextPackage(
            name="game_state_management",
            files=[
                "lib/providers/game_state_provider.dart",
                "lib/providers/idle_earnings_provider.dart",
                "lib/providers/bot_provider.dart",
                "lib/providers/upgrade_provider.dart",
                "lib/models/game_models.dart"
            ],
            documentation=[
                "docs/GAME_DESIGN.md",
                "project-rules/docs/ARCHITECTURE.md"
            ],
            examples=[
                "test/unit/game_models_test.dart",
                "lib/screens/casino_floor_screen.dart"
            ]
        )
```

#### 3.2 Smart Query Routing
**Goal**: Understand what Claude is trying to do and route queries appropriately

**Implementation**:
```python
class SmartQueryRouter:
    def __init__(self):
        self.intent_classifier = IntentClassifier()
        self.context_builders = {
            'debug_issue': DebugContextBuilder(),
            'add_feature': FeatureContextBuilder(),
            'understand_code': CodeUnderstandingBuilder(),
            'refactor_code': RefactorContextBuilder(),
            'write_tests': TestContextBuilder()
        }
    
    async def route_query(self, query: str) -> RoutedSearchResult:
        # Classify Claude's intent
        intent = self.intent_classifier.classify(query)
        
        # Build appropriate context
        context_builder = self.context_builders.get(intent, self.context_builders['understand_code'])
        
        # Get tailored results
        results = await context_builder.build_context(query)
        
        return RoutedSearchResult(
            intent=intent,
            results=results,
            context_type=context_builder.context_type,
            claude_optimized=True
        )
```

## 🛠️ Simple Implementation Steps

### Week 1: Immediate Improvements
1. **Increase chunk sizes** to 4000 characters with 800 overlap
2. **Add code-aware chunking** for .dart, .py, .cairo files
3. **Implement Claude-specific endpoints** with larger context
4. **Add project structure indexing** for better file understanding

### Week 2: Context Enhancement
1. **Build cross-reference system** for related concepts
2. **Create development context packages** for common scenarios
3. **Implement smart query routing** based on development intent
4. **Add dependency mapping** for better code relationships

### Week 3: Optimization
1. **Fine-tune chunk sizes** based on Claude usage patterns
2. **Optimize search algorithms** for development queries
3. **Add performance monitoring** for Claude-specific metrics
4. **Create usage analytics** to improve over time

## 📊 Expected Outcomes for Claude Code

### Immediate Benefits (Week 1)
- **4x larger context chunks** - Claude gets more complete information
- **Code-aware chunking** - Functions and classes stay together
- **Better search results** - More relevant development context

### Medium-term Benefits (Week 2-3)
- **Relationship understanding** - Claude sees connections between files
- **Pre-built context packages** - Faster access to common development scenarios
- **Smart query routing** - Tailored results based on development intent

### Long-term Benefits (Ongoing)
- **Continuous optimization** - System learns from Claude's usage patterns
- **Better development efficiency** - Claude can work with more complete context
- **Faster problem-solving** - Related information provided automatically

## 🎯 Success Metrics

### Claude Code Effectiveness
- **Context completeness**: 80% of Claude queries get complete context in first search
- **Development speed**: 50% faster issue resolution with better context
- **Code quality**: Better suggestions due to understanding full codebase relationships
- **Fewer follow-up queries**: Claude gets what it needs in fewer searches

### Technical Performance
- **Response time**: <100ms for enhanced searches
- **Context size**: 4000-8000 character chunks optimal for Claude
- **Search accuracy**: >90% relevance for development queries
- **System reliability**: 99.9% uptime for Claude Code sessions

## 📈 Implementation Priority

### High Priority (Week 1)
- [x] Increase chunk sizes for better Claude context
- [x] Implement code-aware chunking
- [x] Add Claude-specific search endpoints
- [x] Create project structure indexing

### Medium Priority (Week 2)
- [ ] Build cross-reference system
- [ ] Create development context packages
- [ ] Implement smart query routing
- [ ] Add dependency mapping

### Low Priority (Week 3)
- [ ] Fine-tune based on usage patterns
- [ ] Add advanced analytics
- [ ] Optimize performance
- [ ] Create monitoring dashboard

This focused plan transforms our RAG system into the optimal tool for Claude Code sessions, providing larger context, better understanding, and more efficient development workflows.

---

**Focus**: Claude Code Development Efficiency  
**Timeline**: 3 weeks  
**Primary Goal**: Better context retrieval for Claude Code sessions  
**Success Measure**: 50% faster development with Claude Code