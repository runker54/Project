# coding:utf-8
import arcpy
import xlwt
import time

start_time = time.clock()

print('开始时间：%s' % start_time)

data = "E:/T紫云县台账数据库.gdb/成果数据"
data_list = []
data_list1 = []

with arcpy.da.SearchCursor(data, ['LBBM', 'FXZQMC', 'TXZQMC', 'XZQMC', 'ZXLON', 'ZXLAT', 'ZLLB', 'CQCS',
                                  'SUM_MJ_MU']) as cursor:
    for row in cursor:
        data_list.append(row[0])
        list1 = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
        data_list1.append(list1)
data_list = list(set(data_list))

message_list = []
length_list = []
for bm in data_list:
    c_bm = filter(lambda x: x[0] == bm, data_list1)

    lengths = len(c_bm)  # 措施数量检查
    # print（lengths）
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

workbook = xlwt.Workbook(encoding='utf-8')

ws = workbook.add_sheet('Data')

table_title = ['地块编码', '区县', '乡镇', '行政村', '中心经度', '中心纬度', '质量类别', '采取措施', '面积（亩）', '采取措施',
               '面积（亩）', '采取措施', '面积（亩）', '采取措施', '面积（亩）', '采取措施', '面积（亩）', '任务面积', '措施A',
               '措施B', '措施C', '措施D', '措施E', '措施F', '措施G', '措施H', '措施I','措施J', '措施K', '措施L', '措施M',
               '措施N', '措施O', '措施VIP', '措施FH', '已完成', '未完成']
for i in range(len(table_title)):
    ws.write(0, i, table_title[i])

r = 1  # 开始行

for data_sys in Max_LIST:
    for b in range(len(data_sys)):
        ws.write(r, b, data_sys[b])
    r = r + 1

ws.write(1, 17, xlwt.Formula('SUM(I2:Q2)'))

ws.write(1, 18,
         '=SUMIFS(Q:Q,A:A,A2,F:F,"=A")+SUMIFS(I:I,A:A,A2,H:H,"=A")+SUMIFS(K:K,A:A,A2,J:J,"=A")+SUMIFS(M:M,A:A,A2,L:L,'
         '"=A")+SUMIFS(O:O,A:A,A2,N:N,"=A")')
ws.write(1, 19,
         '=SUMIFS(Q:Q,A:A,A2,F:F,"=B")+SUMIFS(I:I,A:A,A2,H:H,"=B")+SUMIFS(K:K,A:A,A2,J:J,"=B")+SUMIFS(M:M,A:A,A2,L:L,'
         '"=B")+SUMIFS(O:O,A:A,A2,N:N,"=B")')
ws.write(1, 20,
         '=SUMIFS(Q:Q,A:A,A2,F:F,"=C")+SUMIFS(I:I,A:A,A2,H:H,"=C")+SUMIFS(K:K,A:A,A2,J:J,"=C")+SUMIFS(M:M,A:A,A2,L:L,'
         '"=C")+SUMIFS(O:O,A:A,A2,N:N,"=C")')
ws.write(1, 21,
         '=SUMIFS(Q:Q,A:A,A2,F:F,"=D")+SUMIFS(I:I,A:A,A2,H:H,"=D")+SUMIFS(K:K,A:A,A2,J:J,"=D")+SUMIFS(M:M,A:A,A2,L:L,'
         '"=D")+SUMIFS(O:O,A:A,A2,N:N,"=D")')
ws.write(1, 22,
         '=SUMIFS(Q:Q,A:A,A2,F:F,"=E")+SUMIFS(I:I,A:A,A2,H:H,"=E")+SUMIFS(K:K,A:A,A2,J:J,"=E")+SUMIFS(M:M,A:A,A2,L:L,'
         '"=E")+SUMIFS(O:O,A:A,A2,N:N,"=E")')
ws.write(1, 23,
         '=SUMIFS(Q:Q,A:A,A2,F:F,"=F")+SUMIFS(I:I,A:A,A2,H:H,"=F")+SUMIFS(K:K,A:A,A2,J:J,"=F")+SUMIFS(M:M,A:A,A2,L:L,'
         '"=F")+SUMIFS(O:O,A:A,A2,N:N,"=F")')
ws.write(1, 24,
         '=SUMIFS(Q:Q,A:A,A2,F:F,"=G")+SUMIFS(I:I,A:A,A2,H:H,"=G")+SUMIFS(K:K,A:A,A2,J:J,"=G")+SUMIFS(M:M,A:A,A2,L:L,'
         '"=G")+SUMIFS(O:O,A:A,A2,N:N,"=G")')
ws.write(1, 25,
         '=SUMIFS(Q:Q,A:A,A2,F:F,"=H")+SUMIFS(I:I,A:A,A2,H:H,"=H")+SUMIFS(K:K,A:A,A2,J:J,"=H")+SUMIFS(M:M,A:A,A2,L:L,'
         '"=H")+SUMIFS(O:O,A:A,A2,N:N,"=H")')
ws.write(1, 26,
         '=SUMIFS(Q:Q,A:A,A2,F:F,"=I")+SUMIFS(I:I,A:A,A2,H:H,"=I")+SUMIFS(K:K,A:A,A2,J:J,"=I")+SUMIFS(M:M,A:A,A2,L:L,'
         '"=I")+SUMIFS(O:O,A:A,A2,N:N,"=I")')
ws.write(1, 27,
         '=SUMIFS(Q:Q,A:A,A2,F:F,"=J")+SUMIFS(I:I,A:A,A2,H:H,"=J")+SUMIFS(K:K,A:A,A2,J:J,"=J")+SUMIFS(M:M,A:A,A2,L:L,'
         '"=J")+SUMIFS(O:O,A:A,A2,N:N,"=J")')
ws.write(1, 28,
         '=SUMIFS(Q:Q,A:A,A2,F:F,"=K")+SUMIFS(I:I,A:A,A2,H:H,"=K")+SUMIFS(K:K,A:A,A2,J:J,"=K")+SUMIFS(M:M,A:A,A2,L:L,'
         '"=K")+SUMIFS(O:O,A:A,A2,N:N,"=K")')
ws.write(1, 29,
         '=SUMIFS(Q:Q,A:A,A2,F:F,"=L")+SUMIFS(I:I,A:A,A2,H:H,"=L")+SUMIFS(K:K,A:A,A2,J:J,"=L")+SUMIFS(M:M,A:A,A2,L:L,'
         '"=L")+SUMIFS(O:O,A:A,A2,N:N,"=L")')
ws.write(1, 30,
         '=SUMIFS(Q:Q,A:A,A2,F:F,"=M")+SUMIFS(I:I,A:A,A2,H:H,"=M")+SUMIFS(K:K,A:A,A2,J:J,"=M")+SUMIFS(M:M,A:A,A2,L:L,'
         '"=M")+SUMIFS(O:O,A:A,A2,N:N,"=M")')
ws.write(1, 31,
         '=SUMIFS(Q:Q,A:A,A2,F:F,"=N")+SUMIFS(I:I,A:A,A2,H:H,"=N")+SUMIFS(K:K,A:A,A2,J:J,"=N")+SUMIFS(M:M,A:A,A2,L:L,'
         '"=N")+SUMIFS(O:O,A:A,A2,N:N,"=N")')
ws.write(1, 32,
         '=SUMIFS(Q:Q,A:A,A2,F:F,"=O")+SUMIFS(I:I,A:A,A2,H:H,"=O")+SUMIFS(K:K,A:A,A2,J:J,"=O")+SUMIFS(M:M,A:A,A2,L:L,'
         '"=O")+SUMIFS(O:O,A:A,A2,N:N,"=O")')
ws.write(1, 33,
         '=SUMIFS(Q:Q,A:A,A2,F:F,"=VIP")+SUMIFS(I:I,A:A,A2,H:H,"=VIP")+SUMIFS(K:K,A:A,A2,J:J,"=VIP")+SUMIFS(M:M,A:A,'
         'A2,L:L, "=VIP")+SUMIFS(O:O,A:A,A2,N:N,"=VIP")')
ws.write(1, 34,
         '=SUMIFS(Q:Q,A:A,A2,F:F,"=FH")+SUMIFS(I:I,A:A,A2,H:H,"=FH")+SUMIFS(K:K,A:A,A2,J:J,"=FH")+SUMIFS(M:M,A:A,A2,'
         'L:L, "=FH")+SUMIFS(O:O,A:A,A2,N:N,"=FH")')

ws.write(1, 35, xlwt.Formula('SUM(S2:AI2)'))
ws.write(1, 36, xlwt.Formula('SUM(I2:Q2)-SUM(S2:AI2)'))

end_time = time.clock()

times = end_time - start_time

print('耗时：%s' % times)

workbook.save('C:/Users/Administrator/Desktop/NY/ZYX.xls')
