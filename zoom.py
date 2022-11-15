#	Zoom
#https://open.kattis.com/problems/zoom

x,y=list(map(int,input().split()))
g=list(map(int,input().split()))
print(*g[y-1::y])
