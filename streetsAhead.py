#Streets Ahead
#https://open.kattis.com/problems/streetsahead

n1,n2=map(int,input().split())
r =dict()
for i in range(n1):
    p=str(input())
    r[p] = len(r)
for j in range(n2):
    a, b = input().strip().split()
    print((abs(r[b]-r[a])-1) % n1)
