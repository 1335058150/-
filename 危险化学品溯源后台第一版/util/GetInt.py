"""
@Project ：危险化学品溯源后台第一版 
@File    ：GetInt.py
@Author  ：TXL
@Date    ：2022/2/21 17:02 
"""
# -*- coding: UTF-8 -*-

def getint(a):
    """
    将其他变量转变为int整型，如果转换失败，则返回None
    :param a:
    :return:
    """
    try:
        return int(a)
    except ValueError or IndexError:
        pass
