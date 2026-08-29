# NexaAI Platform Architecture

## Overview

NexaAI is a high-performance enterprise AI SaaS starter platform architected for scalable conversational intelligence, document intelligence (RAG), autonomous AI agent orchestration, real-time telemetry, rate limiting, and multi-tenant billing.

```
┌─────────────────────────────────────────────────────────────┐
│                    NexaAI Frontend UI                       │
│        (HTML5 / Modern Vanilla JS / Glassmorphism CSS)      │
└──────────────────────────────┬──────────────────────────────┘
                               │ REST / JSON APIs
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                   NexaAI API Gateway (Flask)                │
├──────────────────────────────┬──────────────────────────────┤
│ Core Endpoints               │ Enterprise Middleware        │
│  - /api/health               │  - CORS Management           │
│  - /api/dashboard            │  - Rate Limiting             │
│  - /api/chats                │  - Auth & Token Verification │
│  - /api/documents            │  - Structured Logging        │
│  - /api/agents               │  - Metrics & Telemetry       │
│  - /api/keys                 │                              │
└──────────────────────────────┴──────────────────────────────┘
                               │
            ┌──────────────────┼──────────────────┐
            ▼                  ▼                  ▼
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│  AI Engine (RAG) │  │ Agent Orchestrator│  │  Platform Stores │
├──────────────────┤  ├──────────────────┤  ├──────────────────┤
│ - Vector Search  │  │ - Multi-Agent    │  │ - Session Store  │
│ - Embeddings     │  │ - Tool Execution │  │ - Document Meta  │
│ - Chunking       │  │ - Guardrails     │  │ - Billing / Keys │
│ - Document Parser│  │ - Memory Cache   │  │ - Analytics Logs │
└──────────────────┘  └──────────────────┘  └──────────────────┘
```

## System Components

### 1. API Service Layer (`backend/app.py`)
- Provides lightweight, high-throughput REST endpoints.
- In-memory data store with JSON persistence capabilities.
- Extensible controller structure for pluggable domain modules.

### 2. Domain Modules (`backend/modules/`)
- **Agents & Orchestration**: Agent lifecycle management, prompt templates, tool execution.
- **RAG & Knowledge**: Chunking, vector indexing, document retrieval, and guardrail enforcement.
- **Billing & Subscriptions**: Usage quotas, token metering, subscription tier validation.
- **Security & Governance**: API key hashing, role-based permissions, rate limiting.

### 3. Frontend Dashboard (`frontend/`)
- Single-page application dashboard rendered without heavy framework overhead.
- Real-time token usage, request metrics, and system status.
- Interactive managers for chats, documents, agents, and API credentials.
