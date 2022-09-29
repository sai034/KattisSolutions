#	Cetvrta
#https://open.kattis.com/problems/cetvrta

i=str(input())
j=str(input())
k=str(input())
s=i.split()
x1=s[0]
y1=s[1]
t=j.split()
x2=t[0]
y2=t[1]
u=k.split()
x3=u[0]
y3=u[1]
X1=int(x1)
X2=int(x2)
X3=int(x3)
Y1=int(y1)
Y2=int(y2)
Y3=int(y3)
l=1
m=1
if X1==X2:
    l=l*X3
elif X2==X3:
    l=l*X1
elif X1==X3:
    l=l*X2
if Y1==Y2:
    m=m*Y3
elif Y2==Y3:
    m=m*Y1
elif Y1==Y3:
    m=m*Y2
print(l,m)
