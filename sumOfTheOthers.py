#	Sum of the Others
#https://open.kattis.com/problems/sumoftheothers\

import sys
for line in sys.stdin:
    print(sum(map(lambda n:int(n),line.split(' ')))//2)
