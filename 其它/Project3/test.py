1  # coding: 'utf-8'
# import xlwt
# import xlsxwriter
# workbook1 = xlsxwriter.workbook
# workbook = xlwt.Workbook(encoding='utf-8')
#
# ws = workbook.add_sheet('data')
#
# ws.write(0, 0, 3)
# ws.write(0, 1, 3)
# ws.write(0, 2, xlwt.Formula('SUMIF(B:B,B1,A:A)'))
# # xlwt.ExcelFormulaParser
# # xlwt.ExcelFormulaLexer
# workbook.save('pakge.xls')
# c = ''
# b = b'\xef\x82\xa3'
# e = b.decode('utf8')
# print(e)
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2020/4/17
# import os
# import xlrd
# import win32com
# from win32com.client import Dispatch
# from win32com.client import Dispatch, constants
#
# # 处理Word文档的类
# class RemoteWord:
#     def __init__(self, filename=None):
#         self.xlApp = win32com.client.Dispatch('Word.Application')  # 此处使用的是Dispatch，DispatchEx
#         self.xlApp.Visible = 0  # 后台运行，不显示
#         self.xlApp.DisplayAlerts = 0  # 不警告
#         if filename:
#             self.filename = filename
#             if os.path.exists(self.filename):
#                 self.doc = self.xlApp.Documents.Open(filename)
#             else:
#                 self.doc = self.xlApp.Documents.Add()  # 创建新的文档
#                 self.doc.SaveAs(filename)
#         else:
#             self.doc = self.xlApp.Documents.Add()
#             self.filename = ''
#
#
# def add_doc_end(self, string):
#     """在文档末尾添加内容"""
#     rangee = self.doc.Range()
#     rangee.InsertAfter('\n' + string)
#
#
# def add_doc_start(self, string):
#     """在文档开头添加内容"""
#     rangee = self.doc.Range(0, 0)
#     rangee.InsertBefore(string + '\n')
#
#
# def insert_doc(self, insertPos, string):
#     """在文档insertPos位置添加内容"""
#     ran_gee = self.doc.Range(0, insertPos)
#
#     if insertPos == 0:
#         ran_gee.InsertAfter(string)
#
#     else:
#         # ran_gee.InsertAfter('\n' + string)
#         ran_gee.InsertAfter(string)
#
#
# def replace_doc(self, string, new_string):
#     """替换文字"""
#     self.xlApp.Selection.Find.ClearFormatting()
#     self.xlApp.Selection.Find.Replacement.ClearFormatting()
#     # (string--搜索文本,
#     # True--区分大小写,
#     # True--完全匹配的单词，并非单词中的部分（全字匹配）,
#     # True--使用通配符,
#     # True--同音,
#     # True--查找单词的各种形式,
#     # True--向文档尾部搜索,
#     # 1,
#     # True--带格式的文本,
#     # new_string--替换文本,
#     # 2--替换个数（全部替换）
#     self.xlApp.Selection.Find.Execute(string, True, True, False, False, False, True, 1, True, new_string, 2)
#
#
# def replace_docs(self, string, new_string):
#     """采用通配符匹配替换"""
#     self.xlApp.Selection.Find.ClearFormatting()
#     self.xlApp.Selection.Find.Replacement.ClearFormatting()
#     self.xlApp.Selection.Find.Execute(string, False, False, True, False, False, False, 1, False, new_string, 2)
#
#
# def save(self):
#     """保存文档"""
#
#     self.doc.Save()
#
#
# def save_as(self, filename):
#     """文档另存为"""
#     self.doc.SaveAs(filename)
#
#
# def close(self):
#     """保存文件、关闭文件"""
#     # self.save()
#     self.xlApp.Documents.Close()
#     self.xlApp.Quit()
#
#
# if __name__ == '__main__':
#     path = 'C:/Users/65680/Desktop/安全利用类.docx'
#     doc = RemoteWord(path)  # 初始化一个doc对象
#     doc.Tables[0].Rows[0].Cells[0].Range.Text = '123123'
# insert_doc(doc, 466, '1')
# insert_doc(doc, 487, '2')
#
# insert_doc(doc, 505, '3')
# insert_doc(doc, 531, '4')
#
# insert_doc(doc, 549, '5')
# insert_doc(doc, 573, '6')
#
# insert_doc(doc, 591, '7')
# insert_doc(doc, 613, '8')
#
# insert_doc(doc, 631, '9')
# insert_doc(doc, 654, '9')
#
# insert_doc(doc, 672, '8')
# insert_doc(doc, 696, '8')
#
# insert_doc(doc, 747, '8')
#
# insert_doc(doc, 801, '8')
#
# insert_doc(doc, 860, '8')


# import win32com
# from win32com.client import Dispatch, constants
# #
# w = win32com.client.Dispatch('Word.Application')
# # 或者使用下面的方法，使用启动独立的进程：
# w = win32com.client.DispatchEx('Word.Application')
# #
# # # 后台运行，不显示，不警告
# # w.Visible = 0
# # w.DisplayAlerts = 0
# #
# # # 打开新的文件
# doc = w.Documents.Open( FileName = 'C:/Users/65680/Desktop/安全利用类.docx' )
# # worddoc = w.Documents.Add() # 创建新的文档
#
# # 插入文字
# myRange = doc.Range(0, 0)
# myRange.InsertBefore('Hello from Python!')

# 使用样式
# wordSel = myRange.Select()
# wordSel.Style = constants.wdStyleHeading1

# 正文文字替换
# w.Selection.Find.ClearFormatting()
# w.Selection.Find.Replacement.ClearFormatting()
# w.Selection.Find.Execute(OldStr, False, False, False, False, False, True, 1, True, NewStr, 2)

# 页眉文字替换
# w.ActiveDocument.Sections[0].Headers[0].Range.Find.ClearFormatting()
# w.ActiveDocument.Sections[0].Headers[0].Range.Find.Replacement.ClearFormatting()
# w.ActiveDocument.Sections[0].Headers[0].Range.Find.Execute(OldStr, False, False, False, False, False, True, 1, False, NewStr, 2)

# 表格操作
# C = doc.Tables
# doc.Tables[0].Rows[1].Cells[0].Range.Text ='123123'
# doc.Tables[1].Rows.Add() # 增加一行

# 转换为html
# wc = win32com.client.constants
# w.ActiveDocument.WebOptions.RelyOnCSS = 1
# w.ActiveDocument.WebOptions.OptimizeForBrowser = 1
# w.ActiveDocument.WebOptions.BrowserLevel = 0 # constants.wdBrowserLevelV4
# w.ActiveDocument.WebOptions.OrganizeInFolder = 0
# w.ActiveDocument.WebOptions.UseLongFileNames = 1
# w.ActiveDocument.WebOptions.RelyOnVML = 0
# w.ActiveDocument.WebOptions.AllowPNG = 1
# w.ActiveDocument.SaveAs( FileName = filenameout, FileFormat = wc.wdFormatHTML )

# 打印
# doc.PrintOut()

# 关闭
# doc.Close()
# w.Documents.Close(wc.wdDoNotSaveChanges)
# w.Quit()
import os
import shutil
#
# path1 = 'C:/Users/Lenovo/Desktop/KML'
# path1_list = os.listdir(path1)
# print(path1_list)
# path2 = 'C:/Users/Lenovo/Desktop/TP1'
# for roots, dirs, files in os.walk(path2):
#     for file in files:
#         b = (file[:-6])
#         length = len(b)
#         for _i in path1_list:
#             ket = _i[:length]
#             if ket == b:
#                 new_path = os.path.join(path1, _i)
#                 old_path = os.path.join(roots, _i)
#                 print("{}已完成".format(_i))
#                 shutil.copyfile(new_path, old_path)
#             else:
#                 pass
# # import os
# import win32com
# from win32com.client import DispatchEx
#
# path = "C:/Users/Lenovo/Desktop/TP2"
# for roots, dirs, files in os.walk(path):
#     for file in files:
#         if file[-3:].lower() == "xls":
#             xls_path = os.path.join(roots, file)
#             pdf_path = xls_path.replace('xls', 'pdf')
#             xlApp = DispatchEx("Excel.Application")
#             wb = xlApp.Workbooks.Open(xls_path)
#             wb.ExportAsfixedFormat(0, pdf_path)
#             xlApp.Quit()
#             print("{}已完成".format(pdf_path))

import os
import shutil

# source_path = os.path.abspath(r'C:\Users\65680\Desktop\图片2')
# target_path = os.path.abspath(r'C:\Users\65680\Desktop\test1')
#
# if not os.path.exists(target_path):
#     # 如果目标路径不存在原文件夹的话就创建
#     os.makedirs(target_path)
# if os.path.exists(source_path):
#     # 如果目标路径存在原文件夹的话就先删除
#     shutil.rmtree(target_path)
# # shutil.copytree(source_path, target_path)
# name = []
# print(len(name))



# import os
# import shutil
#
# source_path = os.path.abspath(r'C:\Users\65680\Desktop\图片2')
# target_path = os.path.abspath(r'C:\Users\65680\Desktop\test1')
# if not os.path.exists(target_path):
#     os.makedirs(target_path)
#
# if os.path.exists(source_path):
#     # root 所指的是当前正在遍历的这个文件夹的本身的地址
#     # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
#     # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
#     for root, dirs, files in os.walk(source_path):
#         for file in files:
#             src_file = os.path.join(root, file)
#             shutil.copy(src_file, target_path)
#             print(src_file)
#
# print('copy files finished!')
dict1 = {"1":8,"2":5}
print(dict1["1"])