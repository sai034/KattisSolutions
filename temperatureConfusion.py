#	Temperature Confusion
#https://open.kattis.com/problems/temperatureconfusion

from math import gcd

class f:
    def __init__(self, a=0,b=1):
        if b < 0:
            a = -a
            b = -b
        d = gcd(a,b)
        self.a = a // d
        self.b = b // d

    def __add__(self, other):
        return f(self.a * other.b + self.b * other.a, self.b * other.b)

    def __neg__(self):
        return f(-self.a, self.b)

    def __sub__(self,other):
        return self + (-other)

    def __mul__(self,other):
        return f(self.a * other.a, self.b * other.b)

    def __truediv__(self,other):
        return f(self.a * other.b, self.b * other.a)

    def __repr__(self):
        return f'{self.a}/{self.b}'

    def __str__(self):
        return f'{self.a}/{self.b}'

def main():
    print((f(*map(int, input().split('/'))) - f(32))*f(5,9))

if __name__ == "__main__":
    main()
