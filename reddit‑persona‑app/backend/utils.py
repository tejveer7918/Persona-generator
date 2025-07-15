import json
from pathlib import Path
from typing import Any

def load_json(path: Path) -> Any:
    return json.loads(path.read_text())

def save_json(obj: Any, path: Path) -> None:
    path.write_text(json.dumps(obj, indent=2))
