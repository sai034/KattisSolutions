#	Hangman
#https://open.kattis.com/problems/hangman

s1=str(input())
s2=list(input())
i=0
gi=0
while i<10 and len(s1)>0:
    if s2[gi] not in s1:
        i=i+1
    else:
        s1=s1.replace(s2[gi],"")
    gi=gi+1
if len(s1)>0:
    print("LOSE")
else:
    print("WIN")
