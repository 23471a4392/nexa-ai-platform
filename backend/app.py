from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import uuid

app = Flask(__name__)
CORS(app)

STORE = {"chats": [], "documents": [], "agents": [], "api_keys": []}

@app.get('/api/health')
def health():
    return jsonify({"status":"ok","service":"NexaAI API","time":datetime.utcnow().isoformat()+'Z'})

@app.get('/api/dashboard')
def dashboard():
    return jsonify({"usage": {"tokens": 184320, "requests": 4821, "cost": 37.42}, "users": 1284, "documents": 342, "agents": 19})

@app.get('/api/chats')
def chats(): return jsonify(STORE['chats'])

@app.post('/api/chats')
def create_chat():
    data=request.get_json(silent=True) or {}
    item={"id":str(uuid.uuid4()),"title":data.get('title','New AI Conversation'),"created_at":datetime.utcnow().isoformat()}
    STORE['chats'].append(item); return jsonify(item),201

@app.post('/api/documents')
def document():
    data=request.get_json(silent=True) or {}
    item={"id":str(uuid.uuid4()),"name":data.get('name','Untitled document'),"status":"indexed"}
    STORE['documents'].append(item); return jsonify(item),201

@app.get('/api/agents')
def agents(): return jsonify(STORE['agents'])

@app.post('/api/agents')
def create_agent():
    data=request.get_json(silent=True) or {}
    item={"id":str(uuid.uuid4()),"name":data.get('name','Untitled Agent'),"model":data.get('model','Nexa Reasoner'),"status":"active"}
    STORE['agents'].append(item); return jsonify(item),201

@app.get('/api/keys')
def keys(): return jsonify(STORE['api_keys'])

@app.post('/api/keys')
def create_key():
    item={"id":str(uuid.uuid4()),"name":"New API Key","prefix":"nx_live_","created_at":datetime.utcnow().isoformat()}
    STORE['api_keys'].append(item); return jsonify(item),201

@app.post('/api/echo')
def echo():
    data=request.get_json(silent=True) or {}
    return jsonify({"reply":"NexaAI received your request.","input":data.get('message','')})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
