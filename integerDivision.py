#Integer Division
#https://open.kattis.com/problems/integerdivision

from collections import defaultdict
n=defaultdict(lambda:0)
d=int(input().split()[1])
for a in map(int,input().split()):
    n[a//d]+=1
print(sum((a*(a-1))//2 for a in n.values()))
