#Križaljka
#https://open.kattis.com/problems/krizaljka

a,b = map(str,input().split())
for i, c in enumerate(a):
    j = b.find(c)
    if j != -1:
        break
for y in range(len(b)):
    if y == j:
        print(a)
    else:
        print('.' * i + b[y] + '.' * (len(a) - i - 1))
