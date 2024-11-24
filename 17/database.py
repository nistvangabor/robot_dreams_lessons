#pip install fastapi sqlalchemy pydantic aiosqlite uvicorn
#pip freeze > requirements.txt

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine #nem fogja blokkolni a végrehajtást az adatbázis művelet
#a session az ami leköveti a változtatásokat amiket csinálunk, és commit-olni tudunk vagy rollback-elni, event loop-ot használ
#az engine küldi a query-ket
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite+aiosqlite:///./movies.db" #aiosqlite megadja hogy az async sqlite driver-t használjuk


engine = create_async_engine(DATABASE_URL, echo=True)  #echo = True ki fog printelni minden sql query-t
AsyncSessionsLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
#expire on commit: a commit után az objektumot a memóriában maradnak
Base = declarative_base() #provides automatic table creation, ORM capabilities

async def get_db():
    async with AsyncSessionsLocal() as session:
        yield session
#session: temporary workspace ahol átmenetileg dolgozunk, ha kész vagyunk, commitolunk