from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    user_id: str
    pwd: str
    class Config:
        orm_mode = True

class Playlists(BaseModel):
    playlist_id: str
    playlist_name: str
    user_id: str
    class Config:
        orm_mode = True
        
class Playlists_songs(BaseModel):
    playlist_id: str
    song_id: str
    song_order: int
    class Config:
        orm_mode = True
        
class Songs(BaseModel):
    song_id: str
    song_title: str
    song_duration: int
    genre: str
    artist_id: str
    album_id: str
    class Config:
        orm_mode = True
        
class Artists(BaseModel):
    artist_id: str
    artist_name: str
    class Config:
        orm_mode = True
        
        
class Albums(BaseModel):
    artist_id: str
    artist_name: str
    class Config:
        orm_mode = True
        
class User_individual_song(BaseModel):
    user_id: str
    song_id: str
    song_play_count: int
    class Config:
        orm_mode = True
        
class Song_similarity(BaseModel):
    user_id: str
    song_id: str
    similarity_score: float
    class Config:
        orm_mode = True