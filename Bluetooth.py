#Bluetooth(	Blåtand)
#https://open.kattis.com/problems/bluetooth

n = int(input())
l = {}
l["left+"] = 8
l["left-"] = 8
l["right+"] = 8
l["right-"] = 8
l1 = {}
l1["left+"] = 0
l1["left-"] = 0
l1["right+"] = 0
l1["right-"] = 0
for i in range(n):
    position, condition = input().split()
    if position[0] == "+":
        place = "left+"
    elif position[0] == "-":
        place = "left-"
    elif position[1] == "+":
        place = "right+"
    else:
        place = "right-"

    if condition == "m":
        l[place] -= 1
    else:
        l1[place] -= 1

N = 1
if N <= l["left+"] and \
    N <= l["left-"] and \
    l1["left+"] == 0 and \
    l1["left-"] == 0:
        print("0")
elif N <=l["right+"] and \
    N <= l["right-"] and \
    l1["right+"] == 0 and \
    l1["right-"] == 0:
        print("1")
else:
