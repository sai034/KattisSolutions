#	A Different Problem
#https://open.kattis.com/problems/different

while True:
    try:
        m,n=map(int,input().split())
    except EOFError:
        break
    print(abs(m-n))
