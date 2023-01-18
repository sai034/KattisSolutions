#	Almost Perfect
#https://open.kattis.com/problems/almostperfect

import sys
import math
def almostPerfect(n):
    c = 1
    for i in range (2,int(math.sqrt(n)) + 1):
        if(n % i == 0):
            c += i
            if(i*i != n):
                c += n // i
    if(c == n):
        return "{} perfect".format(n)
    elif (c == (n-2)):
        return "{} almost perfect".format(n)
    elif (c == (n+2)):
        return "{} almost perfect".format(n)
    elif (c == (n-1)):
        return "{} almost perfect".format(n)
    elif (c == (n+1)):
        return "{} almost perfect".format(n)
    else:
        return "{} not perfect".format(n)
for p in sys.stdin.readlines():
    p = int(p)
    print(almostPerfect(p))
