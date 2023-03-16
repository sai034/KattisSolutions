#	Ball Bearings
#https://open.kattis.com/problems/ballbearings

import math
n=int(input())
for i in range(n):
    D,d,s=map(float,input().split())
    print(int(math.pi / math.asin((s + d) / (D - d))))
