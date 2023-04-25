#	Undead or Alive
#https://open.kattis.com/problems/undeadoralive

s=str(input())
s1=0
s2=0
if ':)' in s:
    s1=True
if ":(" in s:
    s2=True
l=['machine','undead','alive','double agent']
print(l[2*s1+s2])
