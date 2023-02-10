#	Early Winter
#https://open.kattis.com/problems/earlywinter

n,m=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    if i<=m:
        break
    else:
        c=c+1
if c==n:
    print("It had never snowed this early!")
else:
    print("It hadn't snowed this early in ",c," years!")
