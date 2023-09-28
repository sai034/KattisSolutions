#	Spritt
#https://open.kattis.com/problems/spritt

n,x=map(int,input().split())
s=list()
for i in range(n):
    p=int(input())
    s.append(p)
q=sum(s)
if q<=x:
    print('Jebb')
else:
    print('Neibb')
