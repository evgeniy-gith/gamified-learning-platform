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