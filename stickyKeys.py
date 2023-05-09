#Sticky Keys
#https://open.kattis.com/problems/stickykeys

s=str(input())
l=list()
for i in s:
    if not l or l[-1] != i:
        l.append(i)
print(''.join(l))
