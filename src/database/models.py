from src.database.db import Base, Column, Integer, String
from sqlalchemy import Column, Integer, String


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(30), nullable=False)
    director = Column(String(30), nullable=False)
    actors = Column(String(100), nullable=False)
    genre = Column(String(100), nullable=False)
    rating = Column(Integer, nullable=False)
