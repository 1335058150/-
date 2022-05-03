"""
@Project ：安全协议分析结课——聊天室（HTTPS）Server 
@File    ：test client.py
@Author  ：TXL
@Date    ：2022/5/2 9:52 
"""
# -*- coding: UTF-8 -*-
'''
TCP相较于UDP的一大特点就是TCP可以在连接前创建链接从而使得数据更加的稳定
'''

from socket import *

# 创建套接字
tcp_client_socket=socket(AF_INET,SOCK_STREAM)

# 目的信息
serve_ip="127.0.0.1"
serve_port=8899

# 连接服务器
tcp_client_socket.connect((serve_ip,serve_port))

# 用户输入发送的信息
send_data=input('请输入您要发送的信息')

tcp_client_socket.send(send_data.encode('gbk'))

# 接受对方发来的数据，最大为1024字符
recv_data=tcp_client_socket.recv(1024)
print('接收到的数据为：',recv_data.decode('gbk'))

# 关闭套接字
tcp_client_socket.close()

