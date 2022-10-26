#	The Amazing Human Cannonball
#https://open.kattis.com/problems/humancannonball2

import math
n=int(input())
for i in range(0,n):
    v,te,x1,h1,h2=(map(float,input().split()))
    t=(x1)/(v*math.cos(te*math.pi/180))
    y=(v*t*math.sin(te*math.pi/180))-0.5*9.81*((t)**2)
    if y>=h1+1 and y<=h2-1:
        print("Safe")
    else:
        print("Not Safe")
