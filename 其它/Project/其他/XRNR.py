# coding: utf-8
import arcpy
import arcpy.da
import os
import xlwt
import xlrd

# 成果数据所在位置
# workbook = xlwt.Workbook(encoding='utf-8')
# sheet = workbook.add_sheet('name', cell_overwrite_ok=True)

layersdata = ur"E:/Space.gdb/成果数据_1"

# 创建游标遍历图层
with arcpy.da.UpdateCursor(layersdata,
                           ['LBBM', 'FXZQMC', 'TXZQMC', 'XZQMC', 'ZLLB', 'CQCS', 'ZXLON', 'ZXLAT',
                            'SUM_MJ_MU']) as cursor:
    # 创建空列表接受信息

    for row in cursor:
        if row[5] == '':
            row[5] = "无措施"
        # print(row[6])
        # print(row[7])
        # print(row[8])
        row[6] = '%.6f' % row[6]
        row[7] = '%.6f' % row[7]
        row[8] = '%.1f' % row[8]
        # print(row[6])
        # print(row[7])
        # print(row[8])
        cursor.updateRow(row)
with arcpy.da.SearchCursor(layersdata, ['LBBM', 'FXZQMC', 'TXZQMC', 'XZQMC', 'ZLLB', 'CQCS', 'ZXLON', 'ZXLAT',
                                        'SUM_MJ_MU']) as cursor1:
    data_list = []
    for row in cursor:
        data_list.append(row)
# 读取信息
workbook = xlwt.Workbook(encoding='utf-8')
sheet = workbook.add_sheet('data', cell_overwrite_ok=True)
r = 0
c = 0
title_list = ['LBBM', 'FXZQMC', 'TXZQMC', 'XZQMC', 'ZLLB', 'CQCS', 'ZXLON', 'ZXLAT', 'SUM_MJ_MU']
# 写入题头
for message in data_list:
    ws = workbook.add_sheet('地块信息', True)

    ws.write(0, 0, '附件1-1')
    # ws.write(1, 0, '安全利用类耕地调查表')
    ws.write_merge(1, 1, 0, 12, '安全利用类耕地调查表')
    ws.write(2, 0, '责任单位（盖章）：')
    ws.write(2, 4, '填表人：')
    ws.write(2, 9, '联系电话：')

    ws.write(3, 0, '责任单位负责人（签章）：')
    ws.write(3, 4, '调表日期：')
    ws.write(3, 12, '填表人：单位：亩')

    ws.write(4, 0, '地块基本信息')
    ws.write(4, 2, '地块编号')
    ws.write(4, 7, '地理位置')

    ws.write(5, 2, '中心坐标：')
    ws.write(5, 10, '面积')

    ws.write(6, 0, '调查内容')
    ws.write(6, 1, '周边环境')
    ws.write(6, 2, '2公里范围内有或曾经有工矿企业、冶炼厂')
    ws.write(6, 10, '有')
    ws.write(6, 12, '无')

    ws.write(7, 1, '2019年作物种植情况')
    ws.write(7, 2, '水稻')
    ws.write(7, 3, '主要品种')
    ws.write(7, 7, '玉米')
    ws.write(7, 8, '主要品种')
    ws.write(8, 3, '总面积')
    ws.write(8, 8, '总面积')
    ws.write(9, 2, '油菜')
    ws.write(9, 3, '主要品种')
    ws.write(9, 7, '小麦')
    ws.write(9, 8, '主要品种')
    ws.write(10, 3, '总面积')
    ws.write(10, 8, '总面积')
    ws.write(11, 2, '其他主要作物')

    ws.write(12, 1, '2020年作物种植情况')
    ws.write(12, 2, '水稻')
    ws.write(12, 3, '主要品种')
    ws.write(12, 7, '玉米')
    ws.write(12, 8, '主要品种')
    ws.write(13, 3, '总面积')
    ws.write(13, 8, '总面积')
    ws.write(14, 2, '油菜')
    ws.write(14, 3, '主要品种')
    ws.write(14, 7, '小麦')
    ws.write(14, 8, '主要品种')
    ws.write(15, 3, '总面积')
    ws.write(15, 8, '总面积')
    ws.write(16, 2, '其他主要作物')

    ws.write(17, 1, '采取措施')
    ws.write(17, 3, 'A品种调整')
    ws.write(17, 5, '面积：')
    ws.write(17, 7, 'H定向调控（土壤调理）')
    ws.write(17, 10, '面积：')

    ws.write(18, 3, 'B石灰调节')
    ws.write(18, 5, '面积：')
    ws.write(18, 7, 'I微生物修复')
    ws.write(18, 10, '面积：')

    ws.write(19, 3, 'C水分调控')
    ws.write(19, 5, '面积：')
    ws.write(19, 7, 'J植物提取')
    ws.write(19, 10, '面积：')

    ws.write(20, 3, 'D叶面调控')
    ws.write(20, 5, '面积：')
    ws.write(20, 7, 'K退耕还林还草）')
    ws.write(20, 10, '面积：')

    ws.write(21, 3, 'E秸秆还田')
    ws.write(21, 5, '面积：')
    ws.write(21, 7, 'L土地利用变更为非耕地')
    ws.write(21, 10, '面积：')

    ws.write(22, 3, 'F深翻耕')
    ws.write(22, 5, '面积：')
    ws.write(22, 7, 'M少耕免耕休耕')
    ws.write(22, 10, '面积：')

    ws.write(23, 3, 'G原位钝化')
    ws.write(23, 5, '面积：')
    ws.write(23, 7, 'N种植结构调整')
    ws.write(23, 10, '面积：')

    ws.write(24, 3, '综合治理计数（VIP或VIP+n）')

    ws.write(25, 3, '复合措施')
    ws.write(25, 6, '面积：')
    ws.write(25, 10, '面积：')

    ws.write(26, 6, '面积：')
    ws.write(26, 10, '面积：')

    ws.write(27, 2, '实施时间')
    ws.write(27, 4, '2017年')
    ws.write(27, 6, '2018年')
    ws.write(27, 8, '2019年')
    ws.write(27, 11, '2020年')

    ws.write(28, 2, '佐证台账')
    ws.write(28, 4, '图片类')
    ws.write(28, 6, '视频类')
    ws.write(28, 8, '文件方案类')
    ws.write(28, 11, '收据发票类')



    workbook.save(".xls")