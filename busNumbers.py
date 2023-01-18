#	Bus Numbers
#https://open.kattis.com/problems/busnumbers

def rc(c):
    n = len(c)
    if n == 0:
        return ""
    elif n == 1:
        return str(c[0])
    elif n == 2:
        return "{} {}".format(c[0], c[1])
    else:
        return "{}-{}".format(c[0], c[-1])
n = int(input())
b= list(map(int, input().split()))
b.sort()
co = []
cc = []
p = None
for cb in b:
    if p is None:
        cc.append(cb)
    else:
        if p + 1 == cb:
            cc.append(cb)
        else:
            co.append(cc)
            cc = []
            cc.append(cb)
    p = cb
if cc:
    co.append(cc)
    cc = []
r = ""
for c in co:
    if r != "":
        r += " "
    r += rc(c)
print(r)
