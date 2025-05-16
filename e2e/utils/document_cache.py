import json
from pathlib import Path

DATA_FILE = Path("document_store.json")


def save_document(name: str, value: str):
    data = load_all()
    data[name] = value
    DATA_FILE.write_text(json.dumps(data))


def load_document(name: str) -> str:
    return load_all().get(name)


def load_all() -> dict:
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return {}
