# -*- coding: utf-8 -*-
"""
@Time    :  2024/1/2 15:45
@Author  :  Zhao Wanpeng
@Desc    :  None
"""
from user.models.base import IntIDBaseModel
from user.utils import regex_patterns
from sqlmodel import Field
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

"""
微信认证，（扫码/跳转授权登录）
谷歌认证，
"""