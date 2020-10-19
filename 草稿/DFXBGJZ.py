# coding: gbk
import xlwt
import xlrd
import os


def auto(data, _path):
    old_workbook = xlrd.open_workbook(data)
    old_sheet = old_workbook.sheet_by_index(0)
    new_workbook = xlwt.Workbook(encoding="utf-8")
    new_sheet = new_workbook.add_sheet(old_sheet.name)
    old_r = 5  # 开始行
    new_r = 1  # 开始行
    new_sheet.write(0, 0, '地块编号')
    new_sheet.write(0, 1, '面积')
    new_sheet.write(0, 2, '措施')
    new_sheet.write(0, 3, '周边环境')
    new_sheet.write(0, 4, '备注')
    for _i in range(old_r, old_sheet.nrows):
        choice = old_sheet.row(_i)
        print(len(choice))
        choice_2019 = choice[5:8]
        choice_2020 = choice[8:25]
        if (choice_2019[0].value != "") and (choice_2019[0].value == choice_2020[0].value):
            measures = "品种调整"
        elif (choice_2019[1].value != "") and (choice_2019[1].value == choice_2020[1].value):
            measures = "品种调整"
        elif choice_2020[11].value != "":
            measures = "休耕"
        elif choice_2020[13].value != "":
            measures = "非耕地"
        else:
            measures = "种植结构调整"
        environment = choice_2020[14].value
        note = choice_2020[15].value
        old_value_bm = old_sheet.cell_value(_i, 1)  # 编码
        old_value_mj = old_sheet.cell_value(_i, 4)  # 面积
        new_sheet.write(new_r, 0, old_value_bm)  # 写入编码
        new_sheet.write(new_r, 1, old_value_mj)  # 写入面积
        new_sheet.write(new_r, 2, measures)  # 写入措施
        new_sheet.write(new_r, 3, environment)  # 写入周边环境
        new_sheet.write(new_r, 4, note)  # 写入备注
        new_r += 1
    new_workbook.save(os.path.join(_path, file))


path = "C:\\Users\\65680\\Desktop\\新建文件夹\\"  # 表格所在路径
output_path = "C:\\Users\\65680\\Desktop\\CK\\"

for roots, dirs, files in os.walk(path):
    for file in files:
        data_path = os.path.join(roots, file)
        if data_path[-3:].lower() == "xls":
            print(data_path)
            auto(data_path, output_path)
