# -*- coding: utf-8 -*-
"""
@Time    :  2024/1/2 16:49
@Author  :  zhaowanpeng
@Desc    :  最简单的rbac结构
"""
from user.models.base import IntIDBaseModel
from sqlmodel import SQLModel, Field
from typing import Optional
from user.utils import regex_patterns
import secrets


class User(IntIDBaseModel, table=True):

    username: str = Field(regex=regex_patterns.username)
    phone: str = Field(regex=regex_patterns.phone)
    email: str = Field(regex=regex_patterns.email)

    salt: str = Field(default=secrets.token_urlsafe())

    password: str = Field(regex=regex_patterns.password)

    # img:
    deleted: bool = False  # 是否注销
    banned: bool = False  # 是否被禁

    phone_active: bool = False
    email_active: bool = False


class Role(IntIDBaseModel, table=True):
    name: str  #
    role_des: Optional[str] = None
    valid: bool = True


class Permission(IntIDBaseModel, table=True):
    action: str

    valid: bool = True

class Action(IntIDBaseModel, table=True):
    name: str  # [增]
    type: str  # [GET,POST,PUT,DELETE]
