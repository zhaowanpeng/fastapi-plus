# -*- coding: utf-8 -*-
"""
@Time    : 2024/1/4 14:03
@Author  : zhaowanpeng
@Desc    : None
"""
from sqlmodel import SQLModel, Field


class Token(SQLModel):
    token: str
    type: str