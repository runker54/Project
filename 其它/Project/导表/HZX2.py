# -*- coding: utf-8 -*
import arcpy
import xlwt
import os
import sys

defaultencoding = 'utf-8'

if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

data_path = "E:/T赫章县台账数据.gdb/成果数据_无措施_单部件_大于五_安全利用类"  # 数据所在路径
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

    ws.write_merge(0, 0, 0, 22, '赫章县%s耕地种植情况调查表（二）' % xz, style_1)
    ws.write_merge(1, 1, 0, 1, '填报单位（盖章）：', style_3)
    ws.write_merge(1, 1, 3, 4, '填报人：', style_3)
    ws.write_merge(1, 1, 9, 11, '电话：', style_3)
    ws.write_merge(1, 1, 18, 20, '填报时间：', style_3)
    ws.write_merge(2, 4, 0, 0, '序号', style_2)
    ws.write_merge(2, 4, 1, 1, '地块编号', style_2)
    ws.write_merge(2, 4, 2, 2, '村', style_2)

    ws.write_merge(2, 4, 3, 3, '面积m2', style_2)
    ws.write_merge(2, 2, 4, 6, '2019种植品种', style_2)
    ws.write_merge(2, 2, 7, 17, '2020种植品种', style_2)
    ws.write_merge(2, 2, 18, 20, '其他', style_2)
    ws.write_merge(2, 4, 21, 21, '周边环境', style_2)
    ws.write_merge(2, 4, 22, 22, '备注', style_2)

    ws.write_merge(3, 4, 4, 4, '水稻', style_2)
    ws.write_merge(3, 4, 5, 5, '玉米', style_2)
    ws.write_merge(3, 4, 6, 6, '其他', style_2)
    ws.write_merge(3, 4, 7, 7, '水稻', style_2)
    ws.write_merge(3, 4, 8, 8, '玉米', style_2)
    ws.write_merge(3, 4, 9, 9, '小麦', style_2)
    ws.write_merge(3, 4, 10, 10, '薯类', style_2)
    ws.write_merge(3, 4, 11, 11, '豆类', style_2)
    ws.write_merge(3, 4, 12, 12, '油料', style_2)
    ws.write_merge(3, 4, 13, 13, '蔬菜', style_2)
    ws.write_merge(3, 4, 14, 14, '果树', style_2)
    ws.write_merge(3, 4, 15, 15, '茶叶', style_2)
    ws.write_merge(3, 4, 16, 16, '烤烟', style_2)
    ws.write_merge(3, 4, 17, 17, '中药材', style_2)
    ws.write_merge(3, 4, 18, 18, '休耕', style_2)
    ws.write_merge(3, 4, 19, 19, '有机肥', style_2)
    ws.write_merge(3, 4, 20, 20, '非耕地', style_2)

    ws.row(2).set_style(xlwt.easyxf('font:height 320;'))
    ws.row(3).set_style(xlwt.easyxf('font:height 320;'))
    ws.row(4).set_style(xlwt.easyxf('font:height 320;'))

    ws.col(0).width = 256 * 5
    ws.col(4).width = 256 * 4
    ws.col(5).width = 256 * 4
    ws.col(6).width = 256 * 6
    ws.col(7).width = 256 * 4
    ws.col(8).width = 256 * 4
    ws.col(9).width = 256 * 4
    ws.col(10).width = 256 * 4
    ws.col(11).width = 256 * 4
    ws.col(12).width = 256 * 4
    ws.col(13).width = 256 * 4
    ws.col(14).width = 256 * 4
    ws.col(15).width = 256 * 4
    ws.col(16).width = 256 * 4
    ws.col(17).width = 256 * 4
    ws.col(18).width = 256 * 4
    ws.col(19).width = 256 * 4
    ws.col(20).width = 256 * 4
    ws.col(21).width = 256 * 6
    ws.col(22).width = 256 * 10




def su_total(data_path, output_path, so_id, index):
    data = data_path  # 数据所在的路径
    row_list = []  # 收集所有信息的列表
    xz_list = []  # 收集所有乡的列表
    zu_list = []  # 收集所有组的列表
    cm_list = []  # 收集所有村的列表
    #  索引地理数据库数据
    cursor = arcpy.da.SearchCursor(data, ["BSBM", "XZQMC", "ECMJM2", "TXZQMC"])
    for row in cursor:
        txz_qmc = row[3]
        lb_bm = row[0]
        xz_qmc = row[3]+row[1]
        # cb_nh_xm = row[4]
        # dk_mc = row[5]
        mjm = round(row[2], 1)
        list1 = [txz_qmc, lb_bm, xz_qmc, mjm]
        row_list.append(list1)
        cm_list.append(xz_qmc)  # 村列表
        xz_list.append(txz_qmc)  # 乡镇列表
    cu_list = list(set(cm_list))  # 列表化集合
    pz_list = list(set(xz_list))  # 列表化集合
    x_list = [pz_list, cu_list]  # 信息列表  用于下一个for循环索引

    for ys in x_list[so_id]:  # ys 默认为村名

        ys_name_list = filter(lambda x: x[index] == ys, row_list)  # 获得符合条件的内容列表  获得所有同一村排列的列表
        ys_name_list = sorted(ys_name_list, reverse=False)  # 通过地块编码排序
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
        ws.row(r).set_style(xlwt.easyxf('font:height 280;'))  # 设置行高
        for data_sys1 in ys_name_list:
            data_sys1[2] = data_sys1[2][len(data_sys1[0]):]
            col_width = []
            for i in range(len(data_sys1)):
                col_width.append(len(str(data_sys1[i])))
            col2_width = col_width[-6:]
            kuan_du.append(col2_width)
            ws.write(r, 0, r - 4, style_4)
            for b in range(1, len(data_sys1) + 19):
                if b < 4:
                    ws.write(r, b, data_sys1[b], style_4)
                else:
                    ws.write(r, b, '', style_4)
            r = r + 1
        c1 = []
        c2 = []
        c3 = []
        c4 = []
        c5 = []
        for k in kuan_du:
            c1.append(k[1])
            c2.append(k[2])
            c3.append(k[3])
        c1 = max(c1) + 1
        c2 = max(c2)
        if c2 == 0:
            c2 = 11
        c3 = max(c3)
        if c3 == 0:
            c3 = 11

        ws.col(1).width = 256 * c1
        ws.col(2).width = 256 * c2
        ws.col(3).width = 256 * c3


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
        ws.write_merge(len(ys_name_list) + 5, len(ys_name_list) + 5, 2, 3,
                       xlwt.Formula('SUM(D6:D%s)' % (len(ys_name_list) + 5)), style_5)

        print("%s toatle:%s done" % (ys, len(ys_name_list)))
        workbook_1.save('%s/%s-2.xls' % (czpath, cz))


def main():
    su_total(data_path, output_path, so_id, index)


if __name__ == '__main__':
    main()
