# -*- coding: utf-8 -*
import arcpy
import xlwt
import os
import sys

defaultencoding = 'utf-8'

if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

data_path = "E:/T大方县台账数据.gdb/成果数据_无措施数据_单部件_大于一_安全利用类"  # 数据所在路径
output_path = "C:/Users/Administrator/Desktop/TP/"  # 数据输出路径
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

    ws.write_merge(0, 0, 0, 35, '大方县%s耕地种植情况调查表（二）' % xz, style_1)
    ws.write_merge(1, 1, 0, 2, '填报单位（盖章）：', style_3)
    ws.write_merge(1, 1, 6, 7, '填报人：', style_3)
    ws.write_merge(1, 1, 15, 16, '电话：', style_3)
    ws.write_merge(1, 1, 25, 26, '填报时间：', style_3)
    ws.write_merge(2, 3, 0, 0, '序号', style_2)
    ws.write_merge(2, 3, 1, 1, '地块编号', style_2)
    ws.write_merge(2, 3, 2, 2, '乡镇', style_2)
    ws.write_merge(2, 3, 3, 3, '村', style_2)
    ws.write_merge(2, 3, 4, 4, '面积（m2）', style_2)
    ws.write_merge(2, 3, 5, 5, '年份', style_2)
    ws.write_merge(2, 2, 6, 8, '水稻', style_2)
    ws.write_merge(2, 2, 9, 11, '玉米', style_2)
    ws.write_merge(2, 2, 12, 14, '油菜', style_2)
    ws.write_merge(2, 2, 15, 17, '小麦', style_2)
    ws.write_merge(2, 2, 18, 20, '辣椒', style_2)
    ws.write_merge(2, 2, 21, 23, '马铃薯', style_2)
    ws.write_merge(2, 2, 24, 26, '茶叶', style_2)
    ws.write_merge(2, 2, 27, 29, '蔬菜', style_2)
    ws.write_merge(2, 2, 30, 32, '其他', style_2)
    ws.write_merge(2, 3, 33, 33, '2km内有或曾有工矿企业，冶炼厂', style_2)

    ws.col(0).width = 256 * 5
    ws.col(33).width = 256 * 12

    ws.row(1).set_style(xlwt.easyxf('font:height 320;'))

    for _x in range(6, 31, 3):
        ws.write(3, _x, '品种', style_2)
        ws.write(3, _x + 1, '面积', style_2)
        ws.write(3, _x + 2, '有机肥', style_2)


    for _i in range(5, 33):
        ws.col(_i).width = 256 * 6


def su_total(data_path, output_path, so_id, index):
    data = data_path  # 数据所在的路径
    row_list = []  # 收集所有信息的列表
    xz_list = []  # 收集所有乡的列表
    cm_list = []  # 收集所有村的列表
    #  索引地理数据库数据
    cursor = arcpy.da.SearchCursor(data, ["BSBM", "TXZQMC", "XZQMC", "ECMJM2"])
    for row in cursor:
        BSBM = row[0]
        XZ_NAME = row[1]
        XC_NAME = row[1] + row[2]
        MJ_M2 = round(row[3], 1)
        list1 = [BSBM, XZ_NAME, XC_NAME, MJ_M2]
        row_list.append(list1)
        cm_list.append(XC_NAME)  # 村列表
        xz_list.append(XZ_NAME)  # 乡镇列表
    cu_list = list(set(cm_list))  # 列表化集合
    pz_list = list(set(xz_list))  # 列表化集合
    x_list = [pz_list, cu_list]  # 信息列表  用于下一个for循环索引
    for ys in x_list[so_id]:  # ys 默认为村名
        ys_name_list = filter(lambda x: x[index] == ys, row_list)  # 获得符合条件的内容列表  获得所有同一村排列的列表
        ys_name_list = sorted(ys_name_list, reverse=False)  # 通过地块编码排序
        xz = ys_name_list[0][1]
        cz = ys_name_list[0][2]
        xzpath = os.path.join(output_path, xz)  # 乡镇目录
        if os.path.isdir(xzpath):
            pass
        else:
            os.mkdir(xzpath)
        czpath = os.path.join(xzpath, cz)
        if os.path.isdir(czpath):
            pass
        else:
            os.mkdir(czpath)
        r = 4
        xh = 4
        kuan_du = []
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


        for data_sys1 in ys_name_list:
            ws.row(r).set_style(xlwt.easyxf('font:height 300;'))  # 设置行高
            ws.row(r + 1).set_style(xlwt.easyxf('font:height 300;'))  # 设置行高
            data_sys1[2] = data_sys1[2][len(data_sys1[1]):]
            col_width = []
            for i in range(len(data_sys1)):
                col_width.append(len(str(data_sys1[i])))
            col2_width = col_width
            kuan_du.append(col2_width)
            ws.write_merge(r, r + 1, 0, 0, xh - 3, style_4)
            for b in range(1, len(data_sys1) + 30):
                if b < 5:
                    ws.write_merge(r, r + 1, b, b, data_sys1[b - 1], style_4)
                elif b == 5:
                    ws.write(r, b, '2019', style_4)
                    ws.write(r + 1, b, '2020', style_4)
                else:
                    ws.write(r, b, '', style_4)
                    ws.write(r + 1, b, '', style_4)
            r = r + 2
            xh = xh + 1
        c1 = []
        c2 = []
        c3 = []
        c4 = []
        for k in kuan_du:
            c1.append(k[0])
            c2.append(k[1])
            c3.append(k[2])
            c4.append(k[3])

        c1 = max(c1) + 1
        c2 = max(c2)
        if c2 == 0:
            c2 = 11
        c3 = max(c3)
        if c3 == 0:
            c3 = 11
        c4 = max(c4)
        if c4 == 0:
            c4 = 11

        ws.col(1).width = 256 * c1
        ws.col(2).width = 256 * c2
        ws.col(3).width = 256 * c3
        ws.col(4).width = 256 * c4

        style_5 = xlwt.XFStyle()  # 面积格式
        a_1 = xlwt.Alignment()
        a_1_font = xlwt.Font()
        a_1_font.bold = True
        a_1_font.name = u'宋体'
        a_1_font.height = 20 * 10
        style_5.font = a_1_font
        style_5.alignment = a_1
        style_5.alignment.wrap = 1

        ws.write_merge(len(ys_name_list) * 2 + 4, len(ys_name_list) * 2 + 4, 0, 1, '面积合计：', style_5)
        ws.write_merge(len(ys_name_list) * 2 + 4, len(ys_name_list) * 2 + 4, 3, 4,
                       xlwt.Formula('SUM(E5:E%s)' % (len(ys_name_list) * 2 + 4)), style_5)

        print("%s toatle:%s done" % (ys, len(ys_name_list)))
        workbook_1.save('%s/%s-2.xls' % (czpath, cz))


def main():
    su_total(data_path, output_path, so_id, index)


if __name__ == '__main__':
    main()
