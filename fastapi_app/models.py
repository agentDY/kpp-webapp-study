from sqlalchemy import Column, Float, String, Integer
# from sqlalchemy.orm import relationship

from .database import Base

# user_score
# nickname : String
# avg_score : Float

class userScore(Base):
  __tablename__ = "user_score"
  list_num = Column(Integer, autoincrement=True, primary_key=True)
  nickname = Column(String, nullable=False, primary_key=False)
  avg_score = Column(Float, nullable=False)



