# coding: utf-8
import xlwt
import os
import sys

reload(sys)

sys.setdefaultencoding('utf-8')
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

workbook = xlwt.Workbook(encoding='utf-8')  # 新建Excel
ws = workbook.add_sheet('data')  # Excel新增Sheet

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

ws.write_merge(0, 0, 0, 21, '清镇市农耕地植情况调查表' , style_1)
ws.write_merge(1, 1, 0, 1, '填报单位（盖章）：', style_3)
ws.write_merge(1, 1, 4, 5, '填报人：', style_3)
ws.write_merge(1, 1, 9, 12, '电话：', style_3)
ws.write_merge(1, 1, 17, 18, '填报时间：', style_3)
ws.write_merge(2, 4, 0, 0, '序号', style_2)
ws.write_merge(2, 4, 1, 1, '地块编号', style_2)
ws.write_merge(2, 4, 2, 2, '村', style_2)
ws.write_merge(2, 4, 3, 3, '组', style_2)
ws.write_merge(2, 4, 4, 4, '农户姓名', style_2)
ws.write_merge(2, 4, 5, 5, '地块名称', style_2)
ws.write_merge(2, 4, 6, 6, '面积合计', style_2)
ws.write_merge(2, 2, 7, 18, '种植品种', style_2)
ws.write_merge(2, 2, 19, 20, '其他', style_2)
ws.write_merge(2, 4, 21, 21, '备注', style_2)
ws.write_merge(3, 3, 7, 8, '水稻', style_2)
ws.write_merge(3, 3, 9, 10, '玉米', style_2)
ws.write(4, 7, '2019年', style_2)
ws.write(4, 8, '2019年', style_2)
ws.write(4, 9, '2020年', style_2)
ws.write(4, 10, '2020年', style_2)
ws.write_merge(3, 4, 11, 11, '蔬菜', style_2)
ws.write_merge(3, 4, 12, 12, '果树', style_2)
ws.write_merge(3, 4, 13, 13, '中药材', style_2)
ws.write_merge(3, 4, 14, 14, '茶叶', style_2)
ws.write_merge(3, 4, 15, 15, '林木', style_2)
ws.write_merge(3, 4, 16, 16, '烤烟', style_2)
ws.write_merge(3, 4, 17, 17, '豆类', style_2)
ws.write_merge(3, 4, 18, 18, '薯类', style_2)
ws.write_merge(3, 4, 19, 19, '休耕', style_2)
ws.write_merge(3, 4, 20, 20, '变非耕地', style_2)

ws.write_merge(5, 5, 0, 6, '合计', style_2)
ws.write(5, 8, '', style_2)
ws.write(5, 9, '', style_2)
ws.write(5, 10, '', style_2)
ws.write(5, 11, '', style_2)
ws.write(5, 12, '', style_2)
ws.write(5, 13, '', style_2)
ws.write(5, 14, '', style_2)
ws.write(5, 15, '', style_2)
ws.write(5, 16, '', style_2)
ws.write(5, 17, '', style_2)
ws.write(5, 18, '', style_2)
ws.write(5, 19, '', style_2)
ws.write(5, 20, '', style_2)
ws.write(5, 21, '', style_2)
ws.write_merge(5, 5, 7, 7, xlwt.Formula('SUM(G6:G60000)'), style_2)






# ws.write_merge(2, 2, 7, 15, '作物类型', style_2)
# ws.write_merge(3, 3, 7, 8, '水稻品种', style_2)
# ws.write_merge(3, 3, 9, 10, '玉米品种', style_2)



# ws.col(11).width = 256 * 3
# ws.write_merge(3, 4, 11, 11, '蔬菜', style_2)
# ws.col(12).width = 256 * 3
# ws.write_merge(3, 4, 12, 12, '烤烟', style_2)
# ws.col(13).width = 256 * 3
# ws.write_merge(3, 4, 13, 13, '果树', style_2)
# ws.col(14).width = 256 * 3
# ws.write_merge(3, 4, 14, 14, '茶叶', style_2)
# ws.col(15).width = 256 * 3
# ws.write_merge(3, 4, 15, 15, '其他', style_2)
# ws.col(7).width = 256 * 7
# ws.write(4, 7, '2019年', style_2)
# ws.col(8).width = 256 * 7
# ws.write(4, 8, '2020年', style_2)
# ws.col(9).width = 256 * 7
# ws.write(4, 9, '2019年', style_2)
# ws.col(10).width = 256 * 7
# ws.write(4, 10, '2020年', style_2)

workbook.save("penta.xls")