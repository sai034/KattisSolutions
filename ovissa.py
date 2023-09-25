#	Óvissa
#https://open.kattis.com/problems/ovissa

s=str(input())
c=0
for i in s:
    if i=='u':
        c=c+1
    else:
        continue
print(c)
