# coding:utf-8
import arcpy
import xlrd
import xlwt
import time

gis_data = r'D:\重点行业企业资料\重点行业企业成果集成\T520000贵州省_1031更新points.shp'
sheet_data = r'C:\Users\ols\Desktop\合并保存\关闭企业.xls'

gis_list = []
sheet_list = []
search_list = []

# 空间信息数据的点位信息获取
with arcpy.da.SearchCursor(gis_data, ["DKBM", "LXDM"]) as cursor:
    for one_row in cursor:
        if one_row[0][6] == '2':
            one_list = [one_row[0], one_row[1]]
            gis_list.append(one_list)
            search_list.append(one_row[0])
search_list = list(set(search_list))
dk_dict = {}  # 每个地块编码对应的敏感受体点及重点区域点位
for one_dk in search_list:
    dk_list = list(filter(lambda x: x[0] == one_dk, gis_list))
    one_cell_list = []
    for one_cell in dk_list:
        one_cell_list.append(one_cell[1])
    one_cell_list = set(one_cell_list)
    dk_dict[one_dk] = one_cell_list

# 表格信息中点位信息获取
work_book = xlrd.open_workbook(sheet_data)
work_sheet = work_book.sheet_by_index(0)
rows = work_sheet.nrows
cols = work_sheet.ncols
search_dict = {'地块编码': '', '生产区面积': '', '储存区面积': '', '废水治理区面积': '', '固体废物贮存或处置区面积': '',
               '幼儿园': '', '学校': '', '居民区': '', '医院': '', '集中式饮用水水源地': '', '饮用水井': '', '食用农产品产地': '',
               '自然保护区': '', '地表水体': ''}
for cell_col in range(cols):
    for search_cell in search_dict:
        if search_cell in work_sheet.cell_value(0, cell_col):
            search_dict[search_cell] = cell_col
sheet_dk_dict = {}
for cell_row in range(1, rows):
    dkbm = work_sheet.row(cell_row)[search_dict['地块编码']].value
    cell_r_list = []
    scq = work_sheet.row(cell_row)[search_dict['生产区面积']].value
    zcq = work_sheet.row(cell_row)[search_dict['储存区面积']].value
    fsq = work_sheet.row(cell_row)[search_dict['废水治理区面积']].value
    gtfw = work_sheet.row(cell_row)[search_dict['固体废物贮存或处置区面积']].value
    yey = work_sheet.row(cell_row)[search_dict['幼儿园']].value
    xx = work_sheet.row(cell_row)[search_dict['学校']].value
    jmq = work_sheet.row(cell_row)[search_dict['居民区']].value
    yy = work_sheet.row(cell_row)[search_dict['医院']].value
    jzssy = work_sheet.row(cell_row)[search_dict['集中式饮用水水源地']].value
    yysj = work_sheet.row(cell_row)[search_dict['饮用水井']].value
    syncp = work_sheet.row(cell_row)[search_dict['食用农产品产地']].value
    zrbhq = work_sheet.row(cell_row)[search_dict['自然保护区']].value
    dbst = work_sheet.row(cell_row)[search_dict['地表水体']].value
    var_list = [scq, zcq, fsq, gtfw, yey, xx, jmq, yy, jzssy, yysj, syncp, zrbhq, dbst]
    var_dict = {scq: '11', zcq: '12', fsq: '13', gtfw: '14', yey: '21', xx: '22', jmq: '23', yy: '24', jzssy: '25',
                yysj: '26', syncp: '27', zrbhq: '28', dbst: '29'}
    for one_var in var_list:
        if one_var != 0 or one_var != ' ':
            cell_r_list.append(var_dict[one_var])
        else:
            pass
    cell_r_list = set(cell_r_list)
    sheet_dk_dict[dkbm] = cell_r_list

new_work_book = xlwt.Workbook('utf-8')
ws = new_work_book.add_sheet('结果比较')
ws.write(0, 0, '地块编码')
ws.write(0, 1, '对比结果')
r = 1
for one_check in search_list:
    check_end = dk_dict[one_check] ^ sheet_dk_dict[one_check]
    check_end_text = ''
    for one_text in check_end:
        one_text = one_text + ' '
        check_end_text += one_text
    ws.write(r, 0, one_check)
    ws.write(r, 1, check_end_text)
    r += 1
new_work_book.save(r'C:\Users\ols\Desktop\chek_out\结果.xls')
