#Planting Trees
#https://open.kattis.com/problems/plantingtrees

n = int(input())
s = list(map(int, input().split()))
s.sort()
d=0
t = 0
for i in reversed(s):
    d =d+ 1
    t =t- 1
    t = max(t, i)
p = d + t + 1
print(p)
