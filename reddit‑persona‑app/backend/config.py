# backend/config.py

# ✅ Hardcoded Reddit API keys
REDDIT_CLIENT_ID     = "j6q-7lyi0MGUzGaeIkUYeQ"
REDDIT_CLIENT_SECRET = "vyFHBrTD3ZnylD6vVh97deStgsMjyA"
REDDIT_USER_AGENT    = "BeyondChats-Persona/0.1 by u/Sensitive-Power-4272"

# ✅ Gemini API key (Google Generative AI)
GOOGLE_API_KEY       = "AIzaSyAysOUma9D-gXFootFMq9U8h80yFPGXUj8"

# ✅ Sanity debug (will show up when config is loaded)
print("[CONFIG] Using hardcoded credentials:")
print(f"[CONFIG] Reddit ID: {REDDIT_CLIENT_ID}")
print(f"[CONFIG] Gemini Key starts with: {GOOGLE_API_KEY[:10]}...")
