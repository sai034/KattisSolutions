#From A to B
#https://open.kattis.com/problems/fromatob

a, b = list(map(int, input().split()))
s = 0
while b<a:
    if a%2==0:
        a =a // 2
    else:
        a =a+ 1
    s =s+1
s =s+(b - a)
print(s)
