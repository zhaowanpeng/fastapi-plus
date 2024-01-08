# -*- coding: utf-8 -*-
"""
@Time    : 2024/1/5 17:37
@Author  : zhaowanpeng
@Desc    : None
"""
# pylint: disable=E0611,E0401
from typing import List

from fastapi import FastAPI
from models import Users, User_Pydantic, UserIn_Pydantic, UserOut_Pydantic
from pydantic import BaseModel
from starlette.exceptions import HTTPException

# print("UserIn_Pydantic",UserIn_Pydantic)

from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()


class Status(BaseModel):
    message: str


@app.get("/users", response_model=List[UserOut_Pydantic])
async def get_users():
    return await UserOut_Pydantic.from_queryset(Users.all())


@app.post("/users", response_model=UserOut_Pydantic)
async def create_user(user: UserIn_Pydantic):
    # print(dict(**user))
    # print(dict(**user.model_dump(exclude_unset=True)))
    user_obj = await Users.create(**user.model_dump(exclude_unset=True))
    return await UserOut_Pydantic.from_tortoise_orm(user_obj)


@app.get("/user/{user_id}", response_model=UserOut_Pydantic)
async def get_user(user_id: int):
    return await UserOut_Pydantic.from_queryset_single(Users.get(id=user_id))


@app.get("/user/haha/{username}", response_model=UserOut_Pydantic)
async def get_user2(username: str):
    delete_action = await Users.filter(username=username)
    print(delete_action)
    return await UserOut_Pydantic.from_queryset_single(Users.filter(username=username).first())


@app.get("/user/{phone}", response_model=UserOut_Pydantic)
async def get_user3(phone: str):
    return await UserOut_Pydantic.from_queryset_single(Users.filter(phone=phone))


#
#
# @app.put("/user/{user_id}", response_model=User_Pydantic)
# async def update_user(user_id: int, user: UserIn_Pydantic):
#     await Users.filter(id=user_id).update(**user.model_dump(exclude_unset=True))
#     return await User_Pydantic.from_queryset_single(Users.get(id=user_id))
#
#
# @app.delete("/user/{user_id}", response_model=Status)
# async def delete_user(user_id: int):
#     deleted_count = await Users.filter(id=user_id).delete()
#     if not deleted_count:
#         raise HTTPException(status_code=404, detail=f"User {user_id} not found")
#     return Status(message=f"Deleted user {user_id}")


# register_tortoise(
#     app,
#     db_url="sqlite://:memory:",
#     modules={"models": ["models"]},
#     generate_schemas=True,
#     add_exception_handlers=True,
# )


import os

DB_ORM_CONFIG = {
    "connections": {
        "base": {
            'engine': 'tortoise.backends.mysql',
            "credentials": {
                'host': os.getenv('BASE_HOST', '127.0.0.1'),
                'user': os.getenv('BASE_USER', 'root'),
                'password': os.getenv('BASE_PASSWORD', '1230'),
                'port': int(os.getenv('BASE_PORT', 3306)),
                'database': os.getenv('BASE_DB', 'database1'),
            }
        },
    },
    "apps": {
        "base": {"models": ["models"], "default_connection": "base"},
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai'
}

register_tortoise(
    app,
    config=DB_ORM_CONFIG,
    generate_schemas=True,
    add_exception_handlers=True,
)

# u = Users.filter(username="赵abc123").first()
# print(u)
# if __name__ == '__main__':
#
