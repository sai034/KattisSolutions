#	Greedily Increasing Subsequence
#https://open.kattis.com/problems/greedilyincreasing

n=int(input())
l1=list(map(int,input().split()))
l2=list()
l2.append(l1[0])
c=int(l1[0])
l3=l1[1:n+1]
for i in l3:
    if i>c:
        l2.append(i)
        c=i
print(len(l2))
print(*l2)
