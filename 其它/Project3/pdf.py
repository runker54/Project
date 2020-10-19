# coding:utf-8
import os
from win32com.client import DispatchEx

path = r"E:\台账\大方县\大方县导出资料\DFX_SHEET"

for roots, dirs, files in os.walk(path):
    for file in files:
        print(file)
        if file[-3:].lower() == "xls":
            xls_path = os.path.join(roots, file)
            pdf_path_temp = os.path.join(roots, file)
            cy_path = pdf_path_temp.replace("DFX_SHEET", "DFX_PDF")
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
            print("{}已完成".format(pdf_path))