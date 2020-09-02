# coding:utf-8
import arcpy.da
import xlrd
data_path = r'E:\台账\织金县\织金县20200814验证\织金县20200831处理.gdb\T无措施数据合并20200831'
sheet_path = r'C:\Users\65680\Desktop\织金县合并2.xls'
work_book = xlrd.open_workbook(sheet_path)
for i in [0]:
    ws = work_book.sheet_by_index(i)
    rows = ws.nrows
    print("*****************************************")
    print(rows)
    cx_dict = {}
    for row_1 in range(1, rows):
        key = str(ws.row(row_1)[0].value).strip()
        cx_dict[key] = row_1
    with arcpy.da.UpdateCursor(data_path,
                               ['BSBM', 'CQCS', '玉米19年', '玉米20年', '水稻19年', '水稻20年', '主要作物19年', '主要作物20年', '周边环境',
                                '水稻19年面积', '水稻20年面积', '玉米19年面积', '玉米20年面积', 'MJ_MU_QQ']) as currsor:
        ic = 0
        for row in currsor:
            try:
                print('-----')
                print(row[0])
                row_temp = cx_dict[row[0]]
                row_sheet = ws.row(row_temp)
                print(row_sheet[0].value)
                print('+++++')
                row[1] = row_sheet[4].value  # CQCS
                row[2] = row_sheet[5].value  # 玉米19
                row[3] = row_sheet[6].value  # 玉米20
                row[4] = row_sheet[7].value  # 水稻19
                row[5] = row_sheet[8].value  # 水稻20
                row[6] = row_sheet[9].value  # 主要19
                row[7] = row_sheet[10].value  # 主要20
                row[8] = row_sheet[11].value  # 周边环境
                # mj = row_sheet[12].value       # 地块面积
                if row_sheet[7].value != "":
                    row[9] = row[13]
                else:
                    row[9] = 0
                if row_sheet[8].value != "":
                    row[10] = row[13]
                else:
                    row[10] = 0
                if row_sheet[5].value != "":
                    row[11] = row[13]
                else:
                    row[11] = 0
                if row_sheet[6].value != "":
                    row[12] = row[13]
                else:
                    row[12] = 0
                currsor.updateRow(row)
                ic += 1
            except:
                print("该%s未在表中" % row[0])
    print("9999999999999999999999999999999999999999999")
    print(ic)
