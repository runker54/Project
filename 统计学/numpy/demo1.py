#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2021-01-27
# Author:Runker54
# -----------------------
import numpy as np

arr1 = np.array([1, 2, 3, 4])
# print(arr1)
arr2 = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])
# print(arr2)
# print(arr1.shape, arr2.shape)
# print(arr1.dtype, arr2.dtype)
# print(arr1.size, arr2.size)
# print(arr1.itemsize, arr2.itemsize)
# arr2.shape = 6, 2  # 改变形状
# arr1.shape = 2, 2
arr3 = np.arange(0, 1, 0.1)
# print(arr3)
arr4 = np.linspace(0, 1, 19)
# print(arr4)
arr5 = np.logspace(0, 2, 20)
# print(arr5)
# print(arr5.size)
arr6 = np.zeros((2, 3))
# print(arr6)
arr7 = np.eye(4, k=-3)
# print(arr7)
arr8 = np.diag([1, 2, 4, 5])
arr9 = np.fliplr(arr8)  # 反转元素顺序
# print(arr9)
# print(arr8)
arr10 = np.ones((3, 5, 2, 2))
arr11 = np.ones_like(arr10)
# print(arr10)
arr12 = np.random.random(5)
# print(arr12)
arr13 = np.random.rand(10, 4, 4)
# print(arr13)
arr14 = np.random.randn(4, 4, 4)
# print(arr14)
# arr15 = np.random.randint(1, 5, size=(4, 4, 4, 4, 4, 4, 4))
# print(arr15)
arr16 = np.array([[1, 2, 3, 4, 5], [4, 5, 6, 7, 8], [7, 8, 9, 10, 11]])
# print(arr16)
# print(arr16[0, 3:5])
# print(arr16[1:, 2:])
# print(arr16[:,2])

