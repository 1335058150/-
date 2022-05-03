"""
@Project ：安全协议分析结课——聊天室（HTTPS）Server
@File    ：main.py
@Author  ：TXL
@Date    ：2022/5/1 13:02 
"""
# -*- coding: UTF-8 -*-
from socket import *
import threading

from bean.room import chatting_room
from bean.guy import guy
from dao import insert, select
from util.time_now import gettime
from util.alert import alert

tcp_server_socket = socket(AF_INET, SOCK_STREAM)
address = ('', 8899)
tcp_server_socket.bind(address)
tcp_server_socket.listen(128)
online_guys = {}
running_rooms = {}


def register(string: list):
    if len(string) != 3:
        alert("Demo Wrong!!--Register")
        return None
    new_name = string[1]
    passwd_md5 = string[2]
    if passwd_md5 == "1":
        # 游客临时注册并登录
        new_guy = guy(name=new_name, register=True, type__=False, ip=client_add[0])
    else:
        # 长期注册并立即登录
        new_guy = guy(name=new_name, register=True, type__=True, passwd=passwd_md5, ip=client_add[0])
    if new_guy.login:
        online_guys[new_guy.id] = new_guy
        return True, new_guy.id
    else:
        return False, 1


def login(string: list):
    if len(string) != 3:
        alert("Demo Wrong!!--Login")
        return None
    name = string[1]
    passwd_md5 = string[2]
    new_guy = guy(name=name, ip=client_add[0], passwd=passwd_md5)
    if new_guy.login:
        online_guys[new_guy.id] = new_guy
        return True, new_guy.id
    else:
        return False, 1


def attach_room(string: list):
    if len(string) != 4:
        alert("Demo Wrong!!--Attach room")
        return None
    userid = string[1]
    room_id = string[2]
    room_passwd = string[3]
    if userid not in online_guys:
        # 请先登录
        return 1
    if room_id not in running_rooms:
        # 房间不存在
        return 2
    if room_passwd != running_rooms[room_id].passwd:
        # 房间密码错误
        return 3
    online_guys[userid].goinroom(room_id)
    running_rooms[room_id].getguy(userid)
    return 4


def send_msg(string: list):
    if len(string) != 4:
        alert("Demo Wrong!!--Sending msg")
        return None
    userid = string[1]
    username = select.select(a=1, table_name="guys", target=["guy_name"], value=userid)[0][0]
    room_id = string[2]
    msg = string[3]
    if userid not in online_guys:
        # 请先登录
        return 1
    if room_id not in running_rooms:
        # 房间不存在
        return 2
    # 没有问题，直接发送
    msg_update(userid, username, room_id, msg, client_add[0], client_add[1])
    return 3



def create_room(string: list):
    if len(string) != 5:
        alert("Demo Wrong!!--Create room")
        return None
    if string[1] not in online_guys:
        return 1
    new_room = chatting_room(create_guy=string[2], create_guy_id=string[1], passwd=string[4], room_text=string[3])
    if new_room.running:
        running_rooms[new_room.id] = new_room
        return True, new_room.id
    else:
        return False, 1


def keep_alive():
    pass


def msg_update(userid:str, username:str, roomid:str, msg:str, target_ip, target_port):
    pass


def receieve():
    recv_data = client_socket.recv(10240)
    keyword = recv_data.decode('utf-8')
    outprint = "\033[32m[" + gettime() + "]\033[0m" + "\033[33m[" + client_add[0] + ":" + str(
        client_add[1]) + "]\033[0m" + "Received information : ** \033[34m" + keyword + "\033[0m **"
    print(outprint)
    log_("[" + gettime() + "][" + client_add[0] + ":" + str(client_add[1]) + "]Received information : ** " + keyword + " **\n")

    # 回送的消息
    returned = "Copy that"

    # 注册
    if keyword[0] == "1":
        register_ = register(keyword.split("|"))
        if register_ is None:
            returned = "500 Server Error"
        else:
            if register_[0]:
                returned = register_[1]
            else:
                returned = "Register Error"
    # 登录
    elif keyword[0] == "2":
        login_ = login(keyword.split("|"))
        if login_ is None:
            returned = "500 Server Error"
        else:
            if login_[0]:
                returned = login_[1]
            else:
                returned = "Login Error"
    # 加入房间
    elif keyword[0] == "3":
        attach_ = attach_room(keyword.split("|"))
        if attach_ is None:
            returned = "500 Server Error"
        else:
            if attach_ == 1:
                # 请先登录
                returned = "Warning!Please Login First"
            elif attach_ == 2:
                # 房间号不存在
                returned = "Sorry,the room id is not existed."
            elif attach_ == 3:
                # 房间密码错误
                returned = "Sorry,the room password is not correct."
            elif attach_ == 4:
                # 登陆成功
                returned = "Attach Successfully!"
    # 发送信息
    elif keyword[0] == "4":
        send_ = send_msg(keyword.split("|"))
        if send_ is None:
            returned = "500 Server Error"
        else:
            if send_ == 1:
                # 请先登录
                returned = "Warning!Please Login First"
            elif send_ == 2:
                # 房间号不存在
                returned = "Sorry,the room id is not existed."

    # 创建房间
    elif keyword[0] == "5":
        create_ = create_room(keyword.split("|"))
        if create_ is None:
            returned = "500 Server Error"
        else:
            if create_ == 1:
                returned = "Warning:Please Login first"
            elif create_[0]:
                returned = create_[1]
            else:
                returned = "Create room Error"

    client_socket.send(returned.encode("utf-8"))
    outprint = "\033[33m[" + gettime() + "]\033[0m" + "\033[32m[" + client_add[0] + ":" + str(client_add[1]) + "]\033[0m" + "Returned information : ** \033[34m" + returned + "\033[0m **"
    print(outprint)
    log_("[" + gettime() + "][" + client_add[0] + ":" + str(
        client_add[1]) + "]Returned information : ** " + returned + " **\n")
    client_socket.close()


def log_(loging: str):
    with open("log/log.log", "a") as file:
        file.write(loging)


if __name__ == '__main__':
    """
    接下来需要的设计：
    Client也分出线程开启监听功能，并且Server端不时发送心跳包检查其状态
    login后的guy类还需要添加对应的端口功能用来方便Server端实时发包
    Server端需要集中管理公钥信息
    """
    print("\033[32m[" + gettime() + "]\033[0m" + "Server Listening")
    log_("*********************\n[" + gettime() + "]  Server Listening\n")
    while True:
        client_socket, client_add = tcp_server_socket.accept()
        # 首先第一步，接收客户端发来的信息与指令并单独设计线程为其进行处理
        threading.Thread(target=receieve())
