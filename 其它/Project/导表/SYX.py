# -*- coding: utf-8 -*
import arcpy
import xlwt
import os
import sys

defaultencoding = 'utf-8'

if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

data_path = "D:/20200525绥阳县台账数据/T绥阳县台账数据2.gdb/T无措施数据_确权_安全利用类"  # 数据所在路径
output_path = "C:/Users/Lenovo/Desktop/TP2"  # 数据输出路径
so_id = 1  # 分类方法，0按乡镇分，1按村分，2按组分
index = 1  # 要素所在位置，选0对应0，选1对应3，选2对应4


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

    style_10 = xlwt.XFStyle()  # 标题格式
    a_1 = xlwt.Alignment()
    a_1.horz = 0x02
    a_1.vert = 0x01
    a_1_font = xlwt.Font()
    a_1_font.bold = True
    a_1_font.name = u'宋体'
    a_1_font.height = 20 * 18
    style_10.font = a_1_font
    style_10.alignment = a_1
    style_10.alignment.wrap = 1

    bbq = 42
    ws.write_merge(1, 6, 0, 12, '绥阳县%s安全利用类耕地种植情况调查表' % xz, style_10)
    ws.write_merge(10, 12, 3, 5, '填报人:', style_1)
    ws.write_merge(16, 18, 3, 5, '电话:', style_1)
    ws.write_merge(22, 24, 3, 5, '填报时间:', style_1)
    ws.write_merge(28, 30, 3, 5, '填报单位盖章:', style_1)
    ws.write_merge(0 + bbq, 0 + bbq, 0, 14, '绥阳县%s安全利用类耕地种植情况调查表' % xz, style_1)
    ws.write_merge(0 + bbq, 0 + bbq, 15, 26, '绥阳县%s安全利用类耕地种植情况调查表（续表）' % xz, style_1)
    # ws.write_merge(1+bbq, 1+bbq, 1, 1, '填报单位（盖章）：', style_3)
    # ws.write_merge(1+bbq, 1+bbq, 3, 4, '填报人：', style_3)
    # ws.write_merge(1+bbq, 1+bbq, 7, 8, '电话：', style_3)
    # ws.write_merge(1+bbq, 1+bbq, 10, 12, '填报时间：', style_3)
    ws.write_merge(2 + bbq, 4 + bbq, 0, 0, '序号', style_2)
    ws.write_merge(2 + bbq, 4 + bbq, 1, 1, '地块编号', style_2)
    ws.write_merge(2 + bbq, 4 + bbq, 2, 2, '组', style_2)
    ws.write_merge(2 + bbq, 4 + bbq, 3, 3, '农户姓名', style_2)
    ws.write_merge(2 + bbq, 4 + bbq, 4, 4, '地块名称', style_2)
    ws.write_merge(2 + bbq, 4 + bbq, 5, 5, '面积㎡', style_2)
    ws.write_merge(2 + bbq, 2 + bbq, 6, 12, '2019种植作物', style_2)
    ws.write_merge(2 + bbq, 2 + bbq, 13, 20, '2020种植作物', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 6, 6, '水稻', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 7, 7, '玉米', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 8, 8, '辣椒', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 9, 9, '蔬菜', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 10, 10, '高粱', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 11, 11, '烤烟', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 12, 12, '其他', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 13, 13, '水稻', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 14, 14, '玉米', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 15, 15, '辣椒', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 16, 16, '蔬菜', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 17, 17, '高粱', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 18, 18, '烤烟', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 19, 19, '果树', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 20, 20, '其他', style_2)
    ws.write_merge(2 + bbq, 2 + bbq, 21, 27, '品种调整、结构调整以外的措施', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 21, 21, '优化施肥', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 22, 22, '秸秆还田', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 23, 23, '转非耕地', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 24, 24, '深翻耕', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 25, 25, '水分调控', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 26, 26, '石灰调节', style_2)
    ws.write_merge(3 + bbq, 4 + bbq, 27, 27, '退耕还林', style_2)
    ws.write_merge(2 + bbq, 4 + bbq, 28, 28, '周边环境', style_2)

    ws.col(0).width = 256 * 5
    ws.col(21).width = 256 * 6
    ws.col(22).width = 256 * 6
    ws.col(23).width = 256 * 6
    ws.col(24).width = 256 * 6
    ws.col(25).width = 256 * 6
    ws.col(26).width = 256 * 6
    ws.col(27).width = 256 * 6
    ws.col(28).width = 256 * 6


def su_total(data_path, output_path, so_id, index):
    data = data_path  # 数据所在的路径
    row_list = []  # 收集所有信息的列表
    xz_list = []  # 收集所有乡的列表
    zu_list = []  # 收集所有组的列表
    cm_list = []  # 收集所有村的列表
    #  索引地理数据库数据
    cursor = arcpy.da.SearchCursor(data, ["BSBM", "DKBM", "XZQMC", "FBFDZ", "QZLQRXM", "DKMC", "ECMJM2", "TXZQMC"])
    for row in cursor:
        txz_qmc = row[7]
        lb_bm = row[0]
        xz_qmc = row[7] + row[2]
        cb_nh_xm = row[4]
        dk_mc = row[5]
        mjm = round(row[6], 0)
        zm = row[3]
        bm = str(zm)
        try:
            if '区' in bm:
                zm_index = bm.index('区')
                zm = bm[zm_index + 3:]
            else:
                zm_index = bm.index('村')
                zm = bm[zm_index + 3:]
        except:
            zm = zm
        list1 = [txz_qmc, xz_qmc, lb_bm, zm, cb_nh_xm, dk_mc, mjm]
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
        ys_name_list = sorted(ys_name_list, reverse=False)  # 通过地块编码排序
        xz = ys_name_list[0][0]
        cz = ys_name_list[0][1]
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
        r = 5 + 42

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
        set_excel_title(ws, cz)
        tall_style = xlwt.easyxf('font:height 280;')
        for data_sys1 in ys_name_list:
            ws.row(r).set_style(tall_style)  # 设置行高
            col_width = []
            for i in range(len(data_sys1)):
                col_width.append(len(str(data_sys1[i])))
            col2_width = col_width[-5:]
            kuan_du.append(col2_width)
            data_sys = data_sys1[2:]
            ws.write(r, 0, r - 46, style_4)
            for b in range(1, len(data_sys) + 24):
                if b < 6:
                    ws.write(r, b, data_sys[b - 1], style_4)
                else:
                    ws.write(r, b, '', style_4)
            r = r + 1
        c1 = []
        c2 = []
        c3 = []
        c4 = []
        c5 = []
        for k in kuan_du:
            c1.append(k[0])
            c2.append(k[1])
            c3.append(k[2])
            c4.append(k[3])
            c5.append(k[4])
        c1 = max(c1) + 1
        c2 = 11  # max(c2)
        # if c2 == 0:
        #     c2 = 11
        c3 = 11  # max(c3)
        # if c3 == 0:
        #     c3 = 11
        c4 = 11
        # c4 = max(c4)/2
        # if c4 == 0:
        #     c4 = 11
        c5 = max(c5)
        if c5 == 0:
            c5 = 11
        ws.col(1).width = 256 * c1
        ws.col(2).width = 256 * c2
        ws.col(3).width = 256 * c3
        ws.col(4).width = 256 * c4
        ws.col(5).width = 256 * c5

        style_5 = xlwt.XFStyle()  # 面积格式
        a_1 = xlwt.Alignment()
        a_1_font = xlwt.Font()
        a_1_font.bold = True
        a_1_font.name = u'宋体'
        a_1_font.height = 20 * 10
        style_5.font = a_1_font
        style_5.alignment = a_1
        style_5.alignment.wrap = 1

        ws.write_merge(len(ys_name_list) + 47, len(ys_name_list) + 47, 1, 3, '面积合计：', style_5)
        ws.write_merge(len(ys_name_list) + 47, len(ys_name_list) + 47, 4, 5,
                       xlwt.Formula('SUM(F6:F%s)' % (len(ys_name_list) + 47)), style_5)

        print("%s toatle:%s done" % (ys, len(ys_name_list)))
        workbook_1.save('%s/%s-2.xls' % (czpath, ys))


def main():
    su_total(data_path, output_path, so_id, index)


if __name__ == '__main__':
    main()
