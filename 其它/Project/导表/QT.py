# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Author:       A
# Date:         2020-08-25
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*
import arcpy
import xlwt
import os

data_path = r"E:\台账\织金县\织金县20200814验证\处理.gdb\织金县无措施数据20200825_表格"  # 数据所在路径
output_path = r"C:\Users\65680\Desktop\织金县"  # 数据输出路径
so_id = 1  # 分类方法，0按乡镇分，1按村分，2按组分
index = 3  # 要素所在位置，选0对应0，选1对应3，选2对应4


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

    ws.write(0, 0, "编码", style_2)
    ws.write(0, 1, "区县", style_2)
    ws.write(0, 2, "乡镇", style_2)
    ws.write(0, 3, "行政村", style_2)
    ws.write(0, 4, "采取措施", style_2)
    ws.write(0, 5, "主要作物2019年", style_2)
    ws.write(0, 6, "主要作物2020年", style_2)
    ws.write(0, 7, "周边环境", style_2)
    ws.write(0, 8, "面积（亩）", style_2)

    ws.row(1).set_style(xlwt.easyxf('font:height 320;'))


def su_total(data_path, output_path, so_id, index):
    data = data_path  # 数据所在的路径
    row_list = []  # 收集所有信息的列表
    xz_list = []  # 收集所有乡的列表
    cm_list = []  # 收集所有村的列表
    #  索引地理数据库数据
    cursor = arcpy.da.SearchCursor(data, ["BSBM", "FXZQMC", "TXZQMC", "XZQMC", "CQCS", "主要作物19年", "主要作物20年", "周边环境",
                                          "MJ_MU_QQ"])
    for row in cursor:
        BSBM = row[0]
        QX_NAME = row[1]
        XZ_NAME = row[2]
        cqcs = row[4]
        z19 = row[5]
        z20 = row[6]
        zbhj = row[7]
        XC_NAME = row[2] + row[3]
        MJ_M2 = round(row[8], 1)
        list1 = [BSBM, QX_NAME, XZ_NAME, XC_NAME, cqcs, z19, z20, zbhj, MJ_M2]
        row_list.append(list1)
        cm_list.append(XC_NAME)  # 村列表
        xz_list.append(XZ_NAME)  # 乡镇列表
    cu_list = list(set(cm_list))  # 列表化集合
    pz_list = list(set(xz_list))  # 列表化集合
    x_list = [pz_list, cu_list]  # 信息列表  用于下一个for循环索引
    for ys in x_list[so_id]:  # ys 默认为村名
        ys_name_list = filter(lambda x: x[index] == ys, row_list)  # 获得符合条件的内容列表  获得所有同一村排列的列表
        ys_name_list = sorted(ys_name_list, reverse=False)  # 通过地块编码排序
        xz = ys_name_list[0][2]
        cz = ys_name_list[0][3]
        xzpath = os.path.join(output_path, xz)  # 乡镇目录
        if os.path.isdir(xzpath):
            pass
        else:
            os.mkdir(xzpath)
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
        set_excel_title(ws, xz)
        r = 1
        for data_sys1 in ys_name_list:
            ws.row(r).set_style(xlwt.easyxf('font:height 300;'))  # 设置行高
            ws.row(r + 1).set_style(xlwt.easyxf('font:height 300;'))  # 设置行高
            data_sys1[2] = data_sys1[2][len(data_sys1[1]):]
            for data111 in range(len(data_sys1)):
                ws.write(r, data111, data_sys1[data111], style_4)
            r = r + 1
        print("%s toatle:%s done" % (ys, len(ys_name_list)))
        workbook_1.save('%s/%s-2.xls' % (xzpath, cz))


def main():
    su_total(data_path, output_path, so_id, index)


if __name__ == '__main__':
    main()
