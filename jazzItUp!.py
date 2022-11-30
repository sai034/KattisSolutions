#Jazz it Up!
#https://open.kattis.com/problems/jazzitup

n=int(input())
prime=[2,3,5,7,11,13,17]
for i in prime:
    if n%i!=0:
        print(i)
        break
