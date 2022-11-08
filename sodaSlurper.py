#	Soda Slurper
#https://open.kattis.com/problems/sodaslurper

e,f,c=list(map(int,input().split()))
sum=e+f
count=0
while sum>=c:
    sum=sum-c
    count=count+1
    sum=sum+1
print(count)
