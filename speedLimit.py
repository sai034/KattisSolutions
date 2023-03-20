#	Speed Limit
#https://open.kattis.com/problems/speedlimit

while(True):
    n = int(input())
    if n == -1:
        break
    d = 0
    l = 0
    for i in range(n):
        s, t = map(int,input().split())
        d =d + s * (t - l)
        l = t
    print(d, "miles")
