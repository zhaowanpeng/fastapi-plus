# -*- coding: utf-8 -*-
"""
@Time    :  2024/1/2 15:44
@Author  :  zhaowanpeng
@Desc    :  方便开发的基础模型
"""
from sqlmodel import SQLModel, Field, Column, TIMESTAMP
from typing import Optional
from datetime import datetime


class IntIDBaseModel(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(sa_column=Column(
        TIMESTAMP,
        nullable=True,
        default=None,
        onupdate=datetime.now()
    ))