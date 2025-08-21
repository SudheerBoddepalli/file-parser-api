# File Parser CRUD API (Full) - Demo Project

Run the server:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Run tests:
```bash
pytest -q
```

Endpoints:
- POST /auth/signup?email=&password=
- POST /auth/login?email=&password=
- POST /files (multipart) - requires Authorization: Bearer <token>
- GET /files/{file_id}/progress
- GET /files/{file_id}
- GET /files
- DELETE /files/{file_id} (requires auth)
- GET /files/{file_id}/events (SSE)
