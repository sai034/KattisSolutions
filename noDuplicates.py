#	No Duplicates
#https://open.kattis.com/problems/nodup

s=[str(x) for x in input().split()]
a=len(s)!=len(set(s))
if len(s)!=len(set(s)):
    print("no")
else:
    print("yes")
