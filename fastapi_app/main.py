from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from .routers import rank, speech
from .views import home, ranking
from . import models
from .database import engine

tags_metadata = [
    {
        "name": "Rank",
        "description": "발음 랭킹 관련 API",
    },
    {
        "name": "Speech",
        "description": "음성처리 관련 API",
    },
    {
        "name": "Web Pages",
        "description": "웹 페이지 (API 아님)",
    }
]

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI(openapi_tags=tags_metadata, title="api", version="0.0.1", )

routers = [home, ranking, rank, speech]
for r in routers:
    app.include_router(r.router)

app.mount("/static", StaticFiles(directory="static"), name="static")