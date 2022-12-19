#	Tram
#https://open.kattis.com/problems/tram

n=int(input())
sum=0
for i in range(n):
    x,y=map(int,input().split())
    y1=y-x
    sum=sum+y1
print(sum/n)
