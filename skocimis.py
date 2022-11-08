#	Skocimis
#https://open.kattis.com/problems/skocimis

A,B,C=list(map(int,input().split()))
s1=B-A
s2=C-B
print(max(s1,s2)-1)
