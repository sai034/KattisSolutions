#	Piece of Cake!
#https://open.kattis.com/problems/pieceofcake2

i=str(input())
s=i.split()
n=s[0]
h=s[1]
v=s[2]
N=int(n)
H=int(h)
V=int(v)
a=max(H,N-H)
b=max(V,N-V)
c=a*b*4
print(c)
