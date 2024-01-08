# -*- coding: utf-8 -*-
"""
@Time    : 2024/1/8 11:01
@Author  : zhaowanpeng
@Desc    : None
"""
from tortoise import fields, models
from tortoise.validators import RegexValidator
from tortoise.contrib.pydantic import pydantic_model_creator
from user_module.utils import regex_patterns
import re


class Users(models.Model):
    """
    The User model
    """
    id = fields.IntField(pk=True)

    username = fields.CharField(unique=True, index=True, max_length=20,
                                validators=[RegexValidator(regex_patterns.username, re.I)])

    phone = fields.CharField(null=True, index=True, max_length=11,
                             validators=[RegexValidator(regex_patterns.phone, re.I)])

    email = fields.CharField(null=True, index=True, max_length=50,
                             validators=[RegexValidator(regex_patterns.email, re.I)])

    # salt = fields.CharField()
    password = fields.CharField(max_length=10)

    deleted = fields.BooleanField(default=False)  # 是否注销
    banned = fields.BooleanField(default=False)  # 是否被禁

    phone_active = fields.BooleanField(default=False)
    email_active = fields.BooleanField(default=False)

    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    updated_at = fields.DatetimeField(null=True, auto_now=True)

    """
    生成pytandic
    """
    # def full_name(self) -> str:
    #     """
    #     Returns the best name
    #     """
    #     if self.name or self.family_name:
    #         return f"{self.name or ''} {self.family_name or ''}".strip()
    #     return self.username

    # class PydanticMeta:

        # computed = ["full_name"]
        # exclude = ["password_hash","created_at","modified_at"]



User_Pydantic = pydantic_model_creator(Users, name="User")
UserOut_Pydantic = pydantic_model_creator(Users, name="UserOut", include=("id","username","phone","email",))
UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", include=("username","phone","email","password"))#exclude=("id","created_at","updated_at")
print("--start--"*10)
print(UserIn_Pydantic.model_json_schema())
print("--end--"*10)
# exit()
# UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)
# print(123)
