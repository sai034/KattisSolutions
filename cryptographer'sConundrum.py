#	Cryptographer's Conundrum
#https://open.kattis.com/problems/conundrum

s=str(input())
a=s[0::3]
b=s[1::3]
c=s[2::3]
count=0
for i in range(len(a)):
    if a[i] !="P":
        count=count+1
for i in range(len(b)):
    if b[i] !="E":
        count=count+1
for i in range(len(c)):
    if c[i] != "R":
        count=count+1
print(count)
