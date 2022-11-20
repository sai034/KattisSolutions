#	Das Blinkenlights
#https://open.kattis.com/problems/dasblinkenlights

import math
a,b,c=map(int,input().split())
d=math.gcd(a,b)
e=a*b
if e/d<=c :
    print("yes")
else:
    print("no")
