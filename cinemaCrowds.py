#	Cinema Crowds
#https://open.kattis.com/problems/cinema

n,m=map(int,input().split())
l=list(map(int,input().split()))
sum1=0
l1=list()
for i in l:
    if i>n:
        sum1=sum1+1
        l1.append(i)
    else:
        n=n-i
print(sum1)
