from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2
import os



engine=create_engine("postgresql://xvbxecklfindav:4f5a1d204c2188a414f36ee4838616b3c1482d8f4f26a972aacef3bc29a449a0@ec2-34-233-115-14.compute-1.amazonaws.com:5432/d3ej94n4em2egg")

# engine=create_engine("postgresql+psycopg2://postgres:ali123@localhost:5432/Employee",echo=True)

# engine=create_engine(f"{os.getenv('DB_NAME')}://)",echo=True)

SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()


