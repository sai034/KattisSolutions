#	Greedy Polygons
#https://open.kattis.com/problems/greedypolygons

from math import pi,tan
N=int(input())
for i in range(N):
    n, l, d, g = map(int, input().split())
    print(0.25 * n * l**2 * 1/tan(pi / n)+n*l*d*g+(g*d)**2 * pi)
