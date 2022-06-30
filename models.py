from database import Base
from sqlalchemy import VARCHAR, String,Boolean,Integer,Column

class SignUp(Base):
    __tablename__='items'
    id=Column(Integer,primary_key=True)
    name=Column(String(50),nullable=False)
    email=Column(String(30),nullable=False,unique=True)
    mobnumber=Column(VARCHAR(10),nullable=False)
    password=Column(String(10),nullable=False)

    def __repr__(self):
        return f"<Item name={self.name} price={self.email}>"
    