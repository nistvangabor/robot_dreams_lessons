from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped #type hintingre használjuk, azt mondja meg hogy a típus egy ORM, és köti a típust az ORM adatbázis mappingjéhez
from uuid import uuid1
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from database import Base #Base class for ORM models, minden ettől örököl, Python class-okat tudunk táblákkal megfeleltetni.
#DATABASE MODEL:

class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[str] = Column(String, primary_key=True, default=lambda: str(uuid1()))
    title: Mapped[str] = Column(String, nullable=False)
    genre: Mapped[str] = Column(String, nullable=False)
    year: Mapped[int] = Column(Integer, nullable=False)
    length_in_mins: Mapped[int] = Column(Integer, nullable=False)
    rating: Mapped[int] = Column(Integer, nullable=False)


# PYDANTIC MODEL:

class MovieRequest(BaseModel):
    title: str
    genre: str
    year: int
    length_in_mins: int
    rating: Optional[int] = 0

class MovieResponse(MovieRequest):
    id: UUID