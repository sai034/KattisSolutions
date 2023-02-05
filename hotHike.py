# Hot Hike
#https://open.kattis.com/problems/hothike

def f(n, temp):
    m1, m2 = (-1,41)
    for i in range(n-2):
        m = max(temp[i],temp[i+2])
        if m < m2:
            m2 = m
            m1 = i
    return m1 + 1, m2
print("%d %d" % f(int(input()), list(map(int, input().split()))))
