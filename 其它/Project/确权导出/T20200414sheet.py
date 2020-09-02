# coding:utf-8
import arcpy
import xlwt
import time

start_time = time.clock()
print('开始时间：%s' % start_time)

data = "E:/T开阳县台账数据.gdb/成果数据_1"
data_list = []
with arcpy.da.SearchCursor(data, ['LBBM']) as cursor:
    for row in cursor:
        data_list.append(row[0])
    set_list = set(data_list)
data_list1 = list(set_list)
message_list = []

for bm in data_list1:
    with arcpy.da.SearchCursor(data, ['LBBM', 'FXZQMC', 'TXZQMC', 'XZQMC', 'ZLLB', 'CQCS', 'SUM_MJ_MU']) as cursor1:
        onemessage_list = []
        for row1 in cursor1:
            if row1[0] == bm:
                onemessage_list.append(row1[0])
                onemessage_list.append(row1[1])
                onemessage_list.append(row1[2])
                onemessage_list.append(row1[3])
                onemessage_list.append(row1[4])
                onemessage_list.append(row1[5])
                onemessage_list.append(row1[6])
            # elif row1[0] == bm:
            #     twomessage_list = onemessage_list
            #     twomessage_list.append(row1[5])
            #     twomessage_list.append("%.4f" % row1[6])
            # else:
            #     i = i+1
    message_list.append(onemessage_list)
workbook = xlwt.Workbook(encoding='utf-8')
ws = workbook.add_sheet('Data')
table_title = ['地块编码', '区县', '乡镇', '行政村', '质量类别', '采取措施', '面积（亩）', '采取措施', '面积（亩）', '采取措施', '面积（亩）', '采取措施', '面积（亩）']
for i in range(len(table_title)):
    ws.write(0, i, table_title[i])
r = 1  # 开始行
for data_sys in message_list:
    for length in range(len(data_sys)/7):
        if length == 0:
            for b in range(7):
                ws.write(r, b, data_sys[b])
        elif length == 1:
            for b in range(2):
                ws.write(r, b+7, data_sys[12+b])
        elif length == 2:
            for b in range(2):
                ws.write(r, b+9, data_sys[19+b])
        elif length == 3:
            for b in range(2):
                ws.write(r, b+11, data_sys[26+b])
        elif length == 3:
            for b in range(2):
                ws.write(r, b+13, data_sys[33+b])
        elif length == 3:
            for b in range(2):
                ws.write(r, b+15, data_sys[40+b])
    r = r + 1

end_time = time.clock()
times = end_time-start_time

print('结束时间：%s' % end_time)

print('耗时：%s' % times)

workbook.save('datano.xls')
