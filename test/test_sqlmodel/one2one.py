# -*- coding:utf-8 -*-
"""
@Time        :2024/1/2 22:56
@Author      :zhaowanpeng
@description :
"""
from sqlmodel import SQLModel, Field, create_engine, Session, Relationship
from typing import Optional




class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    # user_info: Optional["UserInfo"] = Field(default=None, foreign_key="user.id")


class UserInfo(SQLModel, table=True):
    # id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", primary_key=True)
    age: int



mysql_url = "mysql+pymysql://root:1230@localhost/database1"

engine = create_engine(mysql_url, echo=True)


def create_tables():
    SQLModel.metadata.create_all(engine)


def create():
    with Session(engine) as session:
        user = User(name="zhaowanpeng")
        user_info = UserInfo(age=26,user_id=1)
        # user.user_info = user_info
        session.add(user_info)
        session.commit()


if __name__ == '__main__':
    # create_tables()
    create()
