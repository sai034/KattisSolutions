#	Glasses Foggy, Mom's Spaghetti
#https://open.kattis.com/problems/glassesfoggymomsspaghetti

import math
d, x, y, h = map(int, input().split())
x1, x2, x3 = math.atan2(y+h/2,x), math.atan2(y,x), math.atan2(y-h/2,x)
print(d*(math.tan(x1-x2) + math.tan(x2-x3)))
