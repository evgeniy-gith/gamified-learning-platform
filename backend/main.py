from fastapi import FastAPI

app = FastAPI(title="Solo Leveling Tracker API")

@app.get("/")
def read_root():
    return {"message": "System Awakening: Started!"}