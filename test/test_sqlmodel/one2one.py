# -*- coding:utf-8 -*-
"""
@Time        :2024/1/2 22:56
@Author      :zhaowanpeng
@description :
"""
from sqlmodel import SQLModel, Field, create_engine, Session, Relationship
from typing import Optional
from sqlalchemy.engine import Engine


mysql_url = "mysql+pymysql://root:1230@localhost/database1"
engine = create_engine(mysql_url, echo=False)


class User1(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

class UserInfo1(SQLModel, table=True):
    user_id: int = Field(foreign_key="user1.id", primary_key=True)
    age: int





def create_tables():
    SQLModel.metadata.create_all(engine)


def create_row():
    with Session(engine) as session:
        user = User1(name="zhaowanpeng")
        print(user.id)
        session.add(user)
        session.commit()
        # session.refresh(user)
        print(user.id)
        user_info = UserInfo1(age=100,user_id=user.id)
        session.add(user_info)
        session.commit()

# def create():
#     with Session(engine) as session:
#         user = User(name="zhaowanpeng")
        # user_info = UserInfo(age=26,user_id=1)
        # # user.user_info = user_info
        # session.add(user_info)
        # session.commit()


if __name__ == '__main__':
    create_tables()
    create_row()
    # with Session(engine) as session:
    #     u = session.get(User,(1,"zhaowanpeng"))
    #     print(u)
    # create_tables()
    # user = User(id=1, name="zhaowanpeng")
    # user.create(engine)
    # create()

    # crud = CRUD()
    # user = User(name="zhaowanpeng")
    # print(user.model_dump())
    # print(user.)