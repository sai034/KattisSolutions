#	Subprime
#https://open.kattis.com/problems/subprime

l1, h = map(int, input().split())
p3= input().strip()
l = 13*10**5
s = list(range(l+1))
p1= list()
p2=list()
p = 2
while p <= l:
    if s[p] == p:
        p1.append(str(p))
        p2.append(p)
        for i in range(p*p, l+1, p):
            if s[i] == i:
                s[i] = p
    if p == 2:
        p -= 1
    p += 2
a = 0
for i in range(l1-1, h):
    a += p1[i].find(p3) != -1
print(a)
