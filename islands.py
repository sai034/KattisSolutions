#	Islands
#https://open.kattis.com/problems/islands3

def w(map, x, y):
    return 0 <= x and x < b and 0 <= y and y < h
def c(map, x, y):
    if w(map, x, y):
        return map[y][x]
    else:
        return None
def S(map, x, y, value):
    if w(map, x, y):
        map[y][x] = value
def n(map, x, y, N):
    f = c(map, x, y)
    if f != "C" and f != "L":
        return
    S(map, x, y, N)
    n(map, x-1, y, N)
    n(map, x+1, y, N)
    n(map, x, y-1, N)
    n(map, x, y+1, N)
def no(map):
    j = 0
    for y in range(h):
        for x in range(b):
            f = c(map, x, y)
            if f == "L":
                j = j+1
                n(map, x, y,j)
    print(j)
s = input().split()
h = int(s[0])
b = int(s[1])
map = []
for i in range(h):
    row = list(input())
    map.append(row)
no(map)
