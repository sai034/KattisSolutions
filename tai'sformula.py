#	Tai's formula
#https://open.kattis.com/problems/taisformula

n=int(input())
t=[]
sum=0
for i in range(n):
    t.append(list(map(float,input().split())))
for i in range(n-1):
    sum=sum+(t[i+1][0]-t[i][0])*(t[i+1][1]+t[i][1])/2
print(sum*0.001)
