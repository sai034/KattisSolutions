#	Tower Construction
#https://open.kattis.com/problems/tornbygge

n = int(input())
l = [int(l) for l in input().split()]
r = 1
for i in range(1, n):
    if l[i] > l[i-1]:
        r =r+ 1
print(r)
