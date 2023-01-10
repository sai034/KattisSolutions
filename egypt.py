#	Egypt
#https://open.kattis.com/problems/egypt

t=0
o=0
while True:
    a,b,c=sorted(map(int,input().split()))
    if a==0:
        break
    else:
        t=(a**2)+(b**2)
        o=(c**2)
        if (t==o):
            print("right")
        else:
            print("wrong")
