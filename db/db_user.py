from sqlalchemy.orm.session import Session
from db.schemas import UserBase
from db.models import DbUser
from db.hash import Hash
from fastapi import HTTPException, status

def create_user(db:Session, request:UserBase):
    newUser = DbUser(
        username = request.username,
        email = request.email,
        password =  Hash.bcrypt(request.password)
    )

    db.add(newUser)
    db.commit()
    # Top populate the id column that is done by DB itself
    db.refresh(newUser)
    return newUser

def read_all_users(db: Session):
    return db.query(DbUser).all()

def read_user(db:Session, id:int):
    user = db.query(DbUser).filter(DbUser.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with {id} not found!')
    return user
    
def read_user_by_username(db:Session, username:str):
    user = db.query(DbUser).filter(DbUser.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with {username} not found!')
    return user

def update_user(db:Session,id:int,request:UserBase):
    user = db.query(DbUser).filter(DbUser.id==id)
    user.update({
        DbUser.email: request.email,
        DbUser.password: request.password,
        DbUser.username:request.username
    })

    db.commit()
    return f"User ID : {id} record updated , Successfully!"


def delete_user(db:Session,id:int):
    user = db.query(DbUser).filter(DbUser.id==id).first()
    db.delete(user)
    db.commit()
    return f"User ID: {id} , deleted successfully!"