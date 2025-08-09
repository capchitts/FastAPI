from fastapi import APIRouter, Depends
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from database import get_db
from typing import List
from db_user import *

router = APIRouter(prefix='/user',tags=['user'])


## Create
@router.post('/', response_model = UserDisplay)
def create_new_user(request: UserBase, db:Session= Depends(get_db)):
    return create_user(db,request)

## Read All
@router.get('/',response_model=List[UserDisplay])
def get_all_users_request(db:Session = Depends(get_db)):
    return read_all_users(db)

## Read One user
@router.get('/{id}',response_model=UserDisplay)
def get_user_request(id:int, db:Session = Depends(get_db)):
    return read_user(db,id)


## Update
@router.post('/{id}/update')
def update_user_request(id:int,request:UserBase,db:Session=Depends(get_db)):
    return update_user(db,id,request)


## Delete
@router.post('/{id}/delete')
def delete_user_request(id:int,db:Session=Depends(get_db)):
    try:
        return delete_user(db,id)
    except:
        return "No such User exists!"
        
        