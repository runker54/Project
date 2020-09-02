# coding:utf-8
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


def autocalc(x, y, z, p, w):
    s = ""
    list1 = [x, y, z, p, w]
    max_i = max(list1)
    if max_i == 1:
        return "无"
    count_list = []
    i = 0
    for _i in list1:
        if _i == max_i:
            count_list.append(i)
        i += 1
    for _b, _d in enumerate(count_list):
        if _d == 0:
            count_list[_b] = "镉"
        elif _d == 1:
            count_list[_b] = "汞"
        elif _d == 2:
            count_list[_b] = "砷"
        elif _d == 3:
            count_list[_b] = "铅"
        else:
            count_list[_b] = "铬"
    for _v in count_list:
        s = s + " " + _v
    return s


print(autocalc(1, 2, 1, 1, 1))


# a = [1, 2, 1, 2, 3]
# for x, y in enumerate(a):
#     print x


def calc1(x):
    if x == 1:
        return "Ⅰ"
    elif x == 2:
        return "Ⅱ"
    else:
        return "Ⅲ"
print(calc1(2))



# coding:utf-8
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
a = 0
def calc2():
    global a
    b = 1
    if a ==0:
        a = b
    else:
        a = a+1
    s = "0"*(6-len(str(a))) + str(a)
    return s
print(calc2())
print(calc2())
print(calc2())
print(calc2())
print(calc2())