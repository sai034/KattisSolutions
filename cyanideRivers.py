#Cyanide Rivers
#https://open.kattis.com/problems/cyaniderivers

import math
t = str(input())
r = [t for t in t.split("1") if t]
if not r:
    print(0)
else:
    l = max(len(t) for t in r)
    print(math.ceil(l/ 2))
