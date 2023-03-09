#	This Ain't Your Grandpa's Checkerboard
#https://open.kattis.com/problems/thisaintyourgrandpascheckerboard

import sys
n = int(input())
def check(string):
    w = string.count("W")
    b = string.count("B")
    if w != b:
        return False
    if len(string) < 3:
        return True
    for x, y, z in zip(string, string[1:], string[2:]):
        if x == y and y == z:
            return False
    return True
grandpaboard =list()
for i in range(n):
    s=str(input())
    grandpaboard.append(s)
for i in range(n):
    r = "".join(grandpaboard[i])
    c = "".join(grandpaboard[j][i] for j in range(n))
    if not check(r) or not check(c):
        print(0)
        sys.exit(0)
print(1)
