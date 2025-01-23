from pydantic import BaseModel
from typing import Optional


class MovieInput(BaseModel):
    id: int
    title: str
    director: str
    actors: str
    genre: str
    rating: Optional[float] | None = None
