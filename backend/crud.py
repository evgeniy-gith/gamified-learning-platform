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

def get_quest(db: Session, quest_id: int):
    return db.query(models.Quest).filter(models.Quest.id == quest_id).first()

def create_quest(db: Session, quest: schemas.QuestCreate):
    db_quest = models.Quest(
        title=quest.title,
        description=quest.description,
        xp_reward=quest.xp_reward,
        coin_reward=quest.coin_reward,
        player_id=quest.player_id,
        is_completed=quest.is_completed
    )
    db.add(db_quest)
    db.commit()
    db.refresh(db_quest)
    return db_quest
