#	A List Game
#https://open.kattis.com/problems/listgame

x = int(input())
k = 0
i = 2
while i**2 <= x:
    if x%i == 0:
        x = x // i
        k = k + 1
    else:
        i = i + 1
if x==1:
    y=0
else:
    y=1
print(k +y)
