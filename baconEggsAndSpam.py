#Bacon, Eggs, and Spam
#https://open.kattis.com/problems/baconeggsandspam

from collections import defaultdict
n = int(input())
while n != 0:
    menu = defaultdict(list)
    for k in range(n):
        p = input().split()
        N = p[0]
        for i in p[1:]:
            menu[i].append(N)
    for i, j in sorted(menu.items()):
        print(" ".join([i] + sorted(j)))
    print()
    n = int(input())
