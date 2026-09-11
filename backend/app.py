from __future__ import annotations
import json
import sqlite3
from pathlib import Path
from flask import Flask, jsonify, request, send_from_directory

BASE = Path(__file__).resolve().parent.parent
DB = BASE / "data" / "wordkeep.db"
FRONTEND = BASE / "frontend"
DB.parent.mkdir(parents=True, exist_ok=True)

app = Flask(__name__, static_folder=str(FRONTEND), static_url_path="")


def connect():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    return con


def init_db():
    with connect() as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS app_state (
                key TEXT PRIMARY KEY,
                value_json TEXT NOT NULL,
                updated_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)


@app.get("/api/health")
def health():
    init_db()
    with connect() as con:
        con.execute("SELECT 1")
    return jsonify(ok=True, database="sqlite")


@app.get("/api/state/<key>")
def get_state(key: str):
    init_db()
    with connect() as con:
        row = con.execute("SELECT value_json FROM app_state WHERE key=?", (key,)).fetchone()
    if not row:
        return jsonify(exists=False, value=None)
    try:
        value = json.loads(row["value_json"])
    except json.JSONDecodeError:
        value = None
    return jsonify(exists=True, value=value)


@app.put("/api/state/<key>")
def put_state(key: str):
    init_db()
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict) or "value" not in payload:
        return jsonify(error="Expected JSON body with a value field"), 400
    value_json = json.dumps(payload["value"], ensure_ascii=False)
    with connect() as con:
        con.execute("""
            INSERT INTO app_state(key, value_json, updated_at)
            VALUES (?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(key) DO UPDATE SET
                value_json=excluded.value_json,
                updated_at=CURRENT_TIMESTAMP
        """, (key, value_json))
        con.commit()
    return jsonify(ok=True)


@app.get("/")
def index():
    return send_from_directory(FRONTEND, "index.html")


@app.get("/<path:path>")
def static_files(path: str):
    return send_from_directory(FRONTEND, path)


if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=5000, debug=True)
