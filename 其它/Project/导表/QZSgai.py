# -*- coding: utf-8 -*
import arcpy
import xlwt
import os
import sys

defaultencoding = 'utf-8'

if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

data_path = "E:/T清镇市台账数据.gdb/T无措施数据_确权_严格管控类"  # 数据所在路径
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

    ws.write_merge(0, 0, 0, 26, '清镇市耕地种植情况调查表（三）', style_1)
    ws.write_merge(1, 1, 0, 1, '填报单位（盖章）：', style_3)
    ws.write_merge(1, 1, 3, 4, '填报人：', style_3)
    ws.write_merge(1, 1, 9, 11, '电话：', style_3)
    ws.write_merge(1, 1, 20, 22, '填报时间：', style_3)
    ws.write_merge(2, 4, 0, 0, '序号', style_2)
    ws.write_merge(2, 4, 1, 1, '地块编号', style_2)
    ws.write_merge(2, 4, 2, 2, '村', style_2)
    ws.write_merge(2, 4, 3, 3, '组', style_2)
    ws.write_merge(2, 4, 4, 4, '农户姓名', style_2)
    ws.write_merge(2, 4, 5, 5, '地块名称', style_2)
    ws.write_merge(2, 4, 6, 6, '面积m2', style_2)
    ws.write_merge(2, 2, 7, 22, '种植品种', style_2)
    ws.write_merge(2, 2, 23, 24, '其他', style_2)
    ws.write_merge(2, 4, 25, 25, '环境', style_2)
    ws.write_merge(2, 4, 26, 26, '备注', style_2)
    ws.write_merge(3, 3, 7, 10, '水稻', style_2)
    ws.write_merge(3, 3, 11, 14, '玉米', style_2)
    ws.write(4, 7, '19年', style_2)
    ws.write(4, 8, '面积', style_2)
    ws.write(4, 9, '20年', style_2)
    ws.write(4, 10, '面积', style_2)
    ws.write(4, 11, '19年', style_2)
    ws.write(4, 12, '面积', style_2)
    ws.write(4, 13, '20年', style_2)
    ws.write(4, 14, '面积', style_2)
    ws.write_merge(3, 4, 15, 15, '蔬菜', style_2)
    ws.write_merge(3, 4, 16, 16, '果树', style_2)
    # ws.write_merge(3, 4, 17, 17, '刺梨', style_2)
    ws.write_merge(3, 4, 17, 17, '中药材', style_2)
    ws.write_merge(3, 4, 18, 18, '茶叶', style_2)
    ws.write_merge(3, 4, 19, 19, '林木', style_2)
    ws.write_merge(3, 4, 20, 20, '烤烟', style_2)
    ws.write_merge(3, 4, 21, 21, '豆类', style_2)
    ws.write_merge(3, 4, 22, 22, '薯类', style_2)
    ws.write_merge(3, 4, 23, 23, '休耕', style_2)
    ws.write_merge(3, 4, 24, 24, '非耕地', style_2)

    ws.col(0).width = 256 * 5
    # ws.col(5).width = 256 * 11
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
    ws.col(21).width = 256 * 4
    ws.col(22).width = 256 * 4
    ws.col(23).width = 256 * 4
    ws.col(24).width = 256 * 4
    ws.col(25).width = 256 * 4
    ws.col(26).width = 256 * 4


def su_total(data_path, output_path, so_id, index):
    data = data_path  # 数据所在的路径
    row_list = []  # 收集所有信息的列表
    xz_list = []  # 收集所有乡的列表
    zu_list = []  # 收集所有组的列表
    cm_list = []  # 收集所有村的列表
    #  索引地理数据库数据
    cursor = arcpy.da.SearchCursor(data, ["BSBM", "地块编码", "XZQMC", "地域名称", "承包方名称", "地块名称", "MJ_MU_QQ", "TXZQMC"])
    for row in cursor:
        txz_qmc = row[7]
        lb_bm = row[0]
        # dk_bm = row[1]
        xz_qmc = row[2]
        cb_nh_xm = row[4]
        dk_mc = row[5]
        mjm = round(row[6], 0)
        zm = row[3]
        bm = str(zm)
        try:
            zm_index = bm.index('村')
            zm = bm[zm_index + 3:]
        except:
            zm = zm
        list1 = [txz_qmc, lb_bm, xz_qmc, zm, cb_nh_xm, dk_mc, mjm]
        row_list.append(list1)
        zu_list.append(zm)  # 组列表
        cm_list.append(xz_qmc)  # 村列表
        xz_list.append(txz_qmc)  # 乡镇列表
    cu_list = list(set(cm_list))  # 列表化集合
    bu_list = list(set(zu_list))  # 列表化集合
    pz_list = list(set(xz_list))  # 列表化集合
    x_list = [pz_list, cu_list, bu_list]  # 信息列表  用于下一个for循环索引

    for ys in x_list[so_id]:  # ys 默认为村名

        ys_name_list = filter(lambda x: x[index] == ys, row_list)  # 获得符合条件的内容列表  获得所有同一村排列的列表
        ys_name_list = sorted(ys_name_list, reverse=True)  # 通过地块编码排序
        xz = ys_name_list[0][0]
        cz = ys_name_list[0][2]
        a = xz
        b = cz
        # xzpath = output_path + a + '/'  # 乡镇目录
        xzpath = os.path.join(output_path, xz)
        if os.path.isdir(xzpath):
            pass
        else:
            os.mkdir(xzpath)
        # czpath = xzpath + b + '/'
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
        set_excel_title(ws, a)
        ws.row(r).set_style(xlwt.easyxf('font:height 280;'))  # 设置行高
        for data_sys1 in ys_name_list:
            col_width = []
            for i in range(len(data_sys1)):
                col_width.append(len(str(data_sys1[i])))
            col2_width = col_width[-6:]
            kuan_du.append(col2_width)
            data_sys = data_sys1[1:]
            ws.write(r, 0, r - 4, style_4)
            for b in range(1, len(data_sys) + 21):
                if b < 7:
                    ws.write(r, b, data_sys[b - 1], style_4)
                else:
                    ws.write(r, b, '', style_4)
            r = r + 1
        c1 = []
        c2 = []
        c3 = []
        c4 = []
        c5 = []
        c6 = []
        for k in kuan_du:
            c1.append(k[0])
            c2.append(k[1])
            c3.append(k[2])
            c4.append(k[3])
            c5.append(k[4])
            c6.append(k[5])
        c1 = max(c1) + 1
        c2 = 7  # max(c2)
        # if c2 == 0:
        #     c2 = 11
        c3 = 7  # max(c3) - 1
        # if c3 == 0:
        #     c3 = 11
        c4 = 7  # max(c4)
        # if c4 == 0:
        #     c4 = 11
        c5 = 7  # max(c5)
        # if c5 == 0:
        #     c5 = 11
        c6 = max(c6)
        ws.col(1).width = 256 * c1
        ws.col(2).width = 256 * c2
        ws.col(3).width = 256 * c3
        ws.col(4).width = 256 * c4
        ws.col(5).width = 256 * c5
        ws.col(6).width = 256 * c6

        style_5 = xlwt.XFStyle()  # 面积格式
        a_1 = xlwt.Alignment()
        a_1_font = xlwt.Font()
        a_1_font.bold = True
        a_1_font.name = u'宋体'
        a_1_font.height = 20 * 10
        style_5.font = a_1_font
        style_5.alignment = a_1
        style_5.alignment.wrap = 1

        ws.write_merge(len(ys_name_list) + 5, len(ys_name_list) + 5, 0, 4, '面积合计：', style_5)
        ws.write_merge(len(ys_name_list) + 5, len(ys_name_list) + 5, 5, 6,
                       xlwt.Formula('SUM(G6:G%s)' % (len(ys_name_list) + 5)), style_5)

        # ws.write(len(ys_name_list) + 5, 6, xlwt.Formula('SUM(G6:G%s)' % (len(ys_name_list) + 5)), style_5)
        print("%s toatle:%s done" % (ys, len(ys_name_list)))
        workbook_1.save('%s%s.xls' % (czpath, ys))


def main():
    su_total(data_path, output_path, so_id, index)


if __name__ == '__main__':
    main()
