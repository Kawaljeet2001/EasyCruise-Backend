from datetime import date, datetime, time
from time import time
from typing import List
from pydantic import BaseModel


class JourneyBase(BaseModel):
    pnr : str
    metaData : str
    amountPayed : int


class JourneyCreate(JourneyBase):
    pass

class Journey(JourneyBase):
    id : int
    flightId : int
    scheduleId : int
    userId : int
    class Config():
        orm_mode = True

