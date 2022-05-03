"""
@Project ：危险化学品溯源后台第一版 
@File    ：Globals.py
@Author  ：TXL
@Date    ：2022/2/11 17:38 
"""
# -*- coding: utf-8 -*-
import json
import os


def __init__():  # 初始化
    # print(os.getcwd()+"\\conf\\globals.json")
    global _global_dict
    # with open(os.getcwd()+"\\conf\\globals.json", 'r', encoding='UTF-8') as f:
    with open(".\\conf\\globals.json", 'r', encoding='UTF-8') as f:
        _global_dict = json.load(f)


def set_value(key: str, value: str):
    """ 定义一个全局变量 """
    _global_dict[key] = value


def get_value(key: list, _value=None):
    """ 获得一个全局变量,不存在则返回None."""
    """
    使用案例：
    字典dict/json格式：
        {
          "TEST3": {
            "TEST": {
              "TES": {
                "TE": {
                  "T": "777"
                }
              },
              "BB": 999
            },
            "AA": 888
          }
        }
    在这边我希望获取到其中的777值，则使用方法：
    Globals.get_value(["TEST3", "TEST", "TES", "TE", "T"])
    """
    try:
        if len(key) == 1:
            return _global_dict[key[0]]
        else:
            level = 1
            dict_e = _global_dict[key[0]]
            while True:
                key_ = key[level]
                if key[level] in dict_e:
                    dict_e = dict_e[key_]
                    level += 1
                    if type(dict_e) == type({}):
                        continue
                    else:
                        # print("*" * 30)
                        return dict_e
                else:
                    return _value
    except KeyError:
        return _value


# def get_dict():
#     return _global_dict


if __name__ == '__main__':
    __init__()
    for i in _global_dict:
        print(i)
