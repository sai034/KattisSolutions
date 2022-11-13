#	Just a Minute
#https://open.kattis.com/problems/justaminute

n=int(input())
min=0
sec=0
for i in range(n):
    m,s=list(map(int,input().split()))
    min=min+m
    sec=sec+s
p=sec/60/min
if p>1:
    print(p)
else:
    print("measurement error")
