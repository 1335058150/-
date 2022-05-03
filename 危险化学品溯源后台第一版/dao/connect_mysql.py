"""
@Project ：危险化学品溯源后台第一版 
@File    ：connect_mysql.py
@Author  ：TXL
@Date    ：2022/2/6 11:53 
"""
# -*- coding: UTF-8 -*-
import pymysql

config = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "cdo"
}
conn = pymysql.connect(**config)

