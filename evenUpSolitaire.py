#Even Up Solitaire
#https://open.kattis.com/problems/evenup

from collections import deque
n=int(input())
solitaire=list(map(int,input().split()))
de=deque()
num=n
for i in range(0,n):
    if not de:
        de.append(solitaire[i])
        continue
    l=de.pop()
    if(l+solitaire[i])%2==0:
        num=num-2
    else:
        de.extend([l,solitaire[i]])
print(num)
