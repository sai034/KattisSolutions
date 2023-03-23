#	Ghost Leg
#https://open.kattis.com/problems/ghostleg

n,m=map(int,input().split())
l=list(range(1,n+1))
for j in range(m):
    k=int(input())
    l[k-1],l[k]=l[k],l[k-1]
for i in l:
    print(i)
