#Locust Locus
#https://open.kattis.com/problems/locustlocus

f = None
n = int(input())
for i in range(n):
    y, c1, c2 = list(map(int, input().split()))
    n1 = y + c1
    n2 = y + c2
    while n1 != n2:
        if n1 < n2:
            n1 = n1 + c1
        else:
            n2 = n2 + c2
    ns= n1
    if f is None or ns < f:
        f = ns
print(f)
