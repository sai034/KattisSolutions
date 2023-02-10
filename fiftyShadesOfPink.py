#	Fifty Shades of Pink
#https://open.kattis.com/problems/fiftyshades

n=int(input())
c=0
for i in range(n):
    s=str(input())
    S=s.lower()
    if S.__contains__("rose") or S.__contains__("pink"):
        c=c+1
if c!=0:
    print(c)
else:
    print("I must watch Star Wars with my daughter")
