#	Mixed Fractions
#https://open.kattis.com/problems/mixedfractions

def test(nu,de):
    num=nu//de
    rem=nu%de
    print("{} {} / {}".format(num,rem,de))
while (1):
    n = str(input())
    s = n.split()
    nu = int(s[0])
    de = int(s[1])
    if nu==0 and de==0:
        break
    test(nu,de)
