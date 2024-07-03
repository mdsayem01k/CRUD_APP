from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# Replace this line
# SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# With these lines
engine = create_engine(
    "mysql://root@localhost/test",
    connect_args={"local_infile": True},
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()