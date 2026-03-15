"""
FastAPI backend entry point for the Startup Ecosystem app.
- Exposes REST API endpoints for CRUD and AI operations.
- Handles all business logic and JSON storage.
- Streamlit frontend communicates with this backend via HTTP requests.
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend import crud, ai, models
from typing import List

app = FastAPI(title="Startup Ecosystem Backend")

# Allow CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    """Health check endpoint."""
    return {"status": "ok"}

# --- Startups CRUD ---
@app.get("/startups", response_model=List[models.Startup])
def get_startups():
    return crud.load_startups()

@app.post("/startups", response_model=models.Startup)
def create_startup(startup: models.StartupCreate):
    return crud.create_startup(startup)

@app.put("/startups/{startup_id}", response_model=models.Startup)
def update_startup(startup_id: int, startup: models.StartupUpdate):
    return crud.update_startup(startup_id, startup)

@app.delete("/startups/{startup_id}")
def delete_startup(startup_id: int):
    crud.delete_startup(startup_id)
    return {"ok": True}

# --- Investors CRUD ---
@app.get("/investors", response_model=List[models.Investor])
def get_investors():
    return crud.load_investors()

@app.post("/investors", response_model=models.Investor)
def create_investor(investor: models.InvestorCreate):
    return crud.create_investor(investor)

@app.put("/investors/{investor_id}", response_model=models.Investor)
def update_investor(investor_id: int, investor: models.InvestorUpdate):
    return crud.update_investor(investor_id, investor)

@app.delete("/investors/{investor_id}")
def delete_investor(investor_id: int):
    crud.delete_investor(investor_id)
    return {"ok": True}

# --- Developers CRUD ---
@app.get("/developers", response_model=List[models.Developer])
def get_developers():
    return crud.load_developers()

@app.post("/developers", response_model=models.Developer)
def create_developer(developer: models.DeveloperCreate):
    return crud.create_developer(developer)

@app.put("/developers/{developer_id}", response_model=models.Developer)
def update_developer(developer_id: int, developer: models.DeveloperUpdate):
    return crud.update_developer(developer_id, developer)

@app.delete("/developers/{developer_id}")
def delete_developer(developer_id: int):
    crud.delete_developer(developer_id)
    return {"ok": True}

# --- Events CRUD ---
@app.get("/events", response_model=List[models.Event])
def get_events():
    return crud.load_events()

@app.post("/events", response_model=models.Event)
def create_event(event: models.EventCreate):
    return crud.create_event(event)

@app.put("/events/{event_id}", response_model=models.Event)
def update_event(event_id: int, event: models.EventUpdate):
    return crud.update_event(event_id, event)

@app.delete("/events/{event_id}")
def delete_event(event_id: int):
    crud.delete_event(event_id)
    return {"ok": True}

# --- Networking CRUD ---
@app.get("/networking", response_model=List[models.NetworkingPost])
def get_networking():
    return crud.load_networking_posts()

@app.post("/networking", response_model=models.NetworkingPost)
def create_networking(post: models.NetworkingPostCreate):
    return crud.create_networking_post(post)

# --- AI Endpoints ---
@app.post("/ai/evaluate-startup")
def ai_evaluate_startup(payload: models.AIStartupEvalRequest):
    return ai.analyze_startup_pitch(payload)

@app.post("/ai/assistant")
def ai_assistant(payload: models.AIAssistantRequest):
    return ai.assistant_response(payload)
