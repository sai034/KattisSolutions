#	Töflur
#https://open.kattis.com/problems/toflur

n=int(input())
l=list(map(int,input().split()))
sum=0
l.sort()
for i,j in zip(l[:-1],l[1:]):
    sum=sum+(i-j)**2
print(sum)
