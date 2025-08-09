from fastapi import FastAPI, status, Response

app = FastAPI()

@app.get('/')
def index():
    return "Hello world!"


@app.get('/blog/{id}',status_code=status.HTTP_200_OK)
def index(id: int,response:Response):
    if id > 5:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'error':f"Blog : {id} not found!"}
    else:
        response.status_code=status.HTTP_200_OK
        return "Hello world!"