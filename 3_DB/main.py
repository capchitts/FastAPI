from fastapi import FastAPI
from database import engine
from router import user,article
import models

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)

@app.get('/')
def index():
    return "Hello world!"


models.Base.metadata.create_all(engine)