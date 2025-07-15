from pathlib import Path
from backend.fetch_reddit_data import fetch_reddit_data
from backend.process_persona import generate_persona

DATA_DIR    = Path("data")
PROFILE_URL = "https://www.reddit.com/user/Hungry-Move-6603/"

def main():
    DATA_DIR.mkdir(exist_ok=True)
    raw   = fetch_reddit_data(PROFILE_URL, DATA_DIR)
    pers  = generate_persona(raw)
    print("\n=== Persona ===")
    print(pers)

if __name__ == "__main__":
    main()
