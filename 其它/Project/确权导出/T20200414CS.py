# coding:utf-8
import arcpy
import xlwt
import time

start_time = time.clock()
print('开始时间：%s' % start_time)

data = "E:/T清镇市台账数据.gdb/成果数据_1"
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

    message_list.append(onemessage_list)
workbook = xlwt.Workbook(encoding='utf-8')
ws = workbook.add_sheet('Data')
table_title = ['地块编码', '区县', '乡镇', '行政村', '质量类别', '采取措施', '面积（亩）', '采取措施', '面积（亩）', '采取措施', '面积（亩）', '采取措施', '面积（亩）', '采取措施', '面积（亩）', '任务面积', '措施F', '措施K', '措施L', '措施M', '措施N', '措施O','已完成','未完成']
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
        elif length == 4:
            for b in range(2):
                ws.write(r, b+13, data_sys[33+b])
        elif length == 5:
            for b in range(2):
                ws.write(r, b+15, data_sys[40+b])
    r = r + 1


ws.write(1, 15, xlwt.Formula('SUM(G2:O2)'))
ws.write(1, 16, '=SUMIFS(G:G,A:A,A2,F:F,"=F")+SUMIFS(I:I,A:A,A2,H:H,"=F")+SUMIFS(K:K,A:A,A2,J:J,"=F")+SUMIFS(M:M,A:A,A2,L:L,"=F")+SUMIFS(O:O,A:A,A2,N:N,"=F")')
ws.write(1, 17, '=SUMIFS(G:G,A:A,A2,F:F,"=K")+SUMIFS(I:I,A:A,A2,H:H,"=K")+SUMIFS(K:K,A:A,A2,J:J,"=K")+SUMIFS(M:M,A:A,A2,L:L,"=K")+SUMIFS(O:O,A:A,A2,N:N,"=K")')
ws.write(1, 18, '=SUMIFS(G:G,A:A,A2,F:F,"=L")+SUMIFS(I:I,A:A,A2,H:H,"=L")+SUMIFS(K:K,A:A,A2,J:J,"=L")+SUMIFS(M:M,A:A,A2,L:L,"=L")+SUMIFS(O:O,A:A,A2,N:N,"=L")')
ws.write(1, 19, '=SUMIFS(G:G,A:A,A2,F:F,"=M")+SUMIFS(I:I,A:A,A2,H:H,"=M")+SUMIFS(K:K,A:A,A2,J:J,"=M")+SUMIFS(M:M,A:A,A2,L:L,"=M")+SUMIFS(O:O,A:A,A2,N:N,"=M")')
ws.write(1, 20, '=SUMIFS(G:G,A:A,A2,F:F,"=N")+SUMIFS(I:I,A:A,A2,H:H,"=N")+SUMIFS(K:K,A:A,A2,J:J,"=N")+SUMIFS(M:M,A:A,A2,L:L,"=N")+SUMIFS(O:O,A:A,A2,N:N,"=N")')
ws.write(1, 21, '=SUMIFS(G:G,A:A,A2,F:F,"=O")+SUMIFS(I:I,A:A,A2,H:H,"=O")+SUMIFS(K:K,A:A,A2,J:J,"=O")+SUMIFS(M:M,A:A,A2,L:L,"=O")+SUMIFS(O:O,A:A,A2,N:N,"=O")')
ws.write(1, 22, xlwt.Formula('SUM(Q2:V2)'))
ws.write(1, 23, xlwt.Formula('SUM(G2:O2)-SUM(Q2:V2)'))

end_time = time.clock()

times = end_time-start_time
print('耗时：%s' % times)

workbook.save('清镇市台账数据.xls')
