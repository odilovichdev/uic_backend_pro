from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    description: str|None = None
    price: int
    is_active: bool


class ProductInfo(ProductCreate):
    id: int

    class Config:
        orm_mode = True