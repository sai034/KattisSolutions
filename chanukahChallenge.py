#	Chanukah Challenge
#https://open.kattis.com/problems/chanukah

s=int(input())
for i in range(1,s+1):
    k,n=input().split()
    j=(int(n))
    print(k,(j*(j+1)//2)+j)
