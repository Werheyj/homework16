from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_users() -> list:
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int) -> User:
    new_id = (users[-1].id + 1) if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[str, Path(min_length=1, max_length=20,
                                                   description='Enter user id', example='1')],
                      username: Annotated[str, Path(min_length=5, max_length=20,
                                                    description='Enter username', example='UrbanUser')],
                      age:  Annotated[int, Path(ge=18, le=100, description='Enter User age', example='24')]) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    for user in users:
        if user.id == user_id:
            return users.pop(user)
    raise HTTPException(status_code=404, detail="User was not found")
