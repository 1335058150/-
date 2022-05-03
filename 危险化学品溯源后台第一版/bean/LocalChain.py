"""
@Project ：危险化学品溯源后台第一版 
@File    ：Localchain.py
@Author  ：TXL
@Date    ：2022/2/9 11:40 
"""
# -*- coding: UTF-8 -*-

from bean.Blockchain import Blockchain

class LocalChain(object):

    def __init__(self, blockchain: Blockchain = None):
        # 传入Blockchain参数，如果不传入则为最开始的初始化
        if blockchain is None:
            pass
        else:
            pass
