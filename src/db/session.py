import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Database url if none is passed the default one is used
DATABASE_URL = os.getenv("SQALCHEMY_DATABASE_URI", "postgresql://hello_fastapi:hello_fastapi@localhost/hello_fastapi_dev")

# SQLAlchemy
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        