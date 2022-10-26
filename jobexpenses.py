#Job Expenses
#https://open.kattis.com/problems/jobexpenses

n=int(input())
sum=0
va=input().split()
for i in va:
    if i[0]=='-':
        sum=sum-int(i)
print(sum)
