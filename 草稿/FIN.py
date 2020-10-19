l = []



def find_X(a, b, d, e, f):
    if f == "水稻":
        if e > 7.5:
            ax = 0.8
            bx = 1.0
            cx = 20
            dx = 240
            ex = 350
        elif e > 6.5:
            ax = 0.6
            bx = 0.6
            cx = 25
            dx = 140
            ex = 300
        elif e > 5.5:
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
        if e > 7.5:
            ax = 0.6
            bx = 3.4
            cx = 25
            dx = 170
            ex = 250
        elif e > 6.5:
            ax = 0.3
            bx = 2.4
            cx = 30
            dx = 120
            ex = 200
        elif e > 5.5:
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
# def find_S(a, b, c, d, e, f):
#     if e > 7.5:
#         aS = 4.0
#         bS = 6.0
#         cS = 100
#         dS = 1000
#         eS = 1300
#     elif e > 6.5:
#         aS = 3.0
#         bS = 4.0
#         cS = 120
#         dS = 700
#         eS = 1000
#     elif e > 5.5:
#         aS = 2.0
#         bS = 2.5
#         cS = 150
#         dS = 500
#         eS = 850
#     else:
#         aS = 1.5
#         bS = 2.0
#         cS = 200
#         dS = 400
#         eS = 800
#     print(ax,bx,cx,dx,ex)
# find_X(1, 2, 3, 4, 5)


# a = [1,1,1,1,1,1,2,2,2,3,43,4,4,5]
# c = 1
# if c in a:
#     print(c)
# print()
# b = set(a)
# c = list(b)
# print(b)
# print(c)