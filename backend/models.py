from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from database import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    
    level = Column(Integer, default=1)
    xp = Column(Integer, default=0)
    hp = Column(Integer, default=100)
    coins = Column(Integer, default=0)

class Quest(Base):
    __tablename__ = "quests"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    
    description = Column(String)
    xp_reward = Column(Integer)
    coin_reward = Column(Integer)
    player_id = Column(Integer, ForeignKey("players.id"))
    is_completed = Column(Boolean, default=False)