#	Sum Kind of Problem
#https://open.kattis.com/problems/sumkindofproblem

P=int(input())
pi=0
for m in range(P):
    j=str(input())
    s=j.split()
    k=s[0]
    n=s[1]
    K=int(k)
    N=int(n)
    pi = N * (N + 1) // 2
    e=0
    o=0
    for i in range(1,(2*N)+1):
        if(i%2==0):
            e=e+i
    for i in range(1,(2*N-1)+1):
        if(i%2!=0):
            o=o+i
    print(K,pi,o,e)
