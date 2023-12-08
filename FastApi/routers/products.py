from fastapi import APIRouter

#inicie el server con: python -m uvicorn products:app --reload
router= APIRouter(prefix="/products")

products_list=["producto 1","producto 2","producto 3","producto 4"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id:int):
    return products_list[id]