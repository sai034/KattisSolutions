#	Fading Wind
#https://open.kattis.com/problems/fadingwind

h, k, v, s = map(int, input().split())
dis = 0
while h > 0:
    v =v + s
    v =v - max(1, v//10)
    if v >= k:
        h = h + 1
    if v>0 and v<k:
        h =h-1
        if h == 0:
            v = 0
    if v <= 0:
        h = 0
    dis = dis + v
    if s > 0:
        s =s- 1
print(dis)
