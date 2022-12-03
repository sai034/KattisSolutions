#	Bus
#https://open.kattis.com/problems/bus

T=int(input())
for i in range(T):
    n = int(input())
    k = 0
    while n > 0:
        k=k+0.5
        k = k * 2
        n =n-1
    print(int(k))
