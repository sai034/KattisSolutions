#Death Knight Hero
#https://open.kattis.com/problems/deathknight

n=int(input())
sum=0
for i in range(n):
    s=str(input())
    if s.__contains__("CD"):
        sum=sum+1
print(n-sum)
