# -*- coding: utf-8 -*-
"""
@Time    : 2024/1/8 12:58
@Author  : zhaowanpeng
@Desc    : None
"""
import re
from tortoise import models, fields
from tortoise.validators import RegexValidator
from user_module.models.base import IntIDBaseModel, TimestampMixin
from user_module.utils import regex_patterns


class User(IntIDBaseModel):

    username = fields.CharField(unique=True, index=True, max_length=20,
                                validators=[RegexValidator(regex_patterns.username, re.I,)])

    phone = fields.CharField(null=True, index=True, max_length=11,
                             validators=[RegexValidator(regex_patterns.phone, re.I)])

    email = fields.CharField(null=True, index=True, max_length=50,
                             validators=[RegexValidator(regex_patterns.email, re.I)])


    # salt = fields.CharField()
    # password = fields.CharField()

    deleted = fields.BooleanField(default=False)  # 是否注销
    banned = fields.BooleanField(default=False)  # 是否被禁

    phone_active = fields.BooleanField(default=False)
    email_active = fields.BooleanField(default=False)
