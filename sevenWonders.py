#	Seven Wonders
#https://open.kattis.com/problems/sevenwonders

s=str(input())
tc=0
cc=0
gc=0
tcgc=0
for i in s:
    if i=="T":
        tc=tc+1
    elif i=="C":
        cc=cc+1
    elif i=="G":
        gc=gc+1
print((tc**2)+(cc**2)+(gc**2)+min(tc,cc,gc)*7)
