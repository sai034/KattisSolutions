#Messy lists
#https://open.kattis.com/problems/stokigalistor

n=int(input())
l=list(map(int,input().split()))
p=sorted(l)
c=0
if l==p:
    print("0")
else:
    for i in range(n):
        if l[i]!=p[i]:
            c=c+1
    print(c)
