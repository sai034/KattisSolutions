#	Prsteni
#https://open.kattis.com/problems/prsteni

from fractions import Fraction
n = int(input())
r = list(map(int, input().split()))
p = r[0]
for i in r[1:]:
    l = Fraction(p, i)
    print("{}/{}".format(l.numerator, l.denominator))
