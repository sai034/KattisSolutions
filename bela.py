#	Bela
#https://open.kattis.com/problems/bela

d = input().split()
n = int(d[0])
do= d[1]
s= 4
def belotDominantValue(x):
    return {
        'A': 11,
        'K': 4,
        'Q': 3,
        'J': 20,
        'T': 10,
        '9': 14,
        '8': 0,
        '7': 0,
    }[x]
def belotNonDominantValue(x):
    return {
        'A': 11,
        'K': 4,
        'Q': 3,
        'J': 2,
        'T': 10,
        '9': 0,
        '8': 0,
        '7': 0,
    }[x]
totalValue = 0
for i in range(n):
    for j in range(s):
        card = input()
        value = card[0]
        suit = card[1]
        if suit == do:
            totalValue += belotDominantValue(value)
        else:
            totalValue += belotNonDominantValue(value)
print(totalValue)
