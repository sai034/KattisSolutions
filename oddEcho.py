#	Odd Echo
#https://open.kattis.com/problems/oddecho
n=int(input())
for i in range(1,n+1):
    m=str(input())
    if(i%2!=0):
        print(m)
