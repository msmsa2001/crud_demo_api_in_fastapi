
from distutils.log import error
from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
from fastapi.responses import JSONResponse
import models 
import schema

app=FastAPI()

db=SessionLocal()



# @app.get('/items',response_model=List[schema.Item],status_code=200)
# def get_all_items():
#     items=db.query(models.Item).all()

#     return items


# @app.get('/item/{item_id}',response_model=schema.Item,status_code=status.HTTP_200_OK)
# def get_an_item(item_id:int):
#     item=db.query(models.Item).filter(models.Item.id==item_id).first()

#     return item

@app.post('/register',response_model=schema.SignUp,status_code=status.HTTP_201_CREATED)
def register_an_user(user:schema.SignUp):
    db_New_user=db.query(models.SignUp).filter(models.SignUp.email==user.email or models.SignUp.mobnumber==user.mobnumber).first()
    
    if db_New_user is not None:
        return JSONResponse(status_code=200, content={"message": "Data Already Present","code":"400"})      
        # raise HTTPException(status_code=400,detail="Data Already Present")
    else:
        new_user=models.SignUp(
            name=user.name,
            email=user.email,
            mobnumber=user.mobnumber,
            password=user.password
        )
        db.add(new_user)
        db.commit()
        return JSONResponse(status_code=200, content={"message": "Registration Successful","code":"200"})

    # return new_user


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
                },
                "error":"200"
                }
            return JSONResponse(status_code=200, content=data)

        else:
            return JSONResponse(status_code=200, content={"error":"404","message":"email or password is wrong"})
    else:
        return JSONResponse(status_code=200, content={"error":"404","message":"email or password is wrong"})
        



@app.put('/item/{item_id}',response_model=schema.SignUp,status_code=status.HTTP_200_OK)
def update_an_item(item_id:int,item:schema.SignUp):
    item_to_update=db.query(models.SignUp).filter(models.SignUp.id==item_id).first()
    item_to_update.name=item.name,
    item_to_update.email=item.email,
    item_to_update.mobnumber=item.mobnumber,
    item_to_update.password=item.password

    db.commit()

    return item_to_update    




@app.delete('/item/{item_id}')
def delete_item(item_id:int):
    item_to_delete=db.query(models.SignUp).filter(models.SignUp.id==item_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Record is not Found")
    
    db.delete(item_to_delete)
    db.commit()
    return item_to_delete


