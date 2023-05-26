from app import db, logger
from app.models import MyBaseClass
from sqlalchemy.schema import Column
from sqlalchemy.sql import func
from sqlalchemy.types import (
    Integer, DateTime, String
)

# TODO:
# [ ]: Добавить роли 
class Users(db.Model, MyBaseClass):
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150), nullable=False)
    second_name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    password = Column(String(200), nullable=False)
    qualification = Column(String(200), nullable=False)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    
    def __init__(self,
                 id: int=None,
                 first_name:str="-",
                 second_name:str="-", 
                 email:str="-@mail.com", 
                 password:str='nopass', 
                 qualification:str='-',
                 time_created=None,
                 time_updated=None):
        if id: self.id = id
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.password = password
        self.qualification = qualification
        if time_created: self.time_created = time_created
        if time_updated: self.time_updated = time_updated
        
    def __repr__(self) -> str:
        return f"{self.id},{self.first_name},{self.second_name},{self.email},{self.password},{self.qualification},{self.time_created},{self.time_updated}"



