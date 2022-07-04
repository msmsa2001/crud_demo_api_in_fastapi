from pydantic import BaseModel
from sqlalchemy import CHAR

class SignUp(BaseModel):
    
    name:str
    mobnumber:str
    email:str
    password:str

    class Config:
        orm_mode=True



class Login(BaseModel):
    email:str
    password:str

    class Config:
        orm_mode=True