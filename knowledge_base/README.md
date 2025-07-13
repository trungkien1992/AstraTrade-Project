# Universal RAG/AI Backend

This repository provides a high-performance, project-agnostic Retrieval-Augmented Generation (RAG) backend for multi-platform knowledge bases. It is designed to serve as a standalone AI-powered documentation and search service for any project or platform.

## Features
- Deep document understanding and semantic search
- Template-based chunking and grounded citations
- Multi-modal content support
- Advanced search and categorization
- Knowledge graph integration (optional)
- Extensible platform/documentation indexing

## Usage

### 1. Start the RAG Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

The API will be available at http://localhost:8000

### 2. API Endpoints
- `/search` — Query the knowledge base with natural language
- `/index` — Index new documentation or code
- `/stats` — Get system statistics
- `/graph` — (Optional) Knowledge graph queries

See the OpenAPI docs at `/docs` for full details.

### 3. Integrating with Your Project
- Use the `/search` endpoint to power in-app documentation, code search, or AI assistants.
- Index your own documentation or codebase using the `/index` endpoint.
- Extend platform/documentation indexers for your specific needs.

## Customization
- Add or modify platform indexers in `rag_system.py` for your project.
- Update categorization logic in `categorization_system.py` as needed.
- Use the knowledge graph for advanced relationship tracking.

## No Project Lock-In
This backend is now fully decoupled from any specific app or platform. You can use it for any project requiring advanced RAG/AI-powered documentation and search.

---

For advanced configuration, see the `docs/` folder and in-code comments.
