from pydantic import BaseModel
from sqlalchemy import CHAR

class SignUp(BaseModel):
    
    name:str
    email:str
    gender:str
    dob:str
    mobnumber:str
    password:str

    class Config:
        orm_mode=True



class Login(BaseModel):
    email:str
    password:str

    class Config:
        orm_mode=True


class Employee(BaseModel):
    fname:str
    lname:str
    sname:str
    email:str
    mobnumber:str
    gender:str
    dob:str
    website:str
    occupation:str
    addr1:str
    addr2:str
    city:str
    state:str
    pin:str

    class Config:
        orm_mode=True


class Search_employee(BaseModel):

    occupation:str
    # addr2:str

    class Config:
        orm_mode=True