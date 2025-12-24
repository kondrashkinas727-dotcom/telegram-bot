import json
from pathlib import Path
from config import FILES_DIR

def export_json(data, filename):
    path = Path(FILES_DIR) / f"{filename}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return path
