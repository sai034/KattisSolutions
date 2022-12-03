#	Goat Rope
#https://open.kattis.com/problems/goatrope

import math
(x, y, x1, y1, x2, y2) = map(lambda x: int(x), input().split())
if x >= x1 and x <= x2:
    print(abs(y - y1)) if abs(y - y1) < abs(y - y2) else print(abs(y - y2))
elif y >= y1 and y <= y2:
    print(abs(x - x1)) if abs(x - x1) < abs(x - x2) else print(abs(x - x2))
else:
    near_x = min(x1, x2, key=lambda f : abs(x - f))
    near_y = min(y1, y2, key=lambda f : abs(y - f))
    print(math.sqrt(abs(x-near_x)**2 + abs(y-near_y)**2))
