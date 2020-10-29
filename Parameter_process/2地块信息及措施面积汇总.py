# coding:utf-8
import arcpy
import xlwt
import time
# import os
# import sys

# defaultencoding = 'utf-8'
# if sys.getdefaultencoding() != defaultencoding:
#     reload(sys)
#     sys.setdefaultencoding(defaultencoding)
start_time = time.clock()

print('开始时间：%s' % start_time)

data = r"F:\思南.gdb\T思南县消除中段1027_111_dissolve"  # 数据路径
path = r"C:\Users\65680\Desktop\SNX"  # 保存位置

data_list = []
data_list1 = []
xc_list = []

with arcpy.da.SearchCursor(data, ['LBBM', 'FXZQMC', 'TXZQMC', 'XZQMC', 'ZXLON', 'ZXLAT', 'ZLLB', 'CQCS',
                                  'SUM_MJ_MU']) as cursor:
    for row in cursor:
        data_list.append(row[0])
        list1 = [row[0], row[1], row[2], row[2] + row[3], round(row[4], 6), round(row[5], 6), row[6], row[7], row[8]]
        data_list1.append(list1)
        xc_list.append(row[2] + row[3])
data_list = list(set(data_list))
xc_list = list(set(xc_list))
message_list = []
length_list = []
for bm in data_list:
    c_bm = list(filter(lambda x: x[0] == bm, data_list1))
    lengths = len(c_bm)  # 措施数量检查
    length_list.append(lengths)
    message_list.append(c_bm)
print(max(length_list))
Max_LIST = []
for Data in message_list:
    j = 0
    b_list = []
    for oneData in Data:
        if j == 0:
            b_list = [] + oneData
        else:
            b_list.append(oneData[7])
            b_list.append(oneData[8])
        j += 1
    Max_LIST.append(b_list)

borders = xlwt.Borders()  # 为样式创建边框
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
style_4 = xlwt.XFStyle()  # 标题格式
a_1 = xlwt.Alignment()
a_1.horz = 0x02
a_1.vert = 0x01
a_1_font = xlwt.Font()
a_1_font.bold = False
a_1_font.name = u'仿宋'
a_1_font.height = 20 * 10
style_4.font = a_1_font
style_4.alignment = a_1
# style_4.alignment.wrap = 1
# style_4 = xlwt.easyxf()  # 初始化样式
style_4.borders = borders

style_1 = xlwt.XFStyle()  # 标题格式
a_1 = xlwt.Alignment()
a_1.horz = 0x02
a_1.vert = 0x01
a_1_font = xlwt.Font()
a_1_font.bold = True
a_1_font.name = u'仿宋'
a_1_font.height = 20 * 10
style_1.font = a_1_font
style_1.alignment = a_1
style_1.alignment.wrap = 1

# for cm in xc_list:
#     cm_list = filter(lambda x: x[3] == cm, Max_LIST)
workbook = xlwt.Workbook(encoding='utf-8')
ws = workbook.add_sheet('Data')
# table_title = ['地块编码', '区县', '乡镇', '行政村', '中心经度', '中心纬度', '质量类别', '措施A', '措施B', '措施C', '措施D', '措施E', '措施F', '措施G',
#                '措施H', '措施I', '措施J', '措施K', '措施L', '措施M', '措施N', '措施O', '措施VIP', '措施FH', '未完成', '已完成', '任务面积']
table_title = ['地块编码', '区县', '乡镇', '行政村', '中心经度', '中心纬度', '质量类别', '品种调整', '石灰调节', '水分调控', '叶面调控', '秸秆还田', '深翻耕',
               '原位钝化', '优化施肥',
               '定向调控', '微生物修复', '植物提取', '退耕还林还草', '变更为非耕地', '少耕免耕休耕', '种植结构调整', '其他措施', '综合治理技术', '未完成',
               '已完成', '任务面积']
for i in range(len(table_title)):
    ws.write(0, i, table_title[i], style_1)
r = 1  # 开始行
key_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'VIP', 'QT', '']
# xz = cm_list[0][2]
# cz = cm_list[0][3]
# xzpath = os.path.join(path, xz)  # 乡镇目录
# if os.path.isdir(xzpath):
#     pass
# else:
#     os.mkdir(xzpath)
# czpath = os.path.join(xzpath, cz)
# if os.path.isdir(czpath):
#     pass
# else:
#     os.mkdir(czpath)
for data_sys in Max_LIST:
    # ws.row(r).set_style(xlwt.easyxf('font:height 280;'))
    value_list = []
    for key in key_list:
        try:
            bh = data_sys.index(key)
            # lvalue = round(data_sys[bh + 1], 1)
            lvalue = data_sys[bh + 1]
        except:
            lvalue = ''
        value_list.append(lvalue)
    data_sys = data_sys[:7]
    data_sys[3] = data_sys[3][len(data_sys[2]):]
    data_sys = data_sys + value_list
    for b in range(len(data_sys)):
        ws.write(r, b, data_sys[b], style_4)
    # ws.row(0).set_style(xlwt.easyxf('font:height 320;'))
    ws.col(0).width = 256 * len(data_sys[0])
    ws.col(1).width = 256 * len(data_sys[1]) * 3
    ws.col(2).width = 256 * len(data_sys[2]) * 3
    ws.col(3).width = 256 * len(data_sys[3]) * 3
    ws.col(4).width = 256 * 10
    ws.col(5).width = 256 * 10
    ws.col(6).width = 256 * len(data_sys[6]) * 3
    ws.write(r, 25, xlwt.Formula('SUM(H%s:X%s)' % (r + 1, r + 1)), style_4)
    ws.write(r, 26, xlwt.Formula('SUM(H%s:Y%s)' % (r + 1, r + 1)), style_4)
    r = r + 1

workbook.save('%s/SNX_20201029_dissolve.xls' % path)

end_time = time.clock()
times = end_time - start_time
print('耗时：%s' % times)

