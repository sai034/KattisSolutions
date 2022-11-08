#	Electrical Outlets
#https://open.kattis.com/problems/electricaloutlets

N=int(input())
for i in range(N):
    k=input()
    o=k.split()
    sum=0
    for j in range(1,len(o)):
        sum=sum+int(o[j])
    print(sum+1-int(o[0]))
