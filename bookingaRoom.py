#	Booking a Room
#https://open.kattis.com/problems/bookingaroom

n, nb = list(map(int, input().split()))
b = set()
for i in range(n):
    b.add(str(i + 1))

for j in range(nb):
    i= input()
    b.remove(i)

if b:
    print(b.pop())
else:
    print("too late")
