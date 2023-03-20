#	Cut the Negativity
#https://open.kattis.com/problems/cutthenegativity

n=int(input())
s=[list(map(int,input().split())) for i in range(n)]
N=list()
for i in range(len(s)):
    for j in range(len(s)):
        if s[i][j] > 0:
            N.append((i+1, j+1, s[i][j]))
print(len(N))
for i, j, k in N:
    print(i, j, k)
