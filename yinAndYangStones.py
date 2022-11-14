#	Yin and Yang Stones
#https://open.kattis.com/problems/yinyangstones

s=str(input())
c1=0
c2=0
for i in s:
    if i=="W":
        c1=c1+1
    elif i=="B":
        c2=c2+1
if c1==c2:
    print("1")
else:
    print("0")
