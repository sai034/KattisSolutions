# FizzBuzz
# https://open.kattis.com/problems/fizzbuzz
i=str(input())
s=i.split()
x=s[0]
y=s[1]
n=s[2]
X=int(x)
Y=int(y)
N=int(n)
for i in range(1,N+1):
    if (i % X == 0 and i % Y == 0):
        print("FizzBuzz")
        continue
    if(i%X==0):
        print("Fizz")
        continue
    elif(i%Y==0):
        print("Buzz")
        continue
    else:
        print(i)
