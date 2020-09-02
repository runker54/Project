# coding:utf-8
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

indes_list = []

def auto(x):

    global indes_list
    if x not in indes_list:
        indes_list = list(set(indes_list))
    indes_list.append(x)

    bh = str(0)*(4 - len(str(indes_list.count(x)))) + str(indes_list.count(x))

    return str(x) + bh
print(auto(4))
print(auto(4))
print(auto(5))
print(auto(5))
print(auto(4))
print(auto(4))
