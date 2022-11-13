#	Server
#https://open.kattis.com/problems/server

i,n=list(map(int,input().split()))
sum=0
sum1=0
sum2=[]
k=str(input())
stringArray = k.split(" ")
idx=0
for idx in range(0,i):
    sum += int(stringArray[idx])
    if sum<=n:
        sum2.append(int(stringArray[idx]))
    else:
        break
print(len(sum2))
