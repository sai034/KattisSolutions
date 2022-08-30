# Different Distances
# https://open.kattis.com/problems/differentdistances

import math
def mod(n):
    if n>0:
        return n
    else:
        return n * -1
while (1):
    i = str(input())
    if i == "0":
        break
    s = i.split()
    x1 = s[0]
    y1 = s[1]
    x2 = s[2]
    y2 = s[3]
    p = s[4]
    X1 = float(x1)
    Y1 = float(y1)
    X2 = float(x2)
    Y2 = float(y2)
    P = float(p)

    X=mod(X1-X2)
    P1=math.pow(X,P)
    Y=mod(Y1-Y2)
    P2=math.pow(Y,P)
    sum=P1+P2
    P3=math.pow(sum,1/P)
    print(P3)
