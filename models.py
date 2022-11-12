from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import database as db

class FlightModel(db.Base):
    __tablename__ = 'flight'
    id = Column(Integer , primary_key = True,index=True)
    flightCode = Column(String)
    company = Column(String)
    source = Column(String)
    destination = Column(String)
    arrival = Column(String)
    departure = Column(String)
    duration = Column(String)
    ecoCap = Column(Integer)
    busCap = Column(Integer)
    execCap = Column(Integer)
    ecoPrice = Column(Float)
    busPrice= Column(Float)
    execPrice = Column(Float)
    schedules = relationship("FlightSchedule" , back_populates = "flightDetails")
    journeys = relationship("Journey" , back_populates = "flightDetails")

class UserModel(db.Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key = True,index=True)
    username = Column(String)
    password = Column(String)
    journeys = relationship("Journey" , back_populates = "userDetails")


class Journey(db.Base):
    __tablename__ = "journeys"
    id = Column(Integer , primary_key = True , index = True)
    pnr = Column(String)
    metaData = Column(String)
    amountPayed = Column(Integer)
    ## foreign key for flightID
    userId = Column(Integer , ForeignKey("users.id"))
    userDetails = relationship("UserModel" , back_populates = "journeys")
    flightId = Column(Integer , ForeignKey("flight.id"))
    flightDetails = relationship("FlightModel" , back_populates = "journeys")
    scheduleId = Column(Integer , ForeignKey("flightSchedules.id"))
    scheduleDetails = relationship("FlightSchedule" , back_populates = "journeys")



class FlightSchedule(db.Base):
    __tablename__ = "flightSchedules"
    id = Column(Integer , primary_key = True , index = True)
    date = Column(String)
    ecoRem = Column(Integer)
    busRem = Column(Integer)
    execRem = Column(Integer)
    source = Column(String)
    destination = Column(String)
    flightId = Column(Integer , ForeignKey("flight.id"))
    flightDetails = relationship("FlightModel" , back_populates = "schedules")
    journeys = relationship("Journey" , back_populates = "scheduleDetails")
 