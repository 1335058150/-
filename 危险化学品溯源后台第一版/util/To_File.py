"""
@Project ：危险化学品溯源后台第一版 
@File    ：To_File.py
@Author  ：TXL
@Date    ：2022/2/6 12:16 
"""
# -*- coding: UTF-8 -*-
import os

from util import TimeNow

# 写入字符串数据于文件中
'''
这个函数的意思是写入字符串数据
    第一个参数是目标字符串
    第二个参数是目标文件路径
    第三个参数是是否需要向文件内写入时间
'''
def writefile(str__: str, filepath: str, istime: bool):
    now_time = TimeNow.getTime()
    print("Saving Information:")
    print("\t" + "[" + now_time + "]" + str__)
    with open(filepath, "a") as fp:
        if istime:
            fp.write("[" + now_time + "]" + "\n" + str__ + "\n")
        else:
            fp.write(str__ + "\n")


# readFile_line_or_all读取文件中的字符串数据
'''
这个函数的意思是读取指定文件中的目标内容
传入参数包括目标文件路径以及需要的行数
    如果传入数字为0，则返回整个文件内容
    如果非0，返回指定行的内容
'''
def read_file_line_or_all(filepath: str, num: int):
    with open(filepath, "r") as fp:
        lines = fp.readlines()
        file = fp.read()
    if num == 0:
        return file
    else:
        try:
            return lines[num]
        except:
            return "Num error"


# WriteFile_Bytes向文件内写入二进制数据
def writefile_bytes(bytes__: bytes, filepath: str):
    # 将文件路径中的单斜线转换为双斜线（其中有一个斜线是作为字符串的转义字符使用的）
    filepath = filepath.replace("\\", "\\" + "\\")
    with open(filepath, "wb+") as fp:
        # 写入二进制数据
        fp.write(bytes__)


# ReadFile_Bytes以二进制形式读取文件
def readfile_bytes(filepath: str):
    with open(filepath, "rb+") as fp:
        return fp.read()


# Choose_Newest_File选择指定目录下最新的一个文件
def choose_newest_file(dirpath: str):
    # 获取文件夹中所有的文件(名)，以列表形式返回
    file_lists = os.listdir(dirpath)
    try:
        return file_lists[-1]
    except IndexError as e:
        print("Catch Error:" + str(e))