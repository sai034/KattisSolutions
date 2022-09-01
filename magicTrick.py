#	Magic Trick
#https://open.kattis.com/problems/magictrick
s=list(input())
v=set(list(s))
if len(s)==len(v):
    print("1")
else:
    print("0")
