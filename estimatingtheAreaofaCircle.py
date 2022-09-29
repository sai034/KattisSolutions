#Estimating the Area of a Circle
#https://open.kattis.com/problems/estimatingtheareaofacircle

import math
r = ''
m = ''
c = ''
for i in range(0, 1000):
    r, m, c = list(map(float,input().split()))
    if r == 0 and m == 0 and c == 0:
        break
    else:
        ratio = float(c) / float(m)
        ar = math.pi * float(r) * float(r)
        er = 4 * r * r * ratio
        print(ar, er)
