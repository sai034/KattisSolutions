#	Making A Meowth
#https://open.kattis.com/problems/makingameowth

import itertools
N,P,X,Y = map(int, input().split())
t = 0
for i in itertools.count(1):
    m = i % N == 0
    if P == 0:
        if m:
            t = t+Y
        break
    if m:
        t =t+ Y
    else:
        t =t+ X
        P -= 1
print(t)
