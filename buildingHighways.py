#	Building Highways
#https://open.kattis.com/problems/buildinghighways

n=int(input())
a=list(map(int,input().split()))
print(min(a)*(n-2)+sum(a))
