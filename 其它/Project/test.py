# coding: utf-8
import sys

coding = "utf-8"
coding2 = sys.getdefaultencoding()
if coding2 != coding:
    reload(sys)
    sys.setdefaultencoding('utf-8')

