# coding:utf-8
import os
from win32com.client import DispatchEx
import time
path = r"C:\Users\65680\Desktop\out"  # 表格路径

for roots, dirs, files in os.walk(path):
    for file in files:
        print(file)
        if file[-3:].lower() == "xls":
            xls_path = os.path.join(roots, file)
            pdf_path_temp = os.path.join(roots, file)
            cy_path = pdf_path_temp.replace("out", "out")  # 替换为同一路径下同一级文件夹
            ccc = cy_path[:len(cy_path)-len(file)-1]
            print(ccc)
            if os.path.isdir(ccc):
                pass
            else:
                os.makedirs(ccc)
            pdf_path = cy_path.replace('xls', 'pdf')
            if os.path.exists(pdf_path):
                print("已存在")
            else:
                xlApp = DispatchEx("Excel.Application")
                wb = xlApp.Workbooks.Open(xls_path)
                wb.ExportAsfixedFormat(0, pdf_path)
                xlApp.Quit()
            time.sleep(0.1)
            print("{}已完成".format(pdf_path))
            try:
                os.remove(xls_path)
            except:
                print('删除失败')