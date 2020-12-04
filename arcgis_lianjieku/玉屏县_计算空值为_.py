# -*- coding: utf-8 -*-#
# -----------------------
# Date:2020-11-28
# -----------------------
import arcpy
import time

file_data = r'C:\Users\65680\Desktop\玉屏县\T玉屏县台账数据.gdb\评价单元对应农用地图层_无机5综合_52_Project_SD'

with arcpy.da.UpdateCursor(file_data, ['LBBM', '玉米19年', '玉米20年', '水稻19年', '水稻20年',
                                       '主要作物19年', '主要作物20年', '周边环境',
                                       '玉米19年面积', '玉米20年面积', '水稻19年面积', '水稻20年面积', 'CQCS']) as cursor:
    # 计数
    count = 0  # 更新数量
    for one_change in cursor:
        for index_ in [1, 2, 3, 4, 5, 6]:
            if one_change[index_] is None:
                one_change[index_] = ''
            else:
                print('跳')
        cursor.updateRow(one_change)
        count += 1

    print(f"成功{count}个")
