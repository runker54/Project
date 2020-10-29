# coding: utf-8
import arcpy
import time
import xlwt

# import sys

# defaultencoding = 'utf-8'
# if sys.getdefaultencoding() != defaultencoding:
#     reload(sys)
#     sys.setdefaultencoding(defaultencoding)

gis_data = r'F:\思南.gdb\T思南县消除中段1027_111_连接'

with arcpy.da.SearchCursor(gis_data,
                           ['LBBM', 'MAX_水稻19年', 'MAX_水稻19年面积', 'MAX_水稻20年', 'MAX_水稻20年面积',
                            'MAX_玉米19年', 'MAX_玉米19年面积', 'MAX_玉米20年', 'MAX_玉米20年面积',
                            '周边环境', '主要作物19年', '主要作物20年']) as currsor:
    lbbm_list = []
    message_list = []
    for row in currsor:
        lbbm_list.append(row[0])
        data_list = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]]
        message_list.append(data_list)
    lbbm_list = list(set(lbbm_list))
    print(len(lbbm_list))
    dkxx_list = []
    for _bm in lbbm_list:
        bm_list = filter(lambda x: x[0] == _bm, message_list)
        lbbm = []
        sd19 = []
        sd19a = []
        sd20 = []
        sd20a = []
        ym19 = []
        ym19a = []
        ym20 = []
        ym20a = []
        zbhj = []
        zz19 = []
        zz20 = []
        for _dgdk in bm_list:
            lbbm.append(_dgdk[0])
            sd19.append(_dgdk[1])
            sd19a.append(_dgdk[2])
            sd20.append(_dgdk[3])
            sd20a.append(_dgdk[4])
            ym19.append(_dgdk[5])
            ym19a.append(_dgdk[6])
            ym20.append(_dgdk[7])
            ym20a.append(_dgdk[8])
            zbhj.append(_dgdk[9])
            zz19.append(_dgdk[10])
            zz20.append(_dgdk[11])
            lbbm = list(set(lbbm))
            sd19 = list(set(sd19))
            sd20 = list(set(sd20))
            ym19 = list(set(ym19))
            ym20 = list(set(ym20))
            zbhj = list(set(zbhj))
            zz19 = list(set(zz19))
            zz20 = list(set(zz20))
        dkxx = [lbbm, sd19, sd19a, sd20, sd20a, ym19, ym19a, ym20, ym20a, zbhj, zz19, zz20]
        dkxx_list.append(dkxx)
    work_book = xlwt.Workbook(encoding='utf-8')
    ws = work_book.add_sheet('Data')
    title_list = ['地块编号', '水稻19年', '水稻19年面积', '水稻20年', '水稻20年面积', '玉米19年', '玉米19年面积', '玉米20年', '玉米20年面积', '周边环境',
                  '主载19年', '主载20年']
    for _title in range(len(title_list)):
        ws.write(0, _title, title_list[_title])
    r = 1  # 开始行
    for one_dk in dkxx_list:
        ws.write(r, 0, one_dk[0])
        print(one_dk[0])
        for _x in [1, 3, 5, 7, 9, 10, 11]:
            s = ''
            temp_I_list = []
            for _i in one_dk[_x]:
                print(_i)
                temp_I_list = temp_I_list + str(_i).split(" ")
            print(temp_I_list)
            print('第一个')
            temp_I_list = list(set(temp_I_list))
            print(temp_I_list)
            print('第二个')
            for one_text in temp_I_list:
                one_text = one_text+ ' '
                s += one_text
            s = s.strip()
            print(s)

            ws.write(r, _x, s)
        for _y in [2, 4, 6, 8]:
            s = 0
            for _ii in one_dk[_y]:
                if _ii != 'None' and _ii != '':
                    s = s + float(_ii)
            ws.write(r, _y, s)
        r += 1
    work_book.save(r'C:\Users\65680\Desktop\SNX\SNX_20201028-1.xls')
