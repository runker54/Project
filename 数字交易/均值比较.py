#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2022/1/10
import pandas as pd
import numpy as np
import time

# 读取数据

data = pd.read_excel(r"C:\Users\65680\Desktop\熵值法\品种筛选大区.xlsx")
data.set_index(['品种'], inplace=True)
# 总指标数
n = list(data.columns)
# 正向指标，(x-min)/(max-min)
# 负向指标 (max-x)/(max-min)
# 如果指标体系存在最优指标和最劣指标，采用下面的形式
for i in n:
    # 获取各个指标的最大值和最小值
    mean = np.mean(data[i])
    data[i] = data[i]-mean
data[data>=0]=1
data[data<0]=0
U = data[(data['镉'] == 1)]
U = pd.DataFrame(U)
U.to_excel(r"C:\Users\65680\Desktop\熵值法\大区品种.xlsx")


