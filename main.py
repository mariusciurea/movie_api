from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database.db import SessionLocal, Base, engine
from src.database.models import Movie
from src.schemas import MovieInput
from pydantic import BaseModel

app = FastAPI()


def init_db():
    Base.metadata.create_all(bind=engine)


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def startup():
    init_db()


# class MovieInput(BaseModel):
#     id: int
#     title: str
#     director: str
#     actors: str
#     genre: str


@app.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    return db.query(Movie).all()


@app.get("/movies/{movie_id}")
def get_movie_by_id(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@app.post("/movies")
def add_movie(movie: MovieInput, db: Session = Depends(get_db)):
    if db.query(Movie).filter(Movie.id == movie.id).first():
        raise HTTPException(status_code=400, detail="Movie with this ID already exists.")
    new_movie = Movie(**movie.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return {"message": "Movie added successfully", "movie": new_movie}


@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    db.delete(movie)
    db.commit()
    return {"message": "Movie deleted successfully"}