from fastapi import FastAPI,Depends,HTTPException,status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext

ALGORITHM="HS256"

app=FastAPI

oauth2=OAuth2PasswordBearer(tokenUrl="login")

crypt=CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username:str
    full_name:str
    email:str
    disabled:bool

class UserDB(User):
    password:str    

users_db={
    "mouredev":{
        "username":"mouredev",
        "full_name":"brais moured",
        "email":"braismour@moure.com",
        "disabled":False,
        "password":"$2a$12$zqTGnWamWbE9QedArlp.WuKRxw9R15Ogyh1Y/HajR6vYLPsl76qpq"
    },
     "mouredev2":{
        "username":"mouredev2",
        "full_name":"brais moured2",
        "email":"braismour2@moure.com",
        "disabled":True,
        "password":"654321"
    }
} 

def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username])


@app.post("/login")    
async def login(form:OAuth2PasswordRequestForm=Depends()):
    user_db=users_db.get (form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,detail="el usuario no es correcto")
    
    user=search_user_db(form.username)
    if not form.password==user.password:
         raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,detail="la contraseña no es correcta")
    
    return{"acces_token":user.username,"token_type":"bearer"}