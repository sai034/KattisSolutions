#	Ladder
#https://open.kattis.com/problems/ladder\

import math
i=str(input())
s=i.split()
h=s[0]
v=s[1]
H=int(h)
V=int(v)
x=math.sin(math.radians(V))
d=H/x
print(math.ceil(d))
