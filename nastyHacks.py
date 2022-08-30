# Nasty Hacks
# https://open.kattis.com/problems/nastyhacks

n=int(input())
for i in range(0,n):
    a=str(input())
    s=a.split()
    r=s[0]
    e=s[1]
    c=s[2]
    R=int(r)
    E=int(e)
    C=int(c)
    if(C+R<E):
        print("advertise")
    elif(C+R==E):
        print("does not matter")
    elif(C+R>E):
        print("do not advertise")
