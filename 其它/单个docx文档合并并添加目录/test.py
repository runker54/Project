#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2020-12-10
# Author:Runker54
# -----------------------


vm_list = []
for i in range(1, 9):
    vm_list.append(i)
# print(vm_list)
list1 = zip(*(iter(vm_list),) * 2)
list2 = [list(i) for i in list1]
count = len(vm_list) % 2
list2.append(vm_list[-count:]) if count != 0 else list2

