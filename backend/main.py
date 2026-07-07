from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models
import crud
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Solo Leveling Tracker API")

@app.get("/")
def read_root():
    return {"message": "System Awakening: Started!"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/players/", response_model=schemas.PlayerResponse)
def register_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    db_player = crud.get_player_by_username(db, username=player.username)
    if db_player:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_player(db=db, player=player)

@app.get("/players/{player_id}", response_model=schemas.PlayerResponse)
def read_player(player_id: int, db: Session = Depends(get_db)):
    db_player = crud.get_player(db, player_id=player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player

@app.post("/quests/", response_model=schemas.QuestResponse)
def create_quest(quest: schemas.QuestCreate, db: Session = Depends(get_db)):
    return crud.create_quest(db=db, quest=quest)

@app.get("/quests/{quest_id}", response_model=schemas.QuestResponse)
def read_quest(quest_id: int, db: Session = Depends(get_db)):
    db_quest = crud.get_quest(db, quest_id=quest_id)
    if db_quest is None:
        raise HTTPException(status_code=404, detail="Quest not found")
    return db_quest