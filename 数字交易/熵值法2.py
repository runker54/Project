#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2022/1/10
import pandas as pd
import numpy as np
import time
import os

# 读取数据
adress_path = r"C:\Users\65680\Desktop\罗甸县第五章"
# name = "玉米品种筛选小区"
data1 = pd.ExcelFile(r"C:\Users\65680\Desktop\第五章数据分析之排序-罗甸县.xls")
writer = pd.ExcelWriter(os.path.join(adress_path, "技术筛选.xlsx"))
for name in ["品种筛选小区", "品种筛选大区", "叶面调控小区", "叶面调控大区", "原位钝化小区", "原位钝化大区", "综合技术小区", "综合技术大区", "优化施肥小区", "优化施肥大区", ]:
    data = data1.parse("%s" % name)
    data.set_index(['材料'], inplace=True)
    # 总指标数
    n = list(data.columns)
    # 正向指标，(x-min)/(max-min)
    # 负向指标 (max-x)/(max-min)
    # 如果指标体系存在最优指标和最劣指标，采用下面的形式
    for i in n:
        # 获取各个指标的最大值和最小值
        Max = np.max(data[i])
        Min = np.min(data[i])
        data[i] = (Max - data[i]) / (Max - Min)
        # if (i == '小区') or (i == '大区'):
        #     data[i] = (data[i] - Min) / (Max - Min)
        # else:
        #     data[i] = (Max - data[i]) / (Max - Min)
    data.replace(0, 0.1, inplace=True)
    for i in n:
        # 计算指标总和
        Sum = np.sum(data[i])
        # 计算各地区某一指标占比
        data[i] = data[i] / Sum
    # 地区总数
    m = len(data)
    E = []
    # 计算信息熵值
    for i in n:
        K = 1 / np.log(m)
        e = - K * np.sum(data[i] * np.log(data[i]))
        E.append(e)
    # 转换为数组形式
    E = np.array(E)
    # 计算效用价值
    D = 1 - E

    # W = D / (len(n)-np.sum(D))
    W = D / np.sum(D)
    # 转换形式
    W = np.array([W])

    # 保存 权重 为excel格式
    W1 = pd.DataFrame(W.T, index=n)
    # W1.to_excel(r"C:\Users\65680\Desktop\熵值法\元素权重.xlsx")
    U = []
    for i in range(1, len(data) + 1):
        # 获取样本各个指标的值
        y = data[i - 1:i].values
        u1 = y * W * 100
        # 转换为列表
        u1 = u1.tolist()
        u1 = u1[0]

        # 计算样本综合得分
        ## 因前文构建了数据权重矩阵，故最后综合得分总和为100
        u = np.sum(y * W) * 100
        # 转换为列表
        u = np.array([u])
        u = u.tolist()
        # 各指标得分 和 综合得分
        u = u1 + u
        U.append(u)
    # 获取样本列表
    area = list(data.index)
    # 生成数据框
    U = pd.DataFrame(U, index=area)
    # 重新设置列名称
    U.columns = n + ['综合得分']

    # 为各个指标得分排名
    for i in n:
        i1 = i + '  排名'
        U[i1] = U[i].rank(ascending=False)
    # 为样本综合得分排名
    U['综合得分  排名'] = U['综合得分'].rank(ascending=False)

    # 保存为excel文件
    U.to_excel(writer, sheet_name="%s" % name)
writer.save()
writer.close()
