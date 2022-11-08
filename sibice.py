#	Sibice
#https://open.kattis.com/problems/sibice

i=str(input())
s=i.split()
n=int(s[0])
w=int(s[1])
h=int(s[2])
for i in range(0,n):
    va=int(input())
    m=(w*w)+(h*h)
    s=m**(0.5)
    if s<va:
        print("NE")
    elif s>=va:
        print("DA")
