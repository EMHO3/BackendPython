from fastapi import APIRouter,HTTPException
from pydantic import BaseModel

router=APIRouter()

#inicie el server con: python -m uvicorn users:app --reload

#entidad users

class User(BaseModel):
    id:int
    name:str
    surname:str
    url:str
    age:int


users_list=[User(id=1,name="Emir",   surname="huaroc",url="https://moure.dev",age=20),
            User(id=2,name="brenda", surname="cavre",url="https://bren.dev",age=19),
            User(id=3,name="majinbu",surname="kidbu",url="https://kidbuu.com",age=123)]   


@router.get("/usersjson")
async def usersjson():
    return [{"name":"Emir","surname":"huaroc","url":"https://moure.dev","age":20},
            {"name":"brenda","surname":"cavre","url":"https://bren.dev","age":19} , 
            {"name":"majinbu","surname":"kidbu","url":"https://kidbuu.com","age":123}]


@router.get("/users")
async def users():
    return users_list

#path
@router.get("/user/{id}")
async def user(id:int):
    return search_user(id)

 #query   
@router.get("/user")
async def user(id:int):
   return search_user(id)
    
def search_user(id:int):    
    users= filter(lambda user: user.id == id,users_list)
    try:
      return list(users)[0]
    except:
        return{"Error":"no se ah encontrado el usuario"}
    

@router.post("/user/",response_model=User, status_code=201)
async def user(user:User):
    if type(search_user(user.id)) ==User:
           raise HTTPException(status_code=404,detail="el usuario ya existe")
    users_list.append(user)
    return user

@router.put("/user/")
async def user(user:User):
    found=False
    for index,saved_user in enumerate(users_list):
        if saved_user.id==user.id:
            users_list[index]=user
            found=True

    if not found:
        return{"Error":"no se actualizo el usuario"}   
    return user


@router.delete("/user/{id}")
async def user(id:int):
    found=False
    for index,saved_user in enumerate(users_list):
        if saved_user.id==id:
           del users_list[index]
           found=True

    if not found:
       return{"Error":"no se ah eliminado el usuario"}   

