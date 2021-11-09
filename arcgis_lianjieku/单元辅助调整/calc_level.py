# coding:utf-8
def calc(a1, x1, x2, x3, total, ysdy):
    a1 = int(a1)
    x1 = int(x1)
    x2 = int(x2)
    x3 = int(x3)
    total = int(total)
    # 判断点位数量是否大于三个
    level = 0
    high_sum = 0
    if ysdy is None:
        if total < 3:
            level = a1
        else:
            # 计算原类别为安全利用类的情况

            if a1 == 2:
                if a1 == 2 and x2 + x3 == 0:
                    level = 1
                else:
                    level = 2
            # 计算原类别为严格管控类的情况
            if a1 == 3:
                check_values = float(x1)/total
                if (check_values >= 0.65 and x3 == 0) or (x2 + x3 == 0):
                    level = 2
                else:
                    level = 3
            if a1 == 1:
                level = 1
    else:
        level = a1
    return level


a = calc(3, 2, 1, 0, 3, None)
print(a)
