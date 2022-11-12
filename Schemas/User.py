from datetime import date, datetime, time
from time import time
from typing import List
from pydantic import BaseModel
from . import Journey

class UserBase(BaseModel):
    username : str
    password : str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id : int
    journeys: list[Journey.Journey] = []
    

    class Config():
        orm_mode = True

