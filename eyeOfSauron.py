#	Eye of Sauron
#https://open.kattis.com/problems/eyeofsauron

n=input()
p=n.split("()")
if p[0]==p[1]:
    print("correct")
else:
    print("fix")
