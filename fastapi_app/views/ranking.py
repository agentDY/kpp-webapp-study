from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ..schemas import UserScoreBase
from sqlalchemy.orm import Session
from .. import crud
from ..database import get_db

router = APIRouter(
    tags=["Web Pages"],
    responses={404: {"description": "Not found"}},
)

templates = Jinja2Templates(directory="templates")

@router.get("/ranking", response_class=HTMLResponse)
async def ranking_page(request: Request, db: Session = Depends(get_db)):
    userlist = crud.get_user_score(db, UserScoreBase)
    print("userlist : ", userlist)
    return templates.TemplateResponse(
        "ranking.html",
        {
            "request": request,
            "test_text": "hello ranking page",
            "users": userlist
        })