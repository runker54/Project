# coding=utf-8
# coding:utf-8
import arcpy
import xlwt
import time
import os


def su_total(data_path, output_path, so_id, index):
    data = data_path  # 数据所在的路径
    row_list = []     # 收集所有信息的列表
    xz_list = []      # 收集所有乡的列表
    zu_list = []      # 收集所有组的列表
    cm_list = []      # 收集所有村的列表
    #  索引地理数据库数据
    with arcpy.da.SearchCursor(data,
                               ["LBBM", "地块编码", "XZQMC", "OwnRightNa", "承包农户名", "地块名称", "MJ_MU_QQ",
                                "TXZQMC"]) as cursor:
        for row in cursor:
            txz_qmc = row[7]
            lb_bm = row[0]
            dk_bm = row[1]
            xz_qmc = row[2]
            zm = row[3]
            cb_nh_xm = row[4]
            dk_mc = row[5]
            mjm = row[6]
            list1 = [txz_qmc, lb_bm, dk_bm, xz_qmc, zm, cb_nh_xm, dk_mc, mjm]
            row_list.append(list1)
            zu_list.append(zm)       # 组列表
            cm_list.append(xz_qmc)   # 村列表
            xz_list.append(txz_qmc)  # 乡镇列表
    cu_list = list(set(cm_list))     # 列表化集合
    bu_list = list(set(zu_list))     # 列表化集合
    pz_list = list(set(xz_list))     # 列表化集合
    x_list = [pz_list, cu_list, bu_list]  # 信息列表  用于下一个for循环索引

    for ys in x_list[so_id]:
        ys_name_list = filter(lambda x: x[index] == ys, row_list)  # 获得符合条件的内容列表
        ys_name_list = sorted(ys_name_list)
        workbook = xlwt.Workbook(encoding='utf-8')  # 新建Excel
        ws = workbook.add_sheet('Data')  # Excel新增Sheet
        style_1 = xlwt.XFStyle()  # 标题格式
        a_1 = xlwt.Alignment()
        a_1.horz = 0x02
        a_1.vert = 0x01
        a_1_font = xlwt.Font()
        a_1_font.bold = True
        a_1_font.name = u'宋体'
        a_1_font.height = 20 * 18
        style_1.font = a_1_font
        style_1.alignment = a_1
        style_1.alignment.wrap = 1

        style_2 = xlwt.XFStyle()  # 表头格式
        a_1 = xlwt.Alignment()
        a_1.horz = 0x02
        a_1.vert = 0x01
        a_1_font = xlwt.Font()
        # a_1_font.bold = True
        a_1_font.name = u'宋体'
        a_1_font.height = 20 * 12
        style_2.font = a_1_font
        style_2.alignment = a_1
        style_2.alignment.wrap = 1

        ws.write_merge(0, 0, 0, 15, '开阳县           乡（镇）农作物种植情况调查表', style_1)
        ws.write_merge(1, 1, 0, 1, '填报单位（盖章）：', style_2)
        ws.write_merge(1, 1, 5, 6, '填报人：', style_2)
        ws.write_merge(1, 1, 8, 9, '电话：', style_2)
        ws.write_merge(1, 1, 13, 14, '填报时间：', style_2)
        ws.write_merge(2, 4, 0, 0, '地块编号', style_2)
        ws.write_merge(2, 4, 1, 1, '土地确权编码', style_2)
        ws.write_merge(2, 4, 2, 2, '村', style_2)
        ws.write_merge(2, 4, 3, 3, '组', style_2)
        ws.write_merge(2, 4, 4, 4, '农户姓名', style_2)
        ws.write_merge(2, 4, 5, 5, '地块名称', style_2)
        ws.write_merge(2, 4, 6, 6, '面积（亩）', style_2)
        ws.write_merge(2, 2, 7, 15, '作物类型', style_2)
        ws.write_merge(3, 3, 7, 8, '水稻', style_2)
        ws.write_merge(3, 3, 9, 10, '玉米', style_2)
        ws.write_merge(3, 4, 11, 11, '蔬菜', style_2)
        ws.write_merge(3, 4, 12, 12, '烤烟', style_2)
        ws.write_merge(3, 4, 13, 13, '果树', style_2)
        ws.write_merge(3, 4, 14, 14, '茶叶', style_2)
        ws.write_merge(3, 4, 15, 15, '其他', style_2)
        ws.write(4, 7, '2019品种', style_2)
        ws.write(4, 8, '2020品种', style_2)
        ws.write(4, 9, '2019品种', style_2)
        ws.write(4, 10, '2020品种', style_2)
        r = 5  # 内容开始行
        for data_sys in ys_name_list:  # 写入内容
            for b in range(len(data_sys)):
                if b == 7:
                    pass
                else:
                    ws.write(r, b, data_sys[b + 1])
            r = r + 1
        ws.write_merge(0, 2, 16, 17, '总面积：', style_1)
        ws.write_merge(0, 2, 18, 22, xlwt.Formula('SUM(G6:G60000)'), style_1)
        print("%s toatle:%s done" % (ys, len(ys_name_list)))
        workbook.save('%s%s.xls' % (output_path, ys))


data_path = "E:/T开阳县台账数据.gdb/T无措施数据_确权"  # 数据所在路径
output_path = "C:/Users/Administrator/Desktop/TP/"  # 数据输出路径
so_id = 1  # 分类方法，0按乡镇分，1按村分，2按组分
index = 3  # 要素所在位置，选0对应0，选1对应3，选2对应4

su_total(data_path, output_path, so_id, index)



