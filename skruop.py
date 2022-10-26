#Skru op!
#https://open.kattis.com/problems/skruop

n=int(input())
so=7
for i in range(0,n):
    va=str(input())
    if va=="Skru op!" and so!=10:
        so=so+1
    elif va=="Skru ned!" and so!=0:
        so=so-1
print(so)
