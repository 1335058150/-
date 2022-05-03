"""
@Project ：安全协议分析结课——聊天室（HTTPS）Server 
@File    ：guy.py
@Author  ：TXL
@Date    ：2022/5/1 13:30 
"""
# -*- coding: UTF-8 -*-
import time

from dao import insert, select
from util import random_string
from util.alert import alert


class guy:
    def __init__(self, name: str, type__=False, passwd=None, register=False, ip="0.0.0.0", ):
        """
        :param name: 不得为空，代表用户名
        :param type__: register为True的情况下有效，注册时，为False则仅仅存于内存中，退出后自动销户
        :param passwd: 密码，用于验证身份，游客登陆则不需要
        :param ip: 登录的IP
        :param register: 默认为False，注册情况下和游客登陆时应设置为True
        """
        self.ip = ip
        self.room = []
        if register:
            self.id = random_string.random_str() + str(time.time() / 1000)[0:5]
            if type__:
                # 注册并长期存储用户数据
                if passwd is None:
                    alert("Passwd should not be None")
                else:
                    insert.insert_sql("guys", [self.id, name, passwd])
                    self.name = name
                    self.login = True
            else:
                # 游客登陆成功
                self.name = name
                self.login = True
        else:
            login_status = self.checklogin(name=name, passwd=passwd)
            if login_status:
                self.name = name
                self.login = True
                self.id = select.select(table_name="guys", target=["guy_id"], a=2, passwd=passwd, value=name)[0][0]
            else:
                self.login = False
                alert("Login Error")

    def goinroom(self, roomid):
        """
        加入房间
        :param roomid:
        :return:
        """
        self.room = roomid

    def quitroom(self):
        """
        退出房间
        :param roomid:
        :return:
        """
        self.room = None

    @staticmethod
    def checklogin(name, passwd):
        """
        检查用户名密码用于登录的话是否正确
        :param name:
        :param passwd:
        :return:
        """
        if len(select.select(table_name="guys", target=["*"], value=name, a=3, passwd=passwd)) > 0:
            return True
        else:
            return False
