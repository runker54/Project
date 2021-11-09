#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2021-01-20
# Author:Runker54
# -----------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import xlrd
import xlwt

data_path = r'C:\Users\65680\Desktop\data.xls'
out_book = xlwt.Workbook('utf-8')
ws_sheet = out_book.add_sheet('result')
ws_sheet.write(0, 0, '样本数')
ws_sheet.write(0, 1, '回归方程')
ws_sheet.write(0, 2, 'R²')

data = pd.read_excel(data_path)
cd = data.iloc[:, :1].values
pd_ = data.iloc[:, 1:].values
print(cd)
print(pd_)
r = 2  # 起始字段
srart_r = 1  # 开始写入行

for one_calc in range(2, len(cd)):
    x = cd[:one_calc]
    y = pd_[:one_calc]
    reg = LinearRegression().fit(x, y)
    ws_sheet.write(srart_r, 0, one_calc)
    ws_sheet.write(srart_r, 1, "Y = %.5fX + (%.5f)" % (reg.coef_[0][0], reg.intercept_[0]))
    ws_sheet.write(srart_r, 2, reg.score(x, y))
    print("一元回归方程为:  y = %.5fX + (%.5f)" % (reg.coef_[0][0], reg.intercept_[0]))
    print("R平方为: %s" % reg.score(x, y))
    plt.scatter(x, y, color='black')
    plt.plot(x, reg.predict(x), color='red', linewidth=1)
    plt.show()
    srart_r += 1
out_book.save(r'C:\Users\65680\Desktop\in\result2.xls')
