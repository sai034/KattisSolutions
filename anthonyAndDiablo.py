#	Anthony and Diablo
#https://open.kattis.com/problems/anthonyanddiablo

import math
a,n=map(float,input().split())
p=(n**2)/(4*(math.pi))
if p>=a:
    print("Diablo is happy!")
else:
    print("Need more materials!")
