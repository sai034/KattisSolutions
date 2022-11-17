#Sjecista
#https://open.kattis.com/problems/sjecista

n=int(input())
r=4
def nCr(n, r):
    return (fact(n) / (fact(r) * fact(n - r)))
def fact(n):
    if n == 0:
        return 1
    res = 1
    for i in range(2, n + 1):
        res = res * i
    return res
print(int(nCr(n,r)))
