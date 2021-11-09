# -*- coding: utf-8 -*
import arcpy
import xlwt
import os
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

data_path = "E:/T开阳县台账数据.gdb/T无措施数据_确权_安全利用类"  # 数据所在路径
output_path = "C:/Users/Administrator/Desktop/TP/"  # 数据输出路径
so_id = 1  # 分类方法，0按乡镇分，1按村分，2按组分
index = 3  # 要素所在位置，选0对应0，选1对应3，选2对应4


# 获取字符串长度，一个中文的长度为2
def len_byte(value):
    length = len(value)
    utf8_length = len(value.encode('utf-8'))
    length = (utf8_length - length) / 2 + length
    return int(length)


def set_excel_title(ws, xz):
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
    a_1_font.name = u'宋体'
    a_1_font.height = 20 * 10
    style_2.font = a_1_font
    style_2.alignment = a_1
    style_2.borders = borders
    style_2.alignment.wrap = 1

    ws.write_merge(0, 0, 0, 15, 'mark_logo %s 农作物种植情况调查表' % xz, style_1)
    ws.write_merge(1, 1, 0, 1, '填报单位（盖章）：', style_3)
    ws.write_merge(1, 1, 3, 4, '填报人：', style_3)
    ws.write_merge(1, 1, 6, 7, '电话：', style_3)
    ws.write_merge(1, 1, 9, 10, '填报时间：', style_3)
    ws.write_merge(2, 4, 0, 0, '地块图 斑 编 号', style_2)
    ws.write_merge(2, 4, 1, 1, '土地确  权地块  编  码', style_2)
    ws.write_merge(2, 4, 2, 2, '村', style_2)
    # ws.col(3).width = 256 * 12
    ws.write_merge(2, 4, 3, 3, '组', style_2)
    ws.write_merge(2, 4, 4, 4, '农户姓名', style_2)
    ws.write_merge(2, 4, 5, 5, '地块名称', style_2)
    # ws.col(6).width = 256 * 6.5
    ws.write_merge(2, 4, 6, 6, '面积（亩）', style_2)
    ws.write_merge(2, 2, 7, 15, '作物类型', style_2)
    ws.write_merge(3, 3, 7, 8, '水稻品种', style_2)
    ws.write_merge(3, 3, 9, 10, '玉米品种', style_2)
    # ws.col(11).width = 256 * 3.5
    ws.write_merge(3, 4, 11, 11, '蔬菜', style_2)
    # ws.col(12).width = 256 * 3.5
    ws.write_merge(3, 4, 12, 12, '烤烟', style_2)
    # ws.col(13).width = 256 * 3.5
    ws.write_merge(3, 4, 13, 13, '果树', style_2)
    # ws.col(14).width = 256 * 3.5
    ws.write_merge(3, 4, 14, 14, '茶叶', style_2)
    # ws.col(15).width = 256 * 3.5
    ws.write_merge(3, 4, 15, 15, '其他', style_2)
    # ws.col(7).width = 256 * 7.5
    ws.write(4, 7, '2019年', style_2)
    # ws.col(8).width = 256 * 7.5
    ws.write(4, 8, '2020年', style_2)
    # ws.col(9).width = 256 * 7.5
    ws.write(4, 9, '2019年', style_2)
    # ws.col(10).width = 256 * 7.5
    ws.write(4, 10, '2020年', style_2)


def su_total(data_path, output_path, so_id, index):
    data = data_path  # 数据所在的路径
    row_list = []  # 收集所有信息的列表
    xz_list = []  # 收集所有乡的列表
    zu_list = []  # 收集所有组的列表
    cm_list = []  # 收集所有村的列表
    #  索引地理数据库数据
    cursor = arcpy.da.SearchCursor(data, ["LBBM", "地块编码", "XZQMC", "OwnRightNa", "承包农户名", "地块名称", "MJ_MU_QQ",
                                "TXZQMC"])
    for row in cursor:
        txz_qmc = row[7]
        lb_bm = row[0]
        dk_bm = row[1]
        xz_qmc = row[7]+row[2]
        # xz_qmc = row[2]
        cb_nh_xm = row[4]
        dk_mc = row[5]
        mjm = float(round(row[6],3))
        # lens = len(xz_qmc) + 10
        # zm = row[3][lens:]
        zm = row[3]
        try:
            zm = zm[zm.index('会')+1:]
        except:
            zm = zm
        list1 = [txz_qmc, lb_bm, dk_bm, xz_qmc, zm, cb_nh_xm, dk_mc, mjm]
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
        cz = ys_name_list[0][3]
        a = xz
        b = cz
        xzpath = output_path + a + '/'  # 乡镇目录
        if os.path.isdir(xzpath):
            pass
        else:
            os.mkdir(xzpath)
        czpath = xzpath + b + '/'
        if os.path.isdir(czpath):
            pass
        else:
            os.mkdir(czpath)
        ccc_list = []
        pm_list = []
        for data_sys1 in ys_name_list:
            ccc_list.append(data_sys1[1])
        pm_list = list(set(ccc_list))
        pm_list = sorted(pm_list)
        for sx in pm_list:
            vm_list = filter(lambda x: x[1] == sx, ys_name_list)

            workbook_1 = xlwt.Workbook(encoding='utf-8')  # 新建Excel
            ws = workbook_1.add_sheet('%s' % ys + sx)  # Excel新增Sheet
            borders = xlwt.Borders()  # 为样式创建边框
            # DASHED虚线
            # NO_LINE没有
            # THIN实线
            borders.left = xlwt.Borders.THIN
            borders.right = xlwt.Borders.THIN
            borders.top = xlwt.Borders.THIN
            borders.bottom = xlwt.Borders.THIN
            # style = xlwt.XFStyle()  # 初始化样式
            style_4 = xlwt.easyxf()  # 初始化样式
            style_4.borders = borders

            set_excel_title(ws, a)

            r = 5  # 内容开始行
            for data_sys in vm_list:  # 写入内容
                # col_width = []
                # for i in range(len(data_sys) - 1):
                #     col_width.append(len_byte(data_sys[i]))
                # # 设置栏位宽度，栏位宽度小于10时候采用默认宽度
                # for i in range(len(col_width)):
                #     if col_width[i] > 10:
                #         ws.col(i - 1).width = 256 * (col_width[i] + 1)
                data_sys[3] = data_sys[3][len(data_sys[0]):]
                for b in range(len(data_sys) + 9):
                    if b == 7:
                        pass
                    else:
                        if b < 7:
                            ws.write(r, b, data_sys[b + 1], style_4)
                        else:
                            ws.write(r, b - 1, '', style_4)
                r = r + 1

            ws.write_merge(len(vm_list) + 5, len(vm_list) + 5, 0, 5, '面积合计：')
            ws.write(len(vm_list) + 5, 6, xlwt.Formula('SUM(G6:G%s)' % (len(vm_list) + 5)))
            print("%s toatle:%s done" % (ys, len(ys_name_list)))
            workbook_1.save('%s%s.xls' % (czpath, sx))


su_total(data_path, output_path, so_id, index)
