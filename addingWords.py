#Adding Words
#https://open.kattis.com/problems/addingwords

import sys
k = {}
v = {}
for i in sys.stdin:
    p = i.split()
    if p[0] == 'def':
        if p[1] in k.keys():
            del v[int(k[p[1]])]
        k[p[1]] = p[2]
        v[int(p[2])] = p[1]
    elif p[0] == 'calc':
        if len(list(filter(lambda y: y in k.keys(), p[1:][::2]))) != len(p[1:][::2]):
            print(" ".join(p[1:]), 'unknown')
        else:
            val = eval(" ".join(map(lambda y: k[y] if y in k.keys() else y, p[1:-1])))
            if val in v.keys():
                print(" ".join (p[1:]), v[val])
            else:
                print(" ".join (p[1:]), 'unknown')
    else:
        k.clear()
        v.clear()
