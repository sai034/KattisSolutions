#	Time Travelling Temperatures
#https://open.kattis.com/problems/temperature

x,y=map(int,input().split())
if x==0 and y==1:
    print("ALL GOOD")
elif y==1:
    print("IMPOSSIBLE")
else:
    print(float((x)/(1.0-y)))
