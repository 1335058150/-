"""
@Project ：安全协议分析结课——聊天室（HTTPS）Server 
@File    ：databases.py
@Author  ：TXL
@Date    ：2022/5/1 14:13 
"""
# -*- coding: UTF-8 -*-
def get_sqlinf():
    return {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "database": "chatting_room"
    }