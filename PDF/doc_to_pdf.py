# -*- coding: utf-8 -*-#
# -----------------------
# Date:2020-11-26
# -----------------------
from os import walk
import os
import win32com
from win32com.client import Dispatch

wdFormatPDF = 17


def doc2pdf(input_file):
    word = Dispatch('Word.Application')
    doc = word.Documents.Open(input_file)
    doc.SaveAs(input_file.replace(".docx", ".pdf"), FileFormat=17)
    doc.Close()
    word.Quit()


if __name__ == "__main__":
    directory = r'I:\0开阳县台账\开阳县台账文旦导出（20201214修改后已整理）\开阳县Word'
    for root, dirs, filenames in os.walk(directory):
        for file in filenames:
            # if file.endswith(".doc") or file.endswith(".docx"):
            if '$' not in file:
                print(file)
                # x = str(input("是否需要转换："))
                # if x == "1":
                doc2pdf(os.path.join(root, file))
                print(file)

