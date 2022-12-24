#Another Brick in the Wall
#https://open.kattis.com/problems/anotherbrick

h,w,n=map(int,input().split())
l=list(map(int,input().split()))
w1,c=w,False
for i in l:
    if not c:
        if i > w:
            c=-1
        else:
            w =w-i
            if w==0:
                w=w1
                h=h-1
            c=(h==0)
if c==-1:
    print("NO")
else:
    print("YES")
