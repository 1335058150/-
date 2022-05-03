"""
@Project ：安全协议分析结课——聊天室（HTTPS）Server
@File    ：room.py
@Author  ：TXL
@Date    ：2022/5/1 13:05 
"""
# -*- coding: UTF-8 -*-
import time

from dao import insert
from util import random_string


class chatting_room:
    def __init__(self, create_guy, create_guy_id, passwd=None, room_text="None text"):
        self.id = str(time.time() / 1000)[0:5] + random_string.random_str()
        self.text = room_text
        self.guy_num = 1
        self.guy = []
        self.guys = {
            create_guy: {
                "id": create_guy_id,
                "name": create_guy,
            }
        }
        insert.insert_sql_([self.id, room_text, passwd, create_guy_id])
        self.passwd = passwd
        self.c_time = time.time()
        self.running = True

    def destroy(self):
        self.running = False
        insert.update_sql("room", ["status", "0", self.id])

    def getguy(self, userid):
        self.guy_num += 1
        self.guy.append(userid)

    def outguy(self, userid):
        self.guy.remove(userid)
        self.guy_num -= 1
