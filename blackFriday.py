#Black Friday
#https://open.kattis.com/problems/blackfriday

n = input()
l = input().split(' ')
pro = {i:l.count(i) for i in l}
nl = {}
for key, value in enumerate(l):
    if value not in nl and pro[value] == 1:
        nl[key + 1] = value
if not nl:
    print("none")
else:
    print(max(nl, key=lambda k: nl[k]))
