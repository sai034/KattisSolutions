#	A Furious Cocktail
#https://open.kattis.com/problems/cocktail

n,m=map(int,input().split())
l1=sorted([int(input()) for i in range(n)], reverse=True)
r=l1.pop(0)
for j in l1:
    r=r-m
    r=min(j,r)
if r>0:
    print("YES")
else:
    print("NO")
