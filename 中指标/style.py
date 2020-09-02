# coding:utf-8
"""
装饰器：
style 库
"""

# 处理字符串
str_lst = ['$1.123', '  $1123.454', '$899.12312']


def remove_space(str):
    """
    remove space
    """
    str_no_space = str.replace(' ', '')
    return str_no_space


print(remove_space(str_lst[1]))

import xlwt
