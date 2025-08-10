from fastapi import APIRouter, Depends
from schemas import ArticleBase, ArticleDisplay
from sqlalchemy.orm import Session
from database import get_db
from db_article import *

router = APIRouter(prefix='/article',tags=['article'])

# Create Article
@router.post('/',response_model = ArticleDisplay)
def create_article_request(request:ArticleBase,db:Session=Depends(get_db)):
    return create_article(db,request)


# Fetch article by id
@router.get('/{id}',response_model = ArticleDisplay)
def get_article_request(id:int,db:Session=Depends(get_db)):
    return get_article(db,id)