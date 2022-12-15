#	Saving For Retirement
#https://open.kattis.com/problems/savingforretirement

import math
b,br,bs,a,ar=map(int,input().split())
print(math.floor((br - b) * bs /ar + a) + 1)
