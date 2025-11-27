# Backend - Notes API

Flask + SQLAlchemy service exposing CRUD endpoints for notes with OpenAPI docs.

- Health: GET /health
- Notes:
  - GET /api/notes
  - POST /api/notes
  - GET /api/notes/<id>
  - PUT /api/notes/<id>
  - DELETE /api/notes/<id>

Run locally:
- Install deps: pip install -r requirements.txt
- Start: python run.py (listens on :3001)
- Docs: /docs

CORS enabled for http://localhost:3000.
