# -*- coding:utf-8 -*-
"""
@Time        :2024/1/10 15:26
@Author      :zhaowanpeng
@description :
"""
# example.py

import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi_crudrouter.core.tortoise import TortoiseCRUDRouter
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from tortoise import fields, Tortoise
import os

class TestModel(Model):
    test = fields.IntField(null=False, description=f"Test value")
    ts = fields.IntField(null=False, description=f"Epoch time")


DB_ORM_CONFIG = {
    "connections": {
        "base": {
            'engine': 'tortoise.backends.mysql',
            "credentials": {
                'host': os.getenv('BASE_HOST', '127.0.0.1'),
                'user': os.getenv('BASE_USER', 'root'),
                'password': os.getenv('BASE_PASSWORD', '1230'),
                'port': int(os.getenv('BASE_PORT', 3306)),
                'database': os.getenv('BASE_DB', 'database1'),
            }
        },
    },
    "apps": {
        "base": {"models": ["yy"], "default_connection": "base"},
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai'
}
# Create Database Tables
async def init():
    await Tortoise.init(config=DB_ORM_CONFIG)
    await Tortoise.generate_schemas()

app = FastAPI()





# Tortoise ORM Model


register_tortoise(
    app,
    config=DB_ORM_CONFIG,
    generate_schemas = True,
    add_exception_handlers = True,
)
# Pydantic schema
TestSchema = pydantic_model_creator(TestModel, name=f"{TestModel.__name__}Schema")
# print(TestSchema.model_json_schema())
TestSchemaCreate = pydantic_model_creator(TestModel, name=f"{TestModel.__name__}SchemaCreate", exclude_readonly=True)
# print(TestSchemaCreate)
# # Make your FastAPI Router from your Pydantic schema and Tortoise Model
router = TortoiseCRUDRouter(
    schema=TestSchema,
    create_schema=TestSchemaCreate,
    update_schema=TestSchemaCreate,
    db_model=TestModel,
    prefix="test"
)
#
# # Add it to your app
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("yy:app", host="127.0.0.1", port=5000, log_level="info")
