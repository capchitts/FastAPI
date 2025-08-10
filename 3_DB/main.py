from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from database import engine
from router import user,article
import models
from exceptions import StoryException

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)

@app.get('/')
def index():
    return "Hello world!"

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(status_code=418,content={'detail':exc})

@app.exception_handler(HTTPException)
def story_exception_handler(request: Request, exc: HTTPException):
    return PlainTextResponse(str(exc),status_code=400)

models.Base.metadata.create_all(engine)