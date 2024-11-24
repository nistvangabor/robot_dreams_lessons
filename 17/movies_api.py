from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from models import Movie, MovieRequest, MovieResponse
from database import Base, engine, get_db
from typing import List

app = FastAPI()
# uvicorn movies_api:app --reload
# taskkill /PID 23464 /F
# netstat -ano | findstr :8000

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all) 


@app.get("/movies/", response_model=List[MovieResponse])
async def get_movies(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Movie)) # SELECT * FROM movies
    movies = result.scalars().all() #scalars() unpacks the values from list of list/tuple of tuple format and keeps only the Movie objects
    return movies

@app.post("/movies/", response_model=MovieResponse)
async def add_movie(movie: MovieRequest, db: AsyncSession = Depends(get_db)):
    new_movie = Movie(**movie.dict()) #this convert the pydantic model into a dictionary with .dict() and a list of keyword arguments with **
    """          INSTEAD OF THIS WE ARE DOING **movie.dict()
    new_movie = Movie(
    title=movie.title,
    genre=movie.genre,
    year=movie.year,
    length_in_mins=movie.length_in_mins,
    rating=movie.rating
)"""
   
    db.add(new_movie)
    await db.commit()
    await db.refresh(new_movie) #reload the attributes from the db, so the id will be present.
    return new_movie

@app.get("/movies/{movie_id}", response_model=MovieResponse)
async def get_movie(movie_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Movie).where(Movie.id == str(movie_id)))
    movie = result.scalar_one_or_none() #return a single record or none, if multiple rows returned raises MultipleResultsFound
    if not movie:
        raise HTTPException(status_code=404, detail=f"Movie with id {movie_id} not found")
    return movie

@app.put("/movies/{movie_id}", response_model=MovieResponse)
async def update_movie(movie_id: UUID, movie_update: MovieRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Movie).where(Movie.id == str(movie_id)))
    movie = result.scalar_one_or_none()
    if not movie: #guard clause
        raise HTTPException(status_code=404, detail=f"Movie with id {movie_id} not found")
    
    for key, value in movie_update.dict(exclude_unset=True).items(): #exclude_unset kizárja azokat a field-eket amiket a pydantic model nem tartalmaz mint update, pl ami default value-val rendelkezik és úgy is maradt.
        setattr(movie, key, value) # pl: key: title value: "New title" -> movie.title = "Armageddon 2"

    db.add(movie)
    await db.commit() #ugyanaz mint az insert, automatikusan tudja
    await db.refresh(movie)
    return movie

@app.delete("/movies/{movie_id}", response_model=MovieResponse)
async def delete_movie(movie_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Movie).where(Movie.id == str(movie_id)))
    movie = result.scalar_one_or_none()
    if not movie: #guard clause
        raise HTTPException(status_code=404, detail=f"Movie with id {movie_id} not found")
    
    await db.delete(movie)
    await db.commit()
    return movie