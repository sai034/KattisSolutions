#	Parent Gap
#https://open.kattis.com/problems/parentgap

def leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
c, s = 2000, 14
y=int(input())
while c != y:
    c =c+ 1
    s -= 1+leap(c)
    if s % 7:
        s=s%7+7
    else:
       s=14
if (s+4)%7:
    print(((s+4)%7+45-s)//7, 'weeks')
else:
    print((52-s)//7, 'weeks')
