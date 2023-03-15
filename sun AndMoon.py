#	Sun and Moon
#https://open.kattis.com/problems/sunandmoon

s1, y1 = map(int, input().split())
m1, y2 = map(int, input().split())
for i in range(5001):
    if (i+s1) % y1 or (i+m1) % y2:
        continue
    print(i)
    break
