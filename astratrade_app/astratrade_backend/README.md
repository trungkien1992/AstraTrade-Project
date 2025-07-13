# AstraTrade Backend

This is the dedicated backend service for the AstraTrade app, handling trading logic, user management, XP, and leaderboard features. It is decoupled from the knowledge_base (RAG/AI) system for better performance and maintainability.

## Features
- User management
- Trading endpoints
- XP and gamification
- Leaderboard

## Tech Stack
- Python 3.9+
- FastAPI
- Uvicorn
- Pydantic

## Running Locally

1. Create and activate the virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install fastapi uvicorn[standard] pydantic
   ```

2. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

3. The API will be available at http://localhost:8001 (default FastAPI port is 8000, you can change with --port 8001)

## API Endpoints

- `GET /users` — List all users
- `POST /trade` — Place a trade (returns outcome, XP, etc.)
- `GET /leaderboard` — Get leaderboard
- `POST /xp/add` — Add XP to a user

## Next Steps
- Add persistent storage (database)
- Implement authentication
- Expand trading/game logic
- Integrate with the Flutter app 