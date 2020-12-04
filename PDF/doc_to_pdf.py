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
    directory = r"C:\Users\65680\Desktop\石阡县"
    for root, dirs, filenames in os.walk(directory):
        for file in filenames:
            if file.endswith(".doc") or file.endswith(".docx"):
                if 'HS' in str(file):
                    print(file)
                else:
                    doc2pdf(os.path.join(root, file))
                    print(file)
