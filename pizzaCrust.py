#	Pizza Crust
#https://open.kattis.com/problems/pizza2

import math
r,c=map(int,input().split())
area=math.pi*(r)**2
carea=math.pi*(r-c)**2
print(carea/area*100)
