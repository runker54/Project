# coding:utf-8
import os
from win32com.client import DispatchEx

path = r"C:\Users\65680\Desktop\织金县\织金县总"
for roots, dirs, files in os.walk(path):
    for file in files:
        print(file)
        if file[-3:].lower() == "xls":
            xls_path = os.path.join(roots, file)
            pdf_path_temp = os.path.join(roots, file)
            cy_path = pdf_path_temp.replace("织金县总", "test")
            ccc = cy_path[:len(cy_path)-len(file)-1]
            print(ccc)
            if os.path.isdir(ccc):
                pass
            else:
                os.makedirs(ccc)
            pdf_path = cy_path.replace('xls', 'pdf')
            xlApp = DispatchEx("Excel.Application")
            wb = xlApp.Workbooks.Open(xls_path)
            wb.ExportAsfixedFormat(0, pdf_path)
            xlApp.Quit()
            print("{}已完成".format(pdf_path))