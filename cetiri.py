#	Cetiri
#https://open.kattis.com/problems/cetiri

n = sorted(map(int, input().split()))
d1 = n[1] - n[0]
d2 = n[2] - n[1]
mindi = min(d1, d2)
misnum = None
for n1, n2 in zip(n[:-1], n[1:]):
    d = n2 - n1
    if d != mindi:
        misnum = n1 + mindi
        break
if misnum is None:
    misnum = n2 + mindi
print(misnum)
