# 🇩🇪 AI German Tutor using Retrieval-Augmented Generation (RAG)

> An AI-powered German language tutor designed to provide context-aware grammar explanations, vocabulary assistance, examples, and conversational learning using Retrieval-Augmented Generation.

## 📌 Project Overview

**AI German Tutor** is an ongoing RAG-based project that combines a German learning knowledge base, semantic retrieval, language models, and contextual prompting to act as a retrieval-grounded tutor rather than a simple chatbot.

The project is being developed as a **modular and extensible RAG system**. The architecture below represents the overall intended direction — some components are already implemented, others are planned.

## 🎯 Goals

- German grammar explanations and vocabulary assistance
- Context-based question answering with German examples
- Conversational learning with memory across turns
- Hybrid (semantic + keyword) retrieval from German learning material
- A path toward a production-style deployment (API, database, containers)

## 🏗️ Architecture

```text
                     ┌──────────────┐
                     │     User     │
                     └──────┬───────┘
                            ▼
                     ┌──────────────┐
                     │   FastAPI    │
                     └──────┬───────┘
                            ▼
                     ┌──────────────┐
                     │  LangChain   │
                     │ Orchestration│
                     └──────┬───────┘
                            │
              ┌─────────────┴─────────────┐
              ▼                           ▼
     ┌──────────────────┐        ┌──────────────────┐
     │ Hybrid Retrieval  │        │  Conversation    │
     │ (Semantic +       │        │     Memory       │
     │  Keyword Search)  │        └──────────────────┘
     └────────┬──────────┘
              ▼
     ┌───────────────────────┐        ┌──────────────────────┐
     │ PostgreSQL + pgvector │◄───────│ Hugging Face          │
     │ Documents / Chunks /  │        │ Embedding Models      │
     │ Embeddings / Metadata │        └──────────────────────┘
     └────────┬──────────────┘
              ▼
     ┌───────────────────┐
     │ Contextual Prompt │
     └────────┬──────────┘
              ▼
     ┌───────────────────┐
     │ Ollama + Local LLM│
     └────────┬──────────┘
              ▼
     ┌───────────────────┐
     │ German Tutor       │
     │ Response           │
     └───────────────────┘

  n8n    → external workflow automation
  Docker → containerization / deployment
```

## 🔄 End-to-End Dataflow

```text
German Learning Material
        ↓
Document Loading + Text Extraction
        ↓
Chunking + Metadata
        ↓
Hugging Face Embeddings
        ↓
Vector Storage (PostgreSQL + pgvector)
        ↓
User Question → Query Embedding
        ↓
Hybrid Retrieval (Semantic + Keyword) + Reranking
        ↓
Relevant Context + Conversation Memory
        ↓
Contextual Prompt
        ↓
Ollama / Local LLM
        ↓
German Tutor Response
```

## 📁 Repository Structure

```text
german-rag-tutor/
│
├── data/
│   └── sample_text.txt        # Source German learning material
│
├── src/
│   ├── __init__.py
│   ├── utils.py                # Text loading, chunking, shared helpers
│   ├── ingest.py                # Ingestion: load → chunk → embed → store
│   └── search.py                # Query embedding → similarity search
│
├── storage/
│   ├── chunks.json             # Processed text chunks
│   └── embeddings.npy          # Vector representations
│
├── README.md
├── requirements.txt
└── .gitignore
```

## 🛠️ Technology Stack

| Technology | Intended Role |
|---|---|
| **Python** | Core application and RAG implementation |
| **Hugging Face** | Embedding models |
| **LangChain** | RAG orchestration |
| **PostgreSQL + pgvector** | Structured + vector data storage |
| **FastAPI** | Backend API |
| **Ollama** | Local LLM inference |
| **Docker** | Containerization and deployment |
| **n8n** | Workflow automation |

## 🗺️ Development Roadmap

```text
[✓] Basic document ingestion
[✓] Text chunking
[✓] Multilingual embeddings
[✓] Local vector storage
[✓] Initial semantic retrieval

[→] Improve hybrid retrieval
[→] Metadata-aware retrieval
[→] Contextual prompt construction
[→] RAG response generation

[ ] Ollama integration
[ ] Conversation memory
[ ] FastAPI backend
[ ] PostgreSQL + pgvector integration
[ ] LangChain orchestration
[ ] Docker deployment
[ ] n8n automation
[ ] Additional knowledge sources
```

## 🚀 Future Possibilities

CEFR-level tutoring modes, vocabulary quizzes and grammar exercises, automatic answer evaluation, spaced repetition, personalized learning history, PDF/document ingestion, voice-based interaction, and a web-based frontend.

## 📌 Project Status

This repository is an **ongoing implementation** of the AI German Tutor architecture described above. Not every component is implemented yet — the project is being built incrementally, starting with the retrieval foundation and moving toward a full RAG application with hybrid retrieval, contextual prompting, conversation memory, a local LLM, an API layer, a vector database, containerization, and workflow automation.

## 👨‍💻 Author

**Prathamesh Sudhir Uthale**
MSc Computer Science — Intelligent Systems
RPTU, Germany

## ⭐ Project Vision

> Build a modular AI tutor that combines retrieval, language models, and contextual learning to make German grammar and vocabulary easier to understand, practice, and remember.
