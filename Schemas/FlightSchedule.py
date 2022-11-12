from datetime import date, datetime, time
import sre_compile
from time import time
from typing import List
from pydantic import BaseModel
from . import Journey

class FlightScheduleBase(BaseModel):
    date : str
    ecoRem : int
    busRem : int
    execRem : int
    source : str
    destination : str

class FlightScheduleCreate(FlightScheduleBase):
    pass

class FlightSchedule(FlightScheduleBase):
    id : int
    flightId : int
    journeys: list[Journey.Journey] = []
    class Config():
        orm_mode = True

