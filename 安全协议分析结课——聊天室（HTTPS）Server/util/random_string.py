"""
@Project ：安全协议分析结课——聊天室（HTTPS）Server
@File    ：random_string.py
@Author  ：TXL
@Date    ：2022/5/1 13:13 
"""
# -*- coding: UTF-8 -*-
import random

def random_str(lens=5):
    ranStr = ''.join(random.sample(
        ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e',
         'd', 'c', 'b', 'a'], lens))
    return ranStr
