from fastapi import APIRouter, Depends
from db.schemas import ArticleBase, ArticleDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db.db_article import *
from auth.oauth2 import oauth2_scheme

router = APIRouter(prefix='/article',tags=['article'])

# Create Article
@router.post('/',response_model = ArticleDisplay)
def create_article_request(request:ArticleBase,db:Session=Depends(get_db)):
    return create_article(db,request)


# Fetch article by id
@router.get('/{id}',response_model = ArticleDisplay)
def get_article_request(id:int,db:Session=Depends(get_db),token:str=Depends(oauth2_scheme)):
    return get_article(db,id)