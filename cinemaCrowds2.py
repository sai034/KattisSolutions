# Cinema Crowds 2
#https://open.kattis.com/contests/m77v2v/problems/cinema2

n,m=map(int,input().split())
l=list(map(int,input().split()))
sum1=0
s=0
l1=list()
for i in l:
    if sum1<=n:
        sum1=sum1+i
        l1.append(i)
    if sum1>n:
        break
s=m-len(l1)
print(s+1)
