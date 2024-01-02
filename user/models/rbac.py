# -*- coding: utf-8 -*-
"""
@Time    :  2024/1/2 16:49
@Author  :  zhaowanpeng
@Desc    :  None
"""
from user.models.base import IntIDBaseModel
from user.models.user import User
from sqlmodel import SQLModel, Field
from typing import Optional


class Role(IntIDBaseModel, table=True):
    name: str  #
    role_des: Optional[str] = None
    valid: bool = True


class Permission(IntIDBaseModel, table=True):
    action: str
    valid: bool = True


