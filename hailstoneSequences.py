#	Hailstone Sequences
#https://open.kattis.com/problems/hailstone2

n=int(input())
c=1
while n!=1:
    if n%2!=0:
        n=(n)*3+1
        c=c+1
    elif n%2==0:
        n=n//2
        c=c+1
print(c)
