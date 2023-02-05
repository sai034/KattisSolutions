#	Election Paradox
#https://open.kattis.com/problems/electionparadox

n = int(input())
r = sorted(map(int, input().split()))
v = 0
for i in range((n-1)//2):
    v += r.pop()
v += sum((pop // 2 for pop in r))
print(v)
