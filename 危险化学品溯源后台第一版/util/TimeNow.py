"""
@Project ：危险化学品溯源后台第一版 
@File    ：TimeNow.py
@Author  ：TXL
@Date    ：2022/2/6 12:05 
"""
# -*- coding: UTF-8 -*-
import datetime


def getTime():
    now_time = datetime.datetime.now()
    return str(now_time)

def getTime_Full():
    now_time = datetime.datetime.now()
    return str(now_time).replace(" ", "_")

# if __name__ == '__main__':
#     print(getTime())
