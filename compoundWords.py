#Compound Words
#https://open.kattis.com/problems/compoundwords

w = list()
while True:
    try:
        n = input().split()
    except EOFError:
        break
    w.extend(n)
c = set()
for i, w1 in enumerate(w):
    for w2 in w[i + 1:]:
        c.add(w1 + w2)
        c.add(w2 + w1)
c = sorted(c)
for j in c:
    print(j)
