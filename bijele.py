#	Bijele
# https://open.kattis.com/problems/bijele

i=str(input())
s=i.split()
k=s[0]
q=s[1]
r=s[2]
b=s[3]
kn=s[4]
p=s[5]
K=int(k)
Q=int(q)
R=int(r)
B=int(b)
Kn=int(kn)
P=int(p)
kStandard=1
qStandard=1
rStandard=2
bStandard=2
knStandard=2
pStandard=8
print(kStandard-K,qStandard-Q,rStandard-R,bStandard-B,knStandard-Kn,pStandard-P)
