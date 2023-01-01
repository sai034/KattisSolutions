#	Video Speedup
#https://open.kattis.com/problems/videospeedup

n,p,k=map(int,input().split())
l=list(map(int,input().split()))
s=0
a=0
m=1.0
for i in l:
    a=a+m*(i-s)
    s=i
    m=m+p/100.00
a=a+m*(k-s)
print(a)
