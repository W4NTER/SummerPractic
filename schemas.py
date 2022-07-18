from typing import Union
from datetime import datetime
from pydantic import BaseModel


class PanamaBase(BaseModel):
    url: str
    year: int
    price: int
    mileage: int


class PanamaCreate(PanamaBase):
    pass


class Panama(PanamaBase):
    id: int
    datetime: datetime

    class Config:
        orm_mode = True