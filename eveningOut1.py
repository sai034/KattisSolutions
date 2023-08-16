#	Evening Out 1
#https://open.kattis.com/problems/eveningout1

A, B = map(int, input().split())
p=min(A%B,-A%B)
print(p)
