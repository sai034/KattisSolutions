#	Dice Game
#https://open.kattis.com/problems/dicegame

g=list(map(int,input().split()))
e=list(map(int,input().split()))
if sum(g)>sum(e):
    print("Gunnar")
elif sum(g)<sum(e):
    print("Emma")
else:
    print("Tie")
