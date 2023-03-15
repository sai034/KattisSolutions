#	Catalan Numbers
#https://open.kattis.com/problems/catalan

d= {0: 1, 1: 1}
def catalan(n):
    if d.__contains__(n):
        return d[n]
    if n <= 500:
        d[n] = ((n << 2) - 2) * catalan(n-1) // (n + 1)
    else:
        catalan(n-500)
        d[n] = ((n << 2) - 2) * catalan(n-1) // (n + 1)
    return d[n]
n=int(input())
for i in range(0, n):
    p=int(input())
    print(catalan(p))
