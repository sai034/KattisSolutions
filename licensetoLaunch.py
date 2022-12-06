#	License to Launch
#https://open.kattis.com/problems/licensetolaunch

n = int(input())
e = list(map(int,input().split()))
mind=min(e)
d= e.index(mind)
print(d)
