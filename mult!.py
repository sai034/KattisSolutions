#	Mult!
#https://open.kattis.com/problems/mult

import sys
s = input()
a = list()
for l in sys.stdin:
    n = int(l)
    if not a or n % a[0] != 0:
        a.append(n)
    else:
        print(n)
        a.clear()
