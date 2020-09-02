import win32print
import win32com
from win32com.client import Dispatch
import os
import win32api
import win32com.client


def dayin2(data):
    ExcelApp = win32com.client.Dispatch("Excel.Application")
    ExcelApp.Visible = False
    wb = ExcelApp.Workbooks.Open(data)
    ws = wb.Worksheets(1)
    nrow = ws.usedrange.rows.count
    ncolumn = ws.usedrange.columns.count
    ws.PageSetup.PaperSize = 9
    # ws.PageSetup.Orientation = 2
    # ws.usedrange.Columns.AutoFIt
    ws.PageSetup.CenterHeader = ""
    # ws.PageSetup.CenterFooter = "第&P页，共&N页"
    ws.PageSetup.CenterFooter = ""
    # ws.PageSetup.PrintTitleRows = "$43:$47"
    # ws.PageSetup.PrintTitleColumns = "$A:$A"
    # ws.PageSetup.PrintArea = "$A$1:$M$42,$A$43:$AC$%s" % nrow
    ws.PageSetup.LeftMargin = 1.0*28.35
    ws.PageSetup.RightMargin = 1.0*28.35
    ws.PageSetup.CenterHorizontally = True
    wb.Save()
    wb.Close()


path = r"C:\Users\65680\Desktop\TP"

for roots, dirs, files in os.walk(path):
    for file in files:
        if file[-3:].lower() == "xls":
            name = os.path.join(roots, file)
            print(name)
            dayin2(name)
            print("{}已完成".format(name))

# dayin2(k)
