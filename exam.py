#Exam
#https://open.kattis.com/problems/exam

n=int(input())
sum=0
ma=input()
fa=input()
length=len(ma)
for a,b in zip(ma,fa):
    if a==b:
        sum=sum+1
if sum>=n:
    print(n+(length-sum))
else:
    print(sum+(length-n))
