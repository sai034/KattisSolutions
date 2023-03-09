#	3D Printed Statues
#https://open.kattis.com/problems/3dprinter

import math
n = int(input())
print(math.ceil(1 + math.log(n)/math.log(2)))
