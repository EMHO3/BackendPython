from fastapi import FastAPI
from routers import products,users,basic_auth_users,jwt_auth_users,users_db
from fastapi.staticfiles import StaticFiles 
#inicie el server con: python -m uvicorn main:app --reload
 #siempre hacer un cd a FastApi para que funcione todo
app=FastAPI()

#routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(users_db.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)

app.mount("/static",StaticFiles(directory="static"),name="static")


@app.get("/")
async def root():
    return "!hola fastapi"

@app.get("/url")
async def url():
    return {"url_curso":"https://mouredev.com/python"}


