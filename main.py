from fastapi import FastAPI
from core.config import settings
from db.session import engine 
from db.session import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String,Text
from fastapi import Depends
from faker import Faker
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
import os

'''
# from schema import User
# from schema import Playlists
# from schema import Playlists_songs
# from schema import Songs
# from schema import Artists
# from schema import Albums
# from schema import User_individual_song
# from schema import Song_similarity
     
# from models import Model_User
# from models import Model_Playlists
# from models import Model_Playlists_songs
# from models import Model_Songs
# from models import Model_Artists
# from models import Model_Albums
# from models import Model_User_individual_song
# from models import Model_Song_similarity   
'''

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
fake = Faker()

class UserCreate(BaseModel):
    user_id: int
    name: str
    password: str

def create_user(db, user: UserCreate):
    hashed_password = user.password  
    insert_command = user.insert().values(
        user_id=user.user_id,
        name=user.name,
        password=hashed_password
    )
    db.execute(insert_command)
    db.commit()
    return {"message":"register success"}

@app.post("/populate-data")
async def populate_data(db: Session = Depends(get_db)):
    num_records = 1000 
    sql=text("INSERT INTO Users(user_id, name, password) VALUES(:id, :username, :password)")
    records = [
        {
            'id': i,
            'username': fake.user_name(),
            'password': fake.password()
        }
        for i in range(5, num_records + 1)
    ]
    for record in records:
        db.execute(sql, record)

    db.commit()
    return {"message": f"{num_records} records populated successfully"}


@app.post("/register")
def register(user: UserCreate, db: Session = Depends(SessionLocal)):
    existing_user = db.query(User).filter(User.user_id == user.user_id).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User ID already exists")
    return create_user(db, user)

@app.get("/")
def home():
    return {"msg":"Hello FastAPI🚀"}

