"""
@Project ：安全协议分析结课——聊天室（HTTPS）Server 
@File    ：time_now.py
@Author  ：TXL
@Date    ：2022/5/2 9:57 
"""
# -*- coding: UTF-8 -*-
import time

def gettime():
    return time.ctime(time.time())

# print(time.ctime(time.time()))
# print(time.asctime(time.localtime()))
# print(type(time.ctime(time.time())))
# print(type(time.asctime(time.localtime())))
# print("\033[31m这是红色字体\033[0m")
# print("\033[32m这是绿色字体\033[0m")
# print("\033[33m这是黄色字体\033[0m")
# print("\033[34m这是蓝色字体\033[0m")
# print("\033[38m这是默认字体\033[0m")  # 大于37将显示默认字体
