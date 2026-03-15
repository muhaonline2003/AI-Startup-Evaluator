"""
Backend API helper for Streamlit frontend.
All communication with FastAPI backend is done via these functions.
- This keeps Streamlit code clean and separates frontend from backend logic.
- Update BACKEND_URL if backend runs on a different port or host.
"""
import requests

BACKEND_URL = "http://localhost:8000"  # Change if backend runs elsewhere

def get_health():
    return requests.get(f"{BACKEND_URL}/health").json()

# --- Startups ---
def get_startups():
    return requests.get(f"{BACKEND_URL}/startups").json()

def create_startup(data):
    return requests.post(f"{BACKEND_URL}/startups", json=data).json()

def update_startup(startup_id, data):
    return requests.put(f"{BACKEND_URL}/startups/{startup_id}", json=data).json()

def delete_startup(startup_id):
    return requests.delete(f"{BACKEND_URL}/startups/{startup_id}").json()

# --- Investors ---
def get_investors():
    return requests.get(f"{BACKEND_URL}/investors").json()

def create_investor(data):
    return requests.post(f"{BACKEND_URL}/investors", json=data).json()

def update_investor(investor_id, data):
    return requests.put(f"{BACKEND_URL}/investors/{investor_id}", json=data).json()

def delete_investor(investor_id):
    return requests.delete(f"{BACKEND_URL}/investors/{investor_id}").json()

# --- Developers ---
def get_developers():
    return requests.get(f"{BACKEND_URL}/developers").json()

def create_developer(data):
    return requests.post(f"{BACKEND_URL}/developers", json=data).json()

def update_developer(developer_id, data):
    return requests.put(f"{BACKEND_URL}/developers/{developer_id}", json=data).json()

def delete_developer(developer_id):
    return requests.delete(f"{BACKEND_URL}/developers/{developer_id}").json()

# --- Events ---
def get_events():
    return requests.get(f"{BACKEND_URL}/events").json()

def create_event(data):
    return requests.post(f"{BACKEND_URL}/events", json=data).json()

def update_event(event_id, data):
    return requests.put(f"{BACKEND_URL}/events/{event_id}", json=data).json()

def delete_event(event_id):
    return requests.delete(f"{BACKEND_URL}/events/{event_id}").json()

# --- Networking ---
def get_networking():
    return requests.get(f"{BACKEND_URL}/networking").json()

def create_networking_post(data):
    return requests.post(f"{BACKEND_URL}/networking", json=data).json()

# --- AI ---
def ai_evaluate_startup(data):
    return requests.post(f"{BACKEND_URL}/ai/evaluate-startup", json=data).json()

def ai_assistant(data):
    return requests.post(f"{BACKEND_URL}/ai/assistant", json=data).json()
