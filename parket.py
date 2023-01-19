#	Parket
#https://open.kattis.com/problems/parket

n,m=map(int,input().split())
p,f=n+m,2
l=list()
while True:
    d, m = divmod(p, f)
    if m == 0:
        if n == 2 * d + 2 * f - 4:
            print(d, f)
            break
    f += 1
