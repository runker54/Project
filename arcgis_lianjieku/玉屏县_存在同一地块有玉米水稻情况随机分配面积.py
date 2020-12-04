# -*- coding: utf-8 -*-#
# -----------------------
# Date:2020-11-28
# -----------------------
import arcpy
import time
import random

file_data = r'C:\Users\65680\Desktop\玉屏县\T玉屏县台账数据.gdb\评价单元对应农用地图层_无机5综合_52_Project_SD_消除后1128'

with arcpy.da.UpdateCursor(file_data,
                           ['CQCS', '玉米19年', '玉米20年', '水稻19年', '水稻20年',
                            '玉米19年面积', '玉米20年面积', '水稻19年面积', '水稻20年面积', 'MJ_MU']) as cursor:
    # 计数
    count = 0  # 更新数量
    for one_change in cursor:
        if one_change[0] != '':
            for leibie_ in [1, 2]:
                ran_number = random.random()  # 生成0-1的随机数
                if one_change[leibie_] != '' and one_change[leibie_+2] != '':   # 19 or 20年同时存在水稻玉米
                    one_change[leibie_+4] = one_change[9]*ran_number
                    one_change[leibie_+6] = one_change[9]*(1-ran_number)
                else:
                    if one_change[leibie_] == '':
                        one_change[leibie_+4] = 0
                    else:
                        one_change[leibie_+4] = one_change[9]

                    if one_change[leibie_+2] == '':
                        one_change[leibie_ + 6] = 0
                    else:
                        one_change[leibie_+6] = one_change[9]
            cursor.updateRow(one_change)
            count += 1
        else:
            pass
    print(f"成功{count}个")
