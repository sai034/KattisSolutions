#	A1 Paper
#https://open.kattis.com/problems/a1paper

import math
n=int(input())
N=2
l=list(map(int,input().split()))
t=0
for i in range(n-1):
    t=t+(math.pow(2,(-3/4.0)-i/2)*(N/2.0))
    N=(N-l[i])*2
    if N<=0:
        break
if N<1:
    print(t)
else:
    print("impossible")
