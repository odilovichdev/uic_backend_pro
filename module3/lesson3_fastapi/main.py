from fastapi import FastAPI, Depends, APIRouter

from models import User
from schemas import UserCreate
from routers import router as prodcut_router
from routers import router as order_router
from db import db_dependency


app = FastAPI()


router = APIRouter()


@router.get('/')
async def root(db: db_dependency):
    return {"message": "Hello world"}


@router.get("/users")
async def users_list(db: db_dependency):
    return db.query(User).all()


@router.post("/user/create")
async def user_create(user: UserCreate, db: db_dependency):
    new_user = User(name=user.name, email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"user": new_user}

app.include_router(router)
app.include_router(prodcut_router)
app.include_router(order_router)

