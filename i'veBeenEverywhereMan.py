#	I've Been Everywhere, Man
#https://open.kattis.com/problems/everywhere

n=int(input())
for i in range(n):
    j=int(input())
    set={}
    for m in range(j):
        k=input()
        set[k]=1
    print(len(set))
