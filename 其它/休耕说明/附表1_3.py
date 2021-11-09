#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2020-12-09
# Author:Runker54
# -----------------------
import xlrd
import xlwt
import re
import time
import os

read_sheet = r'C:\Users\65680\Desktop\织金基础数据_原始.xls'
out_path = r'C:\Users\65680\Desktop\put'
read_book = xlrd.open_workbook(read_sheet)
read_cell = read_book.sheet_by_index(0)
ws_book = xlwt.Workbook('utf-8')
ws_sheet = ws_book.add_sheet('DATA')
r = 0
index_number = 1
for one_row in range(1, read_cell.nrows):
    ws_sheet.write(r, 0, read_cell.row(one_row)[2].value)  # 写入乡镇
    ws_sheet.write(r, 1, index_number)  # 写入序号
    ws_sheet.write(r, 2, '')  # 写入页码
    ws_sheet.write(r, 3, read_cell.row(one_row)[0].value)  # 写入地块编码
    ws_sheet.write(r, 4, read_cell.row(one_row)[35].value)  # 写入周边环境
    ws_sheet.write(r, 5, read_cell.row(one_row)[26].value)  # 写入地块面积
    ws_sheet.write(r, 6, read_cell.row(one_row)[30].value)  # 写入2020水稻
    ws_sheet.write(r, 7, read_cell.row(one_row)[34].value)  # 写入2020玉米
    ws_sheet.write(r, 8, '')  # 写入2020油菜
    ws_sheet.write(r, 9, '')  # 写入2020小麦

    ws_sheet.write(r, 10, read_cell.row(one_row)[26].value - read_cell.row(one_row)[30].value - read_cell.row(one_row)[
        34].value - read_cell.row(one_row)[18].value - read_cell.row(one_row)[20].value - read_cell.row(one_row)[
                       19].value)  # 写入2020其它

    # ws_sheet.write(r, 11, 0)  # 写入2020小计
    ws_sheet.write(r, 11, xlwt.Formula('SUM(G%s:K%s)' % (r+1, r+1)))  # 写入2020小计
    if read_cell.row(one_row)[6].value == '安全利用类':
        ws_sheet.write(r, 12, read_cell.row(one_row)[14].value)  # 写入优化施肥 安全利用类
        ws_sheet.write(r, 13, read_cell.row(one_row)[7].value)  # 写入品种调整 2
        ws_sheet.write(r, 14, read_cell.row(one_row)[10].value)  # 写入叶面调控
        ws_sheet.write(r, 15, read_cell.row(one_row)[12].value)  # 写入深翻耕
        ws_sheet.write(r, 16, read_cell.row(one_row)[9].value)  # 写入水分调控
        ws_sheet.write(r, 17, read_cell.row(one_row)[11].value)  # 写入秸秆还田
        ws_sheet.write(r, 18, read_cell.row(one_row)[8].value)  # 写入石灰调节
        ws_sheet.write(r, 19, xlwt.Formula('SUM(M%s:S%s)' % (r+1, r+1)))  # 写入 小计
        ws_sheet.write(r, 20, read_cell.row(one_row)[13].value)  # 写入 原位钝化
        ws_sheet.write(r, 21, read_cell.row(one_row)[15].value)  # 写入 定向调控
        ws_sheet.write(r, 22, xlwt.Formula('SUM(U%s:V%s)' % (r+1, r+1)))  # 写入 小计
        ws_sheet.write(r, 23, read_cell.row(one_row)[16].value)  # 写入 微生物修复
        ws_sheet.write(r, 24, read_cell.row(one_row)[17].value)  # 写入 植物提取
        ws_sheet.write(r, 25, xlwt.Formula('SUM(X%s:Y%s)' % (r+1, r+1)))  # 写入 小计
        ws_sheet.write(r, 26, '')  # 写入 VIP
        ws_sheet.write(r, 27, read_cell.row(one_row)[19].value)  # 写入  耕地利用变更为非农用地
        ws_sheet.write(r, 28, read_cell.row(one_row)[20].value)  # 写入  少耕免耕休耕
        ws_sheet.write(r, 29, read_cell.row(one_row)[21].value)  # 写入  种植结构调整
        ws_sheet.write(r, 30, read_cell.row(one_row)[18].value)  # 写入  退耕还林还草
        ws_sheet.write(r, 31, xlwt.Formula('SUM(AB%s:AE%s)' % (r+1, r+1)))  # 写入 小计
    if read_cell.row(one_row)[6].value == '严格管控类':
        ws_sheet.write(r, 32, read_cell.row(one_row)[21].value)  # 写入  种植结构调整
        ws_sheet.write(r, 33, '')  # 写入  特定农产品划定区
        ws_sheet.write(r, 34, read_cell.row(one_row)[18].value)  # 写入  退耕还林还草
        ws_sheet.write(r, 35, read_cell.row(one_row)[20].value)  # 写入  休耕
        ws_sheet.write(r, 36, read_cell.row(one_row)[19].value)  # 写入  耕地利用变更为非农用地
        ws_sheet.write(r, 37, read_cell.row(one_row)[26].value - read_cell.row(one_row)[19].value
                       - read_cell.row(one_row)[18].value - read_cell.row(one_row)[20].value -
                       read_cell.row(one_row)[21].value)  # 写入  其它措施

        ws_sheet.write(r, 38, xlwt.Formula('SUM(AG%s:AL%s)' % (r+1, r+1)))  # 写入  小计
    index_number += 1
    r += 1
ws_book.save(os.path.join(out_path, '织金县附表.xls'))
