from fastapi import FastAPI
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Solo Leveling Tracker API")

@app.get("/")
def read_root():
    return {"message": "System Awakening: Started!"}