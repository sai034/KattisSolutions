#	Free Food
#https://open.kattis.com/problems/freefood

n=int(input())
no_of_days=list()
for i in range(n):
    a,b=map(int,input().split())
    for j in range(a,b+1):
        if j not in no_of_days:
            no_of_days.append(j)
print(len(no_of_days))
