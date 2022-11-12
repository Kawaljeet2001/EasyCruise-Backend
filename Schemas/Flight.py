from datetime import date, datetime, time
from time import time
from typing import List
from pydantic import BaseModel
from . import FlightSchedule , Journey
class FlightBase(BaseModel):
    flightCode : str
    company : str | None = None
    source : str
    destination : str
    arrival : str | None = None
    duration : str | None = None
    departure : str | None = None
    ecoCap : int | None = None
    busCap : int | None = None
    execCap : int | None = None
    ecoPrice : float | None = None
    busPrice: float | None = None
    execPrice : float | None = None

class FlightCreate(FlightBase):
    pass

class Flight(FlightBase):
    id : int
    schedules: list[FlightSchedule.FlightSchedule] = []
    journeys: list[Journey.Journey] = []

    class Config():
        orm_mode = True