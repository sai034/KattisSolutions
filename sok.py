#	Sok
#https://open.kattis.com/problems/sok

a,b,c=list(map(int,input().split()))
i,j,k=list(map(int,input().split()))
d1=a/i
d2=b/j
d3=c/k
d=min(d1,d2,d3)
d4=a-(d*i)
d5=b-(d*j)
d6=c-(d*k)
print(d4,d5,d6)
