# -*- coding: utf-8 -*-
"""
@Time    : 2024/1/10 18:30
@Author  : zhaowanpeng
@Desc    : None
"""
from fastapi import FastAPI

from easyauth.server import EasyAuthServer

server = FastAPI()

async def create_easy_auth_server():
    return await EasyAuthServer.create(
        server,
        '/auth/token',
        auth_secret='abcd1234',
        admin_title='EasyAuth - Company',
        admin_prefix='/admin',
        env_from_file='server_sqlite.json'
    )
server.auth = create_easy_auth_server()
# server.auth = await EasyAuthServer.create(
#     server,
#     '/auth/token',
#     auth_secret='abcd1234',
#     admin_title='EasyAuth - Company',
#     admin_prefix='/admin',
#     env_from_file='server_sqlite.json'
# )
