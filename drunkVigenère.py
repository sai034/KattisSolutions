#Drunk Vigenère
#https://open.kattis.com/problems/drunkvigenere

import sys
def s(c1, c2):
    if(c1+c2 < ord('A')):
        return ord('Z')+1-(ord('A')-(c1+c2))
    if(c1+c2 > ord('Z')):
        return ord('A')-1+((c1+c2)-ord('Z'))
    return c1+c2
c1 = input()
c2 = input()
for i in range(len(c2)):
    sys.stdout.write(chr(s(ord(c1[i]), -(ord('A')-ord(c2[i])) if i % 2 == 1 else ord('A')-ord(c2[i]))))
