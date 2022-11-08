#Rating Problems
#https://open.kattis.com/problems/ratingproblems

i=str(input())
s=i.split()
n=int(s[0])
k=int(s[1])
s=0
for j in range(0,k):
    r=int(input())
    s=s+r
print((s-3.0*(n-k))/n,((s+3.0*(n-k))/n))
