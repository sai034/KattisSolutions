#School Spirit
#https://open.kattis.com/problems/schoolspirit

from statistics import mean
def universityScore(s, e):
    return 1/5 * s * (4/5) ** e
n = int(input())
S= [0]
for i in range(n):
    s = int(input())
    p = S[0]
    S[0] += universityScore(s, i)
    for j, k in enumerate(S[1:], 1):
        e = i - 1
        S[j] =S[j]+ universityScore(s, e)
    S.append(p)
print(S[0])
print(mean(S[1:]))
