#	Double Password
# https://open.kattis.com/problems/doublepassword

n1=(input())
n2=(input())
sum=0
for i,j in zip(n1,n2):
    if(i!=j):
        sum=sum+1
print(2**sum)
