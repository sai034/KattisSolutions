#	ABC
#https://open.kattis.com/problems/abc

a, b, c = sorted(list(map(int, input().split())))
order = list(input())
f = ""
for i in order:
    if f != "":
        f += " "
    if i == "A":
        f= f+ str(a)
    elif i == "B":
        f =f+ str(b)
    elif i == "C":
        f =f+ str(c)
print(f)
