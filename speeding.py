#	Speeding
#https://open.kattis.com/problems/speeding

n=int(input())
inti,ind=map(int,input().split())
maxs=0
for i in range(n-1):
    pst,psd=map(int,input().split())
    t=pst-inti
    d=psd-ind
    s=d//t
    maxs=max(s,maxs)
    inti=pst
    ind=psd
print(maxs)
