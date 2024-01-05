# -*- coding: utf-8 -*-
"""
@Time    : 2024/1/4 14:05
@Author  : zhaowanpeng
@Desc    : None
"""
from fastapi import APIRouter, Depends
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm
)
from usermodule.models.user import User

token_router = APIRouter()

@token_router.post("/token")
async def create_token(form_data: OAuth2PasswordRequestForm = Depends()):

    # User.

    return {}