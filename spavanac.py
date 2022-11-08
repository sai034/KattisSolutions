#	Spavanac
#https://open.kattis.com/problems/spavanac

h,m=input().split()
h=int(h)
m=int(m)
if h == 0:
    h=24
min45=((h*60)+m)-45
nh=int(min45/60)
nm=min45%60
print("%s %s"%(nh,nm))
