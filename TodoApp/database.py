from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# SQLALCHEMY_DATABASE_URL="sqlite:///./todosapp.db"
SQLALCHEMY_DATABASE_URL="postgresql://postgres:necsws2025@localhost/TodoApplicationDatabase"
# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:necsws2025@db:5432/TodoApplicationDatabase"


engine = create_engine(SQLALCHEMY_DATABASE_URL) #, connect_args={'check_same_thread':False}) # connect_args this is only for sqlite

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

