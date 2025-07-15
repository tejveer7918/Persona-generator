"""
backend/fetch_reddit_data.py
Scrapes a Reddit user’s recent submissions & comments with PRAW,
converts each item to a JSON‑serialisable dict, and caches the result
in data/<username>_raw.json
"""

from pathlib import Path
from urllib.parse import urlparse
import praw
from backend.config import (
    REDDIT_CLIENT_ID,
    REDDIT_CLIENT_SECRET,
    REDDIT_USER_AGENT,
)
from backend.utils import save_json

POST_LIMIT = 50  # number of submissions & comments to fetch


# ---------- helpers -------------------------------------------------
def _username(profile_url: str) -> str:
    parts = urlparse(profile_url).path.strip("/").split("/")
    if "user" in parts:
        return parts[parts.index("user") + 1]
    if parts:
        return parts[-1]
    raise ValueError("Bad Reddit profile URL")


def _safe_dict(obj) -> dict:
    """Return a JSON‑serialisable subset of PRAW Submission / Comment."""
    return {
        k: v
        for k, v in vars(obj).items()
        if isinstance(
            v, (str, int, float, bool, type(None), list, dict)
        )
    }


# ---------- main scraper -------------------------------------------
def fetch_reddit_data(profile_url: str, cache_dir: Path) -> Path:
    """
    Fetches data, caches it, and returns the path to the cached JSON file.
    """
    username = _username(profile_url)
    cache_dir.mkdir(exist_ok=True)
    raw_path = cache_dir / f"{username}_raw.json"

    if raw_path.exists():
        print(f"[cache] Reddit data for u/{username}")
        return raw_path

    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT,
    )

    redditor = reddit.redditor(username)
    avatar_url = getattr(redditor, "icon_img", "https://via.placeholder.com/300")

    print(f"[scrape] submissions for u/{username}")
    submissions = [_safe_dict(s) for s in redditor.submissions.new(limit=POST_LIMIT)]

    print(f"[scrape] comments for u/{username}")
    comments = [_safe_dict(c) for c in redditor.comments.new(limit=POST_LIMIT)]

    data = {
        "username": username,
        "avatar_url": avatar_url,   # 👈 include profile picture
        "submissions": submissions,
        "comments": comments,
    }

    save_json(data, raw_path)
    print(f"[save] → {raw_path}")
    return raw_path
