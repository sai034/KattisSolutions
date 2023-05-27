#	Bracket Matching
#https://open.kattis.com/problems/bracketmatching

import sys
n=int(input())
b = input()
s = []
for p in b:
    if p in '([{':
        s.append(p)
    else:
        if not s or s[-1] != {')':'(', ']':'[', '}':'{'}[p]:
            print('Invalid')
            sys.exit(0)
        else:
            s.pop()
if int(len(s)==0):
    print('Valid')
else:
    print('Invalid')
