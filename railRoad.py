#Railroad
#https://open.kattis.com/problems/railroad2

i=str(input())
s=i.split()
x=int(s[0])
y=int(s[1])
if y%2==0:
    print("possible")
else:
    print("impossible")
