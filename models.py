from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base  = declarative_base()

class User(Base):
    __tablename__ = 'music_users'
    id  = Column(Integer, primary_key=True, index=True)
    uname = Column(String)
    pwd = Column(String)

