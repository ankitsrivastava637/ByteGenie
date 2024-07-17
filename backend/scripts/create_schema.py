from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models.base import Base
from backend.config.index import db

def create_schema():
    engine = create_engine(db.engine.url)
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_schema()
