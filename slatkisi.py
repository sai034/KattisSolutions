#	Slatkisi
#https://open.kattis.com/problems/slatkisi

a,b=map(int, input().split())
c=10**b
k=(a//c) * c
r=a-k
if round((r/c) + 1e-3):
    print(k+c)
else:
    print(k)
