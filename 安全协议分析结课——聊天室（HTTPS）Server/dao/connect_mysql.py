"""
@Project ：安全协议分析结课——聊天室（HTTPS）Server 
@File    ：connect_mysql.py
@Author  ：TXL
@Date    ：2022/5/1 13:38 
"""
# -*- coding: UTF-8 -*-
import pymysql

from conf.databases import get_sqlinf

def connect(Servername=None, user=None, passwd=None, port=3306, database=None):
    if Servername is None or user is None or passwd is None or database is None:
        config = get_sqlinf()
    else:
        config = {
            "host": Servername,
            "port": port,
            "user": user,
            "password": passwd,
            "database": database
        }
    conn = pymysql.connect(**config)
    return conn