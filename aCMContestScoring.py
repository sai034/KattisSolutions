#	ACM Contest Scoring
#https://open.kattis.com/problems/acm

noc = 0
score = 0
ent = {}
while True:
    n = input()
    if n== "-1":
        break
    p, id, c = n.split()
    idt= ent.get(id, 0)
    if c == "wrong":
        ent[id] = idt + 20
    else:
        score += idt + int(p)
        noc += 1
print(noc,score)
