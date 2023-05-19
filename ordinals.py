#	Ordinals
#https://open.kattis.com/problems/ordinals

def o(n):
    if n == 0:
        return '{}'
    return '{' + ','.join(o(i) for i in range(n)) + '}'
s=int(input())
print(o(s))
