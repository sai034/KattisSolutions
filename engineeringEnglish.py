#	Engineering English
#https://open.kattis.com/problems/engineeringenglish

import fileinput
s= set()
for l in fileinput.input():
    w = l.strip().split()
    r = []
    for i in w:
        if i.lower() in s:
            r.append(".")
        else:
            r.append(i)
            s.add(i.lower())
    print(" ".join(r))
