#Joint Jog Jam
#https://open.kattis.com/problems/jointjogjam

i=str(input())
s=i.split()
x1=int(s[0])
y1=int(s[1])
x2=int(s[2])
y2=int(s[3])
x3=int(s[4])
y3=int(s[5])
x4=int(s[6])
y4=int(s[7])
X=max(((x1-x2)**2+(y1-y2)**2)**0.5,((x3-x4)**2+(y3-y4)**2)**0.5)
print(X)
