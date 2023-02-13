#Building Pyramids
#https://open.kattis.com/problems/pyramids

n = int(input())
h = 0
while True:
    s= (h * 2 + 1) ** 2
    n = n- s
    if n < 0:
        break
    h += 1
print(h)
