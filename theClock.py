#	The Clock
#https://open.kattis.com/problems/klockan2

a= {}
for h in range(12):
    for m in range(60):
        hc = 30*h + m/2
        mc = 6*m
        a[(hc - mc) % 360] = f'{str(h).zfill(2)}:{str(m).zfill(2)}'
n=int(input())
print(a[-n/10 % 360])
