# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Author:       A
# Date:         2020-09-13
# -------------------------------------------------------------------------------
import arcpy
import xlwt
import os
import sys

defaultencoding = 'utf-8'

if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

data_path = r"F:\代胜芳\王贵赫章导出村级表_盖章.gdb\赫章县全_Identity_含水稻玉米"  # 数据所在路径
output_path = r"C:\Users\65680\Desktop\HZX"  # 数据输出路径
so_id = 1  # 分类方法，0按乡镇分，1按村分，2按组分
index = 2  # 要素所在位置，选0对应0，选1对应3，选2对应4


def set_excel_title(ws, xz):
    borders = xlwt.Borders()  # 为样式创建边框
    # DASHED虚线 NO_LINE没有 THIN实线
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    # style = xlwt.XFStyle()  # 初始化样式
    style_4 = xlwt.easyxf()  # 初始化样式
    a_1 = xlwt.Alignment()
    a_1.horz = 0x02
    a_1.vert = 0x01
    a_1_font = xlwt.Font()
    # a_1_font.bold = True
    a_1_font.name = u'宋体'
    a_1_font.height = 20 * 10
    style_4.font = a_1_font
    style_4.alignment = a_1
    style_4.borders = borders
    style_4.alignment.wrap = 1
    style_4.borders = borders

    style_1 = xlwt.XFStyle()  # 标题格式
    a_1 = xlwt.Alignment()
    a_1.horz = 0x02
    a_1.vert = 0x01
    a_1_font = xlwt.Font()
    a_1_font.bold = True
    a_1_font.name = u'宋体'
    a_1_font.height = 20 * 14
    style_1.font = a_1_font
    style_1.alignment = a_1
    style_1.alignment.wrap = 1

    style_3 = xlwt.XFStyle()  # 表头格式
    a_1 = xlwt.Alignment()
    a_1.horz = 0x02
    a_1.vert = 0x01
    a_1_font = xlwt.Font()
    # a_1_font.bold = True
    a_1_font.name = u'宋体'
    a_1_font.height = 20 * 10
    style_3.font = a_1_font
    style_3.alignment = a_1
    style_3.alignment.wrap = 1

    style_2 = xlwt.XFStyle()  # 表头格式
    borders = xlwt.Borders()  # 为样式创建边框
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    a_1 = xlwt.Alignment()
    a_1.horz = 0x02
    a_1.vert = 0x01
    a_1_font = xlwt.Font()
    # a_1_font.bold = True
    a_1_font.name = u'宋体'
    a_1_font.height = 20 * 10
    style_2.font = a_1_font
    style_2.alignment = a_1
    style_2.borders = borders
    style_2.alignment.wrap = 1

    ws.write_merge(0, 0, 0, 13, '赫章县%s耕地种植情况调查表' % xz, style_1)
    ws.write_merge(1, 1, 0, 1, '填报单位（盖章）：', style_3)
    ws.write_merge(1, 1, 3, 4, '填报人：', style_3)
    ws.write_merge(1, 1, 6, 7, '电话：', style_3)
    ws.write_merge(1, 1, 10, 11, '填报时间：', style_3)
    ws.write_merge(2, 4, 0, 0, '序号', style_2)
    ws.write_merge(2, 4, 1, 1, '地块编号', style_2)
    ws.write_merge(2, 4, 2, 2, '村', style_2)
    ws.write_merge(2, 4, 3, 3, '农户姓名', style_2)
    ws.write_merge(2, 4, 4, 4, '地块名称', style_2)
    ws.write_merge(2, 4, 5, 5, '面积m2', style_2)
    ws.write_merge(2, 2, 6, 7, '2019年', style_2)
    ws.write_merge(2, 2, 8, 9, '2020年', style_2)

    ws.write_merge(3, 4, 6, 6, '水稻19', style_2)
    ws.write_merge(3, 4, 7, 7, '水稻20', style_2)
    ws.write_merge(3, 4, 8, 8, '玉米19', style_2)
    ws.write_merge(3, 4, 9, 9, '玉米20', style_2)
    ws.write_merge(2, 4, 10, 10, '主要作物19', style_2)
    ws.write_merge(2, 4, 11, 11, '主要作物20', style_2)
    ws.write_merge(2, 4, 12, 12, '周边环境', style_2)
    ws.write_merge(2, 4, 13, 13, '备注', style_2)
    ws.col(0).width = 256 * 6
    ws.col(1).width = 256 * 22
    ws.col(2).width = 256 * 8
    ws.col(3).width = 256 * 10
    ws.col(4).width = 256 * 10
    ws.col(5).width = 256 * 6
    ws.col(6).width = 256 * 10
    ws.col(7).width = 256 * 10
    ws.col(8).width = 256 * 10
    ws.col(9).width = 256 * 10
    ws.col(10).width = 256 * 12
    ws.col(11).width = 256 * 12
    ws.col(12).width = 256 * 6
    ws.col(13).width = 256 * 8
    ws.row(2).set_style(xlwt.easyxf('font:height 320;'))


def su_total(data_path, output_path, so_id, index):
    data = data_path  # 数据所在的路径
    row_list = []  # 收集所有信息的列表
    xz_list = []  # 收集所有乡的列表
    zu_list = []  # 收集所有组的列表
    cm_list = []  # 收集所有村的列表
    #  索引地理数据库数据
    cursor = arcpy.da.SearchCursor(data,
                                   ["BSBM2", "TXZQMC", "XZQMC", "ZJRXM", "DKMC", "MJ_MU", "水稻19年", "水稻20年", "玉米19年",
                                    "玉米20年", "主要作物19年", "主要作物20年", "周边环境"])
    for row in cursor:
        txz_qmc = row[1]
        bs_bm = row[0]
        xz_qmc = row[1] + row[2]
        cb_nh_xm = row[3]
        dk_mc = row[4]
        mjm2 = round(row[5], 1)
        sd19 = row[6]
        sd20 = row[7]
        ym19 = row[8]
        ym20 = row[9]
        zy19 = row[10]
        zy20 = row[11]
        zbhj = row[12]
        list1 = [txz_qmc, bs_bm, xz_qmc, cb_nh_xm, dk_mc, mjm2, sd19, sd20, ym19, ym20, zy19, zy20, zbhj]
        row_list.append(list1)
        cm_list.append(xz_qmc)  # 村列表
        xz_list.append(txz_qmc)  # 乡镇列表
    cu_list = list(set(cm_list))  # 列表化集合
    pz_list = list(set(xz_list))  # 列表化集合
    x_list = [pz_list, cu_list]  # 信息列表  用于下一个for循环索引

    for ys in x_list[so_id]:  # ys 默认为村名
        print(ys)
        ys_name_list = filter(lambda x: x[index] == ys, row_list)  # 获得符合条件的内容列表  获得所有同一村排列的列表
        ys_name_list = sorted(ys_name_list, reverse=True)  # 通过地块编码排序
        xz = ys_name_list[0][0]
        cz = ys_name_list[0][2]
        cz = cz[len(xz):]
        xzpath = os.path.join(output_path, xz)
        if os.path.isdir(xzpath):
            pass
        else:
            os.mkdir(xzpath)
        czpath = os.path.join(xzpath, cz)
        if os.path.isdir(czpath):
            pass
        else:
            os.mkdir(czpath)
        r = 5
        nb = 1
        workbook_1 = xlwt.Workbook(encoding='utf-8')  # 新建Excel
        ws = workbook_1.add_sheet('%s' % ys)  # Excel新增Sheet
        borders = xlwt.Borders()  # 为样式创建边框
        borders.left = xlwt.Borders.THIN
        borders.right = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN
        style_4 = xlwt.easyxf()  # 初始化样式
        a_1 = xlwt.Alignment()
        a_1.horz = 0x02
        a_1.vert = 0x01
        a_1_font = xlwt.Font()
        a_1_font.name = u'宋体'
        a_1_font.height = 20 * 10
        style_4.font = a_1_font
        style_4.alignment = a_1
        style_4.borders = borders
        style_4.alignment.wrap = 1
        style_4.borders = borders
        set_excel_title(ws, xz+cz)
        ws.row(r).set_style(xlwt.easyxf('font:height 280;'))  # 设置行高
        for data_sys1 in ys_name_list:
            data_sys1[2] = data_sys1[2][len(data_sys1[0]):]
            ws.write(r, 0, nb, style_4)
            ws.write(r, 13, "", style_4)

            for b in range(1, len(data_sys1)):
                ws.write(r, b, data_sys1[b], style_4)
            r += 1
            nb += 1
        style_5 = xlwt.XFStyle()  # 面积格式
        a_1 = xlwt.Alignment()
        a_1_font = xlwt.Font()
        a_1_font.bold = True
        a_1_font.name = u'宋体'
        a_1_font.height = 20 * 10
        style_5.font = a_1_font
        style_5.alignment = a_1
        style_5.alignment.wrap = 1

        ws.write_merge(len(ys_name_list) + 5, len(ys_name_list) + 5, 0, 1, '面积合计：', style_5)
        ws.write_merge(len(ys_name_list) + 5, len(ys_name_list) + 5, 4, 5, xlwt.Formula('SUM(F6:F%s)' % (len(ys_name_list) + 5)), style_5)

        print("%s toatle:%s done" % (ys, len(ys_name_list)))
        workbook_1.save('%s/%s调查表.xls' % (czpath, cz))


def main():
    su_total(data_path, output_path, so_id, index)


if __name__ == '__main__':
    main()
