#	Poker Hand
#https://open.kattis.com/problems/pokerhand

cards = input().split()
ranks ={}
for card in cards:
    rank=card[0]
    ranks[rank]=ranks.get(rank,0)+1
m=max(ranks,key=ranks.get)
h=ranks[m]
print(h)
