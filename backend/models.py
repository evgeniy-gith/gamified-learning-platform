from sqlalchemy import Column, Integer, String
from database import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    
    level = Column(Integer, default=1)
    xp = Column(Integer, default=0)
    hp = Column(Integer, default=100)
    coins = Column(Integer, default=0)