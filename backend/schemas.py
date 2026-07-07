from pydantic import BaseModel

class PlayerCreate(BaseModel):
    username: str

class PlayerResponse(BaseModel):
    id: int
    username: str
    level: int
    xp: int
    hp: int
    coins: int

    class Config:
        from_attributes = True

class QuestCreate(BaseModel):
    title: str
    description: str
    xp_reward: int
    coin_reward: int
    player_id: int  # Assuming quests are associated with players
    is_completed: bool = False  # Default to not completed

class QuestResponse(BaseModel):
    id: int
    title: str
    description: str
    xp_reward: int
    coin_reward: int
    player_id: int  
    is_completed: bool

    class Config:
        from_attributes = True