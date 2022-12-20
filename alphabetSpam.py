#	Alphabet Spam
#https://open.kattis.com/problems/alphabetspam

t = input()
total = len(t)
now = 0
nol = 0
nou = 0
nos = 0
for s in t:
    if s == "_":
        now += 1
    elif s.islower():
        nol += 1
    elif s.isupper():
        nou += 1
    else:
        nos += 1
print(now / total)
print(nol / total)
print(nou / total)
print(nos / total)
