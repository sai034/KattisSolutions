#	Cokolada
#https://open.kattis.com/problems/cokolada

import math
n= int(input())
c = 2 ** math.ceil(math.log2(n))
m = 0
if c == n:
    n = 0
b = c
while 0 < n:
    b /= 2
    m += 1
    if b <= n:
        n-= b
print("{} {}".format(c, m))
