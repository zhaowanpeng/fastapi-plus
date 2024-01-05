# -*- coding:utf-8 -*-
"""
@Time        :2024/1/2 22:59
@Author      :zhaowanpeng
@description :
"""
from typing import List, Optional

from sqlmodel import Field, Relationship, Session, SQLModel, create_engine


class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    heroes: List["Hero"] = Relationship(back_populates="team")


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)

    team_id: Optional[int] = Field(default=None, foreign_key="team.id")
    team: Optional[Team] = Relationship(back_populates="heroes")

# Code below omitted 👇

# Code below omitted 👇
mysql_url = "mysql+pymysql://root:1230@localhost/database1"

engine = create_engine(mysql_url, echo=True)


def create_tables():
    SQLModel.metadata.create_all(engine)


# def create():
#     with Session(engine) as session:
#         usermodule = User(name="zhaowanpeng")
#         user_info = UserInfo(age=26,user_id=1)
#         # usermodule.user_info = user_info
#         session.add(user_info)
#         session.commit()


if __name__ == '__main__':
    create_tables()
    # create()
