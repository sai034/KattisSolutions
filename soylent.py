#	Soylent
#https://open.kattis.com/problems/soylent

import math
n=int(input())
for i in range(0,n):
    v=int(input())
    print(math.ceil(v/400))
