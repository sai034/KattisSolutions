#	The Mailbox Manufacturers Problem
#https://open.kattis.com/problems/mailbox

l = [[[0]*101 for j in range(101)] for k in range(11)]
def fc(p, a, q):
    if p == 0:
        return 1e9
    elif p == 1:
        return q*(q+1)//2 - a*(a+1)//2
    elif a == q:
        return 0
    elif l[p][a][q] == 0:
        w = 1e9
        for i in range(a+1, q+1):
            w = min(w, i + max(fc(p-1, a, i-1), fc(p, i, q)))
        l[p][a][q] = w
    return l[p][a][q]
n = int(input())
for i in range(n):
    k, m = map(int, input().split())
    print(fc(k, 0, m))
