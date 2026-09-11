# WORDKEEP — English Vocabulary Memory App

WORDKEEP is a personal English vocabulary memory trainer. It is based on the uploaded HTML prototype and keeps the original visual direction while adding reliable persistence and a Flask + SQLite backend path.

## Stack

- Python + Flask
- SQLite
- HTML5
- CSS3
- JavaScript
- TypeScript-ready frontend structure

## Main features

- Add English words only
- American English / British English preference
- Pronunciation using browser Speech Synthesis
- Speaking practice using browser Speech Recognition where supported
- Star / Favorite words
- Highlight levels
- Daily review
- Spaced-review memory score
- Don't Forget list for repeatedly missed words
- Quiz modes
- Search and filters
- Statistics and learning calendar
- Dark/light theme
- CSV import/export
- JSON backup/restore
- SQLite-backed state when opened through Flask
- Local browser-storage fallback when run as a plain HTML file

## Run locally

### 1. Create environment

Windows:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
```

### 2. Start the server

```bash
python backend/app.py
```

Open:

```text
http://127.0.0.1:5000
```

The first launch creates:

```text
backend/../data/wordkeep.db
```

## Plain HTML mode

You can also open `frontend/index.html` directly. In that mode WORDKEEP automatically falls back to browser localStorage because a browser opened from `file://` cannot use the Flask API.

## Notes about speaking

The Speak button uses the browser's Speech Synthesis API. Speaking Practice uses the browser Speech Recognition API where supported. Browser support and available English voices depend on the device/browser.
# WORDKEEP-English-Vocabulary-Memory-App
