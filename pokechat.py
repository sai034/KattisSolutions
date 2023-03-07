#	Pokechat
#https://open.kattis.com/problems/pokechat

S1 = input()
S2 = input()
S = [int(S2[i:i+3]) for i in range(0, len(S2), 3)]
print("".join(S1[i-1] for i in S))
