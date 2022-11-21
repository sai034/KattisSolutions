#	Overdraft
#https://open.kattis.com/problems/overdraft

n=int(input())
si=0
sb=0
for i in range(n):
    p=int(input())
    sb=sb+p
    si=max(si,-sb)
print(si)
