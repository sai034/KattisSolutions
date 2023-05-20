#	CD
#https://open.kattis.com/problems/cd

import sys
n = m = None
for l in sys.stdin:
    if n == m == None:
        n, m = map(int, l.split())
        a, b = [], 0
    else:
        if n:
            n -= 1
            a.append(int(l))
            if n == 0: a = set(a)
        else:
            m -= 1
            b += int(l) in a
        if n == m == 0:
            n = m = None
            print(b)
