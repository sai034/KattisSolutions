#	Recount
#https://open.kattis.com/problems/recount

vs = {}
while True:
    v = input()
    if v == "***":
        break

    vs[v] = vs.get(v, 0) + 1
w = None
wc = 0
mw = False
for v, count in vs.items():
    if wc < count:
        w = v
        wc = count
        mw = False
    elif wc == count:
        mw = True
if mw:
    print("Runoff!")
else:
    print(w)
