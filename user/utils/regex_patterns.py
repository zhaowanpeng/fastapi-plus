# -*- coding: utf-8 -*-
"""
@Time    :  2024/1/2 15:47
@Author  :  Zhao Wanpeng
@Desc    :  None
"""

ipv4 = "^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})(\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})){3}$"
ipv6 = "^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"

phone = "^1[3456789]\d{9}$"
email = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

#中文英文大小写数字组合，总长度不大于16
username = "^(?=.*[\u4E00-\u9FFF])(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z0-9\u4E00-\u9FFF]{1,16}$"
#必须包含字母和数字，且总长度不小于6
password = "^(?=.*[a-zA-Z])(?=.*\d).{6,}$"