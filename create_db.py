from database import Base,engine
from models import Item

print("Creating DataBase ...")

Base.metadata.create_all(engine)