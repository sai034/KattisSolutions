#	Batter Up
#https://open.kattis.com/problems/batterup


n=int(input())
m=[int(x) for x in input().split()]
t=0
sum=0
total=0
for i in range(n):
    t=m[i]
    if t<0:
        continue
    sum=sum+1
    total=total+t
print(total/sum)
