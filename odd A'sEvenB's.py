# Odd A's, Even B's
#https://open.kattis.com/problems/oddaevenb

n=int(input())
x=[0]*(n+1)
y=[0]*(n+1)
x[1],x[2],y[1],y[2]=1,0,0,1
for i in range(3,n+1):
    x[i]=x[i-2]+y[i-1]
    y[i]=x[i-2]+y[i-2]
f=x[n]+y[n]
p=(10**9)+7
print(f%p)
