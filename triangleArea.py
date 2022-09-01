#	Triangle Area
#https://open.kattis.com/problems/triarea

i = str(input())
s=i.split()
h=s[0]
b=s[1]
c=int(h) * int(b)/2
if(c%2 == 0):
    print(int(c))
else:
    print(float(c))
