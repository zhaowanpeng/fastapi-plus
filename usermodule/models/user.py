# -*- coding: utf-8 -*-
"""
@Time    :  2024/1/2 15:45
@Author  :  Zhao Wanpeng
@Desc    :  None
"""
from usermodule.models.base import IntIDBaseModel
from usermodule.utils import regex_patterns
from sqlmodel import Field
from typing import Optional
import secrets


class User(IntIDBaseModel, table=True):
    username: str = Field(regex=regex_patterns.username, unique=True, index=True)
    phone: Optional[str] = Field(default=None, regex=regex_patterns.phone, unique=True, index=True)
    email: Optional[str] = Field(default=None, regex=regex_patterns.email, unique=True, index=True)

    salt: str = Field(default=secrets.token_urlsafe())

    password: str = Field(regex=regex_patterns.password)

    # img:
    deleted: bool = False  # 是否注销
    banned: bool = False  # 是否被禁

    phone_active: bool = False
    email_active: bool = False


# global mysqlurl


def insert(username, password):
    from sqlmodel import create_engine, Session, SQLModel
    # global mysqlurl
    mysqlurl = SQLModel.mysqlurl#"mysql+pymysql://root:1230@localhost/database1"
    print(mysqlurl)
    # mysqlurl = mysqlurl
    engine = create_engine(mysqlurl, echo=True)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        user = User(
            username = username,
            password = password
        )
        session.add(user)
        session.commit()


def update(newuser,key="username",value=""):
    from sqlmodel import create_engine, Session, SQLModel, select
    # global mysqlurl
    mysqlurl = SQLModel.mysqlurl  # "mysql+pymysql://root:1230@localhost/database1"
    print(mysqlurl)
    # mysqlurl = mysqlurl
    engine = create_engine(mysqlurl, echo=False)
    with Session(engine) as session:
        print(key)
        statement = select(User).where(User.username == value)
        user = session.exec(statement).one()
        print(user)
        user.phone="17862982889"
        session.add(user)
        session.commit()


if __name__ == '__main__':
    print(123)
    from sqlmodel import SQLModel
    SQLModel.mysqlurl = "mysql+pymysql://root:1230@localhost/database1"
    # insert("zhaowanpeng","123")
    user = User(username="zwp123")
    update(user,key="username",value="zhaowanpeng")
"""
微信认证，（扫码/跳转授权登录）
谷歌认证，
"""
