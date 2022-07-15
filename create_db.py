from database import Base,engine
from models import Item
from models import Employee

print("Creating DataBase ...")

Base.metadata.create_all(engine)