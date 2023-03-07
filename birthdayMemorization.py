#Birthday Memorization
#https://open.kattis.com/problems/fodelsedagsmemorisering

from heapq import heappush as hpush, heappop as hpop
from collections import defaultdict as dd
d = dd(list)
for i in range(int(input())):
    n, l, b = input().split()
    hpush(d[b], (-int(l), n))
print(len(d))
print("\n".join(sorted(map(lambda z: hpop(z)[1], d.values()))))
