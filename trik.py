#	Trik
#https://open.kattis.com/problems/trik

ans=1
s=str(input())
for i in s:
    if i=='A':
        if ans==1:
            ans=2
        elif ans==2:
            ans=1
        else:
            ans=3
    elif i=='B':
        if ans==1:
            ans=1
        elif ans==2:
            ans=3
        else:
            ans=2
    else:
        if ans==1:
            ans=3
        elif ans==2:
            ans=2
        else:
            ans=1
print(ans)
