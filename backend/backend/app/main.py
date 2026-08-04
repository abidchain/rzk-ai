from fastapi import FastAPI

app = FastAPI(
    title="RZK AI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to RZK AI",
        "status": "online"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
