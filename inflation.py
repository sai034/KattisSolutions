#	Inflation
#https://open.kattis.com/problems/inflation

def prob(lis):
    m = 1
    for i, x in enumerate(lis):
        if i + 1 < x:
            return -1
        else:
            m = min(m, x / (i+1))
    return m
n = int(input())
i = prob(sorted(map(int, input().split())))
if i < 0:
    print("impossible")
else:
    print('%.6f' % i)
