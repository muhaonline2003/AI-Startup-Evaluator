"""
AI logic for FastAPI backend.
Handles OpenAI API calls and graceful demo mode fallback.
"""
import os
import random
import json
from backend import models
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# --- OpenAI client ---
def get_openai_client():
    if OPENAI_API_KEY:
        return OpenAI(api_key=OPENAI_API_KEY)
    return OpenAI()

client = get_openai_client()

def show_demo_mode_banner():
    return {"demo_mode": True, "message": "Demo AI Mode: OpenAI unavailable, using mock analysis"}

def mock_ai_analysis(startup=None):
    names = ["Impressive team", "Clear market", "Strong solution", "Needs traction", "Competitive space"]
    summary = f"{random.choice(['Promising','Solid','Interesting','Early-stage','Competitive'])} startup with {random.choice(['a clear problem','a strong team','market potential','room for improvement'])}."
    score = random.choice(["7.5", "8.2", "6.8", "7.9", "8.7", "6.2"])
    return {
        "summary": summary,
        "score": score,
        "problem_clarity": random.choice(["Clear", "Good", "Moderate", "Needs work"]),
        "solution_strength": random.choice(["Strong", "Good", "Average", "Unclear"]),
        "market_potential": random.choice(["High", "Moderate", "Emerging", "Niche"]),
        "business_model": random.choice(["SaaS", "Marketplace", "Subscription", "Freemium"]),
        "investor_readiness": random.choice(["Ready for seed", "Needs more traction", "Promising but early", "Investor-ready"]),
        "investor_recommendation": random.choice(["Consider for next round", "Monitor progress", "Schedule meeting", "Pass for now"]),
        "strengths": [random.choice(names), "Clear vision"],
        "weaknesses": [random.choice(["Needs more data", "Unclear go-to-market", "Early revenue"]),],
        "risks": [random.choice(["Market crowded", "Tech risk", "Execution risk"]),],
        "suggestions": [random.choice(["Clarify business model", "Show more traction", "Refine pitch deck"]), "Highlight team experience"],
    }

def analyze_startup_pitch(payload: models.AIStartupEvalRequest):
    pitch_text = payload.pitch_text or ""
    system_prompt = (
        "You are an objective, professional startup evaluator. "
        "You analyze startup pitches for accelerators and early-stage investors. "
        "Always return clear, constructive and honest feedback."
    )
    user_prompt = f"""
Analyze this startup pitch and return valid JSON with:
{{
    \"summary\": \"\",  
    \"score\": \"\",  
    \"problem_clarity\": \"\",  
    \"solution_strength\": \"\",  
    \"market_potential\": \"\",  
    \"business_model\": \"\",  
    \"investor_readiness\": \"\",  
    \"investor_recommendation\": \"\",  
    \"strengths\": [],  
    \"weaknesses\": [],  
    \"risks\": [],  
    \"suggestions\": []  
}}

Startup details:
Name: {payload.name}
Founder: {payload.founder}
Industry: {payload.industry}
Stage: {payload.stage}
Problem: {payload.problem}
Solution: {payload.solution}
Target Market: {payload.target_market}

Pitch:
{pitch_text}
"""
    try:
        if not OPENAI_API_KEY or OPENAI_API_KEY.strip() == "":
            return mock_ai_analysis(payload)
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        content = response.choices[0].message.content
        data = json.loads(content)
        return data
    except Exception:
        return mock_ai_analysis(payload)

def assistant_response(payload: models.AIAssistantRequest):
    """Handles general AI assistant Q&A using OpenAI chat completion."""
    system_prompt = (
        f"You are an expert startup assistant. Answer as a helpful, concise mentor for the following role: {payload.role}. "
        "Give actionable, practical advice for founders, investors, or ecosystem members."
    )
    user_prompt = payload.question
    try:
        if not OPENAI_API_KEY or OPENAI_API_KEY.strip() == "":
            return {"answer": "This is a demo AI assistant response. Add your OpenAI key for real answers."}
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            max_tokens=350,
            temperature=0.7,
        )
        content = response.choices[0].message.content
        return {"answer": content}
    except Exception as e:
        return {"answer": f"AI assistant error: {str(e)}"}
