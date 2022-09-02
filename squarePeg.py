#	Square Peg
#https://open.kattis.com/problems/squarepeg

i=str(input())
s=i.split()
l=s[0]
r=s[1]
L=int(l)
R=int(r)
ac=2*R*R
sa=L*L
if(ac-sa<0):
    print("nope")
else:
    print("fits")
