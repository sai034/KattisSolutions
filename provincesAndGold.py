#	Provinces and Gold
#https://open.kattis.com/problems/provincesandgold

g,s,c=list(map(int,input().split()))
t=(g*3)+(s*2)+(c*1)
if t>=8:
    print("Province or Gold")
elif t>=6:
    print("Duchy or Gold")
elif t>=5:
    print("Duchy or Silver")
elif t>=3:
    print("Estate or Silver")
elif t>=2:
    print("Estate or Copper")
else:
    print("Copper")
