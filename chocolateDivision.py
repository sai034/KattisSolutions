#Chocolate Division
#https://open.kattis.com/problems/chocolatedivision

r,c=map(int,input().split())
a=r*c
if a%2==0:
    print("Alf")
else:
    print("Beata")
