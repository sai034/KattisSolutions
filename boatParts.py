#	Boat Parts
#https://open.kattis.com/problems/boatparts

m,n=map(int,input().split())
l=list()
for i in range(n):
    s=str(input())
    l.append(s)
    s=set(l)
    if len(s)==m:
        print(i+1)
        break
else:
    print("paradox avoided")
