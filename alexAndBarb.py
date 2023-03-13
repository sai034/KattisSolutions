#	Alex and Barb
#https://open.kattis.com/problems/alexandbarb

k,m,n=map(int,input().split())
p=k%(m+n)
if p<m:
    print("Barb")
else:
    print("Alex")
