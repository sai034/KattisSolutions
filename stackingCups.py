#	Stacking Cups
#https://open.kattis.com/problems/cups

def is_integer_num(m):
    try:
        i=int(m)
    except:
        return False
    return True
n=int(input())
s=list()
for i in range(n):
    R=input().split()
    if is_integer_num(R[0]):
        s.append((int(R[0]),R[1]))
    else:
        s.append((2*int(R[1]),R[0]))
for j in sorted(s):
    print(j[1])
