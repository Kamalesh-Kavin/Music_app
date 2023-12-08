from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

Base  = declarative_base()
class User(Base):
    __tablename__ = 'music_users'
    user_id  =  Column(String, primary_key=True, default=str(uuid.uuid4()))
    uname = Column(String)
    pwd = Column(String)

class Playlists(Base):
    __tablename__ = 'playlists'
    playlist_id  =  Column(String, primary_key=True, default=str(uuid.uuid4()))
    playlist_name = Column(String)
    user_id = Column(String, ForeignKey("music_users.user_id"))

class Playlists_songs(Base):
    __tablename__ = 'playlists_songs'
    playlist_id  =  Column(String,primary_key=True)
    song_id = Column(String, ForeignKey("songs.song_id"))
    song_order = Column(Integer)

class Songs(Base):
    __tablename__ = 'songs'
    song_id  =  Column(String, primary_key=True, default=str(uuid.uuid4()))
    song_title = Column(String)
    song_duration = Column(Integer)
    genre = Column(String)
    artist_id = Column(String, ForeignKey("artists.artist_id"))
    album_id = Column(String, ForeignKey("albums.album_id"))
    
class Artists(Base):
    __tablename__ = 'artists'
    artist_id  =  Column(String, primary_key=True, default=str(uuid.uuid4()))
    artist_name = Column(String)
    
class Albums(Base):
    __tablename__ = 'albums'
    album_id  =  Column(String, primary_key=True, default=str(uuid.uuid4()))
    album_title = Column(String)
   
class User_individual_song(Base):
    __tablename__ = 'user_individual_song' 
    user_id = Column(String, ForeignKey("music_users.user_id"),primary_key=True)
    song_id = Column(String, ForeignKey("songs.song_id"))
    song_play_count = Column(Integer)
    
class Song_similarity(Base):
    __tablename__ = 'song_similarity' 
    song_id = Column(String, ForeignKey("songs.song_id"),primary_key=True)
    user_id = Column(String, ForeignKey("music_users.user_id"))
    similarity_score = Column(Float)
    