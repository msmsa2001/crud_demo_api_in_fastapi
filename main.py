
from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
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

@app.post('/items',response_model=schema.SignUp,status_code=status.HTTP_201_CREATED)
def register_an_user(item:schema.SignUp):
    db_New_user=db.query(models.SignUp).filter(models.SignUp.email==item.email or models.SignUp.mobnumber==item.mobnumber).first()
    
    if db_New_user is not None:
        raise HTTPException(status_code=400,detail="Data Already Present")
    
    new_user=models.SignUp(
        name=item.name,
        email=item.email,
        mobnumber=item.mobnumber,
        password=item.password
    )
    db.add(new_user)
    db.commit()

    return new_user

@app.post('/item',response_model=schema.SignUp,status_code=status.HTTP_202_ACCEPTED)
def login_an_user(item:schema.SignUp):
    db_check=db.query(models.SignUp).filter(models.SignUp.email==item.email and models.SignUp.password==item.password)
    print(db_check)

    if db_check is not None:
        print('Successfull')
        # raise HTTPException(status_code=400,detail="login done")
    else:
        print('Invalid')
        # raise HTTPException(status_code=400,detail="Login Done")







# @app.put('/item/{item_id}',response_model=schema.Item,status_code=status.HTTP_200_OK)
# def update_an_item(item_id:int,item:schema.Item):
#     item_to_update=db.query(models.Item).filter(models.Item.id==item_id).first()
#     item_to_update.name=item.name,
#     item_to_update.email=item.email,
#     item_to_update.mob_numbeer=item.mob_numbeer,
#     item_to_update.password=item.password

#     db.commit()

#     return item_to_update    




# @app.delete('/item/{item_id}')
# def delete_item(item_id:int):
#     item_to_delete=db.query(models.Item).filter(models.Item.id==item_id).first()

#     if item_to_delete is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Record is not Found")
    
#     db.delete(item_to_delete)
#     db.commit()
#     return item_to_delete


