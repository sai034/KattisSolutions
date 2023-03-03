#	Riječi
#https://open.kattis.com/problems/rijeci

n = int(input())
na=1
nb=0
def click(n, na, nb):
    if n == 0:
        return (na, nb)
    else:
        return click(n - 1, nb, na + nb)
A, B = click(n, na, nb)
print(A, B)
