#Integer Division
#https://open.kattis.com/problems/integerdivision

import math
n = int(input())
r = list()
c = list()
for i in range(n):
    form, *d = input().split()
    d = list(map(int, d))
    if form == "rectangle":
        r.append(d)
    else:
        c.append(d)
ns = int(input())
for i in range(ns):
    x, y = list(map(int, input().split()))
    nh = 0
    for x1, y1, x2, y2 in r:
        if x1 <= x <= x2 and y1 <= y <= y2:
            nh = nh + 1
    for x1, y1, rad in c:
        X = x1 - x
        Y = y1 - y
        dis = math.sqrt(X ** 2 + Y ** 2)
        if dis <= rad:
            nh = nh + 1
    print(nh
