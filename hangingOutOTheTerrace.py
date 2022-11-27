#Hanging Out on the Terrace
#https://open.kattis.com/problems/hangingout

m,n=map(int,input().split())
p = 0
de = 0
for i in range(n):
    k = input().split()
    s = k[0]
    x = int(k[1])
    if s == "enter":
        np = p+ x
    else:
        np = p - x
    if m < np:
        de=de+1
    else:
        p = np
print(de)
