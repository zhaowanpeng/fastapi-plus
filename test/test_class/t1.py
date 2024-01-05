# -*- coding: utf-8 -*-
"""
@Time    : 2024/1/5 14:21
@Author  : zhaowanpeng
@Desc    : None
"""
class A:

    def __setattr__(self, key, value):
        print("key",key)
        print("value-",value)

a = A()
a.abc=123
