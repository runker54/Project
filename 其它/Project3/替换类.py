#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2020/4/17
import os
import xlrd
import win32com
from win32com.client import Dispatch


# 处理Word文档的类
class RemoteWord:
    def __init__(self, filename=None):
        self.xlApp = win32com.client.Dispatch('Word.Application')  # 此处使用的是Dispatch，DispatchEx
        self.xlApp.Visible = 0  # 后台运行，不显示
        self.xlApp.DisplayAlerts = 0  # 不警告
        if filename:
            self.filename = filename
            if os.path.exists(self.filename):
                self.doc = self.xlApp.Documents.Open(filename)
            else:
                self.doc = self.xlApp.Documents.Add()  # 创建新的文档
                self.doc.SaveAs(filename)
        else:
            self.doc = self.xlApp.Documents.Add()
            self.filename = ''


def add_doc_end(self, string):
    """在文档末尾添加内容"""
    rangee = self.doc.Range()
    rangee.InsertAfter('\n' + string)


def add_doc_start(self, string):
    """在文档开头添加内容"""
    rangee = self.doc.Range(0, 0)
    rangee.InsertBefore(string + '\n')


def insert_doc(self, insertPos, string):
    """在文档insertPos位置添加内容"""
    ran_gee = self.doc.Range(0, insertPos)

    if insertPos == 0:
        ran_gee.InsertAfter(string)

    else:
        ran_gee.InsertAfter('\n' + string)


def replace_doc(self, string, new_string):
    """替换文字"""
    self.xlApp.Selection.Find.ClearFormatting()
    self.xlApp.Selection.Find.Replacement.ClearFormatting()
    # (string--搜索文本,
    # True--区分大小写,
    # True--完全匹配的单词，并非单词中的部分（全字匹配）,
    # True--使用通配符,
    # True--同音,
    # True--查找单词的各种形式,
    # True--向文档尾部搜索,
    # 1,
    # True--带格式的文本,
    # new_string--替换文本,
    # 2--替换个数（全部替换）
    self.xlApp.Selection.Find.Execute(string, True, True, False, False, False, True, 1, True, new_string, 2)


def replace_docs(self, string, new_string):
    """采用通配符匹配替换"""
    self.xlApp.Selection.Find.ClearFormatting()
    self.xlApp.Selection.Find.Replacement.ClearFormatting()
    self.xlApp.Selection.Find.Execute(string, False, False, True, False, False, False, 1, False, new_string, 2)


def save(self):
    """保存文档"""

    self.doc.Save()


def save_as(self, filename):
    """文档另存为"""
    self.doc.SaveAs(filename)


def close(self):
    """保存文件、关闭文件"""
    # self.save()
    self.xlApp.Documents.Close()
    self.xlApp.Quit()


if __name__ == '__main__':

    def tiHUan(mBan, xinXi, baoCun):
        wb = xlrd.open_workbook(xinXi)
        sheet = wb.sheet_by_index(0)
        for table_row in range(1, sheet.nrows):
            path = mBan
            doc = RemoteWord(path)  # 初始化一个doc对象
            for table_col in range(0, sheet.ncols):
                replace_doc(doc, str(sheet.cell_value(0, table_col)), str(sheet.cell_value(table_row, table_col)))

            save_as(doc, "%s%s%s统计信息.docx" % (baoCun,
                                              str(sheet.cell_value(table_row, 0)), str(sheet.cell_value(table_row, 5))))
            if table_row == sheet.nrows - 1:
                close(doc)


    mBan_wei = 'D:/rogram Files/MB/安全利用类.docx'  # 模板存放位置
    xxb = 'C:/Users/Administrator/Desktop/NY/安全利用类.xls'  # 信息表存放位置
    bc = 'C:/Users/Administrator/Desktop/sheel/'  # 文件输出位置
    tiHUan(mBan_wei, xxb, bc)
