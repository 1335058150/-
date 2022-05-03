"""
@Project ：安全协议分析结课——聊天室（HTTPS）Server 
@File    ：no_sqlinjection.py
@Author  ：TXL
@Date    ：2022/5/1 13:41 
"""
# -*- coding: UTF-8 -*-

def filter(word):
    key_word = ['"', 'ASCII', '%', 'open', 'system', '"', "select", "join",
                "union", "where", "insert", "delete", "update", "drop",
                "DROP", "create", "modify", "rename", "alter", "cas",
                "&", ">", "<", "&", "''", "convert", "md5",
                "passwd", "password", "../", "./", "Array", "or 1=1",
                "`set|set&set`", "--", "OR", '"', "*", "-", "+", "=",
                "-- ", " -- ", "|", "`", "//", "!=", "$", "&", "==",
                "#", "@", "CHAR", "char"
                ]
    type = True
    error = []
    for key in key_word:
        if key in word:
            type = False
            error.append(key)
    if type:
        return None
    else:
        return error