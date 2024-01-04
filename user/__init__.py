# -*- coding: utf-8 -*-
"""
@Time    :  2024/1/2 15:40
@Author  :  Zhao Wanpeng
@Desc    :  None
"""
from fastapi import APIRouter
# from

user_router = APIRouter()


@user_router.post("/register", tags=["用户"], summary="用户注册")
async def register(username: str, password: str, code: int):
    return False

@user_router.post("/login", tags=["用户"],summary="用户登录")
async def login(a:int):
    return False

@user_router.post("/token", tags=["JWT"], summary="获得token")
async def token():
    return


@user_router.get("/sendcode/phone", tags=["验证码"],summary="手机发送验证码")
async def sendcode_by_phone(phone:str):
    code = 123
    return code

@user_router.get("/sendcode/email", tags=["验证码"],summary="邮箱发送验证码")
async def sendcode_by_email(email:str):
    code = 123
    return code





@user_router.post("/token")
async def create_token(b:int):
    return False