#	Broken Swords
#https://open.kattis.com/problems/brokenswords

n = int(input())
TB=0
LR=0
for i in range(n):
    l = [int(i) for i in input()]
    TB += (1 if l[0] == 0 else 0) + (1 if l[1] == 0 else 0)
    LR += (1 if l[2] == 0 else 0) + (1 if l[3] == 0 else 0)
s = int((TB if TB < LR else LR) / 2)
TB -= s* 2
LR -= s * 2
print("{} {} {}".format(s, TB, LR))
