from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from db.database import engine
from db.router import user,article, product
import db.models
from db.exceptions import StoryException
from auth import authentication

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(authentication.router)
app.include_router(product.router)


@app.get('/')
def index():
    return "Hello world!"

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(status_code=418,content={'detail':exc})

@app.exception_handler(HTTPException)
def story_exception_handler(request: Request, exc: HTTPException):
    return PlainTextResponse(str(exc),status_code=400)

db.models.Base.metadata.create_all(engine)