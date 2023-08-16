#	Line Them Up
#https://open.kattis.com/problems/lineup

n=int(input())
l=list()
for i in range(n):
    s=str(input())
    l.append(s)
p=sorted(l)
q=l[:]
c=0
if l==p:
    print("INCREASING")
else:
    q.sort(reverse=True)
    if l==q:
        print("DECREASING")
    else:
        print("NEITHER")
