from pydantic import BaseModel


class OrderCreate(BaseModel):
    user_id: int
    created_at: str


class OrderInfo(OrderCreate):
    id: int

    class Config:
        orm_mode = True
