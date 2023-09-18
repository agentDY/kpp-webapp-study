from pydantic import BaseModel
from typing import Optional

class UserScoreBase(BaseModel):
    list_num: Optional[int]
    nickname: str
    avg_score: float