# -*- coding: utf-8 -*-
"""
@Time    : 2024/1/8 12:48
@Author  : zhaowanpeng
@Desc    : None
"""
from tortoise import fields


class TimestampMixin:
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    updated_at = fields.DatetimeField(null=True, auto_now=True)


class IntIDBaseModel(TimestampMixin):
    id = fields.IntField(pk=True)

