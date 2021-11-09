#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2020-12-11
# Author:Runker54
# -----------------------
# coding:utf-8
import arcpy
import os
import re
import time
ag_adress = r'I:\0开阳县台账\开阳县台账文档导出（已整理）\开阳县台账数据库\T开阳县台账数据20201209.gdb\T开阳修改水稻玉米面积'
sd_ix = 14575.9/51101.6265
ym_ix = 37096.1/93667.1648
count_number = 0

currsor = arcpy.da.UpdateCursor(ag_adress, ['水稻20面积', '玉米20面积', '主要作物19年', '主要作物20年'])
print(currsor)
for one_row in currsor:
    if one_row[0] != 0 or one_row[1] != 0:
        sd20_update_area = one_row[0] * sd_ix
        ym20_update_area = one_row[1] * ym_ix
        one_row[2] = '果树'
        one_row[3] = '果树'
        one_row[0] = sd20_update_area
        one_row[1] = ym20_update_area
    currsor.updateRow(one_row)
    count_number += 1
print(f'更新{count_number}个！')
# print(count_number)
