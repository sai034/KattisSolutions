#	Expected Earnings
#https://open.kattis.com/problems/expectedearnings

n,k,p=map(float,input().split())
if -k*(1-p)+(n-k)*p<0:
    print("spela")
else:
    print("spela inte!")
