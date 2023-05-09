#	Bootstrapping Number
#https://open.kattis.com/problems/bootstrappingnumber

n = int(input())
n1, n2 = 1, 10
while abs(n2 - n1) >= 1e-7:
    n3= (n1+ n2) / 2
    exp = n3**n3
    if exp == n:
        break
    elif exp < n:
        n1 = n3
    else:
        n2=n3
print(n3)
