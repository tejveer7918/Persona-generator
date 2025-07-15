# backend/process_persona.py

import json
import requests
from pathlib import Path
from backend.config import GOOGLE_API_KEY
from backend.utils import load_json, save_json

OUTPUT_DIR = Path("data")
MODEL = "models/gemini-2.0-flash"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/{MODEL}:generateContent"

def _call_gemini(raw_data: dict) -> dict:
    if not GOOGLE_API_KEY:
        raise Exception("Missing GOOGLE_API_KEY in environment or config.")

    # Compose prompt
    prompt = f"""
You are an expert researcher. Based on the following Reddit user’s posts and comments,
generate a concise persona profile in structured JSON.

Output keys: persona_name, demographics, psychographics, goals, frustrations,
reddit_usage, quote.

Reddit User JSON:
{json.dumps(raw_data, indent=2)}
"""

    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": GOOGLE_API_KEY
    }

    body = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    response = requests.post(API_URL, headers=headers, json=body)

    if response.status_code != 200:
        print("⚠️ Gemini API error:", response.status_code)
        try:
            print(response.json())
        except Exception:
            print(response.text)
        raise Exception(f"Gemini API error {response.status_code}")

    try:
        reply = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        # Remove code fences if present
        if reply.strip().startswith("```json"):
            reply = reply.strip().removeprefix("```json").removesuffix("```").strip()
        return json.loads(reply)
    except Exception as e:
        print("❌ Failed to parse Gemini response.")
        print("Raw:", reply)
        raise ValueError(f"Failed to parse Gemini response: {e}")

def generate_persona(raw_path: Path) -> dict:
    raw_data = load_json(raw_path)
    username = raw_data["username"]
    persona_path = OUTPUT_DIR / f"{username}_persona.json"

    if persona_path.exists():
        return load_json(persona_path)

    persona = _call_gemini(raw_data)

    # ✅ Attach avatar from Reddit
    persona["avatar_url"] = raw_data.get("avatar_url", "https://via.placeholder.com/300")

    save_json(persona, persona_path)
    return persona
