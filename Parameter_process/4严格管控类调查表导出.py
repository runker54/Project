# coding:utf-8
import xlwt
import xlrd
import os


# style库
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
    a_1_font.name = u'宋体'
    a_1_font.height = 20 * 20
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


style()


def sheet(x):
    workbook = xlwt.Workbook()
    ws = workbook.add_sheet("DATA", True)
    ws.write_merge(0, 0, 0, 22, '附表1-2', style()[7])  # 附表
    ws.write_merge(1, 1, 0, 22, '严格管控类耕地调查表', style()[4])  # 标题
    # 表格头
    ws.write_merge(2, 2, 0, 4, '责任单位（盖章）：', style()[3])   # 责任单位
    ws.write_merge(3, 3, 0, 10, '责任单位负责人（盖章）：%s' % zrdwfze, style()[3])
    ws.write_merge(2, 2, 11, 16, '填表人：%s' % tbr, style()[3])
    ws.write_merge(3, 3, 11, 19, '填表日期：%s' % tbrq, style()[3])
    ws.write_merge(2, 2, 17, 22, '联系电话：%s' % lxdh, style()[3])
    ws.write_merge(3, 3, 20, 22, '单位：亩', style()[3])
    # 表格主体
    ws.write_merge(4, 5, 0, 3, '地块基本信息', style()[0])
    ws.write_merge(4, 4, 4, 6, '地块编号', style()[0])
    ws.write_merge(4, 4, 14, 16, '地理位置', style()[0])
    ws.write_merge(5, 5, 4, 6, '中心坐标', style()[0])
    ws.write_merge(5, 5, 18, 19, '面积', style()[0])
    # 主体1
    ws.write_merge(7, 28, 0, 0, '调查内容', style()[6])
    ws.write_merge(6, 6, 0, 3, '周边环境', style()[0])
    ws.write_merge(7, 11, 1, 3, '2020年作物种植情况', style()[0])
    ws.write_merge(12, 16, 1, 3, '2021年作物种植情况', style()[0])
    ws.write_merge(17, 28, 1, 3, '采取措施', style()[5])
    # 周边环境
    ws.write_merge(6, 6, 4, 15, '2公里范围内有或曾经有工矿企业、冶炼厂', style()[1])
    ws.write_merge(6, 6, 17, 19, '有', style()[11])
    ws.write_merge(6, 6, 21, 22, '无', style()[13])
    # 作物种植情况1
    for _i in [0, 5]:
        ws.write_merge(7 + _i, 8 + _i, 4, 5, '水稻', style()[0])
        ws.write_merge(9 + _i, 10 + _i, 4, 5, '油菜', style()[0])
        ws.write_merge(7 + _i, 8 + _i, 14, 15, '玉米', style()[0])
        ws.write_merge(9 + _i, 10 + _i, 14, 15, '小麦', style()[0])
        ws.write_merge(11 + _i, 11 + _i, 4, 7, '其它主要作物', style()[0])
    for _y in [0, 10]:
        for _z in [0, 5]:
            ws.write_merge(7 + _z, 7 + _z, 6 + _y, 7 + _y, '主要品种', style()[0])
            ws.write_merge(8 + _z, 8 + _z, 6 + _y, 7 + _y, '总面积', style()[0])
            ws.write_merge(9 + _z, 9 + _z, 6 + _y, 7 + _y, '主要品种', style()[0])
            ws.write_merge(10 + _z, 10 + _z, 6 + _y, 7 + _y, '总面积', style()[0])

    cs_list_0 = ['', '', '', '', '', '', '', '']
    cs_list_1 = ['种植结构调整（调整为非食用农产品）', '划定为特定农产品严格管控区', '退耕还林还草', '耕地利用变更为非农用地', '休耕', '其它措施', '', '']
    cs_list_2 = ['', '', '', '', '', '', '', '']
    for _c in range(17, 23):
        ws.write(_c, 4, '£', style()[9])  # 特殊格式
        ws.write(_c, 12, '', style()[9])  # 特殊格式
        ws.write(_c, 5, cs_list_0[_c - 17], style()[8])  # A-H
        ws.write(_c, 13, cs_list_2[_c - 17], style()[8])  # I-O
        ws.write_merge(_c, _c, 5, 15, cs_list_1[_c - 17], style()[8])  # A-H
        ws.write_merge(_c, _c, 16, 17, '面积：', style()[8])

    ws.write_merge(24, 24, 12, 19, '', style()[8])

    ws.write(25, 4, '', style()[8])
    ws.write(26, 4, '', style()[8])

    ws.write_merge(23, 23, 4, 21, '%s' % qtcsqk, style()[8])
    ws.write_merge(24, 24, 4, 21, '', style()[8])
    ws.write_merge(25, 25, 20, 21, '', style()[8])
    ws.write_merge(26, 26, 20, 21, '', style()[8])
    ws.write_merge(26, 26, 12, 13, '', style()[8])
    ws.write_merge(25, 25, 5, 19, '', style()[8])
    ws.write_merge(26, 26, 5, 8, '', style()[8])
    # 写入措施实施时间与佐证台账类型的特殊符号
    chaxun_list1 = [sssj2017, '', '', '', sssj2018, '', '', '', sssj2019, '', '', '', sssj2020]
    chaxun_list2 = [zz_picture, '', '', '', zz_video, '', '', '', zz_file, '', '', '', zz_pick]
    for _x in [0, 4, 8, 12]:
        ws.write(27, 7 + _x, '%s' % chaxun_dict[chaxun_list1[_x]], style()[12])
        ws.write(28, 7 + _x, '%s' % chaxun_dict[chaxun_list2[_x]], style()[12])
    ws.write_merge(27, 27, 4, 6, '实施时间', style()[0])
    ws.write_merge(28, 28, 4, 6, '佐证台账', style()[0])
    ws.write_merge(27, 27, 8, 10, '2018年', style()[11])
    ws.write_merge(27, 27, 12, 14, '2019年', style()[11])
    ws.write_merge(27, 27, 16, 18, '2020年', style()[11])
    ws.write_merge(27, 27, 20, 22, '2021年', style()[13])
    ws.write_merge(28, 28, 8, 10, '图片类', style()[11])
    ws.write_merge(28, 28, 12, 14, '视频类', style()[11])
    ws.write_merge(28, 28, 16, 18, '文件方案类', style()[11])
    ws.write_merge(28, 28, 20, 22, '收据发票类', style()[13])

    # ws.write(27, 19, 'R', style()[12])  # 措施实施时间2020年
    # ws.write(28, 7, 'R', style()[12])  # 佐证台账类型图片类
    # ws.write(28, 15, 'R', style()[12])  # 佐证台账类型文件方案类
    # if tghl != '':
    #     ws.write(27, 7, 'R', style()[12])  # 措施实施时间2017
    # else:
    #     pass

    # 列宽

    def col():
        ws.col(0).width = 256 * 5
        ws.col(1).width = 256 * 2
        ws.col(2).width = 256 * 3
        ws.col(3).width = 256 * 2
        ws.col(4).width = 256 * 4
        ws.col(5).width = 256 * 3
        ws.col(6).width = 256 * 5
        ws.col(7).width = 256 * 4
        ws.col(8).width = 256 * 3
        ws.col(9).width = 256 * 4
        ws.col(10).width = 256 * 4
        ws.col(11).width = 256 * 6
        ws.col(12).width = 256 * 4
        ws.col(13).width = 256 * 3
        ws.col(14).width = 256 * 4
        ws.col(15).width = 256 * 4
        ws.col(16).width = 256 * 5
        ws.col(17).width = 256 * 3
        ws.col(18).width = 256 * 3
        ws.col(19).width = 256 * 4
        ws.col(20).width = 256 * 4
        ws.col(21).width = 256 * 4
        ws.col(22).width = 256 * 6

    col()

    # 调整行高
    tall = xlwt.easyxf('font:height 400;')
    tall_1 = xlwt.easyxf('font:height 420;')
    ws.row(0).set_style(tall_1)
    ws.row(1).set_style(tall_1)
    ws.row(2).set_style(tall_1)
    ws.row(3).set_style(tall_1)
    for r_ in range(4, 30):
        ws.row(r_).set_style(tall)
    # ws.write_merge(4, 4, 7, 13, '%s' % str(int(dkbm)), style()[0])  # 地块编号
    ws.write_merge(4, 4, 7, 13, '%s' % str(dkbm), style()[0])  # 地块编号
    ws.write_merge(4, 4, 17, 22, '%s%s%s' % (qx, xz, xzc), style()[0])  # 地理位置
    ws.write_merge(5, 5, 7, 17, '北纬%s，东经%s' % (lon, lat), style()[0])  # 中心坐标
    ws.write_merge(5, 5, 20, 22, '%s' % str(rwmj), style()[0])  # 面积

    ws.write(6, 16, '%s' % zbhj1, style()[2])  # 有
    ws.write(6, 20, '%s' % zbhj2, style()[2])  # 无

    ws.write_merge(7, 7, 8, 13, '%s' % sd19, style()[0])  # 19年水稻主要品种
    ws.write_merge(7, 7, 18, 22, '%s' % ym19, style()[0])  # 19年玉米主要品种
    ws.write_merge(8, 8, 8, 13, '%s' % sd19a, style()[0])  # 19年水稻总面积
    ws.write_merge(8, 8, 18, 22, '%s' % ym19a, style()[0])  # 19年玉米总面积
    ws.write_merge(9, 9, 8, 13, '', style()[0])  #
    ws.write_merge(9, 9, 18, 22, '', style()[0])  #
    ws.write_merge(10, 10, 8, 13, '', style()[0])  #
    ws.write_merge(10, 10, 18, 22, '', style()[0])  #
    ws.write_merge(11, 11, 8, 22, '%s' % qtzyzw19, style()[0])  # 19年其他主要作物

    ws.write_merge(7 + 5, 7 + 5, 8, 13, '%s' % sd20, style()[0])  # 20年水稻主要品种
    ws.write_merge(7 + 5, 7 + 5, 18, 22, '%s' % ym20, style()[0])  # 20年玉米主要品种
    ws.write_merge(8 + 5, 8 + 5, 8, 13, '%s' % sd20a, style()[0])  # 20年水稻总面积
    ws.write_merge(8 + 5, 8 + 5, 18, 22, '%s' % ym20a, style()[0])  # 20年玉米总面积
    ws.write_merge(9 + 5, 9 + 5, 8, 13, '', style()[0])  #
    ws.write_merge(9 + 5, 9 + 5, 18, 22, '', style()[0])  #
    ws.write_merge(10 + 5, 10 + 5, 8, 13, '', style()[0])  #
    ws.write_merge(10 + 5, 10 + 5, 18, 22, '', style()[0])  #
    ws.write_merge(11 + 5, 11 + 5, 8, 22, '%s' % qtzyzw20, style()[0])  # 20年其他主要作物

    # 写入面积第一列
    for _p1 in range(17, 26):
        ws.write(_p1, 11, '', style()[8])
    # 写入面积第二列
    for _p2 in range(17, 27):
        ws.write(_p2, 22, '', style()[10])
    # 补空
    ws.write_merge(26, 26, 9, 11, '', style()[8])
    ws.write_merge(26, 26, 14, 19, '', style()[8])

    ws.write_merge(17, 17, 18, 21, '%s' % zzjgtz, style()[8])  # 种植结构调整面积
    ws.write_merge(18, 18, 18, 21, '', style()[8])  # 划定为特定农产品严格管控区面积
    ws.write_merge(19, 19, 18, 21, '%s' % tghl, style()[8])  # 退耕还林面积
    ws.write_merge(20, 20, 18, 21, '%s' % bgfgd, style()[8])  # 变更为非农用地面积
    ws.write_merge(21, 21, 18, 21, '%s' % sgmg, style()[8])  # 休耕面积
    ws.write_merge(22, 22, 18, 21, '%s' % qtcsmj, style()[8])  # 其他措施面积
    true_list = [zzjgtz, '', tghl, bgfgd, sgmg, qtcsmj]  # 写入采取措施的各项特殊符号
    for _z1, key1 in enumerate(true_list):  # 对各项措施情况写入对应特殊符号
        if key1 != '':
            cise = 'R'
            ws.write(17 + _z1, 4, cise, style()[9])
        else:
            cise = '£'
            ws.write(17 + _z1, 4, cise, style()[9])

    ws.show_headers = False  # 不显示页眉
    ws.show_footers = False  # 不显示页脚
    ws.header_str = b''
    ws.footer_str = b''
    return workbook


output_path = r"C:\Users\65680\Desktop\jiangkou"  # 输出路径

old_path = r"C:\Users\65680\Desktop\江口导表数据更新.xls"  # 表格路径

old_workbook = xlrd.open_workbook(old_path)
old_ws = old_workbook.sheet_by_index(0)
rows = old_ws.nrows

for row_num in range(1, rows):
    row = old_ws.row(row_num)
    dkbm = row[0].value
    qx = row[1].value
    xz = row[2].value
    xzc = row[3].value
    lat = row[4].value
    lon = row[5].value
    lat = str(lat)
    lon = str(lon)
    if len(lat) < 10:
        lat = str(lat) + (10 - len(lat)) * '0'
    if len(lon) < 9:
        lon = str(lon) + (9 - len(lon)) * '0'

    pztz = row[7].value
    shtj = row[8].value
    sftk = row[9].value
    ymtk = row[10].value
    jght = row[11].value
    sfg = row[12].value
    ywdh = row[13].value
    yhsf = row[14].value
    dxtk = row[15].value
    wswxf = row[16].value
    zwtq = row[17].value
    tghl = row[18].value
    bgfgd = row[19].value
    sgmg = row[20].value
    zzjgtz = row[21].value
    value_dict_qt = {'品种调整': pztz, '石灰调节': shtj, '水分调控': sftk,
                     '叶面调控': ymtk, '秸秆还田': jght, '深翻耕': sfg,
                     '原位钝化': ywdh, '优化施肥': yhsf, '定向调控': dxtk,
                     '微生物修复': wswxf, '植物提取': zwtq}
    qtcsmj = 0  # 其它措施面积
    qtcsqk_list = []  # 其它措施包含项目及面积存储list
    qtcsqk = ''  # 其它措施情况结果
    for mj_value in value_dict_qt:
        if value_dict_qt[mj_value] == '':
            mj = 0
        else:
            mj = round(float(value_dict_qt[mj_value]), 1)
            qtqk = str(mj_value) + ':' + str(value_dict_qt[mj_value]) + '，'  # 各单个措施情况
            qtcsqk_list.append(qtqk)
        qtcsmj += mj  # 累加其它措施面积
        qtcsmj = round(qtcsmj, 1)
    for one_qtqk in qtcsqk_list:
        qtcsqk += one_qtqk
    qtcsqk = f"其他措施为{qtcsqk[:len(qtcsqk)-1]}"
    if qtcsmj <= 0:
        qtcsmj = ''
    rwmj = row[26].value
    sd19 = row[27].value
    sd19a = row[28].value
    sd20 = row[29].value
    sd20a = row[30].value
    ym19 = row[31].value
    ym19a = row[32].value
    ym20 = row[33].value
    ym20a = row[34].value
    zbhj = row[35].value
    qtzyzw19 = row[36].value
    qtzyzw20 = row[37].value
    sssj2017 = row[38].value  # 实施时间2017年
    sssj2018 = row[39].value  # 实施时间2018年
    sssj2019 = row[40].value  # 实施时间2019年
    sssj2020 = row[41].value  # 实施时间2020年
    zz_picture = row[42].value  # 图片类
    zz_video = row[43].value  # 视频类
    zz_file = row[44].value  # 文件方案类
    zz_pick = row[45].value  # 收据发票类
    zrdwfze = row[46].value  # 责任单位负责人
    tbr = row[47].value  # 填表人
    lxdh = row[48].value  # 联系电话
    tbrq = row[49].value  # 填表日期
    chaxun_dict = {"是": 'R', "": '£'}  # 查询用字段
    if zbhj == "有":
        zbhj1 = 'R'
        zbhj2 = '£'
    else:
        zbhj2 = 'R'
        zbhj1 = '£'

    xzm = os.path.join(output_path, xz)
    if os.path.isdir(xzm):
        pass
    else:
        os.mkdir(xzm)
    czm = os.path.join(xzm, xz + xzc)
    if os.path.isdir(czm):
        pass
    else:
        os.mkdir(czm)
    if row[6].value == '严格管控类':
        sheet('DATA').save('%s/%s%s%s-3.xls' % (czm, xz, xzc, dkbm))
        # print(f"{int(dkbm)}")
        print(f"{dkbm}")
    else:
        print(f"{'已跳过'}")
