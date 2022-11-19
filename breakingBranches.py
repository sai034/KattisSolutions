#	Breaking Branches
#https://open.kattis.com/problems/breakingbranches

i=int(input())
if i%2==0:
    print("Alice")
    print(i-1)
elif i%2!=0:
    print("Bob")
