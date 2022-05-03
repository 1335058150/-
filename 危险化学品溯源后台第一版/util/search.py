"""
@Project ：危险化学品溯源后台第一版 
@File    ：search.py
@Author  ：TXL
@Date    ：2022/2/21 17:01 
"""
# -*- coding: UTF-8 -*-

def search_block(chain: list, index: int, fact=False):
    """
    设计静态算法用来快速查找区块中的目标值
    :param fact: 默认为False，如果为True那就证明前边的区块被处理过导致数据出现超出现象
    :param index: 需要查找的目标区块的index索引值
    :param chain:传入区块
    :return:
    """
    if not fact:
        try:
            target = chain[index]
            if target['index'] == index:
                return target
            else:
                return search_block(chain=chain, index=index, fact=True)
        except IndexError:
            return search_block(chain=chain, index=index, fact=True)
    else:
        index_ = index
        while True:
            try:
                target = chain[index_]
                if target['index'] == index:
                    return target
                else:
                    index_ -= 1
            except IndexError:
                index_ -=1
                continue
