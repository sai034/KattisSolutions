#	SMIL
#https://open.kattis.com/problems/smil

p = input()
for i in range(len(p)):
    if p[i:i+2] in [":)", ";)"] or p[i:i+3] in [":-)", ";-)"]:
        print(i)
