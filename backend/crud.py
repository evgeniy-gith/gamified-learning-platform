from sqlalchemy.orm import Session
import schemas
import models

def get_player(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.id == player_id).first()

def get_player_by_username(db: Session, username: str):
    return db.query(models.Player).filter(models.Player.username == username).first()

def create_player(db: Session, player: schemas.PlayerCreate):
    db_player = models.Player(username=player.username)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player
