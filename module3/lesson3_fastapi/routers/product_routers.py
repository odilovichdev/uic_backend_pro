from fastapi import FastAPI, Depends, APIRouter

from models import Product
from db import db_dependency
from schemas import ProductInfo


router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/list")
async def products(db: db_dependency):
    products = db.query(Product).all()

    items = []
    for product in products:
        items.append(ProductInfo(
            id=product.id,
            name=product.name,
            price=product.price
        ))
    
    return items