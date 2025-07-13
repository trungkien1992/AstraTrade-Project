from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="AstraTrade Backend API", version="0.2.0")

# --- Models ---
class User(BaseModel):
    id: int
    username: str
    password: str  # In production, use hashed passwords!
    xp: int = 0
    level: int = 1

class UserRegisterRequest(BaseModel):
    username: str
    password: str

class UserLoginRequest(BaseModel):
    username: str
    password: str

class UserLoginResponse(BaseModel):
    user_id: int
    username: str
    token: str  # Placeholder for JWT/session

class TradeRequest(BaseModel):
    user_id: int
    asset: str
    direction: str  # 'long' or 'short'
    amount: float

class TradeResult(BaseModel):
    outcome: str  # 'profit', 'loss', 'breakeven'
    profit_percentage: float
    message: str
    xp_gained: int

class LeaderboardEntry(BaseModel):
    user_id: int
    username: str
    xp: int
    level: int

# --- In-memory storage (for demo) ---
users = [User(id=1, username="demo", password="demo", xp=100, level=2)]
leaderboard = [LeaderboardEntry(user_id=1, username="demo", xp=100, level=2)]
user_id_counter = 2

# --- Endpoints ---
@app.post("/register", summary="Register a new user", response_model=User)
def register_user(req: UserRegisterRequest):
    global user_id_counter
    if any(u.username == req.username for u in users):
        raise HTTPException(status_code=400, detail="Username already exists")
    user = User(id=user_id_counter, username=req.username, password=req.password)
    users.append(user)
    leaderboard.append(LeaderboardEntry(user_id=user_id_counter, username=req.username, xp=0, level=1))
    user_id_counter += 1
    return user

@app.post("/login", summary="Login a user", response_model=UserLoginResponse)
def login_user(req: UserLoginRequest):
    for user in users:
        if user.username == req.username and user.password == req.password:
            # In production, return a JWT or session token
            return UserLoginResponse(user_id=user.id, username=user.username, token="fake-token")
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/users", summary="List all users", response_model=List[User])
def get_users():
    return users

@app.post("/trade", summary="Place a trade", response_model=TradeResult)
def place_trade(trade: TradeRequest):
    # Placeholder: always return profit
    # In production, validate user, check balance, etc.
    for user in users:
        if user.id == trade.user_id:
            user.xp += 15
            user.level = 1 + user.xp // 100
            # Update leaderboard
            for entry in leaderboard:
                if entry.user_id == user.id:
                    entry.xp = user.xp
                    entry.level = user.level
            return TradeResult(
                outcome="profit",
                profit_percentage=7.5,
                message="Stellar Alignment Achieved!",
                xp_gained=15
            )
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/leaderboard", summary="Get leaderboard", response_model=List[LeaderboardEntry])
def get_leaderboard():
    # Return sorted leaderboard
    return sorted(leaderboard, key=lambda e: e.xp, reverse=True)

@app.post("/xp/add", summary="Add XP to a user")
def add_xp(user_id: int, amount: int):
    for user in users:
        if user.id == user_id:
            user.xp += amount
            user.level = 1 + user.xp // 100
            # Update leaderboard
            for entry in leaderboard:
                if entry.user_id == user.id:
                    entry.xp = user.xp
                    entry.level = user.level
            return {"status": "ok", "new_xp": user.xp}
    raise HTTPException(status_code=404, detail="User not found") 