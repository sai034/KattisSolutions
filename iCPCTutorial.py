#	ICPC Tutorial
#https://open.kattis.com/problems/tutorial

import math
m, n, t = map(int,input().split())
if t == 1:
    if n > 15:
        s = True
    else:
        s = m < math.factorial(n)
if t == 2:
    s = m < 2**n
if t == 3:
    s = m < n**4
if t == 4:
    s = m < n**3
if t == 5:
    s = m < n**2
if t == 6:
    s = m < n * math.log(n, 2)
if t == 7:
    s = m < n
if s:
    print("TLE")
else:
    print("AC")
