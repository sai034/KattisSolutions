#	Baby Bites
#https://open.kattis.com/problems/babybites

n= int(input())
bites = input().split()
m = True
for i, j in enumerate(bites, 1):
    if j == "mumble":
        continue
    else:
        j = int(j)
        if j != i:
            m = False
if m:
    print("makes sense")
else:
    print("something is fishy")
