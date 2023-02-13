#	Parking
#https://open.kattis.com/problems/parking2

n = int(input())
for i in range(n):
    m=int(input())
    l = list(map(int, input().split()))
    fi = min(l)
    la = max(l)
    dis = 2 * (la - fi)
    print(dis)
