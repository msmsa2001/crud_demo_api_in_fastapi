from database import Base
from sqlalchemy import VARCHAR, String,Boolean,Integer,Column

class SignUp(Base):
    __tablename__='items'
    id=Column(Integer,primary_key=True, autoincrement=True)
    name=Column(String(50),nullable=False)
    email=Column(String(30),nullable=False,unique=True)
    mobnumber=Column(VARCHAR(10),nullable=False)
    gender=Column(VARCHAR(10),nullable=False)
    dob=Column(VARCHAR(10),nullable=False)
    password=Column(String(10),nullable=False)

    # def __repr__(self):
    #     return f"<Item name={self.name} price={self.email}>"


class Employee(Base):
    __tablename__='employee'
    id=Column(Integer,primary_key=True,autoincrement=True)
    fname=Column(String(50),nullable=False)
    lname=Column(String(50),nullable=False)
    sname=Column(String(50),nullable=False)
    email=Column(String(30),nullable=False,unique=True)
    mobnumber=Column(VARCHAR(10),nullable=False)
    gender=Column(VARCHAR(10),nullable=False)
    dob=Column(VARCHAR(10),nullable=False)
    website=Column(String(50),nullable=False)
    occupation=Column(String(50),nullable=False)
    addr1=Column(String(50),nullable=False)
    addr2=Column(String(50),nullable=False)
    city=Column(String(50),nullable=False)
    state=Column(String(50),nullable=False)
    pin=Column(String(10),nullable=False)
    
