"""
@Project ：安全协议分析结课——聊天室（HTTPS）Server 
@File    ：insert.py
@Author  ：TXL
@Date    ：2022/5/1 13:40 
"""
# -*- coding: UTF-8 -*-
"""
##########################
# 在此处添加注释对使用方法进行注解：
#     三个函数第一个参数均为字符串，表示需要处理的表名
# insert_sql("guys",["as","bs","cs"])
# # 后边的三个参数分别代表：人/房间ID，人的姓名/房间宣传语，人/房间的密码
# insert_sql_(["aa","bb","cc","dd"])
# # 创建房间用的，依次代表房间ID、房间宣传语、房间密码、创建人ID
# update_sql("guys",["guy_name","123","a"])
# # 后边的三个参数分别代表：处理的列名（只允许一个），处理后的内容，处理的对应内容的ID（一般不允许修改ID）
# delete_sql("guys",["as"])
# # 后边的一个参数代表需要删除的对象的ID
##########################
"""

from dao import connect_mysql
from dao.no_sqlinjection import filter
from util.alert import alert


def insert_sql(table_name, value):
    for i in value:
        if filter(i) is None:
            continue
        else:
            alert(errormsg="No SQLinjections!!\nNo words", Options=filter(i))
            return False
    if table_name == "guys":
        sql = "INSERT INTO " + table_name + "(`guy_id`,`guy_name`,`passwd_md5`) VALUES ('" + value[0] + "','" + value[
            1] + "','" + value[2] + "');"
    elif table_name == "room":
        sql = "INSERT INTO " + table_name + "(`room_id`,`room_text`,`passwd`,`rem`) VALUES ('" + value[0] + "','" + \
              value[1] + "','" + value[2] + "','begin!');"
    else:
        alert("Insert SQL Error")
        return False
    run(sql)

def insert_sql_(value):
    for i in value:
        if filter(i) is None:
            continue
        else:
            alert(errormsg="No SQLinjections!!\nNo words", Options=filter(i))
            return False
    sql = "INSERT INTO room (`room_id`,`room_text`,`passwd`,`creater`) VALUES ('" + value[0] + "','" + value[1] + "','" + value[2] + "','" + value[3] + "')"
    # print(sql)
    run(sql)

def delete_sql(table_name, value):
    for i in value:
        if filter(i) is None:
            continue
        else:
            alert(errormsg="No SQLinjections!!\nNo words", Options=filter(i))
            return False
    if table_name == "guys":
        sql = "DELETE FROM " + table_name + " WHERE `guy_id`='" + value[0] + "';"
    elif table_name == "room":
        sql = "DELETE FROM " + table_name + " WHERE `room_id`='" + value[0] + "';"
    else:
        alert("Delete SQL Error")
        return False
    run(sql)


def update_sql(table_name, value):
    for i in value:
        if filter(i) is None:
            continue
        else:
            alert(errormsg="No SQLinjections!!\nNo words", Options=filter(i))
            return False
    if table_name == "guys":
        sql = "UPDATE " + table_name + " SET `" + value[0] + "`='" + value[1] + "' WHERE `guy_id`='" + value[2] + "';"
    elif table_name == "room":
        sql = "UPDATE" + table_name + " SET `" + value[0] + "`='" + value[1] + "' WHERE `room_id`='" + value[2] + "';"
    else:
        alert("Update SQL Error")
        return False
    run(sql)


def run(sql):
    conn = connect_mysql.connect()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
        conn.commit()
    except Exception as e:
        alert("SQL ERROR,NOT SELECT", Options=e)
        conn.close()
