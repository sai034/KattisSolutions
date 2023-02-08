#Fractal Area
#https://open.kattis.com/problems/fractalarea

from math import pi
def fa(r,n):
    f = r**2
    if n == 1:
        return f * pi
    s = 4 * (r/2)**2
    if n == 2:
        return (f + s) * pi
    re = sum((r/2**i)**2 * 4*3**(i-1) for i in range(2,n))
    return (f + s + re) * pi
N=int(input())
for _ in range(N):
    r,n = map(int, input().split())
    print('%.6f' % fa(r,n))
