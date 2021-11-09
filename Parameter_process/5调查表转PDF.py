# coding:utf-8
import os
from win32com.client import DispatchEx
import time
path = r"C:\Users\65680\Desktop\从江县集中推进区入户调查表"  # 表格路径
file_list = []
for roots, dirs, files in os.walk(path):
    for file in files:
        if file[-4:].lower() == "xlsx":
            xls_path = os.path.join(roots, file)

            file_list.append(xls_path)
file_list.sort(reverse=False)
for one_xls in file_list:
    pdf_path = one_xls.replace('xlsx', 'pdf')
    # pdf_path = pdf_path.replace("赫章县替换", "赫章县PDF")
    temp_dir = os.path.split(pdf_path)[0]
    try:
        os.makedirs(temp_dir)
    except:
        pass
    print(pdf_path)
    if os.path.exists(pdf_path):
        print("已存在")
    else:
        xlApp = DispatchEx("Excel.Application")
        wb = xlApp.Workbooks.Open(one_xls)
        wb.ExportAsfixedFormat(0, pdf_path)
        xlApp.Quit()
    print("{}已完成".format(pdf_path))
