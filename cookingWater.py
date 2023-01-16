#	Cooking Water
#https://open.kattis.com/problems/cookingwater

lo,hi=[-1,1000]
n=int(input())
l=list()
l1=list()
for i in range(n):
    a,b=map(int,input().split())
    l.append(a)
    l1.append(b)
    l.append(lo)
    l1.append(hi)
    lo=max(lo,a)
    hi=min(hi,b)
if lo<=hi:
    print("gunilla has a point")
else:
    print("edward is right")
