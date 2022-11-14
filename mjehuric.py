#	Mjehuric
#https://open.kattis.com/problems/mjehuric

n=list(map(int,input().split()))
s=sorted(n)
while n!=s:
    for i in range(4):
        if (n[i]>n[i+1]):
            n[i],n[i+1]=n[i+1],n[i]
            print(*n)
