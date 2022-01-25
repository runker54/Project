#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2022-01-09
# Author:Runker54
# ----------------------
import MySQLdb
import openpyxl
import time
import os
import random

ch_path = r"C:\Users\65680\Desktop\地址列表文件\delte.xlsx"  # 需更删除的表
ch_wb = openpyxl.load_workbook(ch_path)
chws = ch_wb["Sheet"]
chrows = chws.max_row
host = "rm-wz9clu23kp2cn4lpzbo.mysql.rds.aliyuncs.com"
user = "gdscza"
passwd = "gdsczaGDSCZAcystCYST123!@#"
dbases = "db_gdscza"
charset = "UTF8"
port = 33006
db1 = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=dbases, charset=charset)
ncol = 0
for one_row in range(1, chrows + 1):
    currsor1 = db1.cursor()
    point_id = chws[f"A{one_row}"].value
    business = str(point_id)[str(point_id).rfind("_") + 1:]

    print(point_id, business)
    sql_calc_url_variety = "DELETE FROM db_gdscza.sys_file " \
                           "WHERE id = '%s' " \
                           "AND business_type ='variety'" % point_id

    sql_calc_url_other = "DELETE FROM db_gdscza.sys_file " \
                         "WHERE id = '%s' " \
                         "AND business_type ='other'" % point_id

    if business == "other":
        currsor1.execute(sql_calc_url_other)
    if business == "variety":
        currsor1.execute(sql_calc_url_variety)
    currsor1.close()
    db1.commit()
    ncol += 1
    print(f"已删除{ncol}条记录")

db1.close()
