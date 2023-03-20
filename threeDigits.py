#	Three Digits
#https://open.kattis.com/problems/threedigits

n = int(input())
if n == 5:
    print("12")
elif n == 6:
    print("72")
else:
    p, n1, n2 = 1, 0, 0
    for i in range(2, n + 1):
        p =p * i
        while p % 5 == 0:
            p =p // 5
            n1 =n1 + 1
        while p % 2 == 0:
            p =p // 2
            n2 =n2 + 1
        p %= 1000
    for k in range(n2 - n1):
        p =p* 2
        p = p%1000
    a = str(p)
    print('0' * (3 - len(a)) + a)
