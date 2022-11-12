from datetime import date, datetime, time
from time import time
from typing import List
from pydantic import BaseModel

class Flight(BaseModel):
    id : int
    flightCode : str
    company : str
    source : str
    destination : str
    arrival : int
    departure : int
    ecoCap : int
    busCap : int
    execCap : int
    ecoRes : int
    busRes : int
    execRes : int
    ecoPrice : float
    busPrice: float
    execPrice : float
    class Config:  # If we want to return api response through a schema
        orm_mode = True

class FlightUser(BaseModel):
    flightCode : str
    company : str
    source : str
    destination : str
    arrival : int
    departure : int
    ecoCap : int
    busCap : int
    execCap : int
    ecoRes : int
    busRes : int
    execRes : int
    ecoPrice : float
    busPrice: float
    execPrice : float


    class Config:  # If we want to return api response through a schema
        orm_mode = True

class FlightAdmin(FlightUser):
    manufacturer : str
    hoursFlown : int
    nextMaintainanceSchedule : date

    class Config:  
        orm_mode = True

class FlightsUserList(BaseModel):
    flights : List[FlightUser]

    class Config:  
        orm_mode = True

class FlightsAdminList(BaseModel):
    flights : List[FlightAdmin]
    class Config:  
        orm_mode = True

class Passenger(BaseModel):
    name : str
    age : int

class Ticket(BaseModel):
    flightCode : str
    date : datetime
    numPassenger : int
    passengers : List[Passenger]
    seatType : str
    foodIncluded : bool
    seatRefundable : bool
    paymentMode : str


class Notebase(BaseModel):
    title = str
    desc = str

    class Config:
        orm_mode = True  

class NoteCreate(Notebase):
    pass

class NoteResponse(Notebase):
    id : int

class Tour(BaseModel):
    source : str
    destination : str
    date : datetime