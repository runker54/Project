# -*- coding:utf-8 -*-
"""
python2代码
"""
import sys
_ = sys.getdefaultencoding()
if _ != 'utf-8':
    # reload(sys)
    sys.setdefaultencoding('utf-8')
index_list = []
def aa(x):
    global index_list
    index_list.append(x)
    bH = str(0) * (4 - len(str((index_list.count(x))))) + str(index_list.count(x))
    return str(x) + bH







































