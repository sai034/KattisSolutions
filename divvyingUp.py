#	Divvying Up
#https://open.kattis.com/problems/divvyingup

_input=int(input())
x=[int(x) for x in input().split()]
a=sum(x)
if a%3==0:
    print("yes")
else:
    print('no')
