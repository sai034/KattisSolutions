#99 Problems
#https://open.kattis.com/problems/99problems

n = int(input())
if n<100:
    print(99)
else:
    s = int(str(int(n/100)-1)+'99')
    b = int(str(int(n/100))+'99')
    if abs(n-b) < abs(n-s):
        print(b)
    elif abs(n-b) > abs(n-s):
        print(s)
    elif abs(n-b) == abs(n-s):
        print(b)
