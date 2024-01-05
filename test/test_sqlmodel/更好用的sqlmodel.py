# -*- coding: utf-8 -*-
"""
@Time    : 2024/1/5 14:24
@Author  : zhaowanpeng
@Desc    : None
"""
# from sqlmodel import SQLModel
# 增删改查更简单
from sqlmodel import SQLModel, Field, Column, TIMESTAMP, Session, create_engine, DateTime
from typing import Optional
from datetime import datetime


# SQLModel.global_session = Session(create_engine("mysql+pymysql://root:1230@localhost/database1"))

class IntIDBaseModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    value: str
    created_at: datetime = Field(default=datetime.now(),)
    updated_at: datetime = Field(sa_column=Column(
        DateTime,
        nullable=True,
        default=datetime.now(),
        onupdate=datetime.now()
    ))
    # updated_at: Optional[datetime] = Field(sa_column=Column(
    #     TIMESTAMP,
    #     nullable=True,
    #     default=None,
    #     onupdate=datetime.now()
    # ))


a = IntIDBaseModel(value="123")
print(a.updated_at)
# b = IntIDBaseModel(value="321")

print(a)

# simple增
# class EasyCRUDMixin:
#
#     def __init__(self):
#         if hasattr(SQLModel, "DB_FULL_URL"):
#             raise "请先为SQLModel设置DB_FULL_URL"
#         #self._DB_FULL_URL = SQLModel.DB_FULL_URL
#         #self.engine =
#
#     def insert(self, ):
#
#         SQLModel.global_session.commit()
#         pass
