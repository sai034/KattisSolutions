#	Sort of Sorting
#https://open.kattis.com/problems/sortofsorting

from functools import cmp_to_key
def sort(p,q):
    if p[0]>q[0]:
        return 1
    elif p[0]<q[0]:
        return -1
    if p[1]>q[1]:
        return 1
    elif p[1]<q[1]:
        return -1
    return 0
while True:
    n = int(input())
    l = list()
    if n==0:
        break
    else:
        for i in range(n):
            s = str(input())
            l.append(s)
        l.sort(key=cmp_to_key(sort))
        for i in l:
            print(i)
        print()
