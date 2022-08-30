# Janitor Troubles
# https://open.kattis.com/problems/janitortroubles

import math
i=str(input())
s=i.split()
a=s[0]
b=s[1]
c=s[2]
d=s[3]
A=int(a)
B=int(b)
C=int(c)
D=int(d)
sa=(A+B+C+D)/2
ans=math.sqrt((sa-A)*(sa-B)*(sa-C)*(sa-D))
print(ans)
