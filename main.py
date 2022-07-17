
# from distutils.log import error
from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
from fastapi.responses import JSONResponse
import models 
import schema

app=FastAPI()

db=SessionLocal()



@app.get('/user',response_model=List[schema.SignUp],status_code=200)
def get_all_user():
    user=db.query(models.SignUp).all()

    return user

@app.get('/user/{occupation}/{add2}',response_model=List[schema.Employee],status_code=200)
def get_employee(occupation:str,add2:str):
    employee=db.query(models.Employee).filter(models.Employee.occupation==occupation and models.Employee.addr2==add2).all()

    return employee



# @app.get('/item/{item_id}',response_model=schema.Item,status_code=status.HTTP_200_OK)
# def get_an_item(item_id:int):
#     item=db.query(models.Item).filter(models.Item.id==item_id).all

#     return item


@app.post('/register',response_model=schema.SignUp,status_code=status.HTTP_201_CREATED)
def register_an_user(user:schema.SignUp):
    db_New_user=db.query(models.SignUp).filter(models.SignUp.email==user.email or models.SignUp.mobnumber==user.mobnumber).first()
    # print("db_New_user : ", db_New_user)
    
    if db_New_user is not None:
        return JSONResponse(status_code=200, content={"message": "Data Already Present","code":"400"})      
        # raise HTTPExcseption(status_code=400,detail="Data Already Present")
    else:
        new_user=models.SignUp(
            name=user.name,
            email=user.email,
            mobnumber=user.mobnumber,
            password=user.password,
            gender=user.gender,
            dob=user.dob
        )
        # print("new _user : ", new_user)
        db.add(new_user)
        db.commit()
        return JSONResponse(status_code=200, content={"message": "Registration Successful","code":"200"})

    


@app.post('/login',response_model=schema.Login,status_code=status.HTTP_202_ACCEPTED)
def login_an_user(user:schema.Login):
    db_check=db.query(models.SignUp).filter(models.SignUp.email==user.email).first()
    # db_password=db.query(models.SignUp).filter(models.SignUp.password==item.password)
    # print(db_check)
    # return db_check

    if db_check is not None:
        if db_check.password==user.password is not None:
            data={
                "user":{
                "id":db_check.id,
                "name":db_check.name,
                "mobnumber":db_check.mobnumber,
                "email":db_check.email,
                "gender":db_check.gender,
                "dob":db_check.dob
                },
                "error":"200"
                }
            return JSONResponse(status_code=200, content=data)

        else:
            return JSONResponse(status_code=200, content={"error":"404","message":"email or password is wrong"})
    else:
        return JSONResponse(status_code=200, content={"error":"404","message":"email or password is wrong"})
        



@app.put('/update_user/{user_id}',response_model=schema.SignUp,status_code=status.HTTP_200_OK)
def update_an_item(user_id:int,user:schema.SignUp):
    item_to_update=db.query(models.SignUp).filter(models.SignUp.id==user_id).first()
    item_to_update.name=user.name,
    item_to_update.email=user.email,
    item_to_update.mobnumber=user.mobnumber,
    item_to_update.password=user.password

    db.commit()

    return item_to_update    




# @app.delete('/item/{item_id}')
# def delete_item(item_id:int):
#     item_to_delete=db.query(models.SignUp).filter(models.SignUp.id==item_id).first()

#     if item_to_delete is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Record is not Found")
    
#     db.delete(item_to_delete)
#     db.commit()
#     return item_to_delete




@app.post('/employee',response_model=schema.Employee,status_code=status.HTTP_201_CREATED)
def register_an_employee(employee:schema.Employee):
    db_New_Employee=db.query(models.Employee).filter(models.Employee.email==employee.email or models.Employee.mobnumber==employee.mobnumber).first()
    
    if db_New_Employee is not None:
        return JSONResponse(status_code=200, content={"message": "Data Already Present","code":"400"})      
        # raise HTTPException(status_code=400,detail="Data Already Present")
    else:
        New_Employee=models.Employee(
            fname=employee.fname,
            lname=employee.lname,
            sname=employee.sname,
            email=employee.email,
            mobnumber=employee.mobnumber,
            gender=employee.gender,
            dob=employee.dob,
            website=employee.website,
            occupation=employee.occupation,
            addr1=employee.addr1,
            addr2=employee.addr2,
            city=employee.city,
            state=employee.state,
            pin=employee.pin
        )
        db.add(New_Employee)
        db.commit()
        return JSONResponse(status_code=200, content={"message": "Registration Successful","code":"200"})


# @app.post('/search-employee',response_model=schema.Search_employee,status_code=status.HTTP_202_ACCEPTED)
# def search_employee(src_emp:schema.Search_employee):
#     db_check=db.query(models.Employee).filter(models.Employee.occupation==src_emp.occupation and models.Employee.addr2==src_emp.addr2 ).first()

#     data={
#         "user":{
#         "id":db_check.id,
#         "name":db_check.fname,
#         "mobnumber":db_check.mobnumber,
#         "email":db_check.email,
#         },
#         "error":"200"
#         }
#     return JSONResponse(status_code=200, content=data)
#     db_password=db.query(models.SignUp).filter(models.SignUp.password==item.password)
#     print(db_check)
#     return db_check
