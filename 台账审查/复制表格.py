#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2020-11-30
# Author:Runker54
# -----------------------
import os
import pandas
sheet_path = r'C:\Users\65680\Desktop\清镇市台账审查结果统计表1.3.xlsx'
read_stream = pandas.read_excel(sheet_path, sheet_name='清镇市')

read_stream.to_excel(r'C:\Users\65680\Desktop\大方县台账审查结果统计表1.3.xlsx', sheet_name='PDF内盖章')



