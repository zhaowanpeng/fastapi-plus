# -*- coding: utf-8 -*-
"""
@Time    : 2024/1/4 18:17
@Author  : zhaowanpeng
@Desc    : None
"""
from fastapi import APIRouter
# from
from usermodule.models.user import User, insert

user_router = APIRouter()


@user_router.post("/register", tags=["用户"], summary="用户注册")
async def register(username: str, password: str, code: int):
    # 检查用户名是否符合格式要求

    # 检查密码是否符合格式要求

    # 检查用户是否已经存在

    # 检查code是否正确
    insert(username, password)
    return True


@user_router.post("/login", tags=["用户"], summary="用户登录")
async def login(a: int):
    return False
