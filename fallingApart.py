#Falling Apart
#https://open.kattis.com/problems/fallingapart

n=int(input())
l=[int(x) for x in input().split()]
a=0
b=0
while l:
    a=a+max(l)
    l.remove(max(l))
    if l:
        b=b+max(l)
        l.remove(max(l))
print(a,b)
