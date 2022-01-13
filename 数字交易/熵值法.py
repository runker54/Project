#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2022/1/9
import pandas as pd
import numpy as np
import math
from numpy import array
data_path = r"C:\Users\65680\Desktop\熵值法\test1.xlsx"
df = pd.read_excel(data_path)
df.dropna()

# 定义熵值法函数
def cal_weight(x):
    x = x.apply(lambda x: ((x - np.min(x)) / (np.max(x) - np.min(x))))
    rows = x.index.size
    cols = x.columns.size
    k = 1.0 / math.log(rows)
    lnf = [[None] * cols for i in range(rows)]
    x = array(x)
    lnf = [[None] * cols for i in range(rows)]
    lnf = array(lnf)
    for i in range(0, rows):
        for j in range(0, cols):
            if x[i][j] == 0:
                lnfij = 0.0
            else:
                p = x[i][j] / x.sum(axis=0)[j]
                lnfij = math.log(p) * p * (-k)
            lnf[i][j] = lnfij
    lnf = pd.DataFrame(lnf)
    E = lnf

    d = 1 - E.sum(axis=0)
    w = [[None] * 1 for i in range(cols)]
    for j in range(0, cols):
        wj = d[j] / sum(d)
        w[j] = wj
    w = pd.DataFrame(w)
    return w

if __name__ == '__main__':
    w = cal_weight(df)
    w.index = df.columns
    w.columns = ['weight']
    print(w)
    print('运行完成!')




