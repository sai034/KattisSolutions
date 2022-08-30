# Reversed Binary Numbers
# https://open.kattis.com/problems/reversebinary

n=int(input())
p=bin(n)
v=int(bin(n)[::-1][:-2],2)
print(v)
