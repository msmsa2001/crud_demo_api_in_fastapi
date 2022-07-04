from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2
import os



engine=create_engine("postgresql+psycopg2://postgres:ali123@localhost:5432/Employee",echo=True)

# engine=create_engine(f"{os.getenv('DB_NAME')}://)",echo=True)

SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()


