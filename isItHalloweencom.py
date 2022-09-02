#	IsItHalloween.com
#https://open.kattis.com/problems/isithalloween

i=str(input())
s=i.split()
m=s[0]
d=s[1]
D=int(d)
if(m=="OCT" and D==31 ):
    print("yup")
elif(m=="DEC" and D==25):
    print("yup")
else:
    print("nope")
