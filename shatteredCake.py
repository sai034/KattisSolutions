#Shattered Cake
#https://open.kattis.com/problems/shatteredcake

w=int(input())
n=int(input())
sum=0
for i in range(0,n):
    w1,l1=list(map(int,input().split()))
    a=w1*l1
    sum=sum+a
print(sum//w)
