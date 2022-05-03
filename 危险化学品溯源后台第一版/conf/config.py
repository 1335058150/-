"""
@Project ：危险化学品溯源后台第一版
@File    ：config.py
@Author  ：TXL
@Date    ：2022/1/21 12:16
"""
# -*- coding: UTF-8 -*-

class Block_Properties(object):

    def __init__(self):
        self.transactions_types = [
            'sender',
            'recipient',
            'amount',
            'information'
        ]

    def get_transactions_types(self):
        return self.transactions_types
