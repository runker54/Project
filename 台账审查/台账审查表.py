# coding:utf-8
import xlrd
import xlwt
import os

source_sheet_path = r'C:\Users\65680\Desktop\紫云县.xls'
out_path = r'C:\Users\65680\Desktop\赫章县台账检查'
new_work_book = xlwt.Workbook('utf-8')

read_workbook = xlrd.open_workbook(source_sheet_path)
read_sheet = read_workbook.sheet_by_index(0)
rows = read_sheet.nrows
ncols = read_sheet.ncols
df_list = []
xz_list = []
for one_row in range(1, rows):
    dkbm = read_sheet.row(one_row)[0].value
    xz = read_sheet.row(one_row)[1].value
    zllb = read_sheet.row(one_row)[2].value
    rwmj = read_sheet.row(one_row)[3].value
    a = [dkbm, xz, zllb, rwmj]
    xz_list.append(xz)
    df_list.append(a)
xz_list = list(set(xz_list))
for one_xz in xz_list:
    xz_message_list = list(filter(lambda x: x[1] == one_xz, df_list))
    print(xz_message_list)
    new_sheet = new_work_book.add_sheet("%s" % one_xz)
    r = 6
    sum_area = 0
    for one_index in xz_message_list:
        new_sheet.write(r, 0, one_index[0])
        new_sheet.write(r, 1, round(one_index[3], 1))
        new_sheet.write(r, 2, "√")
        new_sheet.write(r, 3, "√")
        new_sheet.write(r, 4, "√")
        new_sheet.write(r, 5, "√")
        new_sheet.write(r, 6, "√")
        new_sheet.write_merge(r, r, 7, 9, '完善盖章签字内容')
        new_sheet.write(r, 10, "合格")
        r += 1
        sum_area += round(one_index[3], 1)
        sum_area = round(sum_area, 1)
    new_sheet.write(r, 0, '合格性审查结果')
    new_sheet.write_merge(r, r, 1, 10,
                          f'被审查乡镇：安顺市紫云县{one_xz},'
                          f'该乡镇抽查总面积（{sum_area}）亩，完整性与合格性均合格面积（{round(sum_area*0.8)}）亩，'
                          f'合格地块占抽查总面积的比例（100）%。                                       '
                          f'注：某地块台账不完整或其中一项措施不合格，即视为不合格。')
    tall = xlwt.easyxf('font:height 900;')
    new_sheet.row(r).set_style(tall)
    new_sheet.write(r + 1, 0, '整改要求')
    new_sheet.write_merge(r + 1, r + 1, 1, 10, '1、完善调查表盖章签字；2、进一步收集相关佐证文件资料加强各措施的佐证能力。')
    new_sheet.write(r + 2, 0, '审查员签字')
    new_sheet.write_merge(r + 2, r + 2, 1, 10, '')
    new_sheet.write_merge(r + 3, r + 3, 0, 10, '注：市（州）按乡镇填写本表，确保每个乡镇均审查。辖区各县抽查不低于总任务面积的30%。')
new_work_book.save(os.path.join(out_path, '紫云县台账审查附件1.xls'))
