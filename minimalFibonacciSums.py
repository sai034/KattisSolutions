#	Minimal Fibonacci Sums
#https://open.kattis.com/problems/fibonaccisum

class s:
    def f(self, k):
        res, a, b = 0, 1, 1
        p=list()
        while b <= k:
            a, b = b, a + b
        while a > 0:
            if a <= k:
                k -= a
                p.append(a)
                p.sort()
                res += 1
            a, b = b - a, a
        print(*p)
k=int(input())
p=s()
p.f(k)
