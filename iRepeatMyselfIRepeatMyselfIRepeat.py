#	I Repeat Myself I Repeat Myself I Repeat
#	https://open.kattis.com/problems/irepeatmyself

n=int(input())
for i in range(n):
    s=str(input())
    l=len(s)
    for j in range(1,l+1):
        if s==(s[0:j]*(int(l//j)+1))[0:l]:
            print(j)
            break
