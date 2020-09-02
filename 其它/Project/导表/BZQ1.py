# coding:utf8
import xlrd
import xlwt
import sys

# defaultencoding = 'utf-8'
# if sys.getdefaultencoding() != defaultencoding:
#     reload(sys)
#     sys.setdefaultencoding(defaultencoding)

data = ur'C:/Users/Administrator/Desktop/YG.xls'
out_path = 'C:/Users/Administrator/Desktop/PQ'

old_book = xlrd.open_workbook(data)
old_sheet = old_book.sheet_by_index(0)
nrows = old_sheet.nrows
data_list = []
key_list = []
for yaosu in range(2, nrows):
    key = old_sheet.cell_value(yaosu, 3)
    key1 = old_sheet.cell_value(yaosu, 4)
    key2 = key + key1
    key_list.append(key2)
    one_list = [old_sheet.cell_value(yaosu, 1), key, key2,
                old_sheet.cell_value(yaosu, 5), round(old_sheet.cell_value(yaosu, 6), 1),
                round(old_sheet.cell_value(yaosu, 7), 6),
                round(old_sheet.cell_value(yaosu, 8), 6),
                old_sheet.cell_value(yaosu, 9), round(old_sheet.cell_value(yaosu, 10), 1),
                round(old_sheet.cell_value(yaosu, 11), 1),
                round(old_sheet.cell_value(yaosu, 12), 1), round(old_sheet.cell_value(yaosu, 13), 1),
                round(old_sheet.cell_value(yaosu, 14), 1),
                round(old_sheet.cell_value(yaosu, 15), 1)]

    data_list.append(one_list)
ys_list = list(set(key_list))

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

style_2 = xlwt.easyxf()  # 初始化样式
a_1 = xlwt.Alignment()
a_1.horz = 0x02
a_1.vert = 0x01
a_1_font = xlwt.Font()
a_1_font.name = u'宋体'
a_1_font.bold = True
a_1_font.height = 20 * 10
style_2.font = a_1_font
style_2.alignment = a_1
style_2.borders = borders
style_2.alignment.wrap = 1
style_2.borders = borders

name = 1

for ys in ys_list:
    new_book = xlwt.Workbook(encoding='utf-8')
    ws = new_book.add_sheet("Data")
    ws.write_merge(0, 0, 0, 14, '遵义市播州区{}严格管控任务分解表'.format(ys.encode("utf-8")), style_1)
    ws.write_merge(1, 2, 0, 0, '序号', style_2)
    ws.write_merge(1, 2, 1, 1, '地块编号', style_2)
    ws.write_merge(1, 2, 2, 2, '乡镇（街道）', style_2)
    ws.write_merge(1, 2, 3, 3, '行政村', style_2)
    ws.write_merge(1, 2, 4, 4, '质量类别', style_2)
    ws.write_merge(1, 2, 5, 5, '面积（亩）', style_2)
    ws.write_merge(1, 2, 6, 6, '中心经度', style_2)
    ws.write_merge(1, 2, 7, 7, '中心纬度', style_2)
    ws.write_merge(1, 2, 8, 8, '任务年度', style_2)
    ws.write_merge(1, 1, 9, 13, '已完成（亩）', style_2)
    ws.write(2, 9, '措施F（土地整治）', style_2)
    ws.write(2, 10, '措施K（退耕还林还草）', style_2)
    ws.write(2, 11, '措施L（转非耕地）', style_2)
    ws.write(2, 12, '措施N（种植结构调整）', style_2)
    ws.write(2, 13, '小计', style_2)
    ws.write_merge(1, 2, 14, 14, '未完成（亩）', style_2)
    ys_name_list = filter(lambda x: x[2] == ys, data_list)
    p = 3  # 开始行
    for one_data in ys_name_list:
        one_data[2] = one_data[2][len(one_data[1]):]
        ws.write(p, 0, p - 2, style_4)
        for b in range(len(one_data)):
            ws.write(p, b + 1, one_data[b], style_4)
        p += 1
    ws.write_merge(len(ys_name_list) + 3, len(ys_name_list) + 3, 0, 4, '合计', style_2)
    ws.write(len(ys_name_list) + 3, 5, xlwt.Formula('SUM(F4:F%s)' % (len(ys_name_list) + 3)), style_2)
    ws.write(len(ys_name_list) + 3, 6, '-', style_2)
    ws.write(len(ys_name_list) + 3, 7, '-', style_2)
    ws.write(len(ys_name_list) + 3, 8, '-', style_2)
    ws.write(len(ys_name_list) + 3, 9, xlwt.Formula('SUM(J4:J%s)' % (len(ys_name_list) + 3)), style_2)
    ws.write(len(ys_name_list) + 3, 10, xlwt.Formula('SUM(K4:K%s)' % (len(ys_name_list) + 3)), style_2)
    ws.write(len(ys_name_list) + 3, 11, xlwt.Formula('SUM(L4:L%s)' % (len(ys_name_list) + 3)), style_2)
    ws.write(len(ys_name_list) + 3, 12, xlwt.Formula('SUM(M4:M%s)' % (len(ys_name_list) + 3)), style_2)
    ws.write(len(ys_name_list) + 3, 13, xlwt.Formula('SUM(N4:N%s)' % (len(ys_name_list) + 3)), style_2)
    ws.write(len(ys_name_list) + 3, 14, xlwt.Formula('SUM(O4:O%s)' % (len(ys_name_list) + 3)), style_2)

    ws.col(0).width = 256 * 5
    ws.col(1).width = 256 * 13
    ws.col(2).width = 256 * 13
    ws.col(3).width = 256 * 8
    ws.col(4).width = 256 * 10
    ws.col(5).width = 256 * 8
    ws.col(6).width = 256 * 10
    ws.col(7).width = 256 * 10
    ws.col(8).width = 256 * 6
    ws.col(9).width = 256 * 10
    ws.col(10).width = 256 * 10
    ws.col(11).width = 256 * 10
    ws.col(12).width = 256 * 10
    ws.col(13).width = 256 * 8
    ws.col(14).width = 256 * 8
    new_book.save("%s/%s-3.xls" % (out_path, ys))
    name += 1
