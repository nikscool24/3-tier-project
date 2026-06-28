from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import os
import redis
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

# Environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# Connect to Redis
r = redis.Redis.from_url(REDIS_URL)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Simple user model
class User(BaseModel):
    name: str
    phone: str


@app.get("/")
def home():
    return {"message": "Hello World"}


@app.post("/adduser")
def add_user(user: User):
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT, phone TEXT);")
    cur.execute("INSERT INTO users (name, phone) VALUES (%s, %s) RETURNING id;", (user.name, user.phone))
    user_id = cur.fetchone()[0]
    conn.commit()
    conn.close()

    # Cache the new user in Redis
    r.set(f"user:{user_id}", f"{user.name}|{user.phone}")

    return {"id": user_id, "name": user.name, "phone": user.phone}

@app.get("/getuser/{user_id}")
def get_user(user_id: int):
    # Check Redis cache first
    cached = r.get(f"user:{user_id}")
    if cached:
        name, phone = cached.decode("utf-8").split("|")
        return {"id": user_id, "name": name, "phone": phone}

    # Fallback to Postgres if not cached
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("SELECT name, phone FROM users WHERE id = %s;", (user_id,))
    result = cur.fetchone()
    conn.close()

    if result:
        # Save to Redis for future requests
        r.set(f"user:{user_id}", f"{result[0]}|{result[1]}")
        return {"id": user_id, "name": result[0], "phone": result[1]}
    else:
        return {"error": "User not found"}


# Keeps FastAPI running
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
