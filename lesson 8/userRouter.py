from fastapi import FastAPI, Depends, APIRouter, HTTPException
from pydantic import BaseModel, constr, ValidationError, validator, field_validator
from fastapi.encoders import jsonable_encoder

userrouter = APIRouter()


class User(BaseModel):
    name: constr(pattern=r"^[a-zA-Z0-9_]+$")
    password: constr(min_length=1, max_length=120)
    userId: int



users = {}

def is_exist_id(id: int):
    if users[id] is not None:
        return True
    return False


@userrouter.get("/")
async def getUsers():
    return users
    raise HTTPException(status_code=404, detail="oops... your task didn't find")


@userrouter.post("/")
async def add_user(user: User,is_exist:bool = Depends(is_exist_id)):
    try:
        if is_exist is False:
            users[user.userId] = user
        else:
            raise HTTPException(status_code=400, detail="oops... this id is already exist")
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"Hello {user.name}"


@userrouter.put("/{id}", response_model=User)
async def update_user(id: int, item: User):
    update_item = jsonable_encoder(item)
    users[id] = update_item
    return update_item


@userrouter.delete("/{id}")
async def delete_user(id: int):
    del users[id]
    return {"message": "Item deleted"}