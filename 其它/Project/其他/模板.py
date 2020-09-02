# coding:utf-8
import xlwt
import xlrd


# style库
def style():
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
    return style1, style2, style3, style_1, style_2, style_3, style_fj


style()

AQ_workbook = xlwt.Workbook()
ws = AQ_workbook.add_sheet("DATA", True)
ws.write(0, 0, '附表1', style()[6])  # 附表
ws.write_merge(1, 1, 0, 22, '安全利用类耕地调查表', style()[3])  # 标题
# 表格头
ws.write_merge(2, 2, 0, 4, '责任单位（盖章）：')
ws.write_merge(3, 3, 0, 5, '责任单位负责人（盖章）：')
ws.write_merge(2, 2, 11, 14, '填表人：')
ws.write_merge(3, 3, 11, 13, '填表日期：')
ws.write_merge(2, 2, 17, 19, '联系电话：')
ws.write_merge(3, 3, 20, 22, '单位：亩')
# 表格主体
ws.write_merge(4, 5, 0, 3, '地块基本信息')
ws.write_merge(4, 4, 4, 6, '地块编号')
ws.write_merge(4, 4, 14, 16, '地理位置')
ws.write_merge(5, 5, 4, 6, '中心坐标')
ws.write_merge(5, 5, 18, 19, '面积')

ws.write_merge(6, 28, 0, 0, '调查内容')
ws.write_merge(6, 6, 1, 3, '周边环境')
ws.write_merge(7, 11, 1, 3, '2019年作物种植情况')
ws.write_merge(12, 16, 1, 3, '2020年作物种植情况')
ws.write_merge(17, 28, 1, 3, '采取措施')

ws.write_merge(6, 6, 4, 15, '2公里范围内有货曾经有工矿企业、冶炼厂')
ws.write(6, 17, '有')
ws.write(6, 21, '无')
for _i in [0, 5]:
    ws.write_merge(7 + _i, 8 + _i, 4, 5, '水稻')
    ws.write_merge(9 + _i, 10 + _i, 4, 5, '油菜')
    ws.write_merge(7 + _i, 8 + _i, 14, 15, '玉米')
    ws.write_merge(9 + _i, 10 + _i, 14, 15, '小麦')
    ws.write_merge(11 + _i, 11 + _i, 4, 7, '其它主要作物')
for _y in [0, 10]:
    for _z in [0, 5]:
        ws.write_merge(7 + _z, 7 + _z, 6 + _y, 7 + _y, '主要品种')
        ws.write_merge(8 + _z, 8 + _z, 6 + _y, 7 + _y, '总面积')
        ws.write_merge(9 + _z, 9 + _z, 6 + _y, 7 + _y, '主要品种')
        ws.write_merge(10 + _z, 10 + _z, 6 + _y, 7 + _y, '总面积')

cs_list_0 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
cs_list_1 = ['品种调整', '石灰调节', '水分调控', '叶面调控', '秸秆还田', '深翻耕', '原位钝化', '优化施肥']
cs_list_2 = ['I', 'J', 'K', 'L', 'M', 'N', 'O', '']
cs_list_3 = ['定向调控（土壤调理）', '微生物修复', '植物提取', '退耕还林还草', '土地利用变更为非耕地', '少耕免耕休耕', '种植结构调整', '']
for _c in range(17, 25):
    ws.write(_c, 4, '£')   # 特殊格式
    ws.write(_c, 12, '£')   # 特殊格式
    ws.write(_c, 5, cs_list_0[_c - 17])  # A-H
    ws.write(_c, 13, cs_list_2[_c - 17])  # I-O
    ws.write_merge(_c, _c, 6, 8, cs_list_1[_c - 17])  # A-H
    ws.write_merge(_c, _c, 14, 19, cs_list_3[_c - 17])  # I-O
    ws.write_merge(_c, _c, 9, 10, '面积：')
    ws.write_merge(_c, _c, 20, 21, '面积：')
ws.write(25, 4, '£')
ws.write(26, 4, '£')
ws.write_merge(25, 25, 20, 21, '面积：')
ws.write_merge(26, 26, 20, 21, '面积：')
ws.write_merge(26, 26, 12, 13, '面积：')
ws.write_merge(25, 25, 6, 19, '综合治理技术（VIP或VIP+n）')
ws.write_merge(26, 26, 6, 8, '复合措施')

for _x in [0,4,8,12]:
    ws.write(27, 7 + _x, '£')
    ws.write(28, 7 + _x, '£')
ws.write_merge(27, 27, 4, 6, '实施时间')
ws.write_merge(28, 28, 4, 6, '佐证台账')
ws.write_merge(27, 27, 8, 10, '2017年')
ws.write_merge(27, 27, 12, 14, '2018年')
ws.write_merge(27, 27, 16, 18, '2019年')
ws.write_merge(27, 27, 20, 22, '2020年')
ws.write_merge(28, 28, 8, 10, '图片类')
ws.write_merge(28, 28, 12, 14, '视频类')
ws.write_merge(28, 28, 16, 18, '文件方案类')
ws.write_merge(28, 28, 20, 22, '收据发票类')
AQ_workbook.set_height = 256*560
AQ_workbook.save(r"C:\Users\65680\Desktop\xls1.xls")
