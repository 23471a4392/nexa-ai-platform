# NexaAI REST API Reference

Base URL: `http://localhost:8000`

All endpoints consume and return `application/json` unless stated otherwise.

---

### 1. Health & Status

#### `GET /api/health`
Returns current server health status and UTC timestamp.

**Response `200 OK`**:
```json
{
  "status": "ok",
  "service": "NexaAI API",
  "time": "2026-08-29T11:20:00.000Z"
}
```

---

### 2. Dashboard Telemetry

#### `GET /api/dashboard`
Returns high-level platform telemetry, token consumption, and entity counts.

**Response `200 OK`**:
```json
{
  "usage": {
    "tokens": 184320,
    "requests": 4821,
    "cost": 37.42
  },
  "users": 1284,
  "documents": 342,
  "agents": 19
}
```

---

### 3. Conversations (`/api/chats`)

#### `GET /api/chats`
Lists all active conversation sessions.

#### `POST /api/chats`
Creates a new conversation session.

**Request Body**:
```json
{
  "title": "Customer Support Agent Chat"
}
```

**Response `201 Created`**:
```json
{
  "id": "c83b7f14-4321-4f91-9c60-84a51e6be951",
  "title": "Customer Support Agent Chat",
  "created_at": "2026-08-29T11:22:00.000"
}
```

---

### 4. Document Management (`/api/documents`)

#### `POST /api/documents`
Uploads and indexes a document for semantic search (RAG).

**Request Body**:
```json
{
  "name": "Product_Specifications_v2.pdf"
}
```

**Response `201 Created`**:
```json
{
  "id": "d921b72a-61f2-4e08-9b88-51829e0a6d13",
  "name": "Product_Specifications_v2.pdf",
  "status": "indexed"
}
```

---

### 5. Autonomous Agents (`/api/agents`)

#### `GET /api/agents`
Returns all provisioned AI agents.

#### `POST /api/agents`
Creates an autonomous agent definition.

**Request Body**:
```json
{
  "name": "Research Specialist",
  "model": "Nexa Reasoner"
}
```

**Response `201 Created`**:
```json
{
  "id": "a14389fb-1290-482a-9e17-73d82a10be55",
  "name": "Research Specialist",
  "model": "Nexa Reasoner",
  "status": "active"
}
```

---

### 6. API Key Management (`/api/keys`)

#### `GET /api/keys`
Lists registered API keys.

#### `POST /api/keys`
Generates a new secure live API key token.

**Response `201 Created`**:
```json
{
  "id": "k82910fa-4910-482c-a294-8192a7182911",
  "name": "New API Key",
  "prefix": "nx_live_",
  "created_at": "2026-08-29T11:25:00.000"
}
```
