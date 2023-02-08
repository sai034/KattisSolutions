#	Veci
#https://open.kattis.com/problems/veci

import sys
from itertools import permutations
n= sys.stdin.read()
l = n.strip("\n")
p = [''.join(p) for p in permutations(l)]
larger = []
for i in p:
    if int(i) > int(l):
        larger.append(int(i))
if len(larger) > 0:
    print(min(larger))
else:
    print("0")
