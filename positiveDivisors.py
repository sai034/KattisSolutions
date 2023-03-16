#	Positive Divisors
#https://open.kattis.com/problems/positivedivisors

a=list()
b=list()
n=int(input())
k=1
while k*k <= n:
    if n % k == 0:
        a.append(k)
        if k*k != n:
            b.append(n//k)
    k=k+1
for i in a:
    print(i)
for j in b[::-1]:
    print(j)
