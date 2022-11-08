#Laptop Sticker
#https://open.kattis.com/problems/laptopsticker

m=1
i=str(input())
s=i.split()
wc=int(s[0])
hc=int(s[1])
ws=int(s[2])
hs=int(s[3])
wfh=m+ws+m<=wc
wfv=m+hs+m<=hc
wf=wfh and wfv
if wf:
    print(1)
else:
    print(0)
