#	Dice Cup
#https://open.kattis.com/problems/dicecup

i=str(input())
s=i.split()
n=s[0]
m=s[1]
N=int(n)
M=int(m)
if(N==M):
    print(N+1)
if(N>M):
    for i in range(M+1,N+2):
        print(i)
if(M>N):
    for i in range(N+1,M+2):
        print(i)
