#	Restaurant Opening
#https://open.kattis.com/problems/restaurantopening

n, m = map(int, input().split())
p = list()
for i in range(n):
    p.append(list(map(int, input().split())))
b = 1e9
for i in range(n):
    for j in range(m):
        c = 0
        for k in range(n):
            for l in range(m):
                c += (abs(i-k) + abs(j-l))*p[k][l]
        b = min(b, c)
print(b)
