#	Bishops
#https://open.kattis.com/problems/bishops

import sys
for n in sys.stdin:
    print(max(2*int(n)-2, 1))
