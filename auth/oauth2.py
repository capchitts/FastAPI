from fastapi.security import OAuth2PasswordBearer
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from db.database import get_db
from typing import Optional
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException, status
from db import db_user
 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
 
SECRET_KEY = 'b1f78459a3de1f9078b42e93fd27ab6c6349e4fd12f1cd7b980c3e9a582fb7ce'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
 
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.now(datetime.timezone.utc) + expires_delta
  else:
    expire = datetime.now(datetime.timezone.utc) + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt

def get_curr_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
  credential_exception=HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail='Could not validate credentials',
    header={'www-Authenticate':'Bearer'}
  )
  try:
    payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    username:str = payload.get('sub')
    if username is None:
      raise credential_exception
  except JWTError:
    raise credential_exception
  
  user = db_user.read_user_by_username(db,username)
  if user is None:
    raise credential_exception
  
  return user



