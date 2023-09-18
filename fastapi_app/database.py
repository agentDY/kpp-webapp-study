from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

# DB 연결하는 부분
# SQLALCHEMY_DATABASE_URL = "mysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(C.DB_USERNAME, C.DB_PASSWORD, C.DB_HOST,
#                                                                           C.DB_PORT,
#                                                                           C.DB_DATABASE)

# mysql 연결 url 설정
SQLALCHEMY_DATABASE_URL = "mysql://{}:{}@{}:{}/{}?charset=utf8mb4".format("root", "1234","127.0.0.1",3306,"read_db")

# 엔진생성
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 세션생성
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base 객체생성
Base = declarative_base()

def get_db() -> Session:
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()