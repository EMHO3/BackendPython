from fastapi import FastAPI
from routers import products,users
from fastapi.staticfiles import StaticFiles 

 #siempre hacer un cd a FastApi para que funcione todo
app=FastAPI()

#routers
app.include_router(products.router)
app.include_router(users.router)
app.mount("/static",StaticFiles(directory="static"),name="static")


@app.get("/")
async def root():
    return "!hola fastapi"

@app.get("/url")
async def url():
    return {"url_curso":"https://mouredev.com/python"}


