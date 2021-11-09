#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2020-12-08
# Author:Runker54
# -----------------------
import xlrd
import xlwt
import os
import time
roots_ = r'C:\Users\65680\Desktop\shhet'
for one_qx in os.listdir(roots_):
    qx_name = one_qx[:one_qx.rfind('.')]
    print(qx_name)
    sheet_path = r'C:\Users\65680\Desktop\shhet\%s.xls'%qx_name
    out_path = r'C:\Users\65680\Desktop\out\%s' % qx_name
    try:
        os.makedirs(out_path)
    except:
        pass
    read_work = xlrd.open_workbook(sheet_path)
    read_sheet = read_work.sheet_by_index(1)
    dict_sheet = read_work.sheet_by_index(0)
    dict_rows = dict_sheet.nrows
    xzcz_dict = {}
    for one_dict_row in range(1, dict_rows):
        xz = dict_sheet.row(one_dict_row)[0].value
        cz = dict_sheet.row(one_dict_row)[1].value
        xzcz_dict[cz] = xz
    print(f'共{len(xzcz_dict)}村！')

    calc_list = list(set([xzcz_dict[read_sheet.row(one_row)[1].value]+read_sheet.row(one_row)[1].value
                          for one_row in range(2, read_sheet.nrows)]))


    def style():
        # 边框(四面实线)
        borders = xlwt.Borders()
        borders.left = xlwt.Borders.THIN
        borders.right = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN
        # 边框(右实)
        borders1 = xlwt.Borders()
        borders1.left = xlwt.Borders.NO_LINE
        borders1.right = xlwt.Borders.THIN
        borders1.top = xlwt.Borders.DASHED
        borders1.bottom = xlwt.Borders.DASHED
        # 边框(右无，下虚)
        borders2 = xlwt.Borders()
        borders2.left = xlwt.Borders.THIN
        borders2.right = xlwt.Borders.NO_LINE
        borders2.top = xlwt.Borders.THIN
        borders2.bottom = xlwt.Borders.THIN
        # 边框(左无，下虚)
        borders3 = xlwt.Borders()
        borders3.left = xlwt.Borders.NO_LINE
        borders3.right = xlwt.Borders.NO_LINE
        borders3.top = xlwt.Borders.DASHED
        borders3.bottom = xlwt.Borders.DASHED
        # 边框(左右无)
        borders4 = xlwt.Borders()
        borders4.left = xlwt.Borders.NO_LINE
        borders4.right = xlwt.Borders.NO_LINE
        borders4.top = xlwt.Borders.THIN
        borders4.bottom = xlwt.Borders.THIN
        # 边框(左无右实)
        borders5 = xlwt.Borders()
        borders5.left = xlwt.Borders.NO_LINE
        borders5.right = xlwt.Borders.THIN
        borders5.top = xlwt.Borders.THIN
        borders5.bottom = xlwt.Borders.THIN
        # 标题格式
        style_1 = xlwt.XFStyle()
        a_1 = xlwt.Alignment()
        a_1.horz = 0x02
        a_1.vert = 0x01
        a_1_font = xlwt.Font()
        # a_1_font.bold = True
        a_1_font.name = u'仿宋'
        a_1_font.height = 20 * 12
        style_1.font = a_1_font
        style_1.alignment = a_1
        style_1.alignment.wrap = 1
        # 附件格式
        style_fj = xlwt.XFStyle()
        a_fj = xlwt.Alignment()
        a_fj_font = xlwt.Font()
        a_fj_font.name = u'宋体'
        a_fj_font.height = 20 * 14
        style_fj.font = a_fj_font
        style_fj.alignment = a_fj
        style_fj.alignment.wrap = 1
        # 副标题格式1
        style_2 = xlwt.XFStyle()
        a_2_font = xlwt.Font()
        # a_2_font.bold = True
        a_2_font.name = u'宋体'
        a_2_font.height = 20 * 18
        style_2.font = a_2_font
        style_2.alignment = a_1
        style_2.borders = borders
        style_2.alignment.wrap = 1
        # 副标题格式2
        style_3 = xlwt.XFStyle()
        a_3_font = xlwt.Font()
        # a_3_font.bold = True
        a_3_font.name = u'宋体'
        a_3_font.height = 20 * 18
        a_3 = xlwt.Alignment()
        a_3.horz = 0x02
        a_3.vert = 0x01
        style_3.font = a_3_font
        style_3.alignment = a_3
        style_3.borders = borders
        style_3.alignment.wrap = 1
        # 普通格式
        style1 = xlwt.XFStyle()
        al = xlwt.Alignment()
        a1_font = xlwt.Font()
        a1_font.name = u'仿宋'
        a1_font.height = 20 * 10
        al.horz = 0x02  # 水平居中
        al.vert = 0x01  # 垂直居中
        style1.alignment = al
        style1.font = a1_font
        style1.borders = borders
        style1.alignment.wrap = 1  # 自动换行
        # 表幞头格式
        style4 = xlwt.XFStyle()
        style4.font = a1_font
        # 特殊格式
        style2 = xlwt.XFStyle()
        a2 = xlwt.Alignment()
        a2.vert = 0x01
        a_4_font = xlwt.Font()
        a_4_font.name = u'仿宋'
        a_4_font.height = 20 * 10
        style2.font = a_4_font
        style2.alignment = a2
        style2.borders = borders
        style2.alignment.wrap = 1
        # 特殊格式
        style3 = xlwt.XFStyle()
        a2 = xlwt.Alignment()
        a2.vert = 0x01
        a2.horz = 0x02
        a_5_font = xlwt.Font()
        a_5_font.name = 'Wingdings 2'
        a_5_font.height = 20 * 12
        style3.font = a_5_font
        style3.alignment = a2
        style3.borders = borders
        style3.alignment.wrap = 1
        # 右无特殊格式
        style9 = xlwt.XFStyle()
        a10 = xlwt.Alignment()
        a10.vert = 0x01
        a10.horz = 0x02
        a_10_font = xlwt.Font()
        a_10_font.name = 'Wingdings 2'
        a_10_font.height = 20 * 12
        style9.font = a_10_font
        style9.alignment = a10
        style9.borders = borders2
        style9.alignment.wrap = 1

        # 左对齐下虚格式
        style5 = xlwt.XFStyle()
        a6 = xlwt.Alignment()
        a6_font = xlwt.Font()
        a6_font.name = u'仿宋'
        a6_font.height = 20 * 10
        a6.vert = 0x01  # 垂直居中
        style5.alignment = a6
        style5.font = a6_font
        style5.borders = borders3
        style5.alignment.wrap = 1  # 自动换行
        # 右实
        style7 = xlwt.XFStyle()
        a8 = xlwt.Alignment()
        a8_font = xlwt.Font()
        a8_font.name = u'仿宋'
        a8_font.height = 20 * 10
        a8.vert = 0x01  # 垂直居中
        style7.alignment = a8
        style7.font = a8_font
        style7.borders = borders1
        style7.alignment.wrap = 1  # 自动换行
        # 特殊格式2
        style6 = xlwt.XFStyle()
        a7 = xlwt.Alignment()
        a7_font = xlwt.Font()
        a7_font.name = 'Wingdings 2'
        a7_font.height = 20 * 10
        a7.vert = 0x01  # 垂直居中
        a7.horz = 0x02  # 水平居中
        style6.alignment = a7
        style6.font = a7_font
        style6.borders = borders3
        style6.alignment.wrap = 1  # 自动换行
        # 左右无
        style8 = xlwt.XFStyle()
        a9 = xlwt.Alignment()
        a9_font = xlwt.Font()
        a9_font.name = u'仿宋'
        a9_font.height = 20 * 10
        a9.vert = 0x01  # 垂直居中
        a9.horz = 0x02  # 水平居中
        style8.alignment = a9
        style8.font = a9_font
        style8.borders = borders4
        style8.alignment.wrap = 1  # 自动换行
        # 左无右实
        style10 = xlwt.XFStyle()
        a11 = xlwt.Alignment()
        a11_font = xlwt.Font()
        a11_font.name = u'仿宋'
        a11_font.height = 20 * 10
        a11.vert = 0x01  # 垂直居中
        a11.horz = 0x02  # 水平居中
        style10.alignment = a11
        style10.font = a11_font
        style10.borders = borders5
        style10.alignment.wrap = 1  # 自动换行

        return style1, style2, style3, style4, style_1, style_2, style_3, style_fj, style5, style6, style7, style8, style9, style10


    for one_xz in calc_list:
        write_book = xlwt.Workbook('utf-8')
        write_sheet = write_book.add_sheet(one_xz)
        # 写入表头
        write_sheet.write_merge(0, 0, 0, 5, '%s农户自主休耕情况汇总表' % one_xz, style()[4])
        write_sheet.write(1, 0, '地块编码', style()[0])
        write_sheet.write(1, 1, '乡镇', style()[0])
        write_sheet.write(1, 2, '村', style()[0])
        write_sheet.write(1, 3, '中心经度', style()[0])
        write_sheet.write(1, 4, '中心纬度', style()[0])
        write_sheet.write(1, 5, '休耕面积(亩)', style()[0])
        write_sheet.col(0).width = 256 * 13
        write_sheet.col(1).width = 256 * 13
        write_sheet.col(2).width = 256 * 13
        write_sheet.col(3).width = 256 * 16
        write_sheet.col(4).width = 256 * 16
        write_sheet.col(5).width = 256 * 13
        tall = xlwt.easyxf('font:height 400;')
        tall_1 = xlwt.easyxf('font:height 520;')
        tall_2 = xlwt.easyxf('font:height 360')
        write_sheet.row(0).set_style(tall_1)
        write_sheet.row(1).set_style(tall)
        r = 2  # 开始行
        for one_row_cell in range(2, read_sheet.nrows):
            x_name = xzcz_dict[read_sheet.row(one_row_cell)[1].value] +read_sheet.row(one_row_cell)[1].value
            if x_name == one_xz:
                write_sheet.write(r, 0, str(int(read_sheet.row(one_row_cell)[0].value)), style()[0])
                write_sheet.write(r, 1, xzcz_dict[read_sheet.row(one_row_cell)[1].value], style()[0])
                write_sheet.write(r, 2, read_sheet.row(one_row_cell)[1].value, style()[0])
                write_sheet.write(r, 3, read_sheet.row(one_row_cell)[2].value, style()[0])
                write_sheet.write(r, 4, read_sheet.row(one_row_cell)[3].value, style()[0])
                write_sheet.write(r, 5, round(read_sheet.row(one_row_cell)[4].value, 2), style()[0])
                write_sheet.row(r).set_style(tall_2)
                r += 1
        write_sheet.write(r, 0, '合计', style()[0])
        write_sheet.write(r, 1, '-', style()[0])
        write_sheet.write(r, 2, '-', style()[0])
        write_sheet.write(r, 3, '-', style()[0])
        write_sheet.write(r, 4, '-', style()[0])
        write_sheet.write(r, 5, xlwt.Formula('SUM(F2:F%s)' % r), style()[0])
        write_sheet.row(r).set_style(tall_2)
        write_sheet.show_headers = False
        write_sheet.show_footers = False
        write_sheet.header_str = b''
        write_sheet.footer_str = b''
        write_book.save('%s.xls' % os.path.join(out_path, one_xz))
