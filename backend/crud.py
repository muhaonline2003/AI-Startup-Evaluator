"""
CRUD logic for FastAPI backend.
Handles reading/writing JSON files for startups, investors, developers, events, and networking posts.
"""
import json
import os
from typing import List, Dict, Any
from backend import models
from datetime import datetime

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
STARTUPS_DB_PATH = os.path.join(DATA_DIR, '../startups.json')
INVESTORS_DB_PATH = os.path.join(DATA_DIR, '../investors.json')
DEVELOPERS_DB_PATH = os.path.join(DATA_DIR, '../developers.json')
EVENTS_DB_PATH = os.path.join(DATA_DIR, '../events.json')
NETWORKING_DB_PATH = os.path.join(DATA_DIR, '../networking.json')

def _load_json(path: str) -> list:
    if not os.path.exists(path):
        return []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []

def _save_json(path: str, data: list):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# --- Startups ---
def load_startups() -> List[models.Startup]:
    data = _load_json(STARTUPS_DB_PATH)
    return [models.Startup(**item) for item in data]

def create_startup(startup: models.StartupCreate) -> models.Startup:
    startups = _load_json(STARTUPS_DB_PATH)
    new_id = max([s.get('id', 0) for s in startups] or [0]) + 1
    item = startup.dict()
    item['id'] = new_id
    startups.append(item)
    _save_json(STARTUPS_DB_PATH, startups)
    return models.Startup(**item)

def update_startup(startup_id: int, startup: models.StartupUpdate) -> models.Startup:
    startups = _load_json(STARTUPS_DB_PATH)
    for idx, s in enumerate(startups):
        if int(s.get('id')) == int(startup_id):
            updated = startup.dict()
            updated['id'] = startup_id
            startups[idx] = updated
            _save_json(STARTUPS_DB_PATH, startups)
            return models.Startup(**updated)
    raise ValueError('Startup not found')

def delete_startup(startup_id: int):
    startups = _load_json(STARTUPS_DB_PATH)
    startups = [s for s in startups if int(s.get('id')) != int(startup_id)]
    _save_json(STARTUPS_DB_PATH, startups)

# --- Investors ---
def load_investors() -> List[models.Investor]:
    data = _load_json(INVESTORS_DB_PATH)
    return [models.Investor(**item) for item in data]

def create_investor(investor: models.InvestorCreate) -> models.Investor:
    investors = _load_json(INVESTORS_DB_PATH)
    new_id = max([i.get('id', 0) for i in investors] or [0]) + 1
    item = investor.dict()
    item['id'] = new_id
    investors.append(item)
    _save_json(INVESTORS_DB_PATH, investors)
    return models.Investor(**item)

def update_investor(investor_id: int, investor: models.InvestorUpdate) -> models.Investor:
    investors = _load_json(INVESTORS_DB_PATH)
    for idx, i in enumerate(investors):
        if int(i.get('id')) == int(investor_id):
            updated = investor.dict()
            updated['id'] = investor_id
            investors[idx] = updated
            _save_json(INVESTORS_DB_PATH, investors)
            return models.Investor(**updated)
    raise ValueError('Investor not found')

def delete_investor(investor_id: int):
    investors = _load_json(INVESTORS_DB_PATH)
    investors = [i for i in investors if int(i.get('id')) != int(investor_id)]
    _save_json(INVESTORS_DB_PATH, investors)

# --- Developers ---
def load_developers() -> List[models.Developer]:
    data = _load_json(DEVELOPERS_DB_PATH)
    return [models.Developer(**item) for item in data]

def create_developer(developer: models.DeveloperCreate) -> models.Developer:
    developers = _load_json(DEVELOPERS_DB_PATH)
    new_id = max([d.get('id', 0) for d in developers] or [0]) + 1
    item = developer.dict()
    item['id'] = new_id
    developers.append(item)
    _save_json(DEVELOPERS_DB_PATH, developers)
    return models.Developer(**item)

def update_developer(developer_id: int, developer: models.DeveloperUpdate) -> models.Developer:
    developers = _load_json(DEVELOPERS_DB_PATH)
    for idx, d in enumerate(developers):
        if int(d.get('id')) == int(developer_id):
            updated = developer.dict()
            updated['id'] = developer_id
            developers[idx] = updated
            _save_json(DEVELOPERS_DB_PATH, developers)
            return models.Developer(**updated)
    raise ValueError('Developer not found')

def delete_developer(developer_id: int):
    developers = _load_json(DEVELOPERS_DB_PATH)
    developers = [d for d in developers if int(d.get('id')) != int(developer_id)]
    _save_json(DEVELOPERS_DB_PATH, developers)

# --- Events ---
def load_events() -> List[models.Event]:
    data = _load_json(EVENTS_DB_PATH)
    return [models.Event(**item) for item in data]

def create_event(event: models.EventCreate) -> models.Event:
    events = _load_json(EVENTS_DB_PATH)
    new_id = max([e.get('id', 0) for e in events] or [0]) + 1
    item = event.dict()
    item['id'] = new_id
    events.append(item)
    _save_json(EVENTS_DB_PATH, events)
    return models.Event(**item)

def update_event(event_id: int, event: models.EventUpdate) -> models.Event:
    events = _load_json(EVENTS_DB_PATH)
    for idx, e in enumerate(events):
        if int(e.get('id')) == int(event_id):
            updated = event.dict()
            updated['id'] = event_id
            events[idx] = updated
            _save_json(EVENTS_DB_PATH, events)
            return models.Event(**updated)
    raise ValueError('Event not found')

def delete_event(event_id: int):
    events = _load_json(EVENTS_DB_PATH)
    events = [e for e in events if int(e.get('id')) != int(event_id)]
    _save_json(EVENTS_DB_PATH, events)

# --- Networking ---
def load_networking_posts() -> List[models.NetworkingPost]:
    data = _load_json(NETWORKING_DB_PATH)
    return [models.NetworkingPost(**item) for item in data]

def create_networking_post(post: models.NetworkingPostCreate) -> models.NetworkingPost:
    posts = _load_json(NETWORKING_DB_PATH)
    new_id = max([p.get('id', 0) for p in posts] or [0]) + 1
    item = post.dict()
    item['id'] = new_id
    item['created_at'] = item.get('created_at') or datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
    posts.append(item)
    _save_json(NETWORKING_DB_PATH, posts)
    return models.NetworkingPost(**item)
