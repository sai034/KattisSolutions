#	ICPC Awards
#https://open.kattis.com/problems/icpcawards

n=int(input())
w=0
teams=set()
for i in range(n):
    uname,tname=input().split()
    if w<12 and uname not in teams:
        w=w+1
        teams.add(uname)
        print(uname,tname)
