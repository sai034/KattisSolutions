#	Simon Says
#https://open.kattis.com/problems/simonsays

i=int(input())
for j in range(i):
    s=str(input())
    if (s.startswith("Simon says")):
        print(s.replace("Simon says",""))
    else:
        continue
