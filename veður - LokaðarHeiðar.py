#	Veður - Lokaðar heiðar
#https://open.kattis.com/problems/vedurheidar

n1 = int(input())
n = int(input())
for i in range(n): 
    r, k = input().split()
    print(r, ['opin', 'lokud'][int(k) < n1])
