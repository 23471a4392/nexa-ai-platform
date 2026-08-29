# NexaAI Backend Modules Catalog

The NexaAI backend contains modular domain handlers located in `backend/modules/`:

| Module | Purpose |
|---|---|
| `agents.py` | Agent registry, personality configuration, and tool binding |
| `analytics.py` | Event ingestion, query analytics, latency tracking |
| `apikeys.py` | API key lifecycle, scoping, prefix generation, and verification |
| `audit.py` | Security audit logging and compliance event records |
| `auth.py` | JWT token authentication, user session security |
| `billing.py` | Metered billing calculations, stripe webhook bindings |
| `cache.py` | Distributed memory caching and prompt cache layer |
| `chat.py` | Conversation thread management and message history |
| `embeddings.py` | Dense vector embedding generation and cosine similarity |
| `guardrails.py` | Input sanitization, prompt injection protection, safety policies |
| `knowledge.py` | Document knowledge base graph and indexing pipeline |
| `marketplace.py` | Agent and plugin public/private ecosystem store |
| `moderation.py` | Toxic content detection and automated redacting |
| `monitoring.py` | Prometheus-compatible metrics collector |
| `orchestration.py` | Multi-step agent task planning and DAG execution |
| `quotas.py` | Token limits, request bursting, and tier enforcement |
| `rag.py` | Retrieval-Augmented Generation retrieval and context synthesis |
| `ratelimits.py` | Sliding window rate limiters per IP / API key |
| `scheduler.py` | Background recurring jobs and async worker queues |
| `security.py` | Cryptographic hashing, token verification, CSRF defense |
| `tools.py` | Custom tool execution runtime for autonomous agents |
| `webhooks.py` | Outbound webhook notification dispatcher |
| `workflows.py` | Multi-agent workflow pipelines and trigger management |
