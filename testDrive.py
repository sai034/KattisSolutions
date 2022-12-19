#	Test Drive
#https://open.kattis.com/problems/testdrive

a,b,c=map(int,input().split())
d1=b-a
d2=c-b
if d1*d2<0:
    print("turned")
elif abs(d1)<abs(d2):
    print("accelerated")
elif abs(d1)>abs(d2):
    print("braked")
else:
    print("cruised")
