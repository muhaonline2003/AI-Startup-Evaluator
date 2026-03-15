"""
Pydantic models for FastAPI backend.
Defines schemas for startups, investors, developers, events, networking, and AI requests/responses.
"""
from pydantic import BaseModel
from typing import List, Optional

# --- Startup Models ---
class StartupBase(BaseModel):
    name: str
    founder: str
    industry: str
    stage: str
    problem: str
    solution: str
    target_market: str
    business_model: Optional[str] = None
    traction: Optional[str] = None
    funding_ask: Optional[str] = None
    pitch_text: Optional[str] = None
    analysis: Optional[dict] = None

class StartupCreate(StartupBase):
    pass

class StartupUpdate(StartupBase):
    pass

class Startup(StartupBase):
    id: int

# --- Investor Models ---
class InvestorBase(BaseModel):
    name: str
    firm: Optional[str] = None
    sector_interests: Optional[str] = None
    stage_preference: Optional[str] = None
    ticket_size: Optional[str] = None
    location: Optional[str] = None
    bio: Optional[str] = None

class InvestorCreate(InvestorBase):
    pass
class InvestorUpdate(InvestorBase):
    pass
class Investor(InvestorBase):
    id: int

# --- Developer Models ---
class DeveloperBase(BaseModel):
    name: str
    skills: Optional[str] = None
    preferred_roles: Optional[str] = None
    preferred_startup_stage: Optional[str] = None
    availability: Optional[str] = None
    portfolio_link: Optional[str] = None
    bio: Optional[str] = None

class DeveloperCreate(DeveloperBase):
    pass
class DeveloperUpdate(DeveloperBase):
    pass
class Developer(DeveloperBase):
    id: int

# --- Event Models ---
class EventBase(BaseModel):
    name: str
    date: str
    type: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None

class EventCreate(EventBase):
    pass
class EventUpdate(EventBase):
    pass
class Event(EventBase):
    id: int

# --- Networking Models ---
class NetworkingPostBase(BaseModel):
    founder_name: str
    startup_name: Optional[str] = None
    looking_for: str
    message: str
    created_at: Optional[str] = None

class NetworkingPostCreate(NetworkingPostBase):
    pass
class NetworkingPost(NetworkingPostBase):
    id: int

# --- AI Models ---
class AIStartupEvalRequest(BaseModel):
    name: str
    founder: str
    industry: str
    stage: str
    problem: str
    solution: str
    target_market: str
    business_model: Optional[str] = None
    traction: Optional[str] = None
    funding_ask: Optional[str] = None
    pitch_text: Optional[str] = None

class AIAssistantRequest(BaseModel):
    role: str
    question: str
