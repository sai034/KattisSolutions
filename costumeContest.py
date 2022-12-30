#Costume Contest
#https://open.kattis.com/problems/costumecontest

from collections import defaultdict
c = defaultdict(lambda: 0)
for i in range(int(input())):
    c[input()] += 1
c = sorted(c.items(), key=lambda z: (z[1],z[0]))
for co, count in c:
    if count == c[0][1]:
        print(co)
    else:
        break
