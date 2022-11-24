#	Pet
#https://open.kattis.com/problems/pet

l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=list(map(int,input().split()))
l4=list(map(int,input().split()))
l5=list(map(int,input().split()))
L1=sum(l1)
L2=sum(l2)
L3=sum(l3)
L4=sum(l4)
L5=sum(l5)
if L1>L2 and L1>L3 and L1>L4 and L1>L5:
    print("1",L1)
if L2>L1 and L2>L3 and L2>L4 and L2>L5:
    print("2",L2)
if L3>L1 and L3>L2 and L3>L4 and L3>L5:
    print("3",L3)
if L4>L1 and L4>L2 and L4>L3 and L4>L5:
    print("4",L4)
if L5>L1 and L5>L2 and L5>L3 and L5>L4:
    print("5",L5)
