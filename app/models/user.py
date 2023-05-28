from sqlalchemy import ForeignKey
from app import db, logger
from app.models import MyBaseClass
from sqlalchemy.schema import Column
from sqlalchemy.sql import func
from sqlalchemy.types import (
    Integer, DateTime, String
)
from sqlalchemy.orm import relationship

from . import execute, select
class Qualifications(db.Model, MyBaseClass):
    id = Column(Integer, primary_key=True)
    qualification = Column(String(200), nullable=False)
    user = relationship("Users", backref='Qualifications', lazy='dynamic')
    
    def __init__(self, id=None, qual=""):
        if id: self.id = id
        self.qualification = qual

    @classmethod
    def get_ids_names(cls):
        return [(q.id, q.qualification) for q in execute(select(cls)).scalars().all()]
    
    
    # def load_from_file(self, filename):
    #     res = list()
    #     try:
    #         with open(filename, 'r', encoding='UTF8') as f:
    #             for line in f:
    #                 for c_data, c in zip(line.split(','), self.__table__.columns):
    #                     new = self.__init__()
    #                     setattr(new, c.name, c_data) 
    #                 res.append(new)
    #         return res
    #     except Exception as e:
    #         logger.error('Fail load from file')
    #         print('Fail load from file', e, sep='\n')
    

   

class Roles(db.Model, MyBaseClass):
    id = Column(Integer, primary_key=True)
    role = Column(String(50), nullable=False)
    user = relationship("Users", backref='Roles', lazy='dynamic')

    def __init__(self, id=None, role=''):
        if id: self.id = id
        self.role = role

    @classmethod 
    def get_ids_roles(cls):
        return [(q.id, q.role) for q in execute(select(cls)).scalars().all()]



class Users(db.Model, MyBaseClass):
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150), nullable=False)
    second_name = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    qualification_id = Column(Integer, ForeignKey('qualifications.id'))
    role_id = Column(Integer, ForeignKey('roles.id'))
    time_created = Column(db.DateTime(timezone=True), server_default=func.now())
    time_updated = Column(db.DateTime(timezone=True), onupdate=func.now())
    
    def __init__(self,
                 id: int=None,
                 first_name:str="-",
                 second_name:str="-", 
                 email:str="-@mail.com", 
                 password:str='nopass', 
                 qualification_id:str='-',
                 time_created=None,
                 time_updated=None):
        if id: self.id = id
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.password = password
        self.qualification_id = qualification_id
        if time_created: self.time_created = time_created
        if time_updated: self.time_updated = time_updated
        
    def __repr__(self) -> str:
        return f"{self.id},{self.first_name},{self.second_name},{self.email},{self.password},{self.qualification_id},{self.time_created},{self.time_updated}"
    
    @classmethod
    def get_by_email(cls, email:str):
        stmt = select(cls).where(cls.email==email)
        return execute(stmt).scalar()
        



