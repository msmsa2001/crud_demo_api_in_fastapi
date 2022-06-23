from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2


engine=create_engine("postgresql+psycopg2://postgres:ali123@localhost:5432/Employee",echo=True)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)

