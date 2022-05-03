"""
@Project ：安全协议分析结课——聊天室（HTTPS）Server 
@File    ：select.py
@Author  ：TXL
@Date    ：2022/5/1 14:48 
"""
# -*- coding: UTF-8 -*-

from dao import connect_mysql
from dao.no_sqlinjection import filter
from util.alert import alert

"""
DEMO:
# select(table_name="guys",target=["*"],value="a")
##### (('a', '123', 'as'),)
# select(table_name="guys",target=["guy_name","passwd_md5"],value="a")
##### (('123', 'as'),)
"""


def select(target: list, table_name: str, value: str, a=1, passwd=None):
    # select `guy_id`,`guy_name`,`passwd_md5` from guys where guy_id='';
    """
    :param passwd: 密码的md5
    :param a: a为1则代表根据ID查找，2则则根据用户名查找，3则根据用户名密码进行查找（仅针对guys表有用）
    :param table_name: 查看的表名，字符串格式
    :param target: 内容是查看的列明，内容可以为['*'],格式是个列表
    :param value: 需要查看的对象的ID，字符串格式
    :return:
    """
    if filter(value) is not None:
        error = filter(value)
        alert(errormsg="No SQLinjections!!\nNo words", Options=filter(value))
        return False
    sql_ = "_id='" + value + "';"
    if target[0] == "*":
        sql = "SELECT * FROM " + table_name + " WHERE "
    else:
        sql = "SELECT "
        i = 0
        for column in target:
            sql += ("`" + column + "`")
            if i + 1 < len(target):
                sql += ","
                i += 1
            else:
                break
        sql += " FROM " + table_name + " WHERE "
    if table_name == "guys":
        if a == 1:
            sql = sql + "guy" + sql_
        elif a == 2:
            sql = sql + "guy_name='" + value + "';"
        else:
            sql = sql + "guy_name='" + value + "' and `passwd_md5`='" + passwd + "'"
    elif table_name == "room":
        sql = sql + "room" + sql_
    else:
        alert("Select SQL Error")
        return False
    # print(sql)

    ###################
    # Begin Running SQL
    ###################
    conn = connect_mysql.connect()
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        conn.commit()
        conn.close()

        return data
    except Exception as e:
        print('error occured on select' + sql)
        alert("SQL ERROR,NOT SELECT", Options=e)
        conn.close()
        conn.rollback()


if __name__ == '__main__':
    #     pass
    #     print(select(table_name="guys",target=["*"],value="a"))
    #     print(select(table_name="guys", target=["*"], value="123", a=2))
    print((select(table_name="guys", target=["*"], value="123", a=3, passwd="as")))
