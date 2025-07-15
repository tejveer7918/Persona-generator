from fastapi import FastAPI, Query
from pathlib import Path
from backend.fetch_reddit_data import fetch_reddit_data
from backend.process_persona import generate_persona

app = FastAPI()
DATA_DIR = Path("data"); DATA_DIR.mkdir(exist_ok=True)

@app.get("/persona")
def persona(username: str = Query(...)):
    url = f"https://www.reddit.com/user/{username}/"
    raw = fetch_reddit_data(url, DATA_DIR)
    return generate_persona(raw)
