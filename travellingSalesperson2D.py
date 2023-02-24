#	Travelling Salesperson 2D
#https://open.kattis.com/problems/tsp

import math
def dis(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
c = list()
n = int(input())
t = list(range(0,n))
p = {i: False for i in range(0, n)}
p[0] = True
for i in range(0, n):
    c.append((lambda x: (float(x[0]), float(x[1])))(input().split()))
for i in range(1, n):
    s = -1
    for j in range(0, n):
        if not p[j] and (s == -1 or dis(c[t[i-1]], c[j]) < dis(c[t[i-1]], c[s])):
            s = j
    t[i] = s
    p[s] = True
for i in range(0, n):
    print(t[i])
