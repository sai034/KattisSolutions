#	Flexible Spaces
#https://open.kattis.com/problems/flexible

w,p=map(int,input().split())
l=list(map(int,input().split()))
l.append(0)
l.append(w)
t= set()
for i in l:
    for j in l:
        s = abs(i - j)
        if s != 0:
            t.add(s)
sort= sorted(t)
print(" ".join(map(str, sort)))
