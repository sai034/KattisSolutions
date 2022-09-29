#	GCVWR
#https://open.kattis.com/problems/gcvwr

G,T,N=map(int,input().split())
i=map(int,input().split())
print(int(0.9*(G-T))-sum(i))
