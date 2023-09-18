from sqlalchemy.orm import Session
from . import models
from .schemas import UserScoreBase

def get_user_score(db: Session, response_model: UserScoreBase):
    userlist = db.query(models.userScore).order_by(models.userScore.avg_score.desc()).all()

    return userlist


