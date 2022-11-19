#	Beavergnaw
#https://open.kattis.com/problems/beavergnaw

import math
D,V=map(int,input().split())
while  V!=0:
    c=round(pow((pow(D,3)* math.pi /6 - V) /(math.pi/6),1.0/3),9)
    print(c)
    D, V = map(int, input().split())
