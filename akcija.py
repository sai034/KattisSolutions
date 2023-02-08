#Akcija
#https://open.kattis.com/problems/akcija

n=int(input())
l=list()
for i in range(n):
    p=int(input())
    l.append(p)
l.sort()
s=[]
p1=0
for i in range(len(l)):
    s.append(l.pop())
    if len(s)==3:
        p1=p1+sum(s)-min(s)
        s=[]
p1=p1+sum(s)
print(p1)
