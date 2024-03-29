#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2020-12-03
# Author:Runker54
# -----------------------

# from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *
from PDFSignerUI import *
import sys

if __name__ == '__main__':
    appctxt = ApplicationContext()

    appWin = QMainWindow()
    pdfSignerUI = Ui_MainWindow()
    pdfSignerUI.setupUi(appWin)
    appWin.show()

    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)