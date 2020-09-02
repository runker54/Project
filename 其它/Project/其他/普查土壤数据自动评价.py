#coding:utf-8
def findMax(a, b, c, d, e, f, g):
    if g == u"ˮ��":
        if f >7.5:
            ax = 0.8
            bx = 1.0
            cx = 20
            dx = 240
            ex = 350
        elif f > 6.5:
            ax = 0.6
            bx = 0.6
            cx = 25
            dx = 140
            ex = 300
        elif f > 5.5:
            ax = 0.4
            bx = 0.5
            cx = 30
            dx = 100
            ex = 250
        else:
            ax = 0.3
            bx = 0.5
            cx = 30
            dx = 80
            ex = 250
    else:
        if f >7.5:
            ax = 0.6
            bx = 3.4
            cx = 25
            dx = 170
            ex = 250
        elif f > 6.5:
            ax = 0.3
            bx = 2.4
            cx = 30
            dx = 120
            ex = 200
        elif f > 5.5:
            ax = 0.3
            bx = 1.8
            cx = 40
            dx = 90
            ex = 150
        else:
            ax = 0.3
            bx = 1.3
            cx = 40
            dx = 70
            ex = 150
    if f > 7.5:
        aS = 4.0
        bS = 6.0
        cS = 100
        dS = 1000
        eS = 1300
    elif f > 6.5:
        aS = 3.0
        bS = 4.0
        cS = 120
        dS = 700
        eS = 1000
    elif f > 5.5:
        aS = 2.0
        bS = 2.5
        cS = 150
        dS = 500
        eS = 850
    else:
        aS = 1.5
        bS = 2.0
        cS = 200
        dS = 400
        eS = 800
    if a >aS:
        Cd = 3
    elif a >ax:
        Cd = 2
    else:
        Cd = 1

    if b >bS:
        Hg = 3
    elif b >bx:
        Hg = 2
    else:
        Hg = 1

    if c >cS:
        As = 3
    elif c >cx:
        As = 2
    else:
        As = 1

    if d >dS:
        Pb = 3
    elif d >dx:
        Pb = 2
    else:
        Pb = 1

    if e > eS:
        Cr = 3
    elif e > ex:
        Cr = 2
    else:
        Cr = 1
    l = [Cd,Hg,As,Pb,Cr]
    zh_5class = max(l)
    return zh_5class