# coding: UTF-8
import os
import xlwt
import xlrd


def moban(name):
    workbook = xlwt.Workbook(encoding='utf-8')
    ws = workbook.add_sheet(name, True)
    # 格式库

    # 边框(四面实线)
    borders = xlwt.Borders()
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    # 边框(右无)
    borders1 = xlwt.Borders()
    borders1.left = xlwt.Borders.THIN
    borders1.right = xlwt.Borders.NO_LINE
    borders1.top = xlwt.Borders.THIN
    borders1.bottom = xlwt.Borders.THIN
    # 边框(右无，下虚)
    borders2 = xlwt.Borders()
    borders2.left = xlwt.Borders.THIN
    borders2.right = xlwt.Borders.NO_LINE
    borders2.top = xlwt.Borders.THIN
    borders2.bottom = xlwt.Borders.MEDIUM
    # 边框(左无，下虚)
    borders3 = xlwt.Borders()
    borders3.left = xlwt.Borders.NO_LINE
    borders3.right = xlwt.Borders.THIN
    borders3.top = xlwt.Borders.THIN
    borders3.bottom = xlwt.Borders.MEDIUM
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

    ws.write_merge(0, 0, 0, 12, '附件1-2', style_fj)

    ws.write_merge(1, 1, 0, 12, '严格管控类耕地调查表', style_1)  # 合并单元格

    ws.write_merge(2, 2, 0, 3, '责任单位（盖章）：', style4)
    ws.write_merge(2, 2, 5, 8, '填表人：', style4)
    ws.write_merge(2, 2, 9, 12, '联系电话：', style4)

    ws.write_merge(3, 3, 0, 3, '责任单位负责人（盖章）：', style4)
    ws.write_merge(3, 3, 5, 10, '填表日期：', style4)
    ws.write(3, 11, '单位：亩', style4)

    ws.write_merge(4, 5, 0, 1, '地块基本信息', style1)
    ws.write(4, 2, '地块编号', style1)

    ws.write(4, 7, '地理位置', style1)

    ws.write(5, 2, '中心坐标', style1)

    ws.write(5, 10, '面积', style1)

    ws.write_merge(7, 28, 0, 0, '调          查          内          容', style_3)
    ws.write_merge(6, 6, 0, 1, '周边环境', style1)
    ws.write_merge(6, 6, 2, 8, '2公里范围内有或曾经有工矿企业、冶炼场', style2)
    # 周边环境
    style_zbhj = xlwt.XFStyle()
    a2 = xlwt.Alignment()
    a2.vert = 0x01
    a2.horz = 0x02
    a_5_font = xlwt.Font()
    a_5_font.name = 'Wingdings 2'
    a_5_font.height = 20 * 12
    style_zbhj.font = a_5_font
    style_zbhj.alignment = a2
    style_zbhj.borders = borders1
    style_zbhj.alignment.wrap = 1
    ws.write(6, 9, '%s' % zbhj1, style3)
    ws.write(6, 10, '有', style1)
    ws.write(6, 11, '%s' % zbhj2, style3)
    ws.write(6, 12, '无', style1)

    ws.write_merge(7, 11, 1, 1, '2019年作物种植情况', style1)
    ws.write_merge(7, 8, 2, 2, '水稻', style1)
    ws.write(7, 3, '主要品种', style1)
    ws.write_merge(7, 7, 4, 6, '%s' % sd19, style1)
    ws.write_merge(7, 8, 7, 7, '玉米', style1)
    ws.write(7, 8, '主要品种', style1)
    ws.write_merge(7, 7, 9, 12, '%s' % ym19, style1)
    ws.write(8, 3, '总面积', style1)
    ws.write_merge(8, 8, 4, 6, '%s' % sd19a, style1)
    ws.write(8, 8, '总面积', style1)
    ws.write_merge(8, 8, 9, 12, '%s' % ym19a, style1)
    ws.write_merge(9, 10, 2, 2, '油菜', style1)
    ws.write(9, 3, '主要品种', style1)
    ws.write_merge(9, 9, 4, 6, '', style1)
    ws.write_merge(9, 10, 7, 7, '小麦', style1)
    ws.write(9, 8, '主要品种', style1)
    ws.write_merge(9, 9, 9, 12, '', style1)
    ws.write(10, 3, '总面积', style1)
    ws.write_merge(10, 10, 4, 6, '', style1)
    ws.write(10, 8, '总面积', style1)
    ws.write_merge(10, 10, 9, 12, '', style1)
    ws.write_merge(11, 11, 2, 3, '其他主要作物', style1)
    ws.write_merge(11, 11, 4, 12, '', style1)

    ws.write_merge(12, 16, 1, 1, '2020年作物种植情况', style1)
    ws.write_merge(12, 13, 2, 2, '水稻', style1)
    ws.write(12, 3, '主要品种', style1)
    ws.write_merge(12, 12, 4, 6, '%s' % sd20 , style1)
    ws.write_merge(12, 13, 7, 7, '玉米', style1)
    ws.write(12, 8, '主要品种', style1)
    ws.write_merge(12, 12, 9, 12, '%s' % ym20, style1)
    ws.write(13, 3, '总面积', style1)
    ws.write_merge(13, 13, 4, 6, '%s' % sd20a, style1)
    ws.write(13, 8, '总面积', style1)
    ws.write_merge(13, 13, 9, 12, '%s' % ym20a, style1)
    ws.write_merge(14, 15, 2, 2, '油菜', style1)
    ws.write(14, 3, '主要品种', style1)
    ws.write_merge(14, 14, 4, 6, '', style1)
    ws.write_merge(14, 15, 7, 7, '小麦', style1)
    ws.write(14, 8, '主要品种', style1)
    ws.write_merge(14, 14, 9, 12, '', style1)
    ws.write(15, 3, '总面积', style1)
    ws.write_merge(15, 15, 4, 6, '', style1)
    ws.write(15, 8, '总面积', style1)
    ws.write_merge(15, 15, 9, 12, '', style1)
    ws.write_merge(16, 16, 2, 3, '其他主要作物', style1)
    ws.write_merge(16, 16, 4, 12, '%s' % qtzyzw, style1)

    ws.write_merge(17, 28, 1, 1, '采      取      措      施', style_2)
    ws.write_merge(17, 17, 3, 9, '种植结构调整', style2)
    ws.write(17, 10, '面积：', style1)
    ws.write_merge(18, 18, 3, 9, '划定为特定农产品严格管控区', style2)
    ws.write(18, 10, '面积：', style1)
    ws.write_merge(19, 19, 3, 9, '退耕还林还草', style2)
    ws.write(19, 10, '面积：', style1)
    ws.write_merge(20, 20, 3, 9, '耕地利用变更为非耕地', style2)
    ws.write(20, 10, '面积：', style1)
    ws.write_merge(21, 21, 3, 9, '休耕', style2)
    ws.write(21, 10, '面积：', style1)
    ws.write_merge(22, 22, 3, 9, '其它措施', style2)
    ws.write(22, 10, '面积：', style1)

    ws.write(27, 2, '实施时间', style1)
    ws.write(27, 3, '£', style3)
    ws.write(28, 2, '佐证台账', style1)
    ws.write(28, 3, '£', style3)

    ws.write(27, 4, '2017年', style1)
    ws.write(27, 5, '£', style3)
    ws.write(28, 4, '图片类', style1)
    ws.write(28, 5, '£', style3)

    ws.write(27, 6, '2018年', style1)
    ws.write(27, 7, '£', style3)
    ws.write(28, 6, '视频类', style1)
    ws.write(28, 7, 'R', style3)

    ws.write_merge(27, 27, 8, 9, '2019年', style1)
    ws.write(27, 10, 'R', style3)
    ws.write_merge(28, 28, 8, 9, '文件方案类', style1)
    ws.write(28, 10, '£', style3)

    ws.write_merge(27, 27, 11, 12, '2020年', style1)
    ws.write_merge(28, 28, 11, 12, '收据发票类', style1)
    for _x in range(17, 24):
        ws.write(_x, 2, '£', style3)

    ws.write_merge(23, 23, 2, 12, '', style1)
    ws.write_merge(24, 24, 2, 12, '', style1)
    ws.write_merge(25, 25, 2, 12, '', style1)
    ws.write_merge(26, 26, 2, 12, '', style1)
    # 写入面积2
    ws.write_merge(17, 17, 11, 12, '%s' % zzjgtz, style1)
    ws.write_merge(18, 18, 11, 12, '%s' % '', style1)
    ws.write_merge(19, 19, 11, 12, '%s' % tghl, style1)
    ws.write_merge(20, 20, 11, 12, '%s' % bgfgd, style1)
    ws.write_merge(21, 21, 11, 12, '%s' % sgmg, style1)
    ws.write_merge(22, 22, 11, 12, '%s' % sfg, style1)

    if zzjgtz != '':
        ws.write(17, 2, 'R', style3)
    if tghl != '':
        ws.write(19, 2, 'R', style3)
    if bgfgd != '':
        ws.write(20, 2, 'R', style3)
    if sgmg != '':
        ws.write(21, 2, 'R', style3)

    # 地块编号
    ws.write_merge(4, 4, 3, 6, '{}'.format(dkbm), style1)
    # 地理位置
    ws.write_merge(4, 4, 8, 12, '{}{}{}'.format(qx, xz, xzc), style1)
    # 中心坐标
    ws.write_merge(5, 5, 3, 9, '北纬{},东经{}'.format(lon, lat), style1)
    # 面积
    ws.write_merge(5, 5, 11, 12, rwmj, style1)


    # 调整列宽
    ws.col(0).width = 256 * 6
    ws.col(1).width = 256 * 7
    ws.col(3).width = 256 * 10
    ws.col(4).width = 256 * 7
    ws.col(5).width = 256 * 8
    ws.col(6).width = 256 * 8
    ws.col(9).width = 256 * 4
    ws.col(10).width = 256 * 7
    ws.col(11).width = 256 * 4
    ws.col(12).width = 256 * 7

    # 调整行高
    tall = xlwt.easyxf('font:height 400;')
    tall_1 = xlwt.easyxf('font:height 420;')
    ws.row(0).set_style(tall_1)
    ws.row(1).set_style(tall_1)
    ws.row(2).set_style(tall_1)
    ws.row(3).set_style(tall_1)
    for r_ in range(4, 30):
        ws.row(r_).set_style(tall)
    ws.show_headers = False
    ws.show_footers = False
    ws.header_str = b''
    ws.footer_str = b''
    return workbook


output_path = r'C:\Users\65680\Desktop\TP'

old_path = r'C:\Users\65680\Desktop\清镇市\措施总表.xls'

old_workbook = xlrd.open_workbook(old_path)
old_ws = old_workbook.sheet_by_index(3)
rows = old_ws.nrows
for row_num in range(1, rows):
    row = old_ws.row(row_num)
    dkbm = row[0].value
    qx = row[1].value
    xz = row[2].value
    xzc = row[3].value
    lat = round(row[4].value, 6)
    lon = round(row[5].value, 6)
    try:
        pztz = round(row[7].value, 1)
        shtj = round(row[8].value, 1)
        sftk = round(row[9].value, 1)
        ymtk = round(row[10].value, 1)
        jght = round(row[11].value, 1)
        sfg = round(row[12].value, 1)
        ywdh = round(row[13].value, 1)
        yhsf = round(row[14].value, 1)
        dxtk = round(row[15].value, 1)
        wswxf = round(row[16].value, 1)
        zwtq = round(row[17].value, 1)
        tghl = round(row[18].value, 1)
        bgfgd = round(row[19].value, 1)
        sgmg = round(row[20].value, 1)
        zzjgtz = round(row[21].value, 1)
        ywc = round(row[25].value, 1)
        rwmj = round(row[26].value, 1)
    except:
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
        ywc = row[25].value
        rwmj = row[26].value
        sd19 = row[31].value
        sd19a = row[32].value
        ym19 = row[27].value
        ym19a = row[28].value
        sd20 = row[33].value
        sd20a = row[34].value
        ym20 = row[29].value
        ym20a = row[30].value
        qtzyzw = row[35].value
        zbhj = row[36].value
        if zbhj == "有":
            zbhj1 = 'R'
            zbhj2 = '£'
        else:
            zbhj2 = 'R'
            zbhj1 = '£'
    count_list = [pztz, shtj, sftk, ymtk, jght, sfg, ywdh, yhsf, dxtk, wswxf, zwtq, tghl, bgfgd, sgmg, zzjgtz]
    dz_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
               12: 'M', 13: 'N', 14: 'O', }
    cssl = 0  # 采取措施数量
    idset = []  # 对应编号收集
    morecs = ''  # 复合措施编码
    cs1_pd = ''  # 初始化措施查询值
    cs = {'A': '', 'B': '', 'C': '', 'D': '', 'E': '', 'F': '', 'G': '', 'H': '', 'I': '', 'J': '', 'K': '', 'L': '',
          'M': '', 'N': '', 'O': '', 'ZH': '', 'FH': ''}
    for _id, _count in enumerate(count_list):
        if _count != '':
            cssl += 1
            idset.append(_id)
    if cssl > 1:
        cs['FH'] = 'R'
        for _cs in idset:
            onecs = dz_dict[_cs]
            morecs = morecs + onecs + '+'
        morecs = morecs[:-1]
    else:
        try:
            cs1_pd = dz_dict[idset[0]]
            ywc = ''
        except:
            pass

    xzm = os.path.join(output_path, xz)
    if os.path.isdir(xzm):
        pass
    else:
        os.mkdir(xzm)
    czm = os.path.join(xzm, xz+xzc)
    if os.path.isdir(czm):
        pass
    else:
        os.mkdir(czm)
    moban("data").save('%s/%s%s%s-3.xls' % (czm, xz, xzc, dkbm))

    print(f"{dkbm}")








